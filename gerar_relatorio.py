import csv
from datetime import datetime

def gerar_relatorio(dados, arquivo="relatorio.csv"):
    with open(arquivo, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Data", "Funcionário", "Horas Trabalhadas"])
        for linha in dados:
            writer.writerow(linha)
    return {"status": "OK", "arquivo": arquivo}

if __name__ == "__main__":
    dados = [
        [datetime.now().strftime("%d/%m/%Y"), "Higor", 8],
        [datetime.now().strftime("%d/%m/%Y"), "Carlos", 6],
    ]
    resultado = gerar_relatorio(dados)
    print("Relatório gerado:", resultado["arquivo"])
