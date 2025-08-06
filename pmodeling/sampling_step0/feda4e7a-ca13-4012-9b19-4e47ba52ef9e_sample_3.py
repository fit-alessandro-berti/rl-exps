import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
SiteAnalysis = Transition(label='Site Analysis')
EnvScanning = Transition(label='Env Scanning')
FarmDesign = Transition(label='Farm Design')
NutrientMix = Transition(label='Nutrient Mix')
SeedAutomation = Transition(label='Seed Automation')
GrowthMonitor = Transition(label='Growth Monitor')
PestControl = Transition(label='Pest Control')
AI_Diagnostics = Transition(label='AI Diagnostics')
HarvestPlan = Transition(label='Harvest Plan')
RoboticSort = Transition(label='Robotic Sort')
PackagingLine = Transition(label='Packaging Line')
CommunityInput = Transition(label='Community Input')
DataAggregation = Transition(label='Data Aggregation')
WasteRecycle = Transition(label='Waste Recycle')
Sustainability = Transition(label='Sustainability')

# Define the nodes
skip = SilentTransition()
loop = OperatorPOWL(operator=Operator.LOOP, children=[SiteAnalysis, EnvScanning])
xor1 = OperatorPOWL(operator=Operator.XOR, children=[FarmDesign, NutrientMix, skip])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[SeedAutomation, GrowthMonitor, skip])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[PestControl, AI_Diagnostics, skip])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[HarvestPlan, RoboticSort, skip])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[PackagingLine, CommunityInput, skip])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[DataAggregation, WasteRecycle, skip])
xor7 = OperatorPOWL(operator=Operator.XOR, children=[Sustainability, skip])

# Define the order
root = StrictPartialOrder(nodes=[loop, xor1, xor2, xor3, xor4, xor5, xor6, xor7])
root.order.add_edge(loop, xor1)
root.order.add_edge(xor1, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, xor5)
root.order.add_edge(xor5, xor6)
root.order.add_edge(xor6, xor7)
root.order.add_edge(xor7, skip)