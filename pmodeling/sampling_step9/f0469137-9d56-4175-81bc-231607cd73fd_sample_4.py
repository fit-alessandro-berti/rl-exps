import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
SiteAnalysis = Transition(label='Site Analysis')
ClimateSetup = Transition(label='Climate Setup')
NutrientMix = Transition(label='Nutrient Mix')
SeedGerminate = Transition(label='Seed Germinate')
AutoPlanting = Transition(label='Auto Planting')
IrrigationSetup = Transition(label='Irrigation Setup')
IoTMonitoring = Transition(label='IoT Monitoring')
PestDetection = Transition(label='Pest Detection')
DronePollinate = Transition(label='Drone Pollinate')
PesticideSpray = Transition(label='Pesticide Spray')
RoboticHarvest = Transition(label='Robotic Harvest')
QualityCheck = Transition(label='Quality Check')
PackageProduct = Transition(label='Package Product')
WasteRecycle = Transition(label='Waste Recycle')
EnergyOptimize = Transition(label='Energy Optimize')
DataLogging = Transition(label='Data Logging')

skip = SilentTransition()

# Define the loop nodes
loop_Irrigation = OperatorPOWL(operator=Operator.LOOP, children=[IrrigationSetup, skip])
loop_Monitoring = OperatorPOWL(operator=Operator.LOOP, children=[IoTMonitoring, PestDetection, skip])
loop_Harvest = OperatorPOWL(operator=Operator.LOOP, children=[RoboticHarvest, QualityCheck, PackageProduct])

# Define the exclusive choice nodes
xor_PestDetection = OperatorPOWL(operator=Operator.XOR, children=[PestDetection, skip])
xor_Irrigation = OperatorPOWL(operator=Operator.XOR, children=[DronePollinate, PesticideSpray])

# Define the partial order
root = StrictPartialOrder(nodes=[SiteAnalysis, ClimateSetup, NutrientMix, SeedGerminate, AutoPlanting, loop_Irrigation, loop_Monitoring, loop_Harvest, xor_PestDetection, xor_Irrigation, DataLogging])

# Add edges to the partial order
root.order.add_edge(SiteAnalysis, ClimateSetup)
root.order.add_edge(ClimateSetup, NutrientMix)
root.order.add_edge(NutrientMix, SeedGerminate)
root.order.add_edge(SeedGerminate, AutoPlanting)
root.order.add_edge(AutoPlanting, loop_Irrigation)
root.order.add_edge(loop_Irrigation, loop_Monitoring)
root.order.add_edge(loop_Monitoring, loop_Harvest)
root.order.add_edge(loop_Harvest, xor_PestDetection)
root.order.add_edge(xor_PestDetection, xor_Irrigation)
root.order.add_edge(xor_Irrigation, DataLogging)

# Print the POWL model
print(root)