class Person:
    # write your code here
    people = {}
    def __init__(self, name: str, age: int):
        self.name = name  # instance attribute
        self.age = age  # instance attribute
        Person.people[name] = self


def create_person_list(people: list) -> list:
    # write your code here
    person_list = []
    for pers in people:
        person = Person(data["name"], data["age"])
        person_list.append(person)
    
    for data in people_data:
        person = Person.people[data["name"]]

        if data.get("wife"):
            person.wife = Person.people[data["wife"]]

        if data.get("husband"):
            person.husband = Person.people[data["husband"]]
            
    return person_list
