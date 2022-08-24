package Processos;

public class materiaPrima {
    private String nome;
    private double preco;
    private int quantidade;
    static double custoTotal;

    public materiaPrima(String nomeMateria,int qtd, double custoMateria) {
        nome = nomeMateria;
        quantidade = qtd;
        preco = custoMateria;
        custoTotal += (preco * quantidade);
    }

    public static double custoTotal(){
        return custoTotal;
    }

    public String getNome(){
        return nome;
    }
}