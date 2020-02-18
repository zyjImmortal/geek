

import json


def test_city_data(json_file):
    with json_file.open() as f:
        data = json.load(f)
    assert data['hubei']['city'] == '武汉'
