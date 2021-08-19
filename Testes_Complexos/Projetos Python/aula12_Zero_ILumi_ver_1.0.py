import requests


def retornar_dados_por_cep():
    Continuar = 0
    while Continuar == 0:
        try:
            INPUT_CEP = int(input('Digite o CEP que deseja consultar:\n'))
            response = requests.get(f'https://viacep.com.br/ws/{INPUT_CEP}/json/')
            status_da_conecao = response.status_code
            # print(response.text)

            # print(type(response.text))

            # print(response.json())

            # print(type(response.json()))

            if status_da_conecao == 200:

                dados_do_CEP = response.json()

                dado_CEP = dados_do_CEP['cep']

                dado_logradouro = dados_do_CEP['logradouro']

                dado_complemento = dados_do_CEP['complemento']

                dado_bairro = dados_do_CEP['bairro']

                dado_localidade = dados_do_CEP['localidade']

                dado_UF = dados_do_CEP['uf']

                dado_IBGE = dados_do_CEP['ibge']

                dado_GIA = dados_do_CEP['gia']

                dado_DDD = dados_do_CEP['ddd']

                dado_SIAFI = dados_do_CEP['siafi']

                print('O CEP Informado é {CEP}.'
                      ''.format(CEP=dado_CEP))

                print('O Logradouro Vinculado ao CEP: {CEP}, é: {logradouro}.'
                      ''.format(CEP=dado_CEP, logradouro=dado_logradouro))

                print('O Complemento Vinculado ao CEP: {CEP}, é: {complemento}.'
                      ''.format(CEP=dado_CEP, complemento=dado_complemento))

                print('O Bairro Vinculado ao CEP: {CEP}, é: {bairro}.'
                      ''.format(CEP=dado_CEP, bairro=dado_bairro))

                print('A Localidade Vinculada ao CEP: {CEP}, é: {localidade}.'
                      ''.format(CEP=dado_CEP, localidade=dado_localidade))

                print('A UF Vinculada ao CEP: {CEP}, é: {UF}.'
                      ''.format(CEP=dado_CEP, UF=dado_UF))

                print('O IBGE Vinculado ao CEP: {CEP}, é: {IBGE}.'
                      ''.format(CEP=dado_CEP, IBGE=dado_IBGE))

                print('O GIA Vinculado ao CEP: {CEP}, é: {GIA}.'
                      ''.format(CEP=dado_CEP, GIA=dado_GIA))

                print('O DDD Vinculado ao CEP: {CEP}, é: {DDD}.'
                      ''.format(CEP=dado_CEP, DDD=dado_DDD))

                print('O SIAFI Vinculado ao CEP: {CEP}, é: {SIAFI}.'
                      ''.format(CEP=dado_CEP, SIAFI=dado_SIAFI))
            else:
                print('CEP Invalido')
            Continuar_opcao = int(input('Continuar? 1=Sim 2=Não\n'))
            if Continuar_opcao == 1:
                pass
            if Continuar_opcao == 2:
                Continuar = 2
                print('Obrigado por usufruir do sistema do CEP_Zero')
        except ValueError:
            print('Valor Invalido, Digite um número para o CEP.')


def retornar_pokemon(nome_do_pokemon):
    resposta = requests.get(
        'https://pokeapi.co/api/v2/pokemon/{nome_do_pokemon}/'.format(nome_do_pokemon=nome_do_pokemon))
    status_da_conecao = resposta.status_code
    dados_do_pokemon = resposta.json()
    print(status_da_conecao)
    if status_da_conecao == 200:
        return dados_do_pokemon



def retornar_response(url):
    responce = requests.get(url)
    status_da_conecao = responce.status_code
    print(status_da_conecao)
    if status_da_conecao == 200:
        return responce.text


if __name__ == '__main__':
    # input_nome_do_pokemon = input('Digite o nome do pokemon a ser acessado dados sobre:\n')
    # dados_do_pokemon = retornar_pokemon('pikachu')
    # print(dados_do_pokemon['sprites']['front_shiny'])
    print(retornar_response('https://www.trueachievements.com/'))
