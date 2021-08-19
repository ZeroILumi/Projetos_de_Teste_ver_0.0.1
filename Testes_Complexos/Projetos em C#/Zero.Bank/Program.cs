using System;
using System.Collections.Generic;

namespace Zero.Bank
{
    class Program
    {
        static List<Conta> listContas = new List<Conta>();


        static void Main(string[] args)
        {
            string opcaoUsuario = ObterOpcaoUsuario();
            while(opcaoUsuario.ToUpper() != "X")
            {
                switch(opcaoUsuario)
                {
                    case "1":
                        ListarContas();
                        break;
                    
                    case "2":
                        InserirNovaConta();
                        break;
                    
                    case "3":
                        Transferir();
                        break;
                    
                    case "4":
                        Sacar();
                        break;
                    
                    case "5":
                        Depositar();
                        break;
                    
                    case "C":
                        Console.Clear();
                        break;
                    
                    default:
                        throw new ArgumentOutOfRangeException();
                }  
                opcaoUsuario = ObterOpcaoUsuario();
            }
            Console.WriteLine("Obrigado por utilizar nossos serviços.");

            Console.ReadLine();
        }
        public static string ObterOpcaoUsuario()
        {
            Console.WriteLine();

            Console.WriteLine("Zero Bank ao seu dispor ! ! !");

            Console.WriteLine("Escreva a opção desejada");

            Console.WriteLine("1- Listar contas");

            Console.WriteLine("2- Inserir uma nova conta");

            Console.WriteLine("3- Transferir");

            Console.WriteLine("4- Sacar");

            Console.WriteLine("5- Depositar");

            Console.WriteLine("C- Limpar Tela");

            Console.WriteLine("X- Sair");

            Console.WriteLine();

            string opcaoUsuario = Console.ReadLine().ToUpper();

            Console.WriteLine();

            return opcaoUsuario;

        }
        private static void InserirNovaConta()
        {
            Console.WriteLine("Inserir Nova Conta");

            Console.WriteLine("Digite 1 para Pessoa_Fisica ou 2 para Pessoa_Juridica: ");
            int entradaTipoConta = int.Parse(Console.ReadLine());

            Console.WriteLine("Digite o Nome do Cliente: ");
            string entradaNome = Console.ReadLine();

            Console.WriteLine("Digite o saldo inicial: ");
            double entradaSaldo = double.Parse(Console.ReadLine());

            Console.WriteLine("Digite o credito inicial: ");
            double entradaCredito = double.Parse(Console.ReadLine());

            Conta novaConta = new Conta
            (
                tipoConta: (TipoConta)entradaTipoConta,
                saldo: entradaSaldo,
                credito: entradaCredito,
                nome: entradaNome
            );

            listContas.Add(novaConta);

        }
        private static void ListarContas()
        {
            Console.WriteLine("Listar Contas");

            if(listContas.Count == 0)
            {
                Console.WriteLine("Nenhuma conta cadastrada");
                return;
            }

            for(int i= 0; i < listContas.Count; i++)
            {
                Conta conta = listContas[i];
                Console.WriteLine($"#{i} -");
                Console.WriteLine($"{conta}");
            }

        }

        private static void Sacar()
        {
            Console.WriteLine("Digite o Numero da Conta a qual sera efetuado o Saque");
            int indexConta = int.Parse(Console.ReadLine());

            Console.WriteLine("Digite o valor a ser Sacado");
            double valorSaque = double.Parse(Console.ReadLine());

            listContas[indexConta].Sacar(valorSaque);
        }
        private static void Depositar()
        {
            Console.WriteLine("Digite o Numero da Conta a qual recebera o Deposito");
            int indexConta = int.Parse(Console.ReadLine());

            Console.WriteLine("Digite o Valor a ser Depositado");
            double valorDepositado = double.Parse(Console.ReadLine());

            listContas[indexConta].Depositar(valorDepositado);

        }
        private static void Transferir()
        {
            Console.WriteLine("Digite o Numero da Conta que irá transferir seu Saldo (origin)");
            int indexContaRaiz = int.Parse(Console.ReadLine());

            Console.WriteLine("Digite o Numero da Conta que recebera a transferencia (destino)");
            int indexContaDestino = int.Parse(Console.ReadLine());

            Console.WriteLine("Digite o Valor a ser Transferido");
            double valorTransferido = double.Parse(Console.ReadLine());

            listContas[indexContaRaiz].Transferir(valorTransferido, listContas[indexContaDestino]);

        }
    }
}
