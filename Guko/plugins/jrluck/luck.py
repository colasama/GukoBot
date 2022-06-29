import json
import random
import datetime
from pathlib import Path


CUR_DIR = Path(__file__).resolve().parent


def random_rp(qq):
    time = datetime.date.today()
    times = str(time)[0:4] + str(time)[5:7] + str(time)[8:10]
    seed = int(qq) + int(times)
    random.seed(seed)
    result = random.randint(0, 100)
    return result


def random_luck(qq):
    time = datetime.date.today()
    times = str(time)[0:4] + str(time)[5:7] + str(time)[8:10]
    seed = int(qq) + int(times) + int(20)
    random.seed(seed)
    numb = random.randint(0, 100)
    result = ""
    with open(CUR_DIR / "luck_data.json", "r", encoding="utf-8") as f:
        data = json.load(f)
        if numb == 100:
            result = data[0]["fields"]["img_url"]
        else:
            result = data[numb]["fields"]["img_url"]

    return result
