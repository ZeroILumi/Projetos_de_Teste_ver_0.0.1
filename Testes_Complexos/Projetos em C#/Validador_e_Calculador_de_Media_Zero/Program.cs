using System;
using System.Globalization;

namespace Validador_e_Calculador_de_Media_Zero
{
    class Program
    {
        static void Main(string[] args)
        {
            int X = 1;
            int Xnota1 = 1;
            int Xnota2 = 1;
            string Nota1digitada = "1";
            string Nota2digitada = "1";
            var Nota1 = 1.1;
            var Nota2 = 1.1;
            string Y= "1";
            while(X == 1)
            { 
                while(Xnota1 == 1)
                {  
                    Console.WriteLine("Digite a primeira Nota de 0 a 10");
                    Nota1digitada = Console.ReadLine();
                    double Testenegativo = double.Parse(Nota1digitada);
                    while(Testenegativo != 1)
                    {
                        if(Testenegativo < 0)
                        {
                            Console.WriteLine("nota invalida");
                            Console.WriteLine("Digite a primeira Nota de 0 a 10");
                            Nota1digitada = Console.ReadLine();
                            Testenegativo = double.Parse(Nota1digitada);
                        }else
                        {
                            Testenegativo = 1;
                        }
                    }
                    Nota1 = double.Parse(Nota1digitada, NumberStyles.AllowDecimalPoint, NumberFormatInfo.InvariantInfo);

                    if(Nota1 < 0 || Nota1 > 10)
                    {
                    Console.WriteLine("nota invalida");
                    }else
                    {
                    Xnota1 = 0;
                    }
                }

                while(Xnota2 == 1)
                {
                    Console.WriteLine("Digite a segunda Nota de 0 a 10");
                    Nota2digitada = Console.ReadLine();
                    double Testenegativo = double.Parse(Nota2digitada);
                    while(Testenegativo != 1)
                    {
                        if(Testenegativo < 0)
                        {
                            Console.WriteLine("nota invalida");
                            Console.WriteLine("Digite a segunda Nota de 0 a 10");
                            Nota2digitada = Console.ReadLine();
                            Testenegativo = double.Parse(Nota1digitada);
                        }else
                        {
                            Testenegativo = 1;
                        }
                    }

                    Nota2 = double.Parse(Nota2digitada, NumberStyles.AllowDecimalPoint, NumberFormatInfo.InvariantInfo);

                    if(Nota2 < 0 || Nota2 > 10)
                    {
                        Console.WriteLine("nota invalida");
                    }else
                    {
                         Xnota2 = 0;
                    }
                }
                double media = (Nota1 + Nota2)/2;
                Console.WriteLine($"media = {media.ToString("N2")}");
            
                Console.WriteLine("novo calculo (1-sim 2-nao)");
                Y = Console.ReadLine();
                while(Y != "1")
                {
                    if(Y == "2")
                    {   
                        Console.WriteLine("Obrigado por usar nosso sistema de calculo de notas");
                        return;
                    }else if(Y != "1")
                    {
                        Console.WriteLine("Opção invalida escolha 1 ou 2");
                        Console.WriteLine("novo calculo (1-sim 2-nao)");
                        Y = Console.ReadLine();
                    }
                    Xnota1 = 1;
                    Xnota2 = 1;
                    X = int.Parse(Y); 
                }  
            }
        }
    }
}
