

# 创建一个Person类
class Person(object):
	# 类的构造方法，实例化时自动执行
	def __init__(self, name, age):
		self.name = name
		self.age = age

# 实例化一个Person类的对象，自动执行类中的__init__方法
# 将alex和18封装到person1的name和age属性中
person1 = Person("alex", 18)

# 实例化一个Person类的对象，自动执行类中的__init__方法
# 将qimi和20封装到person2的name和age属性中
person2 = Person("qimi", 20)

# 调用alex的封装
print(person1.name)    # 输出=> alex

# 调用20的封装
print(person2.age)    # 输出=> 20
