import warnings

import osconfeed
'''
from schedule import *
import shelve
db = shelve.open(DB_NAME)
if CONFERENCE not in db:
    load_db(db)
    
speaker = db['speaker.3471']
type(speaker)
Out[7]: schedule.Record
speaker.name
Out[8]: 'Anna Martelli Ravenscroft'
db.close()
'''


DB_NAME = 'fluent_python/data/schedule1_db'
CONFERENCE = 'conference.115'

class Record:
    def __init__(self, **kwargs):
        # 使用关键字参数传入的属性构建实例的常用便捷方式
        self.__dict__.update(kwargs)

    # def __eq__(self, other):
    #     if isinstance(other, Record):
    #         return self.__dict__ == other.__dict__
    #     else:
    #         return NotImplemented


def load_db(db):
    raw_data = osconfeed.load()
    for collection, rec_list in raw_data['Schedule'].items():
        record_type = collection[:-1]
        for record in rec_list:
            key = '{}.{}'.format(record_type, record['serial'])
            record['serial'] = key
            db[key] = Record(**record)