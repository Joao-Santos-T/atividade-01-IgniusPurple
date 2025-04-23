import pytest
from aluno import Aluno

@pytest.fixture
def aluno():
    return Aluno(nome="Lucas", matricula="2023001")

def test_adicionar_nota(aluno):
    aluno.adicionar_nota("Matemática", 8.5)
    assert aluno.notas["Matemática"] == [8.5]

def test_adicionar_varias_notas(aluno):
    aluno.adicionar_nota("Matemática", 6.0)
    aluno.adicionar_nota("Matemática", 7.0)
    assert aluno.notas["Matemática"] == [6.0, 7.0]

def test_calcular_media(aluno):
    aluno.adicionar_nota("História", 5.0)
    aluno.adicionar_nota("História", 7.0)
    assert aluno.calcular_media("História") == 6.0

def test_calcular_media_sem_nota(aluno):
    assert aluno.calcular_media("Física") == 0.0

def test_verificar_aprovacao_aprovado(aluno):
    aluno.adicionar_nota("Geografia", 8.0)
    aluno.adicionar_nota("Geografia", 7.0)
    assert aluno.verificar_aprovacao("Geografia") is True

def test_verificar_aprovacao_reprovado(aluno):
    aluno.adicionar_nota("Química", 4.0)
    aluno.adicionar_nota("Química", 5.0)
    assert aluno.verificar_aprovacao("Química") is False

def test_registrar_falta(aluno):
    aluno.registrar_falta("Biologia")
    aluno.registrar_falta("Biologia")
    assert aluno.faltas["Biologia"] == 2

def test_calcular_frequencia(aluno):
    aluno.registrar_falta("Física")
    aluno.registrar_falta("Física")
    assert aluno.calcular_frequencia("Física", 10) == 80.0

def test_frequencia_disciplina_nunca_teve_falta(aluno):
    assert aluno.calcular_frequencia("Português", 20) == 100.0

def test_frequencia_total_aulas_zero(aluno):
    aluno.registrar_falta("Filosofia")
    assert aluno.calcular_frequencia("Filosofia", 0) == 0.0
