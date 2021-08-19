//Função deste algoritmo: calcular a média aritmética do total das vendas do primeiros 4 meses do ano
//Autor: Aquiles Mauro (Zero ILumi)

programa
{
	

	funcao inicio()
	{
	MediaAritmeticadasvendas()
	}
	funcao MediaAritmeticadasvendas()
		{
		real janeiro, fevereiro, marco, abril
		real MediaAritmeticadototaldevendas
		escreva("Digite o Total de lucro em janeiro:")
		leia(janeiro)
		escreva("Digite o Total de lucro em fevereiro:")
		leia(fevereiro)
		escreva("Digite o Total de lucro em março:")
		leia(marco)
		escreva("Digite o Total de lucro em abril:")
		leia(abril)
		MediaAritmeticadototaldevendas = (janeiro+fevereiro+marco+abril)/4
			se(MediaAritmeticadototaldevendas>=70)
			{	
			escreva("A media de suas venda foi: "+MediaAritmeticadototaldevendas+"  "+ "Parabéns você rebera um abono salarial de 10%")	
			}
	 				senao
	 				{
	 				escreva("A media de suas venda foi: "+MediaAritmeticadototaldevendas+"  "+ "Você recebera um abono salarial de 3%")
	 				}
		}
}