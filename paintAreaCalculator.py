def paint_calc(height, width, coverage):
    return int((height * width / coverage) + 0.99999999)
height = int(input())
width = int(input())
coverage = 5
print(paint_calc(height, width, coverage))
