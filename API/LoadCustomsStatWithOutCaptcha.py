import json
import logging

import requests


def view_captcha():
    try:
        url = "http://stat.customs.gov.ru/api/Capcha/View"
        headers = {'Access-Control-Expose-Headers': 'captcha-key', 'Accept-Encoding': 'gzip, deflate',
                   'Accept-Language': 'ru-RU'}

        response = requests.request("GET", url, headers=headers)
        key_captcha = response.headers.get("captcha-key")
        return {'content': response.content, 'keyCaptcha': key_captcha}
    except Exception as err:
        logging.error(f"{err}; url: {url}")
        raise err


def check_captcha(captcha_key, captcha_val):
    try:
        url = "http://stat.customs.gov.ru/api/Capcha/Check"
        headers = {'Access-Control-Expose-Headers': 'captcha-key', 'Accept-Encoding': 'gzip, deflate',
                   'Accept-Language': 'ru-RU', 'captcha-key': captcha_key, 'captcha-val': captcha_val}

        response = requests.request("GET", url, headers=headers)
        return response.text
    except Exception as err:
        logging.error(f"{err}; url: {url}")
        raise err


def unload_file_zip(captcha_key, period):
    try:
        url = "http://stat.customs.gov.ru/api/DataAnalysis/UnloadData"

        payload = json.dumps(
            {"exportType": "Csv", "tnved": [], "tnvedLevel": 10, "federalDistricts": [], "subjects": [], "direction": "",
                "period": period})
        headers = {'captcha-key': captcha_key, 'Content-Type': 'application/json'}

        response = requests.request("POST", url, headers=headers, data=payload)
        return response.content
    except Exception as err:
        logging.error(f"{err}; url: {url}")
        raise err
