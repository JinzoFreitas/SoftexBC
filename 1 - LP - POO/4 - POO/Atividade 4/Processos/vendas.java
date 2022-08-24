package Processos;

public class vendas {
    private static int quantidadeX;
    private static int quantidadeY;
    private static int quantidadeZ;
    private static double receitaX;
    private static double receitaY;
    private static double receitaZ;
    private static double precoX = 50.00;
    private static double precoY = 40.00;
    private static double precoZ = 30.00;

    public vendas(String nomeProduto, int qtd) {
        switch (nomeProduto) {
            case "x":
                receitaX += (precoX * qtd);
                quantidadeX += qtd;
                break;
            case "y":
                receitaY += (precoY * qtd);
                quantidadeY += qtd;
                break;
            case "z":
                receitaZ += (precoZ * qtd);
                quantidadeZ += qtd;
                break;
        }
    }

    public static int getQuantidadeX(){return quantidadeX;}
    public static int getQuantidadeY(){return quantidadeY;}
    public static int getQuantidadeZ(){return quantidadeZ;}
    public static double getReceitaX(){return receitaX;}
    public static double getReceitaY(){return receitaY;}
    public static double getReceitaZ(){return receitaZ;}
    public static int getQuantidadeTotal(){return quantidadeX + quantidadeY + quantidadeZ;}
    public static double getReceitaTotal(){return receitaX + receitaY + receitaZ;}
}