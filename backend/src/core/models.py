from pydantic import BaseModel

class FinancialInput(BaseModel):
    salario_bruto: float
    outras_rendas: float = 0
    despesas_fixas: float
    despesas_variaveis: float
    investimentos: float = 0
    reserva_emergencia: float = 0
    dividas_atuais: float = 0