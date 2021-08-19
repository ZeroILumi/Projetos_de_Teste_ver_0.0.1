from datetime import date, time, datetime, timedelta
import locale

locale.setlocale(locale.LC_ALL, 'pt_BR.utf8')


def mostrar_data_atual_com_date():
    data_atual = date.today()
    data_atual_brasil = data_atual.strftime('%d/%m/%Y')
    data_atual_brasil_formatado = data_atual.strftime('%A em %B de %Y')

    print(f'Hoje é: {data_atual_brasil},\n'
          f'Mais é também: {data_atual_brasil_formatado.title()},\n'
          f'O Dia Atuel é: {data_atual.strftime("%A").title()}, '
          f'do número {data_atual.strftime("%d")},\n'
          f'O Mes Atual é: {data_atual.strftime("%B").title()}, '
          f'o mes de número {data_atual.strftime("%m")},\n'
          f'O Ano Atual é: {data_atual.strftime("%Y")}.\n')


def mostrar_horario_atual_com_time():
    horario_teorico_do_evento_teorico = time(hour=15, minute=17, second=20)
    # print(type(horario_teorico_do_evento_teorico))
    # print(horario_teorico_do_evento_teorico)
    # Forma 1
    horario_teorico_do_evento_teorico_formatado = horario_teorico_do_evento_teorico.strftime('%H:%M:%S')
    print('O Horário do qual ocorrera nosso evento hipotético é: {horário_do_evento}'
          ''.format(horário_do_evento=horario_teorico_do_evento_teorico_formatado))
    # Forma 2
    # print('O Horário do qual ocorrera nosso evento hipotético é: {horário_do_evento}'
    #       ''.format(horário_do_evento=horario_teorico_do_evento_teorico.strftime('%H:%M:%S')))
    print('No qual {hora} representa a hora,'
          ''.format(hora=horario_teorico_do_evento_teorico.strftime('%H')))
    print('{minutos} representa os minutos è'
          ''.format(minutos=horario_teorico_do_evento_teorico.strftime('%M')))
    print('{segundos} representa os segundos.'
          ''.format(segundos=horario_teorico_do_evento_teorico.strftime('%S')))


def mostrar_data_e_horario_com_datatime():
    data_e_hora_atual = datetime.now()
    data_e_hora_atual_formatado = data_e_hora_atual.strftime('%d/%m/%Y e são %H:%M:%S')
    print('Hoje é: {data_e_hora_atual}'
          ','.format(data_e_hora_atual=data_e_hora_atual_formatado))
    print('Mais também é: {dia_mes_ano}'
          ','.format(dia_mes_ano=data_e_hora_atual.strftime('%A em %B de %Y').title()))
    print('Hoje é: {dia}, de número {numero_do_dia}'
          ','.format(dia=data_e_hora_atual.strftime('%A').title(),
                     numero_do_dia=data_e_hora_atual.strftime('%d')))
    print('O Mes é: {mes}, de número {numero_do_mes}'
          ','.format(mes=data_e_hora_atual.strftime('%B').title(),
                     numero_do_mes=data_e_hora_atual.strftime('%m')))
    print('O Ano é: {ano}'
          ','.format(ano=data_e_hora_atual.strftime('%Y')))
    print('São {horas} Horas'
          ','.format(horas=data_e_hora_atual.strftime('%H')))
    print('No Minuto {minuto}'
          ','.format(minuto=data_e_hora_atual.strftime('%M')))
    print('Com {segundos} Segundos'
          '\n'.format(segundos=data_e_hora_atual.strftime('%S')))
    # print(data_e_hora_atual.strftime('%c'))
    # print(data_e_hora_atual.date())
    # print(data_e_hora_atual.time())
    # print(data_e_hora_atual.weekday())
    # print(data_e_hora_atual.day)
    # print(data_e_hora_atual.month)
    # print(data_e_hora_atual.year)
    # print(data_e_hora_atual.hour)
    # print(data_e_hora_atual.minute)
    # print(data_e_hora_atual.second)
    # print(data_e_hora_atual.microsecond)
    # tupla_de_dias = (
    #     'Segunda',
    #     'Terça',
    #     'Quarta',
    #     'Quinta',
    #     'Sexta',
    #     'Sábado',
    #     'Domingo')
    # print(tupla_de_dias[data_e_hora_atual.weekday()])
    data_e_hora_teorica_para_um_evento_hipotetico = datetime(day=17,
                                                             month=5,
                                                             year=2022,
                                                             hour=16,
                                                             minute=00,
                                                             second=00)
    data_e_hora_teorica_para_um_evento_hipotetico_formatado = data_e_hora_teorica_para_um_evento_hipotetico.strftime(
        '%A de %B em %Y, %d/%m/%Y as %H:%M')
    print(f'Nosso evento Hipotético ocorrera na data a seguir:\n'
          f'{data_e_hora_teorica_para_um_evento_hipotetico_formatado.title()}\n'.title())

    # string_de_data = '07/09/1999 12:20:22'

    # coverter_string_de_data = datetime.strptime(string_de_data, '%d/%m/%Y %H:%M:%S')

    # print(type(coverter_string_de_data))
    # print(coverter_string_de_data)
    #
    # print(coverter_string_de_data.now())

    ano_passado_de_hoje = data_e_hora_atual.now() - timedelta(days=365)
    # ano_passado_de_hoje = data_e_hora_atual.now() - timedelta(days=365,
    #                                                           hours=5,
    #                                                           minutes=15,
    #                                                           seconds=60,
    #                                                           milliseconds=40,
    #                                                           microseconds=50)
    print(f'Ano Passado foi {ano_passado_de_hoje.strftime("%d/%m/%Y")}'.title())
    ano_futuro_de_hoje = data_e_hora_atual.now() + timedelta(days=365)
    print(f'Ano Futuro será {ano_futuro_de_hoje.strftime("%d/%m/%Y")}'.title())

if __name__ == '__main__':
    # mostrar_data_atual_com_date()
    # mostrar_horario_atual_com_time()
    mostrar_data_e_horario_com_datatime()
