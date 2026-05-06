from crewai import Task


def create_financial_collection_task(agent, financial_data: dict):
    return Task(
        description=(
            "Organize e valide os seguintes dados financeiros do usuário:\n\n"
            f"{financial_data}\n\n"
            "Verifique consistência e organize as informações claramente."
        ),
        expected_output="Um resumo organizado e validado dos dados financeiros.",
        agent=agent,
    )


def create_financial_analysis_task(agent, financial_data):
    return Task(
        description=(
            "Use a ferramenta 'Financial Calculation Tool'.\n\n"
            f"Dados:\n{financial_data}\n\n"
            "Retorne EXCLUSIVAMENTE no formato JSON:\n\n"
            "{\n"
            '  "financial_analysis": {\n'
            '    "metricas": {...},\n'
            '    "classificacao": "...",\n'
            '    "score": numero,\n'
            '    "resumo": "texto curto objetivo"\n'
            "  }\n"
            "}\n\n"
            "Sem texto fora do JSON."
        ),
        expected_output="JSON estruturado com análise financeira.",
        agent=agent,
    )

def create_real_estate_task(agent, financial_metrics, property_value, monthly_rent):
    payload = {
        "financial_metrics": financial_metrics,
        "property_value": property_value,
        "monthly_rent": monthly_rent
    }

    return Task(
        description=(
            "Use a ferramenta 'Real Estate Evaluation Tool' "
            f"com os seguintes dados:\n\n{payload}\n\n"
            "Você DEVE retornar exclusivamente um JSON estruturado no formato:\n\n"
            "{\n"
            '  "real_estate_analysis": {\n'
            '    "aluguel": {...},\n'
            '    "compra": {...},\n'
            '    "conclusao": "texto curto objetivo"\n'
            "  }\n"
            "}\n\n"
            "NÃO inclua texto fora do JSON."
        ),
        expected_output="JSON estruturado com análise imobiliária.",
        agent=agent,
    )
    
def create_recommendation_task(agent):
    return Task(
        description=(
            "Com base nos resultados anteriores no contexto, "
            "gere exclusivamente o JSON final no formato:\n\n"
            "{\n"
            '  "final_recommendation": {\n'
            '    "decisao_aluguel": true/false,\n'
            '    "decisao_compra": true/false,\n'
            '    "nivel_segurança": "baixo/medio/alto",\n'
            '    "acoes_recomendadas": [\n'
            '       "ação 1",\n'
            '       "ação 2"\n'
            "    ]\n"
            "  }\n"
            "}\n\n"
            "Sem texto adicional."
        ),
        expected_output="JSON estruturado com decisão final.",
        agent=agent,
    )