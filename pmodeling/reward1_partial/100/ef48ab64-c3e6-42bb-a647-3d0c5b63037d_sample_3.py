import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
SiteSelect = Transition(label='Site Select')
EnvAssess = Transition(label='Env Assess')
DesignModules = Transition(label='Design Modules')
HydroponicsSetup = Transition(label='Hydroponics Setup')
SoftwareDev = Transition(label='Software Dev')
SeedChoose = Transition(label='Seed Choose')
LEDInstall = Transition(label='LED Install')
TrainStaff = Transition(label='Train Staff')
ComplianceCheck = Transition(label='Compliance Check')
EngageCommunity = Transition(label='Engage Community')
PlantCrops = Transition(label='Plant Crops')
MonitorGrowth = Transition(label='Monitor Growth')
OptimizeYields = Transition(label='Optimize Yields')
WasteManage = Transition(label='Waste Manage')
EnergyAudit = Transition(label='Energy Audit')
WaterRecycle = Transition(label='Water Recycle')

# Define silent transitions for empty steps
skip = SilentTransition()

# Define loops and choices
env_loop = OperatorPOWL(operator=Operator.LOOP, children=[SiteSelect, EnvAssess, DesignModules, HydroponicsSetup, SoftwareDev])
seed_loop = OperatorPOWL(operator=Operator.LOOP, children=[SeedChoose, LEDInstall, TrainStaff, ComplianceCheck, EngageCommunity])
plant_loop = OperatorPOWL(operator=Operator.LOOP, children=[PlantCrops, MonitorGrowth, OptimizeYields])
waste_loop = OperatorPOWL(operator=Operator.LOOP, children=[WasteManage, EnergyAudit, WaterRecycle])

# Create the root node of the POWL model
root = StrictPartialOrder(nodes=[env_loop, seed_loop, plant_loop, waste_loop])
root.order.add_edge(env_loop, seed_loop)
root.order.add_edge(seed_loop, plant_loop)
root.order.add_edge(plant_loop, waste_loop)

print(root)