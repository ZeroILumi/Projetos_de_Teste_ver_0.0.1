if __name__ == '__main__':
      conjunto1 = {1, 2, 3, 4, 5}
      conjunto2 = {5, 6, 7, 8}

      conjunto_uniao_1_2 = conjunto1.union(conjunto2)

      print('União do conjunto 1 com o conjunto 2:\n{conjunto_uniao_1_2}'
            ''.format(conjunto_uniao_1_2=conjunto_uniao_1_2))

      conjunto_intersccao_1_2 = conjunto1.intersection(conjunto2)

      print('Interscção entre o conjunto 1 eo conjunto 2:\n{conjunto_intersccao_1_2}'
            ''.format(conjunto_intersccao_1_2=conjunto_intersccao_1_2))

      conjunto_diferenca_1_2 = conjunto1.difference(conjunto2)

      print('Diferença entre o conjunto 1 eo conjunto 2:\n{conjunto_diferenca_1_2}'
            ''.format(conjunto_diferenca_1_2=conjunto_diferenca_1_2))

      conjunto_diferenca_2_1 = conjunto2.difference(conjunto1)

      print('Diferença entre o conjunto 2 eo conjunto 1:\n{conjunto_diferenca_2_1}'
            ''.format(conjunto_diferenca_2_1=conjunto_diferenca_2_1))

      conjunto_diferenca_simetrica = conjunto1.symmetric_difference(conjunto2)

      print('Diferença Simetrica entre o conjunto 1 eo conjunto 2:\n{conjunto_diferenca_simetrica}'
            ''.format(conjunto_diferenca_simetrica=conjunto_diferenca_simetrica))

      conjunto_a = {1, 2, 3}

      conjunto_b = {1, 2, 3, 4, 5}

      conjunto_subset_a_b = conjunto_a.issubset(conjunto_b)

      if conjunto_subset_a_b:
            print('Conjunto A é uma sub-atribuição do conjunto B')
      else:
            print('Conjunto A não é uma sub-atribuição do conjunto B')

      conjunto_subset_b_a = conjunto_b.issubset(conjunto_a)

      if conjunto_subset_b_a:
            print('Conjunto B é uma sub-atribuição do conjunto A')
      else:
            print('Conjunto B não é uma sup-atribuição do conjunto A')

      conjunto_superset_b_a = conjunto_b.issuperset(conjunto_a)

if conjunto_superset_b_a:
      print('Conjunto B é uma super-atribuição do conjunto A')
else:
      print('Conjunto B não é uma super-atribuição do conjunto A')

conjunto_superset_a_b = conjunto_a.issuperset(conjunto_b)

if conjunto_superset_a_b:
      print('Conjunto A é uma super-atribuição do conjunto B')
else:
      print('Conjunto A não é uma super-atribuição do conjunto B')

lista_de_animais = ['cachorro', 'cachorro', 'gato', 'gato', 'elefante']

print(lista_de_animais)

conjunto_animais = set(lista_de_animais)

print(conjunto_animais)

lista_animais_2 = list(conjunto_animais)

print(lista_animais_2)




# conjunto = {1, 2, 3, 4}
# conjunto.add(5)
# conjunto.discard(2)
# print(conjunto)