package br.edu.insper.tecprog;

public class MaisCaro implements MochilaBinaria {

	// Fazer o algoritmo de ordenar o array:
	public static void selectionSort(int[] A){
		for (int i = 0; i < A.length-1; i++) {
			int menor = i;

			for (int j = i + 1; j < A.length; j++) {
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

		// copiar os valores para ordenar sem mexer no array original 
		int[] valoresOrdenados = new int[valor.length];
		for (int i = 0; i < valor.length; i++){
			valoresOrdenados[i] = valor[i];
		}

		selectionSort(valoresOrdenados);


		// montar o array de indices em ordem decrescente de valor
		int[] IDS = new int [valoresOrdenados.length];
		boolean[] usados = new boolean[valoresOrdenados.length];
		int p = 0; // auxiliar para montar o array do IDS de forma decrescente

		for (int k = valoresOrdenados.length - 1; k >= 0; k--){
			int alvo = valoresOrdenados[k];

			for (int i = 0; i < valor.length; i++){
				if (!usados[i] && valor[i] == alvo){
					IDS[p] = i; // o indice p da minha lista IDS é o maior da lista de valores que nao foi usado.
					usados[i] = true;
					p++;
					break;
				}
			}
		}
		// ok, até aqui temos que o IDS é um array com os IDs do maior para o menor
		boolean[] objtsSelecionados = new boolean[valor.length];
		int pesoTotal = 0;
		int valorTotal = 0;

		for (int k = 0; k < valor.length; k++){
			int id = IDS[k]; // pegar o id do maior
			if (pesoTotal + peso[id] <= capacidade){
				objtsSelecionados[id] = true;
				pesoTotal += peso[id];
				valorTotal += valor[id];
			}
		}

		// preencher a solucao:
		Solucao S = new Solucao(valor.length);
		S.peso = pesoTotal;
		S.valor = valorTotal;
		S.objetos = objtsSelecionados;

		return S;

	}

}