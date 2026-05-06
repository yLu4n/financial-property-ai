import os
from dotenv import load_dotenv
from crewai import Crew, Process

from src.core.financial_engine import calculate_financial_metrics
from src.agents.financial_collector import create_financial_collector
from src.agents.financial_analyst import create_financial_analyst
from src.agents.real_estate_analyst import create_real_estate_analyst
from src.tasks.financial_tasks import (
    create_financial_collection_task,
    create_financial_analysis_task,
    create_real_estate_task
)

load_dotenv()


def run_full_analysis():

    financial_data = {
        "salario_bruto": 9000,
        "outras_rendas": 0,
        "despesas_fixas": 3000,
        "despesas_variaveis": 1500,
        "reserva_emergencia": 30000,
        "dividas_atuais": 2000
    }

    property_value = 500000
    monthly_rent = 2500

    financial_metrics = calculate_financial_metrics(financial_data)

    print("\n===== MÉTRICAS FINANCEIRAS OFICIAIS =====\n")
    print(financial_metrics)


    collector, analyst, real_estate_agent = create_financial_collector(), create_financial_analyst(), create_real_estate_analyst()
    agents = [collector, analyst, real_estate_agent]


    collection_task, analysis_task, real_estate_task = create_financial_collection_task(collector, financial_data), create_financial_analysis_task(analyst, financial_data), create_real_estate_task(real_estate_agent, financial_metrics, property_value, monthly_rent)
    tasks = [collection_task, analysis_task, real_estate_task]

    crew = Crew(
        agents=agents,
        tasks=tasks,
        process=Process.sequential,
        verbose=True
    )

    result = crew.kickoff()

    print("\n\n===== RESULTADO FINAL CONSOLIDADO =====\n")
    print(result)


if __name__ == "__main__":
    run_full_analysis()