class Players():
    def __init__(self, firstName, LastName, jerseyNo):
        self.firstName = firstName
        self.lastName = LastName
        self.jerseyNo = jerseyNo
    
    def __repr__(self):
        return '({} {}, {})'.format(self.firstName, self.lastName, self.jerseyNo)


p1 = Players('Pranay', 'Halder', 5)
p2 = Players('Subhasish', 'Bose', 2)
p3 = Players('Arindam', 'Bhattacharya', 1)
p4 = Players('Pritam', 'Kotal', 20)

players = [p1, p2, p3, p4]


from operator import attrgetter
s_players1 = sorted(players, key=attrgetter('firstName'))
print(s_players1)
s_players2 = sorted(players, key=attrgetter('lastName'))
print(s_players2)
s_players3 = sorted(players, key=attrgetter('jerseyNo'))
print(s_players3)
