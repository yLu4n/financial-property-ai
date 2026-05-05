def calculate_financial_metrics(data: dict):
    renda_total = data["salario_bruto"] + data.get("outras_rendas", 0)
    despesas_totais = data["despesas_fixas"] + data["despesas_variaveis"]

    comprometimento = despesas_totais / renda_total

    meses_reserva = 0
    if despesas_totais > 0:
        meses_reserva = data["reserva_emergencia"] / despesas_totais

    score = 100

    if comprometimento > 0.5:
        score -= 30
    elif comprometimento > 0.35:
        score -= 15

    if meses_reserva < 3:
        score -= 20
    elif meses_reserva < 6:
        score -= 10

    if data["dividas_atuais"] > renda_total:
        score -= 20

    score = max(0, min(score, 100))
    
    if score >= 75:
        risco = "Baixo"
    elif score >= 50:
        risco = "Médio"
    else:
        risco = "Alto"

    return {
        "renda_total": renda_total,
        "despesas_totais": despesas_totais,
        "comprometimento_percentual": round(comprometimento * 100, 2),
        "meses_reserva": round(meses_reserva, 2),
        "score": score,
        "classificacao_risco": risco
    }