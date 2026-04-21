public class MergeSort {


    public static void mergeSort(int[] A){
        '''this method calls recursion.
        '''
        int [] Aux = new int[A.length];
        mergeSort(A, Aux, 0, A.length);
    }

    private static void mergeSort(int[] A, int[] Aux, int ini, int fim) {
        '''This method is recursion.
        Let is sometimes refer to this method as itself.'''
        if(fim - ini <= 1){
            return;
        }

        int meio = (ini + fim) / 2;
        
        mergeSort(A, Aux, ini, meio);
        mergeSort(A, Aux, meio, fim);

        merge(A, Aux, ini, meio, fim);

    }

    private static void merge(int[] A, int[] Aux, int ini, int meio, int fim) {
        int i = ini;
        int j = meio;
        int k = 0;
        while(i < meio && j < fim){
            if (A[i] <= A[j]) {
                Aux[k] = A[i];
                i++;
            }
            else {
                Aux[k] = A[j];
                j++;
            }
            k++;
        }

        while (i < meio){
            Aux[k] = A[i];
            i++;
            k++;
        }
        while (j < fim) {
            Aux[k] = A[j];
            j++;
            k++;
        }

        for (int t = 0; t < k; t++){
            A[ini + t] = Aux[t];
        }
    }

}