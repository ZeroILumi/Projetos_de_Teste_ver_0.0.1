using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.Linq;
using System.Threading.Tasks;

namespace APICatalogoJogos.InputModel
{
    public class JogoInputModel
    {
        [Required]
        [StringLength(100, MinimumLength = 3, ErrorMessage = "O Nome do Jogo deve conter de 3 a 100 caracteres" )]

        public string Nome { get; set; }

        [Required]
        [StringLength(100, MinimumLength = 1, ErrorMessage = "O Nome da Produtora do Jogo deve conter de 1 a 100 caracteres")]

        public string Produtora { get; set; }

        [Required]
        [Range(1, 1000, ErrorMessage = "O Preço do Jogo deve ser no mínimo R$1 e no máximo R$1000 escreva sem o R$")]

        public double Preco { get; set; }

    }
}
