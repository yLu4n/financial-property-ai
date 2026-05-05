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


def create_financial_analysis_task(agent, financial_data: dict):
    return Task(
        description=(
            "Use a ferramenta 'Financial Calculation Tool' passando os dados abaixo:\n\n"
            f"{financial_data}\n\n"
            "Após receber o JSON com as métricas oficiais, explique os resultados "
            "de forma estratégica e profissional.\n\n"
            "NÃO faça cálculos manualmente."
        ),
        expected_output=(
            "Explicação estratégica baseada exclusivamente no JSON retornado pela ferramenta."
        ),
        agent=agent,
    )