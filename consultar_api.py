import requests

def consultar_api(nome="higor"):
    url = f"https://api.agify.io/?name={nome}"
    response = requests.get(url)
    if response.status_code == 200:
        dados = response.json()
        return {"nome": nome, "idade_estimada": dados.get("age")}
    else:
        return {"erro": f"Erro {response.status_code} ao consultar API"}

if __name__ == "__main__":
    nome = input("Digite um nome para consultar: ")
    print(consultar_api(nome))
