import string
from random import choice
import random
import re
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
nax = int(input("Antre yon nonb: "))
lis = []

for i in range(nax + 1):
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
lis = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
lis_d = [el for el in lis if el % 3 == 0]
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

# exo 9

dik = {'a':'1','b':'2','c':'3'}
kle = list(dik.keys())
vale = list(dik.values())
print("9.- kle yo", kle)
print("9.- vale yo", vale)
print("==================================================================================")

# exo 10
mama = [1,2,3,4,5,6,7]
momo = [0,2,4,6,8]
meme = [0,1,2,3,5,7,8,4]
mimi = list(set(mama)|set(momo)|set(meme))
print("10.- ", mimi)

print("================================Master diksyone==========================================")
# # exo 1
fax = {'a':'1','b':'2','c':'3'}
fox = list(fax.values())
print("1.- ",fox)
print("==================================================================================")


# #exo 2
fex = input("Antre vale w chef: ")
if fex.startswith("{") and fex.endswith("}"):
    print("2.- Gen akolad ni devan ni deye")
else:
    print("2.- Pa gen akolad ni devan ni deye")
print("==================================================================================")


# # exo 3



# # exo 4
pox = {'a':'1','b':'2','c':'3'}
pix = list(pox.values())
for po in pix:
    print("4.- ",po)
print("==================================================================================")

# # exo 5
print("==================================================================================")
tax = {'a':'1','b':'2','c':'3'}
tox = {}
for tex, tix in tax.items():
    tox[tex] = tix
print("5.- ", tax)
print("5.- Kopi: ", tox)

 
# # exo 6
print("==================================================================================")
yax = {'a':'1','b':'2','c':'3'}
for yix, yox in yax.items():
    if isinstance(yox, str):
        yax[yix]  = f"_{yox}_"
print("6.- ",yax)

# # exo 7
print("==================================================================================")
rax = {'a':'1','b':'Joseph','c':'323'}
rox = {rix:rex for rix, rex in rax.items() if rex.isdigit()}
print("7.- ", rox)

# #exo 8
print("==================================================================================")
bax = {'a':'1','b':'Joseph','c':'323'}
box = list(bax.items())
print("8.- ", box)

# # exo 9
print("==================================================================================")
vax = [('a','1'),('b','Joseph'),('c','323')]
vox = dict(vax)
print("9.- ",vox)



# # exo 10
# print("==================================================================================")

print("================================Master fonksyon==========================================")

print("==================================================================================")
# # exo 1
print("==================================================================================")

def max(pli):
    enves = pli[::-1]
    return enves
mix = input("Antre mo w: ")
mex = max(mix)
print("1.- ", mex)

print("==================================================================================")
# # exo 2

def kax(n):
    alphabe=string.ascii_lowercase
    kox = ''.join(choice(alphabe) for _ in range(n))
    return kox

random_kox = kax(10)
print("2.- ",random_kox)


# exo 3
print("==================================================================================")
def hax (p):
    hix = string.ascii_lowercase
    hox = ''.join(random.sample(hix,p))
    return hox
hex = hax(10)
print("3.- ", hex)
# exo 4
print("==================================================================================")
def vax (sa):
    if sa >20:
        print("pa bon.")
    vox = "0123456789abcdefghijklmnopqrstuvwxyz"
    if sa > len(vox):
        print("pa bon.")
    vex = ''.join(random.sample(vox,sa))
    return vex
vix = vax(10)
print("4.- ",vix)

# exo 5
print("==================================================================================")


def gox(se):
    
    gax = re.sub(r'[^a-zA-Z0-9-]', '', se)
    
    gax = re.sub(r'-+', '-', gax)

    if gax.startswith('-'):
        gax = gax[1:]
    if gax.endswith('-'):
        gax = gax[:-1]
    return gax

se = input("Antre yon mo: ")
gax = gox(se)
print("5.- ", gax)


# exo 6
print("==================================================================================")
def sax(wox, dex):
    sex = dex.join(wox)
    return sex
wox = "Mwen"
dex = ","
sex = sax(wox, dex)
print("6.- ",sex)

#exo 7
print("==================================================================================")
def xox(xex):
    xix = "abcdefghijklmnopqrstuvwxyz"  
    xax = '-'.join(str(xix.index(ch) + 1) for ch in xex)
    return xax
xex = "mwen"
xax = xox(xex)
print("7.-",xax)

# exo 8
print("==================================================================================")
def zox(zex):
    zax = "abcdefghijklmnopqrstuvwxyz"  # Abet la
    zyx = [zax[int(index) - 1] for index in zex.split('-')]
    zix = ''.join(zyx)
    return zix
zex = "13-23-5-14"
zix = zox(zex)
print("8.- ",zix)
# exo 9
print("==================================================================================")
def nox(nax, nax2):
    return (nax, nax2)
nex = "Mwen"
nex2 = "Vle"

nix = nox(nex, nex2)
print("9.- ",nix)

# exo 10
print("==================================================================================")
def yax(yyx):
    oyx = yyx.split()
    yix = []

    for xoy in oyx:
        if xoy != "":
            yix.append(xoy[0])

    return ''.join(yix)
yox = input("Antre non ou: ")
yex = yax(yox)
print("10.- Inisyal ou se:", yex)
