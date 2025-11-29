import unittest # módulo nativo para testes unitários
from operacao import Operacao #importando classe para teste

class TestOperacao(unittest.TestCase):

    def test_somaFalsa(self):
        res = Operacao.somaFalsa(4,5)
        self.assertEqual(res, 9)

    def test_somaSuc(self):
        res = Operacao.somaSuc(4,5)
        self.assertEqual(res, 9)

unittest.main(argv=[''],exit=False)

