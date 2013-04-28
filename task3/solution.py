class Person:

    def __init__(self, name, birth_year, gender, father=None, mother=None):
        self.name = name
        self.birth_year = birth_year
        self.gender = gender
        self._children = []
        self.father = father
        self.mother = mother
        for parent in mother, father:
            if parent:
                parent._children += [self]

    def get_brothers(self):
        return self.get_siblings("M")

    def get_sisters(self):
        return self.get_siblings("F")

    def get_siblings(self, gender):
        return sorted(set(self.father.children(gender) +
                          self.mother.children(gender)) - {self})

    def children(self, gender=None):
        if gender:
            return list(filter(lambda x: x.gender == gender, self._children))
        return self._children

    def is_direct_successor(self, person):
        return person in self._children
