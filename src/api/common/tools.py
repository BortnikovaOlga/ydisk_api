import json
import logging

logger = logging.getLogger("api")


def to_dict(oo) -> dict:
    """
    Возвращает объект как словарь.
    """
    return json.loads(json.dumps(oo, default=lambda o: o.__dict__))


def from_rus_to_lat(rus_json, translate_map: dict):
    """
    :param rus_json:  исходный с ключами на русском
    :param translate_map: карта соответствия русских ключей латинским
    :return: с латинскими ключами
    """

    def tranc_item(rus_dict: dict, translate: dict):
        lat_dict = dict()
        for key in rus_dict:
            lat_dict[translate[key]] = rus_dict[key]
        return lat_dict

    if isinstance(rus_json, dict):
        lat_json = tranc_item(rus_json, translate_map)
    elif isinstance(rus_json, list):
        lat_json = list()
        for item in rus_json:
            lat_json.append(tranc_item(item, translate_map))
    else:
        lat_json = None
    return lat_json
