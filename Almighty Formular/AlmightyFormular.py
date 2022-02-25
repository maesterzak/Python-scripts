a = float( input('input variable a: ' ))
b = float(input('input variable b: '))
c = float(input('input variable c: '))

s1 = "b^2 +- sqrt(4 * a * c)"
s2 = f"-{b}^2 +- sqrt(4 * {a} * {c})"
print('formular', s1 )
print('Input Variables', s2 )
x1 = f"x1 = {-(b**2)} + sqrt(4 * {a} * {c})"
print(f">> {x1}")
x1 = f"x1 = {-(b**2)} + sqrt{(4 * a * c)}"
print(f">> {x1}")
x1 = f"x1 = {-(b**2)} + {(4 * a * c)**0.5}"
print(f">> {x1}")
x1 = f"x1 = {-(b**2) + (4 * a * c)**0.5}"

x2 = f"x2 = {-(b**2)} - sqrt(4 * {a} * {c})"
print(f">> {x2}")
x2 = f"x2 = {-(b**2)} - sqrt{(4 * a * c)}"
print(f">> {x2}")
x2 = f"x2 = {-(b**2)} - {(4 * a * c)**0.5}"
print(f">> {x2}")
x2 = f"x2 = {-(b**2) - (4 * a * c)**0.5}"

print(x1)
print(x2)