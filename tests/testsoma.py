import unittest
from src.listas.lista import busca


class TestBusca(unittest.TestCase):
    def test_retorno_lista(self):
        lista = [0, 1, 2, 3, 4, 5]
        self.assertEqual(busca(lista, 2), 2)

    def test_retorno_lista_false(self):
        lista = [0, 1, 2, 3, 4, 5]
        self.assertEqual(busca(lista, 7), None)
