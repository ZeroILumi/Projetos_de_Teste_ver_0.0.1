//Função deste algoritmo: Mostrar o nome, cidade , e telefone das pessoas inventadas através da matriz 
//pessoa_cidade_telefone criase dinamicamente através de seu conteúdo atual 3 linhas e 3 colunas e através
//da var contador controla o numero de repetições do, do while e controlar o numero das linhas sendo necessario
//somente as colunas ser escritas
//Autor: Aquiles Mauro (Zero ILumi)

programa
{
	
	funcao inicio()
	{
     inteiro contador = 0
		cadeia pessoa_cidade_telefone[][]= 
		{
		{"João","São Paulo","(11)9999-5241"}
		,
		{"Maria","Ribeirão Preto","(16)9999-8596"}
		,
		{"Ana","Manaus","(92)9999-8574"}
		}
			faca
			{
			escreva(" Pessoa: "+
			pessoa_cidade_telefone[contador][0] 
			+
			" Cidade :" 
			+ 
			pessoa_cidade_telefone[contador][1] 
			+
			" Numero de Telefone "+pessoa_cidade_telefone[contador][2] 
			+
			"\n")	
			contador ++	
			}enquanto(contador<=2)
	}

}