import java.io.*;
public class Exemplo_Gravacao {
    public static void main(String[] args) {
        try {
            OutputStream output = new FileOutputStream("novo_exemplo.txt");
            String s = "TESTANDO A GRAVAÇÃO";
            int count = 0;
            while (count < s.length()) {
                output.write(s.charAt(count));
                count++;
            }
            output.close();
            System.out.println("Arquivo gerado com sucesso.");
        } catch (Exception e) {
            e.printStackTrace();
        }    }     }