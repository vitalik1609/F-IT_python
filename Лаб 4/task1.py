# TODO решите задачу
import json


def task() -> float:
    with open('input.json') as f:
        data = json.load(f)
        return round(sum([d['score']*d['weight'] for d in data]), 3)


print(task())
