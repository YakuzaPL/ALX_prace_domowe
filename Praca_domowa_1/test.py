def triangle_checker(a, b, c):
    sides = [a, b, c]
    sides.sort()
    a = sides[0]
    b = sides[1]
    c = sides[2]

    if a + b > c:
        print("OK")
    else:
        print("Z takich boków nie da się zbudować trójkata.")

    return


print(triangle_checker(5,2,4))