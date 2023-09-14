public class App{
    public static void main(String[] args) {
        
        // System.out.println("\n");
        // new MinhaThread("Divisíveis", 1, 300).start();
        // System.out.println("\n");

        System.out.println("----------------------------------------");

        new MinhaThread("(1): De 100 a 300", 100, 300).start();

        new MinhaThread("(2): De 301 a 500", 301, 500).start();

        new MinhaThread("(3): De 501 a 700", 501, 700).start();
    }
}