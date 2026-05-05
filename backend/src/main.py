import os
from dotenv import load_dotenv
from crewai import Crew, Process

from src.agents.financial_collector import create_financial_collector
from src.agents.financial_analyst import create_financial_analyst
from src.tasks.financial_tasks import (
    create_financial_collection_task,
    create_financial_analysis_task
)

load_dotenv()

def run_financial_analysis():

    financial_data = {
        "salario_bruto": 8000,
        "outras_rendas": 1000,
        "despesas_fixas": 3000,
        "despesas_variaveis": 1500,
        "investimentos": 20000,
        "reserva_emergencia": 10000,
        "dividas_atuais": 5000
    }

    collector, analyst = create_financial_collector(), create_financial_analyst()
    agents = [collector, analyst]

    collection_task, analysis_task = create_financial_collection_task(collector, financial_data), create_financial_analysis_task(analyst, financial_data)
    tasks = [collection_task, analysis_task]

    crew = Crew(
        agents=agents,
        tasks=tasks,
        process=Process.sequential,
        verbose=True
    )

    result = crew.kickoff()
    print("\n\n===== RESULTADO FINAL =====\n")
    print(result)

if __name__ == "__main__":
    run_financial_analysis()