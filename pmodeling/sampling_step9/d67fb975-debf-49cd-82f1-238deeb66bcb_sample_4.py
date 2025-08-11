import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
SiteAnalyze = Transition(label='Site Analyze')
SoilEnhance = Transition(label='Soil Enhance')
SeedSelect = Transition(label='Seed Select')
PlantPrecise = Transition(label='Plant Precise')
SensorDeploy = Transition(label='Sensor Deploy')
ClimateMonitor = Transition(label='Climate Monitor')
IrrigateAdjust = Transition(label='Irrigate Adjust')
NutrientFeed = Transition(label='Nutrient Feed')
PestControl = Transition(label='Pest Control')
CommunityEngage = Transition(label='Community Engage')
FeedbackCollect = Transition(label='Feedback Collect')
YieldHarvest = Transition(label='Yield Harvest')
WasteSort = Transition(label='Waste Sort')
CompostCreate = Transition(label='Compost Create')
DataAnalyze = Transition(label='Data Analyze')
NetworkDistribute = Transition(label='Network Distribute')

# Define silent transitions
skip = SilentTransition()

# Define loops and exclusive choices
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[ClimateMonitor, IrrigateAdjust, NutrientFeed, PestControl])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[CommunityEngage, FeedbackCollect])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[YieldHarvest, WasteSort])
loop4 = OperatorPOWL(operator=Operator.LOOP, children=[DataAnalyze, NetworkDistribute])

# Define the root of the POWL model
root = StrictPartialOrder(nodes=[loop1, loop2, loop3, loop4])

# Add edges between the nodes
root.order.add_edge(loop1, loop2)
root.order.add_edge(loop2, loop3)
root.order.add_edge(loop3, loop4)

# Print the POWL model
print(root)