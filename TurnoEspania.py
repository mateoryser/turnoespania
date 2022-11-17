import requests
from bs4 import BeautifulSoup
import time
import http.client

last_opening = None
next_opening = None

correct_message = "¡¡¡¡¡ YA HAY TURNOS ANDA URGENTE PINGGGGGGG !!!!!"
error_message = "HUBO UN ERROR CON EL SERVIDOR, REVISAR"
normal_message = "No hubo novedades en el dia de hoy"

json = {
        "chat_id": 932650947,
        "text": None
    }

count = 0

while True:
    try:
        url_data = requests.get("https://www.cgeonline.com.ar/informacion/apertura-de-citas.html")
        html = BeautifulSoup(url_data.content, "html.parser")
        tr = html.find("td", string="Registro Civil-Nacimientos").parent
        td_list = tr.find_all("td")

        if not last_opening == td_list[1].text or not next_opening == td_list[2].text:
            last_opening = td_list[1].text
            next_opening = td_list[2].text
            data = "\n Ultima Apertura = %s\n Proxima Apertura = %s" % (last_opening, next_opening)
            json["text"] = correct_message + data
            conn = http.client.HTTPSConnection('https://api.telegram.org/bot5659537734:AAF1y_3Y_o6LvuPu3yAk0kcaYfpD_iVhS7s/sendMessage', 443)
            requests.post('https://api.telegram.org/bot5659537734:AAF1y_3Y_o6LvuPu3yAk0kcaYfpD_iVhS7s/sendMessage', json=json)
        
        if count == 288:
            data = "\n Ultima Apertura = %s\n Proxima Apertura = %s" % (last_opening, next_opening)
            json["text"] = normal_message + data
            conn = http.client.HTTPSConnection('https://api.telegram.org/bot5659537734:AAF1y_3Y_o6LvuPu3yAk0kcaYfpD_iVhS7s/sendMessage', 443)
            requests.post('https://api.telegram.org/bot5659537734:AAF1y_3Y_o6LvuPu3yAk0kcaYfpD_iVhS7s/sendMessage', json=json)
            count = 0

    except Exception as a:
        print(a)
        json["text"] = error_message
        conn = http.client.HTTPSConnection('https://api.telegram.org/bot5659537734:AAF1y_3Y_o6LvuPu3yAk0kcaYfpD_iVhS7s/sendMessage', 443)
        requests.post('https://api.telegram.org/bot5659537734:AAF1y_3Y_o6LvuPu3yAk0kcaYfpD_iVhS7s/sendMessage', json=json)
        time.sleep(300)

    time.sleep(300)
    count += 1
