import json
import random
from pathlib import Path

CUR_DIR = Path(__file__).resolve().parent


def add_meal(kind: str, meal: str):
    meal_list = open(CUR_DIR / "meal.json", 'r+', encoding='utf-8')
    data = json.load(meal_list)
    data[kind].append(meal)
    json.dump(data, meal_list, ensure_ascii=False)
    meal_list.close()


def del_meal(kind: str, meal: str):
    meal_list = open(CUR_DIR / "meal.json", 'r+', encoding='utf-8')
    data = json.load(meal_list)
    data[kind].remove(meal)
    json.dump(data, meal_list, ensure_ascii=False)
    meal_list.close()


def get_random_meal(kind: str):
    meal_list = open(CUR_DIR / "meal.json", 'r', encoding='utf-8')
    data = json.load(meal_list)
    if len(data[kind]) == 0:
        return "西北风"
    else:
        return data[kind][random.randint(0, len(data[kind])-1)]


def get_meal_list(kind: str):
    meal_list = open(CUR_DIR / "meal.json", 'r', encoding='utf-8')
    data = json.load(meal_list)
    meal_list.close()
    return data[kind]
