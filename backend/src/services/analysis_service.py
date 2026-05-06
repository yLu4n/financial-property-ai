from src.core.financial_engine import calculate_financial_metrics
from src.core.real_estate_engine import evaluate_real_estate_capacity


def run_full_analysis(financial_data, property_value, monthly_rent):

    financial_metrics = calculate_financial_metrics(financial_data)

    real_estate_metrics = evaluate_real_estate_capacity(
        financial_metrics=financial_metrics,
        property_value=property_value,
        monthly_rent=monthly_rent
    )

    final_recommendation = {
        "decisao_aluguel": real_estate_metrics["aluguel"]["aprovado"],
        "decisao_compra": real_estate_metrics["compra"]["aprovado"],
        "nivel_segurança": financial_metrics["classificacao_risco"].lower(),
        "acoes_recomendadas": []
    }

    if not real_estate_metrics["compra"]["aprovado"]:
        final_recommendation["acoes_recomendadas"].append(
            "Reduzir comprometimento financeiro antes de financiar imóvel."
        )

    if financial_metrics["meses_reserva"] < 6:
        final_recommendation["acoes_recomendadas"].append(
            "Aumentar reserva de emergência para pelo menos 6 meses."
        )

    return {
        "financial_analysis": financial_metrics,
        "real_estate_analysis": real_estate_metrics,
        "final_recommendation": final_recommendation
    }