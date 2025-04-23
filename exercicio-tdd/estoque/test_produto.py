"""
Testes da classe Produto.
"""
import unittest
from datetime import datetime, timedelta
from produto import Produto


class TestProduto(unittest.TestCase):
    """Testa a classe Produto."""

    def setUp(self):
        """Configura o ambiente de teste."""
        self.produto = Produto("Sabonete", 10, 2.5, datetime.now().date() + timedelta(days=10))

    def test_inicializacao(self):
        """Verifica se o produto é inicializado corretamente."""
        self.assertEqual(self.produto.nome, "Sabonete")
        self.assertEqual(self.produto.quantidade, 10)
        self.assertEqual(self.produto.preco_unitario, 2.5)

    def test_adicionar_estoque(self):
        """Verifica se o estoque é adicionado corretamente."""
        self.produto.adicionar_estoque(5)
        self.assertEqual(self.produto.quantidade, 15)

    def test_remover_estoque(self):
        """Verifica se o estoque é removido corretamente."""
        self.produto.remover_estoque(4)
        self.assertEqual(self.produto.quantidade, 6)

    def test_remover_estoque_insuficiente(self):
        """Verifica se erro é lançado ao remover mais do que o estoque disponível."""
        with self.assertRaises(ValueError):
            self.produto.remover_estoque(20)

    def test_verificar_estoque_baixo(self):
        """Verifica se a detecção de estoque baixo funciona corretamente."""
        self.produto.remover_estoque(7)  # Fica com 3
        self.assertTrue(self.produto.alerta_estoque_baixo())

    def test_calcular_valor_total(self):
        """Verifica se o valor total é calculado corretamente."""
        self.assertEqual(self.produto.valor_total(), 25.0)

    def test_verificar_validade(self):
        """Verifica se a validação de data de validade funciona corretamente."""
        self.assertFalse(self.produto.esta_vencido())
        vencido = Produto("Leite", 5, 4.0, datetime.now().date() - timedelta(days=1))
        self.assertTrue(vencido.esta_vencido())


if __name__ == "__main__":
    unittest.main()
