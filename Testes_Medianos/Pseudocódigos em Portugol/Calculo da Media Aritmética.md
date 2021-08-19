//Função deste algoritmo: calcular a média aritmética 
//Autor: Aquiles Mauro (Zero ILumi)

programa
{
	

	funcao inicio()
	{
	mediaaritmeticafuncional()		
	}
		funcao mediaaritmeticafuncional()
		{
		real nota1, nota2 ,nota3 ,nota4 , mediaaritmetica	
		cadeia aluno
		escreva("Digite o nome do aluno que deseja verificar a media aritmetica: ")
		leia(aluno)
		escreva("Digite a 1 primeita nota do aluno entitulado como "+aluno+":")
		leia(nota1)
		escreva("Digite a 2 segunda nota do aluno entitulado como "+aluno+":")10
		leia(nota2)
		escreva("Digite a 3 terceira nota do aluno entitulado como "+aluno+":")
		leia(nota3)
		escreva("Digite a 4 quarta nota do aluno entitulado como "+aluno+":")
		leia(nota4)
		mediaaritmetica = (nota1+nota2+nota3+nota4)/4
			escreva("A media do aluno entitulado como "+aluno+" é: "+mediaaritmetica+"  ")
			se(mediaaritmetica>=7)
			{	
			escreva("\n"+aluno+" foi aprovado ")
			}
				senao 
				{
				escreva("\n"+aluno+" foi reprovado ")
				}
		}
}