import logging
import time

import requests

key = '25c25a91e50ee47054dda541f6498edf'


def decode_captcha(image):
    try:
        url = "http://rucaptcha.com/in.php"
        payload = {'key': key, 'phrase': 1, 'calc': 1, 'language': 1, 'numeric': 1}
        files = [('file', ('captcha_image.png', image, 'image/png'))]
        response = requests.request("POST", url, data=payload, files=files)
        return response.text.replace("OK|", "")
    except Exception as err:
        logging.error(f"{err}; url: {url}")
        raise err


def result_decode(key_captcha, second):
    try:
        print(f"Прошла(о) {second} секунд(а,ы) для ожидания декодирования каптчи с id {key_captcha}")
        time.sleep(1.0)
        url = f"http://rucaptcha.com/res.php?key={key}&id={key_captcha}&action=get"
        response = requests.request("GET", url)
        result_text = response.text.replace("OK|", "")
        if result_text == "CAPCHA_NOT_READY":
            second = second + 1
            return result_decode(key_captcha, second)
        return result_text
    except Exception as err:
        logging.error(f"{err}; url: {url}")
        raise err
