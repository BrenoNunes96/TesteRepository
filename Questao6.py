import requests

class Medicao:
    def __init__(self, cidade, estado, hora, temperatura, umidade):
        self.cidade = cidade
        self.estado = estado
        self.hora = hora
        self.temperatura = temperatura
        self.umidade = umidade

    def __repr__(self):
        return f"{self.cidade}-{self.estado} {self.hora} -> Temp: {self.temperatura}, Umid: {self.umidade}"


def pegar_dados():
    cidade = "Aimorés"
    estado = "MG"
    codigo = "A534"

    url = "https://apitempo.inmet.gov.br/estacao/2024-03-01/2024-03-01/" + codigo

    response = requests.get(url)

    if response.status_code != 200 or not response.text:
        print("Sem dados da API")
        return []

    try:
        dados = response.json()
    except:
        print("Erro ao converter JSON")
        return []

    lista = []

    for x in dados:
        hora = x.get("HR_MEDICAO", "")[:5]
        temp = x.get("TEM_INS")
        umid = x.get("UMD_INS")

        if hora and temp and umid:
            med = Medicao(cidade, estado, hora, temp, umid)
            lista.append(med)

    return lista



dados = pegar_dados()

for d in dados:
    print(d)