package br.edu.insper.tecprog;

import java.util.ArrayList;

public class DFSMelhor {

    public boolean[][] parseLabirinto(String labirinto) {
        String[] linhas = labirinto.strip().split("\n");
        int n = linhas.length;
        int m = linhas[0].length();

        boolean[][] paredes = new boolean[n][m];

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                paredes[i][j] = linhas[i].charAt(j) == '#';
            }
        }

        return paredes;
    }

    public boolean encontrarSaidaAMenosDeXPassos(String L, int i, int j,
                                                 ArrayList<Posicao> caminho,
                                                 int tamMax) {

        boolean [][] lab = parseLabirinto(L);
        boolean [][] visitado = new boolean [lab.length][lab[0].length];

        return dfsLimite(lab, i, j, 0, tamMax, visitado, caminho);
    }

    private boolean dfsLimite(boolean[][] lab, int i, int j,
                              int passos, int tamMax,
                              boolean[][] visitado,
                              ArrayList<Posicao> caminho) {

        // Essa função serve apenas para saber se existe algum caminho possivel dentro do limite de passos

        // Casos base:
        // Não esta dentro do lab:
        if (!dentro(lab, i, j)) return false;

        // bateu em alguma parede?
        if (lab[i][j]) return false;

        // ja passou pela casa:
        if (visitado[i][j]) return false;

        // Pssou do limite de passos?
        if (passos > tamMax) return false;

        // marcar como visitado e adicionar no caminho
        visitado[i][j] = true;
        caminho.add(new Posicao(i, j));

        // conferir se chegamos na saida antes de chamar a recusao
        if (ehSaida(lab, i, j)) return true;

        // chamar a recursao para todas as direções:
        if (dfsLimite(lab, i + 1, j, passos + 1, tamMax, visitado, caminho)) return true;
        if (dfsLimite(lab, i - 1, j, passos + 1, tamMax, visitado, caminho)) return true;
        if (dfsLimite(lab, i, j + 1, passos + 1, tamMax, visitado, caminho)) return true;
        if (dfsLimite(lab, i, j - 1, passos + 1, tamMax, visitado, caminho)) return true;
            
        caminho.remove(caminho.size() - 1);
        visitado[i][j] = false;

        return false;
    }

    public boolean encontrarSaidaMaisProxima(String L, int i, int j,
                                              ArrayList<Posicao> caminho) {

        // aqui é onde chamaremos a dfsMelhor para saber qual o caminho mais prox
        boolean [][] lab = parseLabirinto(L);
        boolean [][] visitado = new boolean[lab.length][lab[0].length];

        ArrayList<Posicao> atual = new ArrayList<>();
        ArrayList<Posicao> melhor = new ArrayList<>();

        dfsMelhor(lab, i, j, visitado, atual, melhor);

        caminho.clear();
        caminho.addAll(melhor);
        return !melhor.isEmpty();
    }

    private void dfsMelhor(boolean[][] lab, int i, int j,
                           boolean[][] visitado,
                           ArrayList<Posicao> atual,
                           ArrayList<Posicao> melhor) {

        // FINALMENTE, o DFS melhor realmente chegou
        // casos base:
        if(!dentro(lab, i, j)) return;
        if (lab[i][j]) return;
        if (visitado[i][j]) return;

        // marcar como visitado e adicionar a posicao ao caminho
        visitado[i][j] = true;
        atual.add(new Posicao(i, j));

        // conferir se chegou na saida e comparar com o tamanho do caminho anterior para pegar o menor:
        if (ehSaida(lab, i, j)) {
            if (melhor.isEmpty() || atual.size() < melhor.size()) {
                melhor.clear();
                melhor.addAll(atual);
            }
        }

        // chamar recursividade:
        dfsMelhor(lab, i + 1, j, visitado, atual, melhor);
        dfsMelhor(lab, i - 1, j, visitado, atual, melhor);
        dfsMelhor(lab, i, j + 1, visitado, atual, melhor);
        dfsMelhor(lab, i, j - 1, visitado, atual, melhor);

        // caso de errado eu devo voltar atrás
        atual.remove(atual.size() - 1);
        visitado[i][j] = false;
        
    }

    private boolean dentro(boolean[][] lab, int i, int j) {
        return i >= 0 && i < lab.length && j >= 0 && j < lab[0].length;
    }

    private boolean ehSaida(boolean[][] lab, int i, int j) {
        return i == 0 || j == 0 || i == lab.length - 1 || j == lab[0].length - 1;
    }
}