import urllib
import urllib.error
import urllib.request 

try:
    url = "https://www.pudim.com.br/"
    site = urllib.request.urlopen(url)
except urllib.error.URLError:
    print(f"O {url} não está acessivel no momento.")
else: 
    print(f"Consegui acessar o {url} ")
    print(site.read()) #pegar o html do site.
