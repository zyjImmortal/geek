

import pytest
import json


@pytest.fixture(scope='module')
def json_file(tmpdir_factory):
    city_data={
        'hubei':{
            'city':'武汉'
        },
        'hunan':{
            'city': '长沙'
        },
        'hainan':{
            'city': '海口'
        }
    }
    file = tmpdir_factory.mktemp('data').join('data.json')
    print('file:{}'.format(str(file)))
    with file.open('w') as f:
        json.dump(city_data, f)
    return file