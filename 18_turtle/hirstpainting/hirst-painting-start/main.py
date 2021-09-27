###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##
import colorgram

rgb_colors = []
colors = colorgram.extract('image.jpg', 30)
for color in colors:
    #print(color.rgb)
    rgb_colors.append((color.rgb.r,color.rgb.g,color.rgb.g))

print(rgb_colors)

# tuples = []
# for item in rgb_colors:
#     tuples.append((item.r,item.g,item.b))

# print(tuples)