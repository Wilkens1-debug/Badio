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

#exo 4
q = ("alo la polis m ap vini.")
m = q.split()
u = ''
for mo in m:
    if mo:
        p = mo[0]
        u += p
print("4: ",u)

#exo 5
o = "alo la polis m ap vini."
j = o.replace("a","@")
print("5: ",j)

#exo 6
r = "Badio"
s = ''.join(reversed(r.upper()))
print("6: ",s)

#exo 7
t = "alo la polis m ap vini."
v ="a"
k = t.count(v)
print("7: ", k)