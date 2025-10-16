import pybullet as p
import pybullet_data
import time

physicsClient = p.connect(p.GUI)
p.configureDebugVisualizer(p.COV_ENABLE_GUI,0)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-9.8, physicsClient)

planeId = p.loadURDF("plane.urdf")
p.loadSDF("tower.sdf")

for i in range(1000):
    p.stepSimulation()
    time.sleep(1/60)

p.disconnect()
