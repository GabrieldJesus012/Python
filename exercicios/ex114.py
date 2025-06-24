import requests

def verificar_site(url):
    try:
        resposta = requests.get(url)
        if resposta.status_code == 200:
            return True
        else:
            return False
    except requests.exceptions.RequestException:
        return False

site = "https://www.pudim.com.br/"
if verificar_site(site):
    print(f"O site {site} está funcionando.")
else:
    print(f"O site {site} não está funcionando.")