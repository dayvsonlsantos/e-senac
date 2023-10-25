import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.Statement;

public class Conexao {
    private static final String USUARIO = "root";
    private static final String SENHA = "senha";
    private static final String URL = "jdbc:mysql://ip:3306/banco_muita_grana";
    private static final String DRIVER = "com.mysql.cj.jdbc.Driver";

    public static void salvar(Conta conta) {
        try {
            Class.forName(DRIVER);
            Connection conn = DriverManager.getConnection(URL, USUARIO, SENHA);
            Statement stmt = conn.createStatement();
            String query = "INSERT INTO CONTA (codigo, nome, saldo) VALUES(" + conta.getCodigo() + " , '" + conta.getNome() + "' , " + conta.getSaldo()
                    + ")";
            stmt.executeUpdate(query);
            stmt.close();
            System.out.println(" Conta cadastrada.");
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
