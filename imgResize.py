from PIL import Image
import os

i = 0
count = 1
size = [(28, 28)], [(56, 56)], [(112, 112)], [(800, 800)]
name = ["28x28", "56x56", "112x112", "800x800"]
execPath = os.getcwd()

for filename in os.listdir(os.path.abspath(execPath)):
    if filename.endswith(".png"):
        base = filename.split(".")[0]
        os.mkdir(str(base))
        while i < 4:
            with Image.open(filename) as im:
                im.thumbnail((size[i][0]))
                im.save(str(base) + "/" + name[i] + ".png", "PNG")
                i = i + 1
        i = 0
        count = count + 1
