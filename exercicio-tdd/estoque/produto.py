from datetime import datetime

class Produto:
    def __init__(self, nome, quantidade, preco_unitario, validade):
        self.nome = nome
        self.quantidade = quantidade
        self.preco_unitario = preco_unitario
        self.validade = validade

    def adicionar_estoque(self, quantidade):
        self.quantidade += quantidade

    def remover_estoque(self, quantidade):
        if quantidade > self.quantidade:
            raise ValueError("Estoque insuficiente")
        self.quantidade -= quantidade

    def alerta_estoque_baixo(self):
        return self.quantidade < 5

    def valor_total(self):
        return self.quantidade * self.preco_unitario

    def esta_vencido(self):
        return datetime.now().date() > self.validade
