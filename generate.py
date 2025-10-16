import pyrosim.pyrosim as pyrosim

length = 1
width = 1
height = 1
x = 0
y = 0
z = 1.5
n = 0

# [z,x,y]


def Create_World():
    pyrosim.Start_SDF("world.sdf")
    pyrosim.Send_Cube(
        name="Box", pos=[-10, -5, 1], size=[length, width, height])
    pyrosim.End()





Create_World()
Create_Robot()


# green line x
# red line z
