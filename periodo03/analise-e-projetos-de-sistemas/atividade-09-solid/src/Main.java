public class Main {
    public static void main(String[] args) throws Exception {
        Conta conta = new Conta (1, "Pedro", 1200.00);
        Conexao.salvar(conta);
    }
}
