/*
Softex - Recife
Janderson Freitas
Unidade 1 - Mod 4 - Atividade 7


Crie uma situação em que ocorra uma exceção dentro de um código. utilize try/catch para realizar a captura e tratamento dessa exceção.*/

public class Desenvolvimento_27 {
    public static void main(String[] args) {
        try {
            String texto = null;
            texto = texto.toLowerCase(); //Erro de manipulação de variável null
        } catch (Exception e) {
            System.out.println(e);
        }
        try {
            int num1 = 10;
            int num2 = 0;
            System.out.println(num1/num2); //Erro de divisão por zero
        } catch (Exception e) {
            System.out.println(e);
        }
    }
}