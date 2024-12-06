taxas_cambio = {
    "USD": {"BRL": 5.25, "EUR": 0.92, "JPY": 137.50, "ARS": 365.00, "GBP": 0.81, "CAD": 1.36, "CHF": 0.91},
    "BRL": {"USD": 0.19, "EUR": 0.17, "JPY": 26.18, "ARS": 69.55, "GBP": 0.15, "CAD": 0.26, "CHF": 0.17},
    "EUR": {"USD": 1.09, "BRL": 5.88, "JPY": 149.00, "ARS": 396.00, "GBP": 0.88, "CAD": 1.49, "CHF": 0.99},
    "JPY": {"USD": 0.0073, "BRL": 0.038, "EUR": 0.0067, "ARS": 2.66, "GBP": 0.006, "CAD": 0.0093, "CHF": 0.0066},
    "ARS": {"USD": 0.0027, "BRL": 0.014, "EUR": 0.0025, "JPY": 0.38, "GBP": 0.0022, "CAD": 0.0034, "CHF": 0.0025},
    "GBP": {"USD": 1.23, "BRL": 6.60, "EUR": 1.14, "JPY": 179.50, "ARS": 456.00, "CAD": 1.69, "CHF": 1.12},
    "CAD": {"USD": 0.74, "BRL": 3.85, "EUR": 0.67, "JPY": 115.00, "ARS": 268.00, "GBP": 0.59, "CHF": 0.66},
    "CHF": {"USD": 1.10, "BRL": 5.88, "EUR": 1.01, "JPY": 151.00, "ARS": 398.00, "GBP": 0.89, "CAD": 1.52},
}

def normalizar_moeda(moeda):
    mapeamento = {
        "dólar": "USD",
        "dolar": "USD",
        "usd": "USD",
        "euro": "EUR",
        "eur": "EUR",
        "iene": "JPY",
        "jpy": "JPY",
        "real": "BRL",
        "brl": "BRL",
        "peso argentino": "ARS",
        "peso": "ARS",
        "ars": "ARS",
        "libra": "GBP",
        "gbp": "GBP",
        "dólar canadense": "CAD",
        "dolar canadense": "CAD",
        "cad": "CAD",
        "franco suíço": "CHF",
        "franco": "CHF",
        "chf": "CHF",
    }
    return mapeamento.get(moeda.lower(), moeda.upper())

# Função para realizar a conversão de moedas
def converter_moeda(origem, destino, valor):
    origem = normalizar_moeda(origem)
    destino = normalizar_moeda(destino)
    
    if origem not in taxas_cambio or destino not in taxas_cambio[origem]:
        raise ValueError(f"Conversão de {origem} para {destino} não disponível.")
    
    taxa = taxas_cambio[origem][destino]
    return valor * taxa
