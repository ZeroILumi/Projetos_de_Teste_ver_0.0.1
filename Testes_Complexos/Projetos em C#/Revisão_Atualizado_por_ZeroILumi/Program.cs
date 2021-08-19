using System;

namespace Revisão
{
    class Program
    {
        static void Main(string[] args)
        {
            Aluno[] alunos = new Aluno[5];
            var indiceALuno = 0;
            string opcaoUsuario = ObterOpcaoUsuario();
          
            while (opcaoUsuario != "X")
            {
                switch(opcaoUsuario)
                {
                    case "1":
                        Console.WriteLine("Informe o Nome do aluno a ser inserido no sistema:");
                        var aluno = new Aluno();
                        aluno.Nome = Console.ReadLine();
                        Console.WriteLine();
                        Console.WriteLine("Informe a Nota deste aluno:");
                        if(decimal.TryParse(Console.ReadLine(), out decimal nota))
                        {
                            aluno.Nota = nota;
                        }
                        else
                        {
                            throw new ArgumentException("Informe um numero Decimal para a Nota");
                        }
                        alunos[indiceALuno] = aluno;
                        indiceALuno++;
                        break;
                    case "2":
                        foreach(var a in alunos)
                        {
                            if(!string.IsNullOrEmpty(a.Nome))
                            {
                                Conceito conceitoIndividual;
                                if(a.Nota < 2)
                                {
                                    conceitoIndividual = Conceito.F;
                                }
                                else if(a.Nota < 4)
                                {
                                    conceitoIndividual = Conceito.E;
                                }
                                else if(a.Nota < 6)
                                {
                                    conceitoIndividual = Conceito.C;
                                }
                                else if(a.Nota < 8)
                                {
                                    conceitoIndividual = Conceito.B;
                                }
                                else
                                {
                                    conceitoIndividual = Conceito.A;
                                }    
                                Console.WriteLine($"Aluno: {a.Nome} Nota: {a.Nota} Conceito: {conceitoIndividual}");
                                Console.WriteLine();
                            }
                        }
                        break;
                    case "3":
                        decimal notaTotal = 0;
                        var nmrAlunos = 0;
                        for (int i = 0; i < alunos.Length; i++)
                        {
                            if(!string.IsNullOrEmpty(alunos[i].Nome))
                            {
                                notaTotal = notaTotal + alunos[i].Nota;
                                nmrAlunos++;
                            }
                        }
                        var mediaGeral = notaTotal / nmrAlunos;
                        Conceito conceitoGeral;
                        if(mediaGeral < 2)
                        {
                            conceitoGeral = Conceito.F;
                        }
                        else if(mediaGeral < 4)
                        {
                            conceitoGeral = Conceito.E;
                        }
                        else if(mediaGeral < 6)
                        {
                            conceitoGeral = Conceito.C;
                        }
                        else if(mediaGeral < 8)
                        {
                            conceitoGeral = Conceito.B;
                        }
                        else
                        {
                            conceitoGeral = Conceito.A;
                        }                  
                        Console.WriteLine($"A Media Geral e :{mediaGeral} e o Conceito e {conceitoGeral}");
                        break;
                    default:
                        throw new ArgumentOutOfRangeException();
                }
                opcaoUsuario = ObterOpcaoUsuario();
            }
            Console.WriteLine("Xau ate mais");
        }
        private static string ObterOpcaoUsuario()
        {
            Console.WriteLine();
            Console.WriteLine("Informe a opção desejada:");
            Console.WriteLine("1- Inserir novo aluno");
            Console.WriteLine("2- Listar alunos");
            Console.WriteLine("3- Calcular Media Geral");
            Console.WriteLine("X- Sair");
            Console.WriteLine();
            string opcaoUsuario = Console.ReadLine();
            Console.WriteLine();
            return opcaoUsuario.ToUpper();
        }
    }
}
