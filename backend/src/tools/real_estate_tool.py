import json
from crewai.tools import BaseTool
from src.core.real_estate_engine import evaluate_real_estate_capacity


class RealEstateEvaluationTool(BaseTool):
    name: str = "Real Estate Evaluation Tool"
    description: str = (
        "Avalia capacidade de aluguel e compra com base nas métricas financeiras oficiais."
    )

    def _run(self, input_data: str) -> str:
        data = json.loads(input_data)

        result = evaluate_real_estate_capacity(
            financial_metrics=data["financial_metrics"],
            property_value=data["property_value"],
            monthly_rent=data.get("monthly_rent")
        )

        return json.dumps(result, indent=2)


real_estate_evaluation_tool = RealEstateEvaluationTool()