package br.edu.insper.tecprog;

public class MaisCaro implements MochilaBinaria {

	public static void selectionSort(int[] A){
		for(int i = 0; i < A.length-1; i++){
			int menor = i;

			for( int j = i + 1; j < A.length; j++){
				if (A[menor] > A[j]){
					menor = j;
				}
			}
			int aux = A[menor];
			A[menor] = A[i];
			A[i] = aux;
		}
	}

	public Solucao resolveMochila(int[] valor, int[] peso, int capacidade) {

		// Copia os valores para ordenar sem mexer no array original
		int[] valoresOrdenados = new int[valor.length];
		for (int i = 0; i < valor.length; i++) {
			valoresOrdenados[i] = valor[i];
		}

		// Ordena em ordem crescente usando o seu selectionSort
		selectionSort(valoresOrdenados);

		// Monta o array de índices em ordem decrescente de valor
		int[] IDS = new int[valor.length];
		boolean[] usado = new boolean[valor.length];
		int p = 0;

		for (int k = valoresOrdenados.length - 1; k >= 0; k--) {
			int alvo = valoresOrdenados[k];

			for (int i = 0; i < valor.length; i++) {
				if (!usado[i] && valor[i] == alvo) {
					IDS[p] = i;
					usado[i] = true;
					p++;
					break;
				}
			}
		}

		// Monta a solução
		boolean[] objetosSelecionados = new boolean[valor.length];
		int pesoTotal = 0;
		int valorTotal = 0;

		for (int k = 0; k < valor.length; k++) {
			int id = IDS[k];

			if (pesoTotal + peso[id] <= capacidade) {
				objetosSelecionados[id] = true;
				pesoTotal += peso[id];
				valorTotal += valor[id];
			}
		}

		// Preenche a Solucao
		Solucao S = new Solucao(valor.length);
		S.peso = pesoTotal;
		S.valor = valorTotal;
		S.objetos = objetosSelecionados;

		return S;
	}
}