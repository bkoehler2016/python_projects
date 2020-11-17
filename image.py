image_str = [
    "#############################",
    "#                           #",
    "#      #########            #",
    "#     #  #      #           #",
    "#    #  # #     #           #",
    "#    #  # #  ###            #",
    "#    #   #  #        ###    #",
    "#     ##    #        # #    #",
    "#      #####       ### ###  #",
    "#                  #     #  #",
    "#                  ### ###  #",
    "#                    # #    #",
    "#############################",
]

image = []

for i in image_str:
    image.append(list(i))

def print_image():
    for i in image:
        print("".join(i))

def floodfill(row, col, char):
    if image[row][col] != ' ':
        return

    image[row][col] = char

    floodfill(row, col + 1, char)
    floodfill(row, col - 1, char)
    floodfill(row + 1, col, char)
    floodfill(row - 1, col, char)

floodfill(4, 7, '*')
floodfill(2, 2, '.')

print_image()