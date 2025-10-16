import pyrosim.pyrosim as pyrosim

pyrosim.Start_SDF("box.sdf")  # Name of the world file

pyrosim.Send_Cube(
    name="Box", 
    pos=[0,0,0.5],  # x, y, z position
    size=[1,1,1]    # length, width, height
)

pyrosim.End()
