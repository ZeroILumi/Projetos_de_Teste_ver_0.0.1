//Função deste algoritmo: Inserir numa matriz chamada cesta 4 indíces para as linha e 2 indíces nas colunas mas 
//de maneira adptativa ao conteúdo da matriz, a através da var contador eu controlo tanto o numero de repetiçoes
//do, do while tanto controlo o indíce referente as linhas trocando manualmente somente as colunas
//Autor: Aquiles Mauro (Zero ILumi)

programa
{
	
	funcao inicio()
	{
	inteiro contador=0
		cadeia cesta[][] = 
		{
		{"Pera","100"}
		,
		{"Jaca","200"}
		,
		{"Maça","900"}
		,
		{"Uva","89"}
		}
			faca
			{
			escreva(" Produto: "
			+
			cesta[contador][0] 
			+ 
			" Quantidade: " 
			+ 
			cesta[contador][1] 
			+ 
			"\n")	
			contador ++
			}enquanto(contador<=3)
	}
}