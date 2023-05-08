import json
import logging
from json import JSONDecodeError
import requests
from requests.exceptions import HTTPError

from app.api import random_goods_api

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(message)s',
    datefmt='%Y-%m-%dT%H:%M:%S')


log = logger = logging


class HttpRequest(object):
    @staticmethod
    def get_data(resp_json):
        if resp_json.get('retCode', '404') != '200':
            print(resp_json.get('message', 'connect failed'))
            return None
        else:
            print(resp_json.get('message'))
            return resp_json.get('data')

    @staticmethod
    def to_python(json_str):
        try:
            if json_str is None:
                return json.loads('{}')
            resp_json = json.loads(json_str.text)
        except JSONDecodeError as e:
            log.error(f'JSONDecode error:\n{e}')
        else:
            return resp_json

    @staticmethod
    def to_json(obj):
        return json.dumps(obj, indent=4, ensure_ascii=False)

    @staticmethod
    def request(method, url, max_retry: int = 2, params=None, data=None, json=None, headers=None, **kwargs):
        for i in range(max_retry + 1):
            try:
                s = requests.Session()
                response = s.request(method, url, params=params, data=data, json=json, headers=headers, **kwargs)
            except HTTPError as e:
                log.error(f'HTTP error:\n{e}')
                log.error(f'The NO.{i + 1} request failed, retrying...')
            except KeyError as e:
                log.error(f'Wrong response:\n{e}')
                log.error(f'The NO.{i + 1} request failed, retrying...')
            except Exception as e:
                log.error(f'Unknown error:\n{e}')
                log.error(f'The NO.{i + 1} request failed, retrying...')
            else:
                return response


req = HttpRequest()
