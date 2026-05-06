from pydantic import BaseModel, Field


class FinancialData(BaseModel):
    salario_bruto: float = Field(..., ge=0)
    outras_rendas: float = Field(0, ge=0)
    despesas_fixas: float = Field(..., ge=0)
    despesas_variaveis: float = Field(..., ge=0)
    reserva_emergencia: float = Field(..., ge=0)
    dividas_atuais: float = Field(..., ge=0)


class AnalysisRequest(BaseModel):
    financial_data: FinancialData
    property_value: float = Field(..., gt=0)
    monthly_rent: float = Field(..., gt=0)