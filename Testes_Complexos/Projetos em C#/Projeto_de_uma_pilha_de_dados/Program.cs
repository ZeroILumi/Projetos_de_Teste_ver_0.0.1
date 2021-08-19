using System;
using EstruturaDoPrograma.Exemplos;

namespace EstruturaDoPrograma
{
    class Program
    {
        static void Main()
        {
        var s = new Pilha();
        s.Empilha(1);
        s.Empilha(10);
        s.Empilha(100);
        Console.WriteLine($"O iten no topo: {s.Desempilha()} é desempilhado");
        Console.WriteLine($"O iten no topo: {s.Desempilha()} é desempilhado");
        Console.WriteLine($"O iten no topo: {s.Desempilha()} é desempilhado");
        }
    }
}
