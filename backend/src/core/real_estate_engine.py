def evaluate_real_estate_capacity(
    financial_metrics: dict,
    property_value: float,
    monthly_rent: float = None,
    entrada_percentual: float = 0.2,
    taxa_juros_anual: float = 0.10,
    prazo_anos: int = 30
):
    renda = financial_metrics["renda_total"]
    despesas = financial_metrics["despesas_totais"]
    reserva_meses = financial_metrics["meses_reserva"]
    score = financial_metrics["score"]

    resultado = {}

    # -------------------------
    # 🔹 Avaliação de Aluguel
    # -------------------------
    if monthly_rent:
        percentual_aluguel = monthly_rent / renda

        pode_alugar = (
            percentual_aluguel <= 0.3 and
            reserva_meses >= 3 and
            (renda - despesas - monthly_rent) > 0
        )

        resultado["aluguel"] = {
            "percentual_renda": round(percentual_aluguel * 100, 2),
            "aprovado": pode_alugar
        }

    # -------------------------
    # 🔹 Avaliação de Compra
    # -------------------------
    entrada = property_value * entrada_percentual
    valor_financiado = property_value - entrada

    taxa_mensal = taxa_juros_anual / 12
    parcelas = prazo_anos * 12

    # Fórmula simplificada PRICE
    parcela = (
        valor_financiado *
        (taxa_mensal * (1 + taxa_mensal) ** parcelas) /
        ((1 + taxa_mensal) ** parcelas - 1)
    )

    percentual_parcela = parcela / renda

    reserva_restante_meses = (
        (financial_metrics["meses_reserva"] * despesas - entrada)
        / despesas if despesas > 0 else 0
    )

    pode_comprar = (
        percentual_parcela <= 0.3 and
        reserva_restante_meses >= 6 and
        score >= 60
    )

    resultado["compra"] = {
        "parcela_estimada": round(parcela, 2),
        "percentual_renda": round(percentual_parcela * 100, 2),
        "reserva_restante_meses": round(reserva_restante_meses, 2),
        "aprovado": pode_comprar
    }

    return resultado