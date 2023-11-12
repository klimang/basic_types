import json

FILE = "input.json"


def sum_dict_lists(data: dict) -> float:
    result = sum([dict_["score"] * dict_["weight"] for dict_ in data])
    return round(result, 3)


if __name__ == "__main__":
    with open(FILE, 'r') as file:
        data = json.load(file)
    print(sum_dict_lists(data))
