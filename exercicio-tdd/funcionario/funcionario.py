"""
Sistema de gerenciamento de funcionários.
"""
from dataclasses import dataclass


@dataclass
class Funcionario:
    """Representação de um funcionário com foco em custos trabalhistas e comissões.
    
    Attributes:
        nome: Nome do funcionário
        matricula: Número de matrícula do funcionário
        salario_hora: Valor do salário por hora trabalhada
        horas_trabalhadas: Quantidade de horas trabalhadas no mês
        custo_empregador: Custo fixo mensal do empregador (INSS, FGTS, etc)
        tem_comissao: Indica se o funcionário recebe comissão
        valor_comissao: Valor da comissão por contrato fechado
        contratos_fechados: Número de contratos fechados no mês
    """

    nome: str
    matricula: int
    salario_hora: float = 100.0
    horas_trabalhadas: float = 0.0
    custo_empregador: float = 1000.0
    tem_comissao: bool = True
    valor_comissao: float = 100.0
    contratos_fechados: int = 0

    def calcular_salario_bruto(self) -> float:
        """Calcula o salário bruto do funcionário.
        
        Returns:
            float: Salário bruto calculado baseado nas horas trabalhadas
        """
        raise NotImplementedError()

    def calcular_custo_total(self) -> float:
        """Calcula o custo total do funcionário para a empresa.
        
        Returns:
            float: Custo total (salário + custos do empregador)
        """
        raise NotImplementedError()

    def calcular_comissao(self) -> float:
        """Calcula o valor total da comissão do funcionário.
        
        Returns:
            float: Valor total da comissão baseado nos contratos fechados
        """
        raise NotImplementedError() 