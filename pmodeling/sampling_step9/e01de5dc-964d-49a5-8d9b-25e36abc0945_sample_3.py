import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
SeedSelect = Transition(label='Seed Select')
GerminateSeeds = Transition(label='Germinate Seeds')
TransplantSeedlings = Transition(label='Transplant Seedlings')
MixNutrients = Transition(label='Mix Nutrients')
AdjustpH = Transition(label='Adjust pH')
MonitorClimate = Transition(label='Monitor Climate')
ControlHumidity = Transition(label='Control Humidity')
CO2Regulation = Transition(label='CO2 Regulation')
DetectPests = Transition(label='Detect Pests')
DeployBiocontrols = Transition(label='Deploy Biocontrols')
ScheduleHarvest = Transition(label='Schedule Harvest')
AutomatePicking = Transition(label='Automate Picking')
PackageProduce = Transition(label='Package Produce')
CompostWaste = Transition(label='Compost Waste')
RecycleWater = Transition(label='Recycle Water')
DataLogging = Transition(label='Data Logging')
SystemMaintenance = Transition(label='System Maintenance')

# Define silent transitions for pauses or no activities
skip = SilentTransition()

# Define exclusive choice for monitoring climate, humidity, and CO2 levels
xor = OperatorPOWL(operator=Operator.XOR, children=[MonitorClimate, ControlHumidity, CO2Regulation])

# Define exclusive choice for pest detection and biocontrol deployment
xor2 = OperatorPOWL(operator=Operator.XOR, children=[DetectPests, DeployBiocontrols])

# Define loop for nutrient mixing and pH adjustment
loop = OperatorPOWL(operator=Operator.LOOP, children=[MixNutrients, AdjustpH])

# Define loop for data logging and system maintenance
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[DataLogging, SystemMaintenance])

# Define the root POWL model
root = StrictPartialOrder(nodes=[SeedSelect, GerminateSeeds, TransplantSeedlings, loop, xor, xor2, ScheduleHarvest, AutomatePicking, PackageProduce, CompostWaste, RecycleWater, loop2])
root.order.add_edge(SeedSelect, GerminateSeeds)
root.order.add_edge(GerminateSeeds, TransplantSeedlings)
root.order.add_edge(TransplantSeedlings, loop)
root.order.add_edge(loop, xor)
root.order.add_edge(xor, xor2)
root.order.add_edge(xor2, ScheduleHarvest)
root.order.add_edge(ScheduleHarvest, AutomatePicking)
root.order.add_edge(AutomatePicking, PackageProduce)
root.order.add_edge(PackageProduce, CompostWaste)
root.order.add_edge(CompostWaste, RecycleWater)
root.order.add_edge(RecycleWater, loop2)
root.order.add_edge(loop2, DataLogging)
root.order.add_edge(DataLogging, SystemMaintenance)
root.order.add_edge(SystemMaintenance, loop2)