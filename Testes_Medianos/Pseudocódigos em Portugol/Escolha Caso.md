//Função deste algoritmo: Escolhe entre 4 opção com a estrutura do while, e mostrar Escolha 1,2,3 ou 4 caso nem uma seja escolhida
//Autor: Aquiles Mauro (Zero ILumi)

programa
{
	
	funcao inicio()
	{
	escreva("1- Abrir Netflix" + "\n"+ "2- Abrir Amazon Prime Video" + "\n"+ "3- Abrir HBO GO" + "\n"+"4- Sair")
	inteiro menu = 0
	escreva("\n"+"Qual opção você quer:")
	leia(menu)
	 	escolha(menu)
	 	{
	 	caso 1:
	 	escreva("\n"+"Abrindo Netflix")	
	 	pare
	 	caso 2:
	 	escreva("\n"+"Abrindo Amazon Prime Video")	
	 	pare
	 	caso 3:
	 	escreva("\n"+"Abrindo HBO GO")	
	 	pare
	 	caso 4:
	 	escreva("\n"+"Saindo do Menu")	
	 	pare
	 	caso contrario:
	 	escreva("\n"+"Escolha 1,2,3 ou 4")
	 	}	
	}
}