from crewai import Agent

def create_recommendation_agent():
    return Agent(
        role="Chief Financial Decision Officer",
        goal=(
            "Consolidar análise financeira e imobiliária "
            "e gerar decisão estratégica final estruturada."
        ),
        backstory=(
            "Você é o responsável final por decisões financeiras estratégicas. "
            "Você recebe análises estruturadas e gera uma decisão objetiva."
        ),
        verbose=True
    )