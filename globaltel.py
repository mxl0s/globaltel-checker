import requests
from requests.api import request

listabrojeva = open ("brojevi.txt", "r").readlines()

link = "https://www.globaltel.rs/functionality/checkChosenNumberAvailability.php"

fullbroj = "067", listabrojeva
brojevi = listabrojeva

headers = {
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Mobile Safari/537.36",
    "chooseNumber": brojevi,
    "number": fullbroj
}

    req = requests.post(link, data=headers).text
    if not "Brojevi" in req:
        print("Nasao: ", + brojevi)
    else:
        print("Zauzet: ", + brojevi)
