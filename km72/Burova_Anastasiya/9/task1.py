x1 = float(input("Enter x1:"))
y1 = float(input("Enter y1:"))
x2 = float(input("Enter x2:"))
y2 = float(input("Enter y2:"))
def distance(x1, y1, x2, y2):
    result = (((x1 - x2)**2 + (y1 - y2)**2)**0.5)
    return result
print(distance(x1, y1, x2, y2))
