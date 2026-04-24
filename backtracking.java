package br.edu.insper.tecprog;

public class BackTracking implements MochilaBinaria {

    @Override
    public Solucao resolveMochila(int[] valor, int[] peso, int capacidade) {

        int n = valor.length;

        // solução atual (em construção)
        boolean[] atual = new boolean [n]; // exemplo: [true, false, true]

        Solucao melhor = new Solucao(n); // melhor solucao encontrada

        backtracking(0, capacidade, 0, 0, valor, peso, atual, melhor);

        return melhor;
    }

    private void backtracking(int i, int capacidadeRestante, int valorAtual, int pesoAtual,
    int[] valor, int[] peso,
    boolean[] atual, Solucao melhor) {

        // Caso 1: Terminou todos os objetos
        if(i == valor.length) {
            if (valorAtual > melhor.valor){
                melhor.valor = valorAtual;
                melhor.peso = pesoAtual;

                // copiar objetos 
                for (int j = 0; j < atual.length; j++){
                    melhor.objetos[j] = atual[j];
                }
            }
            return;
        }

        // Caso 2: Não pega o objeto i --> vamos pular para o proximo objeto (i + 1)
        atual[i] = false;
        backtracking(i+1, capacidadeRestante, valorAtual, pesoAtual, valor, peso, atual, melhor);

        // Caso 3: Pega o objeto i (se couber)
        if (peso[i] <= capacidadeRestante) {
            atual[i] = true;

            backtracking(i+1, capacidadeRestante - peso[i], valorAtual + valor[i], pesoAtual + peso[i], valor, peso, atual, melhor);
        }


    }
}