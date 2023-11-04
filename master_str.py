print("================================Master str==========================================")

# exo 1
print("==================================================================================")
a = "Alo la polis m ap vini."
while ' ' in a or a.upper():
    a = a.lower()
    print("1.- ",a)
    break

print("==================================================================================")
# exo 2
karakte = "Alo la polis m ap vini. "
lis = karakte.split()
print("2.- ",lis)

print("==================================================================================")
#exo 3
c = "alo la polis  map vini"
n = " ".join(mot.capitalize() for mot in c.split())
print("3.- ",n)
print("==================================================================================")

#exo 4
q = ("alo la polis m ap vini.")
m = q.split()
u = ''
for mo in m:
    if mo:
        p = mo[0]
        u += p
print("4.- ",u)

print("==================================================================================")
#exo 5
o = "alo la polis m ap vini."
j = o.replace("a","@")
print("5.- ",j)

print("==================================================================================")

#exo 6
r = "Badio"
s = ''.join(reversed(r.upper()))
print("6.- ",s)

print("==================================================================================")

#exo 7
t = "alo la polis m ap vini."
v ="a"
k = t.count(v)
print("7.- ", k)

print("==================================================================================")
chenn = "alo la polis m ap vini"
kantite_a = 0

for karakter in chenn:
    if karakter.lower() == "a":
        kantite_a += 1

print("8.-:", kantite_a)
print("==================================================================================")
chenn = "Ayiti ap vanse"
l = "a"

e = [i for i, ka in enumerate(chenn) if ka == l]

if e:
    print(f"9.- karakte '{l}' endeks: {len(e)}")
    print(f"Endeks yo se: {e}")
else:
    print(f"Karakte '{l}' pa  nan chenn la.")
print("==================================================================================")

#exo 10
teks = ("Teks san espas.")
espas = teks.replace(" ","")
print("10.- ",espas)

print("================================Master list==========================================")
# exo 1
n = int(input("Antre yon nonb: "))
lis = []

for i in range(n + 1):
    if i % 2 == 0:
        lis.append(i)

print("1.- ",lis)
print("==================================================================================")

# exo 2
antye = [1,2,3,4,5]
li = [str(n) for n in antye]
print("2.- ",li)
print("==================================================================================")
 
# exo 3
mi = ['patrick','mars','maximum']
maj =[mo.upper() for mo in mi]
print("3.- ",maj)
print("==================================================================================")

# exo 4
lis = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
lis_d = [el for index, el in enumerate(lis) if index % 3]
print("4.- ",lis_d)
print("==================================================================================")

# exo 5
lis_e = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]
lis_n = [tuple(lis_e[i:i+3])for i in range(0, len(lis_e),3)]
print("5.- ",lis_n)
print("==================================================================================")

# exo 6
lis_eleman = [1,2,3,4,5,6,1,2,3,4,5,6]
doublon = list(set(lis_eleman))
print("6.- ",doublon)
print("==================================================================================")

# exo 7
la = [1,2,3,4,5,6,7,8,9]
lo = [1,23,34,5,67,8,9,0]
ns = [f for f in la if f in lo]
print("7.- ",ns)
print("==================================================================================")

# exo 8
ji = [1,2,3,4,5,6,7,8,9,0]
jo = [1,3,5,7,9]
no = [fa for fa in ji if fa not in ji] + [fa for fa in ji if fa not in jo]
print("8.- ",no)
print("==================================================================================")
