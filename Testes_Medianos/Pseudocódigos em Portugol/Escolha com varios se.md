//Função deste algoritmo: Escolher entre 4 opções com o if
//Autor: Aquiles Mauro (Zero ILumi)

programa
{
	
	funcao inicio()
	{
	escreva("1- Abrir Netflix" + "\n"+ "2- Abrir Amazon Prime Video" + "\n"+ "3- Abrir HBO GO" + "\n"+"4- Sair")
	inteiro menu = 0
	escreva("\n"+"Qual opção você quer:")
	leia(menu)
	 	se(menu==1)
	 	{
	 	escreva("\n"+"Abrindo Netflix")
	 	}
	 		se(menu==2)
	 		{
	 		escreva("\n"+"Abrindo Amazon Prime Video")	
	 		}
	 			se(menu==3)
	 			{
	 			escreva("\n"+"Abrindo HBO GO")
	 			}
	 				se(menu==4)
	 				{
	 				escreva("\n"+"Saindo do menu")
	 				}	
	}
}