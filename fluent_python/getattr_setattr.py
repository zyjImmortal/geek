class Cat:
    class_level = '贵族'
    def __init__(self,name,type,speed,age):
        self.name = name
        self.type= type
        self.speed = speed
        self.age = age


    def run(self):
        print('%s岁的%s%s正在以%s的速度奔跑' % (self.age,self.type,self.name,self.speed))

    def __getattr__(self, item):
        print('你找的属性不存在')

    def __setattr__(self, key, value):
        # print('你在设置属性')
        # self.key = value这里不能这么写，因为这种方式本身也会触发setattr，会造成无限递归
        # __dict__ 方法会获取到对象的所有属性
        self.__dict__[key] = value  # 内部原理就是这么实现的，

    def __delattr__(self, item):
        print('你在删除属性')

xiaohua = Cat('小花','波斯猫','10m/s',10)
xiaohua.run() #10岁的波斯猫小花正在以10m/s的速度奔跑
xiaohua.wight = 50
print(xiaohua.__dict__)
