using System;
using System.Collections.Generic;

namespace Zero.Series
{
    class Program
    {
        static SerieRepositorio repositorio = new SerieRepositorio();

        static Menu Menu = new Menu();

        static void Main(string[] args)
        {

            SerieRepositorio listaSerie = new SerieRepositorio();

            string opcao_do_Usuario = Obter_Opcao_Usuario();

            while(opcao_do_Usuario.ToUpper() != "X")
            {

                switch(opcao_do_Usuario)
                {

                    case "1":

                        ListarSeries();

                        break;

                    case "2":

                        InserirSerie();

                        break;

                    case "3":

                        AtualizarSerie();

                        break;

                    case "4":

                        ExcluirSerie();

                        break;

                    case "5":

                        VisualizarSerie();

                        break;

                    case "C":

                        Console.Clear();
                        
                        break;

                    default:

                        throw new ArgumentOutOfRangeException();
                }
        
                opcao_do_Usuario = Obter_Opcao_Usuario();

            }

            Console.WriteLine("Obrigado por usar nossos serviços");
            Console.ReadLine();

        }

        private static void ListarSeries()
        {

            Console.WriteLine("Listar séries");

            var lista = repositorio.Lista();

            if( lista.Count == 0)
            {

                Console.WriteLine("Nenhuma série esta cadastrada");
                return;

            }

            foreach( var serie in lista)
            {
                var excluido = serie.retornaExcluido();

                    Console.WriteLine("#ID {0}: - {1} {2}", serie.retornaId(), serie.retornaTitulo(), (excluido ? "*Excluido*" : ""));
     
            }    

        }

        private static void InserirSerie()
        {
   
            repositorio.Insere(Menu.MenuInserirSerie());

        }

        private static void AtualizarSerie()
        {

            Console.WriteLine("Atualizar Série");

            Console.WriteLine("Escreva o ID da serie a qual deseja atualizar seu conteudo");

            int indiceserie = int.Parse(Console.ReadLine());

            Console.WriteLine("Inserir série");

            foreach(int i in Enum.GetValues(typeof(Genero)))
            {

                Console.WriteLine("{0}-{1}", i, Enum.GetName(typeof(Genero), i));

            }

            Console.WriteLine("Digite o genêro da Série entre as opçoes acima: ");

            int entradaGenero = int.Parse(Console.ReadLine());

            Console.WriteLine("Digite o Título da Série: ");

            string entradaTitulo = Console.ReadLine();

            Console.WriteLine("Digite o Ano de Inicio da Série: ");

            int entradaAno = int.Parse(Console.ReadLine());

            Console.WriteLine("Digite a Descrição da Série: ");

            string entradaDescricao = Console.ReadLine();
            
            Serie atualizacaoSerie = new Serie(
                id: indiceserie,
                genero: (Genero)entradaGenero,
                titulo: entradaTitulo,
                descricao: entradaDescricao,
                ano: entradaAno
            );

            repositorio.Atualiza(id: indiceserie,objeto: atualizacaoSerie);

        }

        private static void ExcluirSerie()
        {

            Console.WriteLine("Excluir Série");

            Console.WriteLine("Digite o ID da Série da qual sera excluida");
            
            int indiceserie = int.Parse(Console.ReadLine());

            Console.WriteLine("Tem certeza que quer excluir do ID-{0}",indiceserie);

            Console.WriteLine("1- SIM");

            Console.WriteLine("2- NÃO");

            string confirmacao = Console.ReadLine();

            if(confirmacao.ToUpper() == "1")
            {

                repositorio.Exclui(id: indiceserie);

                return;

            }
            
            Console.WriteLine("Ok nada excluido");

            return;
        }

        private static void VisualizarSerie()
        {

            Console.WriteLine("Visualizar Série");

            Console.WriteLine("Digite o ID da série que quer visualizar");

            int indiceserie = int.Parse(Console.ReadLine());

            var serie = repositorio.RetornaPorId(id: indiceserie);

            Console.WriteLine(serie.ToString());

        }

        private static string Obter_Opcao_Usuario()
        {

            Console.WriteLine();    

            Console.WriteLine("Zero.Series ao seu Dispor");

            Console.WriteLine("Imforme a opção desejada: ");

            Console.WriteLine("1- Listar séries ");

            Console.WriteLine("2- Inserir nova série ");

            Console.WriteLine("3- Atualizar uma série ");

            Console.WriteLine("4- Excluir uma série ");

            Console.WriteLine("5- Visualizar uma série ");

            Console.WriteLine("C- Limpar Tela ");

            Console.WriteLine("X- Sair");

            Console.WriteLine();

            string opcao_do_Usuario = Console.ReadLine().ToUpper();

            Console.WriteLine();

            return opcao_do_Usuario;

        }


    }

}
