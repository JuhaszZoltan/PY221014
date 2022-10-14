import random

# random.random() -> visszaad egy [0; 1) közötti véletlen számot
for x in range(10):
    print(random.random())

# random.randint(a, b) -> [a; b] között generál egy véletlen egész számot
# úgy van értelme, hogy a < b
for x in range(10):
    print(random.randint(10, 20))

# random.randrange(start, stop, step) -> [start, stop) között állít elő véletlen számokat úgy, hogy a start és stop közötti 'lépték' a step
for x in range(10):
    print(random.randrange(10, 20, 2))