using System;    
    
    
    
    namespace Zero.Series
    {
        public class Menu
        {
            SerieRepositorio repositorio = new SerieRepositorio();
            public Serie MenuInserirSerie()
            {
                Console.WriteLine("Inserir Série");
                    
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

                Serie novaSerie = new Serie(
                    id: repositorio.Proximoid(),
                    genero: (Genero)entradaGenero,
                    titulo: entradaTitulo,
                    descricao: entradaDescricao,
                    ano: entradaAno
                    );

                return novaSerie;


            }

        }
    }