/*
Softex - Recife
Janderson Freitas

Crie dois pacotes baseados nas atribuições de uma empresa e inclua classes neles. Lembre-se de trabalhar com os padrões java.*/

import Pessoas.*;
import Processos.*;

public class Desenvolvimento_24 {
    public static void main(String[] args) {
        /* Testando a Classe funcionario */
        funcionario F1 = new funcionario("José", 2000.00);
        F1.setSalario(3000.00);
        System.out.println(F1.getSalario());

        /* Testando a Classe terceiro */
        terceiro E1 = new terceiro("E1","12345678-9",1000.00);
        terceiro E2 = new terceiro("E2", "98765432_1", 1500.00);
        System.out.println(terceiro.custoTotal());
        System.out.println(E1.info());
        System.out.println(E2.info());

        /* Testando a Classe materiaPrima */
        materiaPrima mP1 = new materiaPrima("mP1", 2, 350.00);
        materiaPrima mP2 = new materiaPrima("mP2", 3, 500.00);
        System.out.println(materiaPrima.custoTotal());
        System.out.println(mP1);
        System.out.println(mP2);

        /* Testando a Classe vendas */
        vendas v1 = new vendas("x", 2);
        vendas v2 = new vendas("x", 1);
        vendas v3 = new vendas("x", 3);
        vendas v4 = new vendas("x", 5);
        vendas v5 = new vendas("x", 1);
        vendas v6 = new vendas("y", 8);
        vendas v7 = new vendas("y", 7);
        vendas v8 = new vendas("z", 5);
        vendas v9 = new vendas("z", 1);
        vendas v10 = new vendas("z", 4);
        System.out.println(vendas.getQuantidadeX());
        System.out.println(vendas.getQuantidadeY());
        System.out.println(vendas.getQuantidadeZ());
        System.out.println(vendas.getQuantidadeTotal());
        System.out.println(vendas.getReceitaX());
        System.out.println(vendas.getReceitaY());
        System.out.println(vendas.getReceitaZ());
        System.out.println(vendas.getReceitaTotal());
        
        /* Imprimindo os objetos */
        System.out.println(v1);
        System.out.println(v2);
        System.out.println(v3);
        System.out.println(v4);
        System.out.println(v5);
        System.out.println(v6);
        System.out.println(v7);
        System.out.println(v8);
        System.out.println(v9);
        System.out.println(v10);
    }
}