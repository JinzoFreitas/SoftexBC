package Pessoas;

public class funcionario {
    private String nome;
    private double salario;

    public funcionario(String nomeFuncionario, double salarioFuncionario) {
        nome = nomeFuncionario;
        salario = salarioFuncionario;
    }

    public void setSalario(double novoSalario){
        salario = novoSalario;        
    }

    public double getSalario(){
        return salario;
    }

    public String getNome(){
        return nome;
    }
}