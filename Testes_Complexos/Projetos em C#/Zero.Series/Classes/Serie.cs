using System;    
    
    namespace Zero.Series
    {
        public class Serie : EntidadeBase
        {

            //Atributos

            private Genero Genero { get; set; }

            private string Titulo { get; set; }

            private string Descricao { get; set; }

            private int Ano { get; set; }

            private bool Excluido { get; set; }

            public Serie(int id, Genero genero, string titulo, string descricao, int ano)
            {

                this.Id = id;

                this.Genero = genero;

                this.Titulo = titulo;

                this.Descricao = descricao;

                this.Ano = ano;

                this.Excluido = false;

            }

            public override string ToString()
            {
            
                string retorno = "";

                retorno += "Genero: " + this.Genero + Environment.NewLine;

                retorno += "Titulo: " + this.Titulo + Environment.NewLine;

                retorno += "Descricao: " + this.Descricao + Environment.NewLine;

                retorno += "Ano: " + this.Ano + Environment.NewLine;

                retorno += "Excluido: " + this.Excluido;

                return retorno;

            }

            public string retornaTitulo()
            {

                return this.Titulo;    

            }

            public int retornaId()
            {

                return this.Id;

            }

            public bool retornaExcluido()
            {

                return Excluido;

            }





            public void Excluir()
            {

                this.Excluido = true;

            }


        }

    }