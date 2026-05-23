def classify_triangle(a, b, c):
    try:
        a = float(a)
        b = float(b)
        c = float(c)
    except ValueError:
        return "Invalid input"
    if a <= 0 or b <= 0 or c <= 0 or a > 100 or b > 100 or c > 100:
        return "Invalid input"
    if a + b <= c or a + c <= b or b + c <= a:
        return "Not a triangle"
    if a == b == c:
        return "Equilateral"
    if a == b or a == c or b == c:
        return "Isosceles"
    return "Scalene"
triangle_type = classify_triangle(3, 4, 5)
print(triangle_type)