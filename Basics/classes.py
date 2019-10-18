class parent:
    def country(self):
        print(f'{self.name} is from {self.language}')


class Person(parent):
    # constractor function called when you intialized an object
    def __init__(self, name, language, country_name):
                                      # self refers to the object that you have intialized from the class
        self.name = name
        self.language = language
        self.country_name = country_name

    def talk(self):
        print(f'{self.name} is speaking {self.language}')


person = Person("jemy", "arabic", "egypt")
person.talk()
person.country()
