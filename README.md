# Automacoes n8n em Python

Este repositório contém exemplos práticos de scripts Python para uso em **nós "Code" do n8n**, e também podem ser executados localmente.

## 🧩 Estrutura

| Arquivo | Descrição |
|----------|------------|
| `calcular_ferias.py` | Calculadora de férias com opção de venda de dias |
| `consultar_api.py` | Consulta uma API pública (exemplo: Agify) |
| `gerar_relatorio.py` | Gera um relatório CSV com dados simulados |

---

## 🛠️ Requisitos

- Python 3.10 ou superior  
- Pacote `requests` (para o exemplo da API)

Instale com:
```bash
pip install -r requirements.txt
```

---

## 🚀 Executar localmente

```bash
python calcular_ferias.py
python consultar_api.py
python gerar_relatorio.py
```

---

## ⚙️ Uso no n8n

1. Crie um **nó "Code" (Python)**.
2. Copie o conteúdo da função que desejar.
3. Passe os parâmetros pelos *inputs* do n8n.
4. Execute e use o resultado no fluxo.

Exemplo de uso no n8n:
```python
salario = 3000
dias = 30
vender_dias = True

return calcular_ferias(salario, dias, vender_dias)
```

---

## 📄 Licença
MIT License © 2025 - Automações em Python para n8n
