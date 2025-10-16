from pyrosim.pyrosim import Pyrosim

num_blocks = 10
length = width = height = 1
x = 0
y = 0

pyrosim = Pyrosim("tower.sdf")
pyrosim.Start_SDF()

for i in range(num_blocks):
    z = (height/2) + i * height
    pyrosim.Send_Cube(name=f"Block{i}", pos=[x, y, z], size=[length, width, height])
    # shrink each block for visual effect
    length *= 0.9
    width  *= 0.9
    height *= 0.9

pyrosim.End()
