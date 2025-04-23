import pytest
from funcionario import Funcionario

def test_salario_bruto():
    f = Funcionario("João", 1, salario_hora=50.0, horas_trabalhadas=160)
    assert f.calcular_salario_bruto() == 8000.0

def test_comissao_ativa():
    f = Funcionario("Maria", 2, valor_comissao=200, contratos_fechados=5)
    assert f.calcular_comissao() == 1000.0

def test_comissao_inativa():
    f = Funcionario("Carlos", 3, tem_comissao=False, contratos_fechados=5)
    assert f.calcular_comissao() == 0.0

def test_custo_total_com_comissao():
    f = Funcionario("Ana", 4, salario_hora=60.0, horas_trabalhadas=100, custo_empregador=1200.0, valor_comissao=150.0, contratos_fechados=3)
    esperado = (60 * 100) + 1200 + (150 * 3)
    assert f.calcular_custo_total() == esperado

def test_custo_total_sem_comissao():
    f = Funcionario("Leo", 5, salario_hora=40.0, horas_trabalhadas=80, custo_empregador=800.0, tem_comissao=False, contratos_fechados=10)
    esperado = (40 * 80) + 800
    assert f.calcular_custo_total() == esperado
