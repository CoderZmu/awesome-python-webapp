class Cat:
  def eat(self):
    print('233')

cat = Cat()
print(cat)

import decorator


class Student(object):
    def __init__(self, name, gender):
        self.name = name
        self.__gender = gender

    def set_gender(self, gender):
      if gender in self.legal_gender_values():
        self.__gender = gender
      else:
        raise ValueError('bad gender')

    def get_gender(self):
      return self.__gender

    def legal_gender_values(self):
        return ['male', 'female']


xiaoming = Student('xiaoming', 'male')
print(xiaoming._Student__gender)
l = []
print(type(l))
