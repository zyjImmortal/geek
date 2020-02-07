import warnings

import osconfeed

'''

'''

DB_NAME = 'fluent_python/data/schedule2_db'
CONFERENCE = 'conference.115'


class MissingDatabaseError(RuntimeError):
    "未指定数据库异常"


class Record:
    def __init__(self, **kwargs):
        # 使用关键字参数传入的属性构建实例的常用便捷方式
        self.__dict__.update(kwargs)

    def __eq__(self, other):
        if isinstance(other, Record):
            return self.__dict__ == other.__dict__
        else:
            return NotImplemented

class DbRecord(Record):

    __db = None  # 存储一个打开的数据库引用

    @staticmethod
    def set_db(db):
        DbRecord.__db = db


    @staticmethod
    def get_db():
        return DbRecord.__db

    # 类方法可以在子类中重新定制
    @classmethod
    def fetch(cls, ident):
        db = cls.get_db()
        try:
            return db[ident]
        except TypeError:
            if db is None:
                msg = "database not set; class '{}.set_db(my_db)'"
                raise MissingDatabaseError(msg.format(cls.__name__))
            else:
                raise

    def __repr__(self):
        if hasattr(self, 'serial'):
            cls_name = self.__class__.__name__
            return '<{} serial={!r}>'.format(cls_name, self.serial)
        else:
            return super(DbRecord, self).__repr__()


def load_db(db):
    raw_data = osconfeed.load()
    for collection, rec_list in raw_data['Schedule'].items():
        record_type = collection[:-1]
        for record in rec_list:
            key = '{}.{}'.format(record_type, record['serial'])
            record['serial'] = key
            db[key] = Record(**record)