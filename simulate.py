from simulation import SIMULATION
import sys

# Accept either:
#   python simulate.py <DIRECT|GUI> <solutionID>
# or
#   python simulate.py <DIRECT|GUI>
# or no args at all. Provide safe defaults.
args = sys.argv[1:]

if len(args) >= 1:
	directOrGUI = args[0].upper()
else:
	directOrGUI = 'GUI'

if directOrGUI in ("D", "HEADLESS", "1", "TRUE"):
	directOrGUI = "DIRECT"
elif directOrGUI in ("G", "WINDOW", "0", "FALSE"):
	directOrGUI = "GUI"
elif directOrGUI not in ("DIRECT", "GUI"):
	directOrGUI = "GUI"

if len(args) >= 2:
	solutionID = args[1]
else:
	# Some callers don't use solutionID; default to '0'
	solutionID = '0'

print(f"Starting simulation: mode={directOrGUI}, id={solutionID}")

simulation = SIMULATION(directOrGUI, solutionID)
simulation.Run()
simulation.Get_Fitness()
simulation.Run()
simulation.Get_Fitness()
