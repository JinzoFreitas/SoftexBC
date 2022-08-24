package Pessoas;

public class terceiro {
    private String nome;
    private String cnpj;
    private double custo;
    static double custoTotal;

    public terceiro(String nomeEmpresa, String CNPJ, double custoEmpresa) {
        nome = nomeEmpresa;
        cnpj = CNPJ;
        custo = custoEmpresa;
        custoTotal += custoEmpresa;
    }

    public static double custoTotal(){
        return custoTotal;
    }
    
    public void setCusto(double novoCusto){
        custo = novoCusto;
    }

    public String info(){
        return nome + cnpj + custo;
    }
}