def soma(*args):
    print(sum(args))


def valor_de_args(*argumentos):
    print(f"args {argumentos}")
    for args in argumentos:
        print(f"{args}")


def filmes_favoritos(*filmes):
    print("\n Meus Filmes Favoritos:")
    for i, filme in enumerate(filmes, start=1):
        print(f"\t{i}. {filme}")


def filmes_favoritos_da_pessoa(nome_da_pessoa, *filmes):
    print(f"\nOs Filmes Favoritos do(a) {nome_da_pessoa} são:")
    for i, filme in enumerate(filmes, start=1):
        print(f"\t{i}. {filme}")


def testando_kwargs(**kwargs):
    print(f"kwargs {kwargs}")
    for key, value in kwargs.items():
        print(key, value)


def favoritos_da_pessoa(nome_da_pessoa, **kwargs):
    print(f"\nOs Favoritos do(a) {nome_da_pessoa} são:")
    for key, value in kwargs.items():
        chave = key.replace("_", " ").capitalize()
        valor = value.capitalize()
        print(f"\t-{chave}: {valor}")


def parametros(x, *args, **kwargs):
    print(f"\nx e {x}")
    print("\nOs args são:")
    for i, arg in enumerate(args, start=1):
        print(f"\t{i}. {arg}")
    print("\nOs kwargs são:")
    for key, value in kwargs.items():
        chave = key.replace("_", " ").capitalize()
        valor = value.capitalize()
        print(f"\t{chave}: {valor}")


dicionario_1 = {
    "Anime": "Pokemon",
    "Numero": 100,
    "Tipo": "Gelo"
}


def leitor_de_dicionarios_kwargs(**kwargs):
    print("\nO conteudo desse dicionario é:")
    for key, value in kwargs.items():
        print(f"\t-{key}: {value}")


lista_1 = [
    "Genshin Impact",
    "Lendario",
    "Bacon"
]


def leitor_de_listas_args(*args):
    print(f"\nO conteudo da sua lista é:")
    for arg in args:
        print(f"\t-{arg}")


primeiro, *valores_do_meio, ultimo = lista_1

if __name__ == "__main__":
    soma(10, 10)
    soma(20, 40, 70, 500)
    valor_de_args("teste 1", "Eae")
    filmes_favoritos("Batman", "Yugioh")
    filmes_favoritos_da_pessoa("Zero ILumi", "Batman", "Yugioh")
    testando_kwargs(nome="Zero", idade="22", linguagens_de_progamacao=["Python", "C#"])
    favoritos_da_pessoa("Zero ILumi",
                        tipo_de_jogo="anime",
                        trabalho="progamador",
                        comida="tilapia")
    parametros("Teste", "Argumento", "Teste2", Yugioh="Duel links", Anime="Pokemon")
    leitor_de_dicionarios_kwargs(**dicionario_1)
    leitor_de_listas_args(*lista_1)
    leitor_de_listas_args(*valores_do_meio)
