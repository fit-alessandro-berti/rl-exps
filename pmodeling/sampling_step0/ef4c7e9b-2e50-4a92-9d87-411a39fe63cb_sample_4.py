import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator
from pm4py.algo.filtering.powl.powl import powl

SeedSelection = Transition(label='Seed Selection')
NutrientMix = Transition(label='Nutrient Mix')
EnvironmentSetup = Transition(label='Environment Setup')
PestScan = Transition(label='Pest Scan')
LightControl = Transition(label='Light Control')
GrowthMonitor = Transition(label='Growth Monitor')
WaterCycle = Transition(label='Water Cycle')
AirQuality = Transition(label='Air Quality')
RoboticHarvest = Transition(label='Robotic Harvest')
QualityCheck = Transition(label='Quality Check')
DataLogging = Transition(label='Data Logging')
Packaging = Transition(label='Packaging')
WasteSort = Transition(label='Waste Sort')
EnergyAudit = Transition(label='Energy Audit')
RetailSync = Transition(label='Retail Sync')

skip = SilentTransition()

# Define the POWL model
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[SeedSelection, NutrientMix, EnvironmentSetup, PestScan, LightControl, GrowthMonitor, WaterCycle, AirQuality])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[RoboticHarvest, QualityCheck, DataLogging, Packaging, WasteSort])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[EnergyAudit, RetailSync])

xor1 = OperatorPOWL(operator=Operator.XOR, children=[loop1, skip])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[loop2, skip])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[loop3, skip])

root = StrictPartialOrder(nodes=[xor1, xor2, xor3])

root.order.add_edge(xor1, xor2)
root.order.add_edge(xor1, xor3)
root.order.add_edge(xor2, xor3)

# Print the POWL model
print(root)