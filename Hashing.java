class myHash {
    static void print(int arr[]) {
        for (int element : arr) {
            System.out.print(element + " ");
        }
    }

    void linearProbing(int table[], int table_size, int arr[]) {
        for (int i = 0; i < arr.length; i++) {
            int remainder = arr[i] % table_size;
            if (table[remainder] == -1) {
                table[remainder] = arr[i];
            } else {
                for (int j = 0; j < arr.length; j++) {
                    int t = (remainder + j) % table_size;
                    if (table[t] == -1) {
                        table[t] = arr[i];
                        break;
                    }
                }
            }
        }
        print(table);
    }

    void quadraticProbing(int table[], int table_size, int arr[]) {
        for (int i = 0; i < arr.length; i++) {
            int remainder = arr[i] % table_size;
            if (table[remainder] == -1) {
                table[remainder] = arr[i];
            } else {
                for (int j = 0; j < arr.length; j++) {
                    int t = (remainder + j * j) % table_size;
                    if (table[t] == -1) {
                        table[t] = arr[i];
                        break;
                    }
                }
            }
        }
        print(table);
    }
}

class Hashing {
    public static void main(String[] args) {
        int[] arr = { 50, 700, 76, 85, 92, 73, 101 };
        int[] table = new int[7];
        for (int i = 0; i < table.length; i++) {
            table[i] = -1;
        }
        myHash obj = new myHash();
        obj.quadraticProbing(table, table.length, arr);
    }
}