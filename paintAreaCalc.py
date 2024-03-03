def paint_calc(height,width):
    cans=(height*width)/5
    print(f"The amount of cans needed is :{round(cans)}")

test_h = int(input("height of the wall:\n"))
test_w = int(input("width of the wall :\n"))
paint_calc(height=test_h, width=test_w)
