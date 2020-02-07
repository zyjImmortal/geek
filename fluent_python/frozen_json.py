from collections import abc
import keyword

class FrozenJson:

    def __init__(self, mapping):
        # self.__data = dict(mapping)
        self.__data = {}
        for key, value in mapping.items():
            # 处理无效的属性名，如果发发现有python内置关键字，在其后面加下划线_
            if keyword.iskeyword(key):
                key += '_'
            self.__data[key] = value

    @classmethod
    def build(cls, obj):
        # mapping 对象就是key value对象
        if isinstance(obj, abc.Mapping):
            return cls(obj)
        elif isinstance(obj, abc.MutableSequence):
            return [cls.build(item) for item in obj]
        else:
            return obj

    # 仅当无法使
    # 用常规的方式获取属性（即在实例、类或超类中找不到指定的属性），
    # 解释器才会调用特殊的 __getattr__ 方法。
    def __getattr__(self, name):
        if hasattr(self.__data, name):
            return getattr(self.__data, name)
        else:
            # self.__data.

            if self.__data.get(name, None):
                return FrozenJson.build(self.__data[name])
            else:
                raise AttributeError(f"{name} dose not exist.")



class FrozenJsonV2:

    def __new__(cls, arg):
        if isinstance(arg, abc.Mapping):
            return super().__new__(cls)
        elif isinstance(arg, abc.MutableMapping):
            return [cls(item) for item in arg]
        else:
            return arg

    def __init__(self, mapping):
        self.__data = {}
        for key, value in mapping.items():
            # 处理无效的属性名，如果发发现有python内置关键字，在其后面加下划线_
            if keyword.iskeyword(key):
                key += '_'
            self.__data[key] = value

    def __getattr__(self, name):
        if hasattr(self.__data, name):
            return getattr(self.__data, name)
        else:
            # self.__data.

            if self.__data.get(name, None):
                return FrozenJson.build(self.__data[name])
            else:
                raise AttributeError(f"{name} dose not exist.")