import java.io.*;
import java.util.Scanner;

public class Exemplo_Leitor {
    public static void main(String[] args) {
        InputStream inputstream;
        int forma_escolhida = 0;
        Scanner scanner = new Scanner(System.in);
        try {
            inputstream = new FileInputStream("exemplo.txt");
            int data = inputstream.read();
            System.out.println("Conteúdo do arq. exemplo.txt:");
            System.out.println(
                    "Gostaria de gerar a saída do programa em: \n1 - decimal \n2 - hexadecimal \n3 - binário \nResposta: ");
            forma_escolhida = scanner.nextInt();
            scanner.close();
            while (data != -1) {
                switch (forma_escolhida) {
                    case 1:
                        System.out.print(data);
                        break;
                    case 2:
                        System.out.print(Integer.toHexString(data));
                        break;
                    case 3:
                        System.out.print(Integer.toBinaryString(data) + " ");
                        break;
                    default:
                        System.out.println("O valor informado é inválido");
                }
                data = inputstream.read();
            }
            inputstream.close();
        } catch (Exception e1) {
            e1.printStackTrace();
        }
    }
}