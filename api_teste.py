import requests

servidor = "https://www.metaweather.com/api/"
endpoint = "location/search/?query="
query = input("Digite o nome de uma cidade: ")
url = servidor + endpoint + query

resposta = requests.get(url)

if resposta.status_code == 200 and len(resposta.json()) > 0:
    cidade = resposta.json()[0]
    title = cidade['title']
    lat = cidade['latt_long'].split(',')[0]
    lot = cidade['latt_long'].split(',')[1]
    woeid = cidade['woeid']
    texto = "A cidade {} fica na latitude {} e longitude {}".format(title, lat, lot)
    print(texto)

    endpoint = "location/{}/".format(woeid)
    
    url = servidor + endpoint

    resposta2 = requests.get(url)
    clima = resposta2.json()
    hora = clima['time']
    temp = clima['consolidated_weather'][0]['the_temp']

    print("Em {} são {} e faz {} °C".format(title, hora, temp))
    
else:
    print("Cidade não encontrada")

'''
https://rockcontent.com/blog/rest-api/
https://github.com/public-apis/public-apis#health
https://www.metaweather.com/api/
https://docs.python.org/pt-br/3/library/http.client.html
https://httpstatuses.com/
https://requests.readthedocs.io/pt_BR/latest/user/quickstart.html#resposta-crua
'''