def calcular_ferias(salario: float, dias: int, vender_dias: bool = False):
    valor_dia = salario / 30
    valor_ferias = valor_dia * dias
    adicional_terco = valor_ferias / 3
    valor_venda_dias = 0
    dias_vendidos = 0

    if vender_dias and dias == 30:
        dias_vendidos = 10
        valor_venda_dias = (valor_dia * dias_vendidos) + (valor_dia * dias_vendidos / 3)

    total = valor_ferias + adicional_terco + valor_venda_dias
    return {
        "salario": salario,
        "dias": dias,
        "dias_vendidos": dias_vendidos,
        "valor_ferias": round(valor_ferias, 2),
        "adicional_terco": round(adicional_terco, 2),
        "valor_venda_dias": round(valor_venda_dias, 2),
        "total": round(total, 2)
    }


if __name__ == "__main__":
    salario = float(input("Digite o salário mensal: R$ "))
    dias = int(input("Quantos dias de férias? "))
    vender = input("Vai vender 10 dias? (S/N): ").strip().upper() == "S"

    resultado = calcular_ferias(salario, dias, vender)
    print("\n=== CÁLCULO DE FÉRIAS ===")
    for chave, valor in resultado.items():
        print(f"{chave.capitalize()}: {valor}")
