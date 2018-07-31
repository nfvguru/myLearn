#!/usr/bin/env python3

class Scoop():
    def __init__(self, flavor):
        self.flavor = flavor

    def __repr__(self):
        return f"Scoop of {self.flavor}"

s1 = Scoop('chocolate')
s2 = Scoop('vanilla')
s3 = Scoop('coffee')
s4 = Scoop('flavor 4')
s5 = Scoop('flavor 5')
s6 = Scoop('flavor 6')

print(s1.flavor)

for one_scoop in [s1, s2, s3]:
    print(one_scoop.flavor)
    

class Bowl():
    max_scoops = 3
    
    def __init__(self):
        self.scoops = [ ]
    def add_scoops(self, *args):
        self.scoops += args[:self.max_scoops
                            - len(self.scoops)]

        # for one_scoop in args:
            # if len(self.scoops) >= 3:
            #     break
            # self.scoops.append(one_scoop)
        
    def flavors(self):
        return ','.join([one_scoop.flavor
                         for one_scoop in self.scoops])

        # output = []
        # for one_scoop in self.scoops:
        #     output.append(one_scoop.flavor)
        # return output
    def __repr__(self):
        output = 'Bowl of: \n'
        output += '\n'.join([f"\t{index}: {one_scoop}"
                             for index, one_scoop in enumerate(self.scoops, 1)])
        return output


b = Bowl()
b.add_scoops(s1, s2)
b.add_scoops(s3)
b.add_scoops(s4,s5, s6)
print(b.flavors()) # ['chocolate', 'vanilla', 'coffee']

class BigBowl(Bowl):
    max_scoops = 5

bb = BigBowl() # up to 5 scoops
bb.add_scoops(s1, s2)
bb.add_scoops(s3)
bb.add_scoops(s4,s5, s6)
print(bb.flavors()) 

print(s1)   #  Scoop of chocolate

print(b)   #
print(bb)

# Bowl with:
# (1) Scoop of chocolate
# (2) Scoop of vanilla
# (3) Scoop of coffee
