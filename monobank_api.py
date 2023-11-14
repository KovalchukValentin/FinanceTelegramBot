import os
import pprint
from datetime import datetime

from requests import get

import keys

MONOBANK_TOKEN = os.environ["MONOBANK_TOKEN"]
APIURL = "https://api.monobank.ua"
url = APIURL + '/personal/statement/account'


def get_info():
    api = get(APIURL+"/personal/client-info", headers={"X-Token": MONOBANK_TOKEN}).json()
    pprint.pprint(api)


def get_info_trans(from_unix_time, to_unix_time):
    api = get(f"{APIURL}/personal/statement/0/{from_unix_time}/{to_unix_time}", headers={"X-Token": MONOBANK_TOKEN}).json()
    pprint.pprint(api)


def get_first_day_of_current_month_unix_time():
    return int(datetime.now().replace(day=1).timestamp())


def get_unix_time():
    return int(datetime.now().timestamp())


if __name__ == "__main__":
    get_info_trans(from_unix_time=get_first_day_of_current_month_unix_time(), to_unix_time=get_unix_time())