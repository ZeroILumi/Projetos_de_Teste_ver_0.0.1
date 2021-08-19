using System;

namespace Classes_e_Objetos
{
    class Program
    {
        static void Main(string[] args)
        {
            Produto[] produtos = new Produto[5];
            Produto produto0 = new Produto();
            Produto produto1 = new Produto();
            Produto produto2 = new Produto();
            Produto produto3 = new Produto();
            Produto produto4 = new Produto();
            string opcaoEscolhida = MenuCompras();


            while(opcaoEscolhida.ToUpper() != "X")
            {
                switch(opcaoEscolhida)
                {
                    case "1":
                        if(string.IsNullOrEmpty(produto0.Nome))
                        {
                            for(int IndexProduto = 0; IndexProduto < produtos.Length; IndexProduto++)
                            {
                                produto0.Codigo = 0;
                                produto0.Nome = "vasio";
                                produto0.Preco = 0;
                                produtos[IndexProduto] = produto0;
                                IndexProduto++;
                                produto1.Codigo = 0;
                                produto1.Nome = "vasio";
                                produto1.Preco = 0;
                                produtos[IndexProduto] = produto1;
                                IndexProduto++;
                                produto2.Codigo = 0;
                                produto2.Nome = "vasio";
                                produto2.Preco = 0;
                                produtos[IndexProduto] = produto2;
                                IndexProduto++;
                                produto3.Codigo = 0;
                                produto3.Nome = "vasio";
                                produto3.Preco = 0;
                                produtos[IndexProduto] = produto3;
                                IndexProduto++;
                                produto4.Codigo = 0;
                                produto4.Nome = "vasio";
                                produto4.Preco = 0;
                                produtos[IndexProduto] = produto4;
                                IndexProduto++;
                            }
                        }
                        if(produto0.Nome == "vasio")
                        {
                            Console.WriteLine("Informe o Codigo do Produto a ser Inserido");
                            if(int.TryParse(Console.ReadLine(), out int numerodoCodigodoProduto0))
                            {
                                produto0.Codigo = numerodoCodigodoProduto0;
                            }
                            else
                            {   
                                throw new ArgumentException("Informe um valor Numerico");
                            }
                            Console.WriteLine("Informe o Nome do Produto a ser Inserido");
                            produto0.Nome = Console.ReadLine();
                            Console.WriteLine("Informe o Preço do Produto a ser Inserido");
                            if(decimal.TryParse(Console.ReadLine(), out decimal precodoProduto0))
                            {
                                produto0.Preco = precodoProduto0;
                            }
                            else
                            {
                             throw new ArgumentException("Informe um valor Decimal");
                            }
                        }
                            if(produto0.Nome != "vasio" & produto1.Nome != "vasio" & produto2.Nome != "vasio" & produto3.Nome != "vasio" & produto4.Nome != "vasio")
                            {
                                Console.WriteLine("Não e Possivel adicionar mais produtos pois o carinho de compras ja esta cheio");
                                break;
                            }
                            string querInserirOutroProduto = InserirOutroProduto();
                            if(querInserirOutroProduto == "S" & produto1.Nome == "vasio")
                            {
                                Console.WriteLine("Informe o Codigo do Produto a ser Inserido");
                                if(int.TryParse(Console.ReadLine(), out int numerodoCodigodoProduto1))
                                {
                                    produto1.Codigo = numerodoCodigodoProduto1;
                                }
                                else
                                {   
                                    throw new ArgumentException("Informe um valor Numerico");
                                }
                                Console.WriteLine("Informe o Nome do Produto a ser Inserido");
                                produto1.Nome = Console.ReadLine();
                                Console.WriteLine("Informe o Preço do Produto a ser Inserido");
                                if(decimal.TryParse(Console.ReadLine(), out decimal precodoProduto1))
                                {
                                    produto1.Preco = precodoProduto1;
                                }
                                else
                                {
                                throw new ArgumentException("Informe um valor Decimal");
                                }
                            }
                            else
                            {
                                break;
                            }
                            querInserirOutroProduto = InserirOutroProduto();
                            if(querInserirOutroProduto == "S" & produto2.Nome == "vasio")
                            {
                                Console.WriteLine("Informe o Codigo do Produto a ser Inserido");
                                if(int.TryParse(Console.ReadLine(), out int numerodoCodigodoProduto2))
                                {
                                    produto2.Codigo = numerodoCodigodoProduto2;
                                }
                                else
                                {   
                                    throw new ArgumentException("Informe um valor Numerico");
                                }
                                Console.WriteLine("Informe o Nome do Produto a ser Inserido");
                                produto2.Nome = Console.ReadLine();
                                Console.WriteLine("Informe o Preço do Produto a ser Inserido");
                                if(decimal.TryParse(Console.ReadLine(), out decimal precodoProduto2))
                                {
                                    produto2.Preco = precodoProduto2;
                                }
                                else
                                {
                                    throw new ArgumentException("Informe um valor Decimal");
                                }
                            }
                            else
                            {
                                break;
                            }
                            querInserirOutroProduto = InserirOutroProduto();
                            if(querInserirOutroProduto == "S" & produto3.Nome == "vasio")
                            {
                                Console.WriteLine("Informe o Codigo do Produto a ser Inserido");
                                if(int.TryParse(Console.ReadLine(), out int numerodoCodigodoProduto3))
                                {
                                    produto3.Codigo = numerodoCodigodoProduto3;
                                }
                                else
                                {   
                                    throw new ArgumentException("Informe um valor Numerico");
                                }
                                Console.WriteLine("Informe o Nome do Produto a ser Inserido");
                                produto3.Nome = Console.ReadLine();
                                Console.WriteLine("Informe o Preço do Produto a ser Inserido");
                                if(decimal.TryParse(Console.ReadLine(), out decimal precodoProduto3))
                                {
                                    produto3.Preco = precodoProduto3;
                                }
                                else
                                {
                                    throw new ArgumentException("Informe um valor Decimal");
                                }
                            }
                            else
                            {
                                break;
                            }
                            querInserirOutroProduto = InserirOutroProduto();
                            if(querInserirOutroProduto == "S" & produto4.Nome == "vasio")
                            {
                                Console.WriteLine("Informe o Codigo do Produto a ser Inserido");
                                if(int.TryParse(Console.ReadLine(), out int numerodoCodigodoProduto4))
                                {
                                    produto4.Codigo = numerodoCodigodoProduto4;
                                }
                                else
                                {   
                                    throw new ArgumentException("Informe um valor Numerico");
                                }
                                Console.WriteLine("Informe o Nome do Produto a ser Inserido");
                                produto4.Nome = Console.ReadLine();
                                Console.WriteLine("Informe o Preço do Produto a ser Inserido");
                                if(decimal.TryParse(Console.ReadLine(), out decimal precodoProduto4))
                                {
                                    produto4.Preco = precodoProduto4;
                                }
                                else
                                {
                                throw new ArgumentException("Informe um valor Decimal");
                                }
                            }
                        break;
                    case "2":
                        foreach(var p in produtos)
                        {    
                                Console.WriteLine($" Codigo: {p.Codigo} Nome: {p.Nome} Preço: {p.Preco}");
                                Console.WriteLine();
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
        private static string InserirOutroProduto()
        {
            Console.WriteLine("Quer Colocar outro Produto?:");
            Console.WriteLine("S (para sim)");
            Console.WriteLine("N (para não)");
            string querInserirOutroProduto = Console.ReadLine();
            return querInserirOutroProduto.ToUpper();
        }
    }
}

