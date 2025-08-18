import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define POWL activities with their labels
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

# Define the POWL model
root = StrictPartialOrder(nodes=[SeedSelect, NutrientMix, SensorSetup, EnvMonitor, GrowthScan, PestControl, WaterCycle, HarvestRobo, YieldAssess, WasteProcess, EnergySync, PackBiodeg, MarketTrack, OrderAlign, LogisticsPlan, FeedbackLoop])

# Define the dependencies between activities
root.order.add_edge(SeedSelect, NutrientMix)
root.order.add_edge(NutrientMix, SensorSetup)
root.order.add_edge(SensorSetup, EnvMonitor)
root.order.add_edge(EnvMonitor, GrowthScan)
root.order.add_edge(GrowthScan, PestControl)
root.order.add_edge(PestControl, WaterCycle)
root.order.add_edge(WaterCycle, HarvestRobo)
root.order.add_edge(HarvestRobo, YieldAssess)
root.order.add_edge(YieldAssess, WasteProcess)
root.order.add_edge(WasteProcess, EnergySync)
root.order.add_edge(EnergySync, PackBiodeg)
root.order.add_edge(PackBiodeg, MarketTrack)
root.order.add_edge(MarketTrack, OrderAlign)
root.order.add_edge(OrderAlign, LogisticsPlan)
root.order.add_edge(LogisticsPlan, FeedbackLoop)

# Print the root POWL model
print(root)