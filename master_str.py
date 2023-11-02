# exo 1
a = "Mwen se Wilkens"
while ' ' in a or a.upper():
    a = a.lower()
    print(a)
    break

# exo 2
karakte = "Tale konsa nou prale"
lis = karakte.split()
print(lis)

#exo 3
c = "alo la polis  map vini"
n = " ".join(mot.capitalize() for mot in c.split())
print(n)