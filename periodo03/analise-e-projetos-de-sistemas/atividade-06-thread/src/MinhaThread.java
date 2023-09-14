class MinhaThread extends Thread {
    private String nome;
    private int valorInicial;
    private int valorFinal;

    public MinhaThread(String nome, int valorInicial, int valorFinal) {
        this.nome = nome;
        this.valorInicial = valorInicial;
        this.valorFinal = valorFinal;
    }

    public void run() {
        int contador = 0;
        for (int i = valorInicial; i < valorFinal; i++) {
            if ((i % 3 == 0) && (i % 5 == 0)) {
                contador++;
                System.out.println("\nThread " + nome + " | " + "O valor " + i + " é divisivel por 3 e 5.");

                try {
                    Thread.sleep(100);
                } catch (Exception e) {

                }

            }
        }
        if (contador == 0) {
            System.out
                    .println("\nNenhum valor entre " + valorInicial + " e " + valorFinal + " é divisivel por 3 e 5\n");
        }
    }
    // public void run(){
    // for (int i = 0; i < 10; i++){
    // System.out.println("Thread " + nome + ": " + i);

    // try {
    // Thread.sleep(100);
    // } catch (Exception e) {

    // }

    // // System.out.println("Thread " + nome + " Concluído");
    // }
    // }
}