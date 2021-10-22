#This program prints the Inverse of a 3 by 3 matrix

print("If the three by three matrix A is given in the form shown below, Input your values for the respective variables ")
print("This program will return the inverse of the three by three matrix")
print("[a, b, c]")
print("[d, e, f]")
print("[g, h, i]")
# To let the user understand what and how the program works
a = float(input("Input the value of a: "))
b = float(input("Input the value of b: "))
c = float(input("Input the value of c: "))
d = float(input("Input the value of d: "))
e = float(input("Input the value of e: "))
f = float(input("Input the value of f: "))
g = float(input("Input the value of g: "))
h = float(input("Input the value of h: "))
i = float(input("Input the value of i: "))

determinant = ((a*e*i)-(a*f*h)-(b*d*i)+(b*f*g)+(c*d*h)-(c*e*g))
aa = (e*i)-(f*h)
bb = -1*((d*i)-(f*g))
cc = ((d*h)-(g*e))
dd = -1*((b*i)-(c*h))
ee = ((a*i)-(c*g))
ff = -1*((a*h)-(g*b))
gg = ((b*f)-(c*e))
hh = -1*((a*f)-(c*d))
ii = ((a*e)-(b*d))

aaa = aa/determinant
bbb = bb/determinant
ccc = cc/determinant
ddd = dd/determinant
eee = ee/determinant
fff = ff/determinant
ggg = gg/determinant
hhh = hh/determinant
iii = ii/determinant

salim = [
    [aaa,ddd,ggg],
    [bbb,eee,hhh],
    [ccc,fff,iii]
]
for rows in salim:
    print(rows)
