class Pyrosim:
    def __init__(self, filename):
        self.filename = filename
        self.lines = []

    def Start_SDF(self):
        self.lines.append('<sdf version="1.6">')
        self.lines.append('  <world name="default">')

    def End(self):
        self.lines.append('  </world>')
        self.lines.append('</sdf>')
        with open(self.filename, 'w') as f:
            f.write('\n'.join(self.lines))

    def Send_Cube(self, name, pos=[0,0,0.5], size=[1,1,1]):
        self.lines.append(f'    <model name="{name}">')
        self.lines.append('      <static>false</static>')
        self.lines.append(f'      <link name="{name}Link">')
        self.lines.append(f'        <pose>{pos[0]} {pos[1]} {pos[2]} 0 0 0</pose>')
        self.lines.append('        <collision name="collision">')
        self.lines.append('          <geometry>')
        self.lines.append(f'            <box><size>{size[0]} {size[1]} {size[2]}</size></box>')
        self.lines.append('          </geometry>')
        self.lines.append('        </collision>')
        self.lines.append('        <visual name="visual">')
        self.lines.append('          <geometry>')
        self.lines.append(f'            <box><size>{size[0]} {size[1]} {size[2]}</size></box>')
        self.lines.append('          </geometry>')
        self.lines.append('        </visual>')
        self.lines.append('        <inertial>')
        self.lines.append('          <mass>1</mass>')
        self.lines.append('          <inertia>')
        self.lines.append('            <ixx>0.16666667</ixx>')
        self.lines.append('            <iyy>0.16666667</iyy>')
        self.lines.append('            <izz>0.16666667</izz>')
        self.lines.append('            <ixy>0</ixy><ixz>0</ixz><iyz>0</iyz>')
        self.lines.append('          </inertia>')
        self.lines.append('        </inertial>')
        self.lines.append('      </link>')
        self.lines.append('    </model>')
