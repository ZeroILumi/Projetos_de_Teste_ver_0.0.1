import pytest

from restaurante import Restaurante


@pytest.fixture
def objeto_restaurante_fila_vazia():
    return Restaurante('Pizzaria X')


@pytest.fixture
def objeto_restaurante_fila_com_um_pedido():
    return Restaurante('Pizzaria X', 1)


def test_pedidos_na_fila_valor_inicial_padrao_igual_a_zero(objeto_restaurante_fila_vazia):
    assert objeto_restaurante_fila_vazia.pedidos_na_fila == 0


def test_pedidos_na_fila_valor_incial_maior_que_zero(objeto_restaurante_fila_com_um_pedido):
    assert objeto_restaurante_fila_com_um_pedido.pedidos_na_fila == 1


def test_pedidos_na_fila_valor_inicial_menor_que_zero():
    with pytest.raises(ValueError):
        Restaurante("Pizzaria X", -1)


def test_adiciona_um_pedido_na_fila(objeto_restaurante_fila_com_um_pedido):
    objeto_restaurante_fila_com_um_pedido.adiciona_pedido()
    assert objeto_restaurante_fila_com_um_pedido.pedidos_na_fila == 2


def test_remove_um_pedido_na_fila(objeto_restaurante_fila_com_um_pedido):
    objeto_restaurante_fila_com_um_pedido.remove_pedido()
    assert objeto_restaurante_fila_com_um_pedido.pedidos_na_fila == 0


def test_remove_um_pedido_na_fila_vazia(objeto_restaurante_fila_vazia):
    objeto_restaurante_fila_vazia.remove_pedido()
    assert objeto_restaurante_fila_vazia.pedidos_na_fila == 0


@pytest.mark.parametrize("inicial,final", [(0, 0), (1, 0), (2, 1)])
def test_remocao_de_pedidos(inicial, final):
    restaurante = Restaurante("Pizzaria X", inicial)
    restaurante.remove_pedido()
    assert restaurante.pedidos_na_fila == final
