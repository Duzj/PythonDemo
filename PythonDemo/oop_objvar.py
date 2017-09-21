# coding=UTF-8
class Robot:
    """表示有一个带有名字的机器人"""
    popularion = 0

    def __init__(self, name):
        """初始化数据"""
        self.name = name
        print('(Initializing {})'.format(self.name))

        Robot.popularion += 1

    def die(self):
        """我挂了"""
        print("{} is being destroyed!".format(self.name))

        Robot.popularion -= 1
        self.__class__.popularion

        if Robot.popularion == 0:
            print("{} was the last one".format(self.name))
        else:
            print("there are still {:d} robots working".format(Robot.popularion))

    def say_hi(self):
        """来自机器人的问候

        没问题,你做得到"""
        print("greetings ,my masters call me {}.".format(self.name))
    # @staticmethod

    @classmethod
    def how_many(cls):
            """打印当前机器人数量"""
            print("we have {:d} robots".format(cls.popularion))


droid1 = Robot("R2-D2")

droid1.say_hi()

Robot.how_many()


droid2 = Robot("C-3PO")
droid2.say_hi()
Robot.how_many()

print("\nrobots can do some work here\n")

print("robots have finished their work. so let`s destory them")

droid1.die()

droid2.die()

Robot.how_many()

Robot.say_hi.__doc__
