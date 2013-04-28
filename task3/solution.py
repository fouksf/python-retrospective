class Person:

    def __init__(self, name, birth_year, gender, father=None, mother=None):
        self.name = name
        self.birth_year = birth_year
        self.gender = gender
        self._children = []
        self.father = father
        self.mother = mother
        if father:
            father._children += [self]
        if mother:
            mother._children += [self]

    def get_brothers(self):
        return self.get_siblings("M")

    def get_sisters(self):
        return self.get_siblings("F")

    def get_siblings(self, gender):
        siblings = []
        if self.father:
            siblings += self.father.children(gender)
        if self.mother:
            siblings += self.mother.children(gender)
        return sorted(set(siblings) - {self})

    def children(self, gender=None):
        if gender:
            return list(filter(lambda x: x.gender == gender, self._children))
        return self._children

    def is_direct_successor(self, person):
        return person in self._children
