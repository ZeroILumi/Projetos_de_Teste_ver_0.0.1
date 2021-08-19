using System;

namespace Classes_e_Objetos
{
    class Program
    {
        static void Main(string[] args)
        {
            Produto[] produtos = new Produto[5];
            var IndexProduto = 0;

            string opcaoEscolhida = MenuCompras();

            while(opcaoEscolhida.ToUpper() != "X")
            {
                switch(opcaoEscolhida)
                {
                    case "1":
                        Console.WriteLine("Informe o Codigo do Produto a ser Inserido");
                        Produto produto = new Produto();
                        if(int.TryParse(Console.ReadLine(), out int numerodoCodigodoProduto))
                        {
                            produto.Codigo = numerodoCodigodoProduto;
                        }
                        else
                        {
                            throw new ArgumentException("Informe um valor Numerico");
                        }
                        Console.WriteLine("Informe o Nome do Produto a ser Inserido");
                        produto.Nome = Console.ReadLine();
                        Console.WriteLine("Informe o Preço do Produto a ser Inserido");
                        if(decimal.TryParse(Console.ReadLine(), out decimal precodoProduto))
                        {
                            produto.Preco = precodoProduto;
                        }
                        else
                        {
                            throw new ArgumentException("Informe um valor Decimal");
                        }
                        produtos[IndexProduto] = produto;
                        IndexProduto++;
                        break;
                    case "2":
                        foreach(var p in produtos)
                        {
                            if(!string.IsNullOrEmpty(p.Nome))
                            {
                                Console.WriteLine($" Codigo: {p.Codigo} Nome: {p.Nome} Preço: {p.Preco}");
                                Console.WriteLine();
                            }
                        }
                        break;
                    default:
                        throw new ArgumentOutOfRangeException("Escolha 1 ou 2");
                }
                opcaoEscolhida = MenuCompras();    
            }
            Console.WriteLine("Xau");



        }
        private static string MenuCompras()
        {
            Console.WriteLine("Informe a opção desejada");
            Console.WriteLine("1- Inserir novo produto");
            Console.WriteLine("2- Listar Produtos");
            Console.WriteLine("X- Sair");
            Console.WriteLine();
            string opcaoEscolhida = Console.ReadLine();
            Console.WriteLine();
            return opcaoEscolhida.ToUpper();
        }
    }
}

