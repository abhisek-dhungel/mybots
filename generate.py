import pyrosim.pyrosim as pyrosim

pyrosim.Start_SDF("box.sdf")  # Name of the world file

pyrosim.Send_Cube(name="box", pos=[0,0,0.5] , size=[1,1,1])

pyrosim.End()


