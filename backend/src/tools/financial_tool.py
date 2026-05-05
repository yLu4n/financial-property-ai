import json
from crewai.tools import BaseTool
from src.core.financial_engine import calculate_financial_metrics


class FinancialCalculationTool(BaseTool):
    name: str = "Financial Calculation Tool"
    description: str = (
        "Recebe dados financeiros em formato JSON string, "
        "executa cálculos determinísticos e retorna métricas financeiras oficiais."
    )

    def _run(self, financial_data: str) -> str:
        data = json.loads(financial_data)
        result = calculate_financial_metrics(data)
        return json.dumps(result, indent=2)

financial_calculation_tool = FinancialCalculationTool()