from manim import *

# Insert Complex Points in the following list as a of two list
"""
z1 = 4+5i
z2 = -6+9i
The third list will be the product of first two and is calculated by the program
complex_points= [
    [4,5],
    [-6,9]
]
"""
cp =  [
    [2,3],
    [6,2]
]

# Product of first two 
# Note product is carried out like complex numbers are multiplied
cp.append(
    [
    cp[0][0]*cp[1][0] - cp[0][1]*cp[1][1],
    cp[0][0]*cp[1][1] + cp[0][1]*cp[1][0]
    ]
)

# Radiuses of all the complex points
r = [
]
# Calculating radius of each point and storing them in r list
for i in range(0,len(cp)):
    r.append(np.sqrt(cp[i][0]**2 + cp[i][1]**2))

# Angle of all the complex points
t = [
]
# Calculating theta of each point and storing them in t list
for i in range(0,len(cp)):
    t.append(np.arctan(cp[i][1]/cp[i][0]))

# Printing the values
print("<--Complex Form-->")
print(f"z1 = {cp[0][0]}+{cp[0][1]}i , z2 = {cp[1][0]}+{cp[1][1]}i")
print(f"z1 * z2 = {cp[2][0]} + {cp[2][1]}i")
print(f"<--Polar Coordinates-->")
print(f"z1 = ({r[0]}{t[0]}\nz2 = ({r[1]},{t[1]})\nz1 * z2 = ({r[2]},{t[2]})")


# Ploting Points with manim
class complex_to_polar(Scene):
    def construct(self):
        axes = Axes(x_range= [-25,25], y_range= [-25,25]).add_coordinates(font_size= 15)
        self.add(axes)
        for i in range(0,len(cp)):
            pt = Dot(color= YELLOW).move_to(axes.polar_to_point(r[i],t[i]))
            self.add(
                pt,
                MathTex(f"z{i} = {cp[i][0]} + ({cp[i][1]})i").next_to(pt, UR, buff= 1),
                Vector(axes.polar_to_point(r[i],t[i]), color= BLUE)
            )
