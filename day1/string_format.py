__author__ = 'Q1mi'

name = input("Name:").strip()
age = input("Age:")
job = input("Job:").strip()

print("Information of "+name+":\n"+"Name:"+name+"\nAge:"+age+"\nJob:"+job)
print("Information of %s：\nName:%s \nAge:%s \nJob:%s" % (name, name, age, job))
msg = '''
Information of %s:
    Name:%s
    Age:%s
    Job:%s
''' % (name, name, age, job)
print(msg)
