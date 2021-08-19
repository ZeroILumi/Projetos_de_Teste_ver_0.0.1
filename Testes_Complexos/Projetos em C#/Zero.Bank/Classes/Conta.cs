using System;

namespace Zero.Bank
{
    public class Conta
    {
        private TipoConta TipoConta { get; set; }
        
        private double Saldo { get; set; }

        private double Credito { get; set; }

        private string Nome { get; set; }

        public Conta(TipoConta tipoConta, double saldo, double credito, string nome)
        {
            this.TipoConta = tipoConta;

            this.Saldo = saldo;

            this.Credito = credito;

            this.Nome = nome;
        }

        public bool Sacar(double valorSaque)
        {

            //Validação para verificar se tem Saldo Suficiente na Conta do Cliente
            if(this.Saldo - valorSaque < (this.Credito * -1))
            {
                Console.WriteLine("Saldo insuficiente");

                return false;
            }
            this.Saldo -= valorSaque;

            Console.WriteLine($"Foi Sacado um total de {valorSaque} da Conta de {this.Nome}");

            Console.WriteLine($"Saldo Atual da Conta de {this.Nome} agora é {this.Saldo}");

            return true;
        }
        public double Depositar(double valorDepositado)
        {
            this.Saldo += valorDepositado;

            Console.WriteLine($"Foi Depositado um Total de {valorDepositado} na Conta de {this.Nome}");

            Console.WriteLine($"Saldo Atual da conta de {this.Nome} agora é {this.Saldo}");

            return this.Saldo;
        }

        public void Transferir(double valorTransferido, Conta contaDestino)
        {
            if(this.Sacar(valorTransferido))
            {
                contaDestino.Depositar(valorTransferido);

                Console.WriteLine($"Um Total de {valorTransferido} foi Transferido de {this.Nome} para {contaDestino.Nome}");

                Console.WriteLine($"Saldo Atual da conta de {this.Nome} agora é {this.Saldo}");
                
            }
        }
        public override string ToString()
        {
            string retorno = "";
            retorno += "TipoConta: " + this.TipoConta + " | ";
            retorno += "Nome: " + this.Nome + " | ";
            retorno += "Saldo: " + this.Saldo + " | ";
            retorno += "Credito: " + this.Credito ;
            return retorno;
        }


    }
}