//Função deste algoritmo: através do do while, permitir ao usuário escolher qual tabuada ele que o multiplicador máximo
//Autor: Aquiles Mauro (Zero ILumi)

programa
{
	

	funcao inicio()
	{
	 inteiro contador, limite, resultado, qualtabuada
	 contador = 0
	 limite = 10
	 escreva("qual tabuada você quer: ")
	 leia(qualtabuada)
	 escreva("qual o limite você quer de multiplicador: ")
	 leia(limite)
	 		faca
	 		{
	      	resultado = qualtabuada*contador
	      	escreva("\n"+qualtabuada+"x"+contador+"="+resultado)
	      	contador ++
	 		}enquanto(contador<=limite)
	}
}