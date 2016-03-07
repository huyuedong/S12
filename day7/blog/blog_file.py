

# 创建一个Person类
class Person(object):
	# 父类的构造方法，实例化时自动执行
	def __init__(self, name, age):
		self.name = name
		self.age = age

	# 父类的方法
	def print(self):
		print("{} is {} years old.".format(self.name, self.age))


# 定义一个Teacher的类，继承Person类
class Teacher(Person):

	# # 不推荐这么写
	# def __init__(self, habit):
	# 	super(Person, self).__init__()
	# 	self.habit = habit

	# 旧的写法，也不推荐这么写
	# def __init__(self, name, age, habit):
	# 	Person.__init__(self, name, age)
	# 	self.habit = habit

	# 推荐写法，在子类的构造方法里只出现子类的类名
	def __init__(self, name, age, habit):
		super(Teacher, self).__init__(name, age)
		self.habit = habit

	# 定义一个方法
	def get_habit(self):
		print("The habit of {} is {}.".format(self.name, self.habit))

# 实例化一个老师
alex = Teacher("alex", 18, "Girl")
# 调用父类的方法
alex.print()
# 调用本类的方法
alex.get_habit()









# # 实例化一个Person类的对象，自动执行类中的__init__方法
# # 将alex和18封装到person1的name和age属性中
# person1 = Person("alex", 18)
#
# # 实例化一个Person类的对象，自动执行类中的__init__方法
# # 将qimi和20封装到person2的name和age属性中
# person2 = Person("qimi", 20)
#
# # 调用alex的封装
# print(person1.name)    # 输出=> alex
#
# # 调用20的封装
# print(person2.age)    # 输出=> 20
