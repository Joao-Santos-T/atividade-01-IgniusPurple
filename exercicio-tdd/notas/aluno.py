from dataclasses import dataclass
from typing import Dict, List

@dataclass
class Aluno:
    nome: str
    matricula: str
    notas: Dict[str, List[float]] = None
    faltas: Dict[str, int] = None

    def __post_init__(self):
        if self.notas is None:
            self.notas = {}
        if self.faltas is None:
            self.faltas = {}

    def adicionar_nota(self, disciplina: str, nota: float) -> None:
        if disciplina not in self.notas:
            self.notas[disciplina] = []
        self.notas[disciplina].append(nota)

    def calcular_media(self, disciplina: str) -> float:
        if disciplina not in self.notas or not self.notas[disciplina]:
            return 0.0
        return sum(self.notas[disciplina]) / len(self.notas[disciplina])

    def verificar_aprovacao(self, disciplina: str) -> bool:
        return self.calcular_media(disciplina) >= 7.0

    def registrar_falta(self, disciplina: str) -> None:
        if disciplina not in self.faltas:
            self.faltas[disciplina] = 0
        self.faltas[disciplina] += 1

    def calcular_frequencia(self, disciplina: str, total_aulas: int) -> float:
        if total_aulas == 0:
            return 0.0
        faltas = self.faltas.get(disciplina, 0)
        return ((total_aulas - faltas) / total_aulas) * 100
