import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions
SeedSelect = Transition(label='Seed Select')
NutrientMix = Transition(label='Nutrient Mix')
SensorSetup = Transition(label='Sensor Setup')
EnvMonitor = Transition(label='Env Monitor')
GrowthScan = Transition(label='Growth Scan')
PestControl = Transition(label='Pest Control')
WaterCycle = Transition(label='Water Cycle')
HarvestRobo = Transition(label='Harvest Robo')
YieldAssess = Transition(label='Yield Assess')
WasteProcess = Transition(label='Waste Process')
EnergySync = Transition(label='Energy Sync')
PackBiodeg = Transition(label='Pack Biodeg')
MarketTrack = Transition(label='Market Track')
OrderAlign = Transition(label='Order Align')
LogisticsPlan = Transition(label='Logistics Plan')
FeedbackLoop = Transition(label='Feedback Loop')

# Define silent transitions
Skip = SilentTransition()

# Define operators
loop = OperatorPOWL(operator=Operator.LOOP, children=[SeedSelect, NutrientMix, SensorSetup, EnvMonitor, GrowthScan, PestControl, WaterCycle, HarvestRobo, YieldAssess, WasteProcess, EnergySync, PackBiodeg, MarketTrack, OrderAlign, LogisticsPlan, FeedbackLoop])

xor = OperatorPOWL(operator=Operator.XOR, children=[FeedbackLoop, Skip])

# Define the root of the POWL model
root = StrictPartialOrder(nodes=[loop, xor])
root.order.add_edge(loop, xor)

print(root)