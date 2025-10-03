class Person:
    def __init__(self, name,last_name, age, city):
        self.name = name
        self.last_name = last_name
        self.age = age
        self.city = city
    def info(self):
       return f' {self.name} {self.last_name} {self.age} {self.city}'
pro1=Person('Nuraiym', 'Zhenishbekova', 18, 'Talas')
print(pro1.info())