import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
SiteSurvey = Transition(label='Site Survey')
LoadTest = Transition(label='Load Test')
SoilSample = Transition(label='Soil Sample')
WaterCheck = Transition(label='Water Check')
DesignPlan = Transition(label='Design Plan')
BedSetup = Transition(label='Bed Setup')
IrrigationInstall = Transition(label='Irrigation Install')
ClimateSetup = Transition(label='Climate Setup')
SeedSelection = Transition(label='Seed Selection')
PlantingPhase = Transition(label='Planting Phase')
PestControl = Transition(label='Pest Control')
GrowthMonitor = Transition(label='Growth Monitor')
HarvestPrep = Transition(label='Harvest Prep')
CommunityMeet = Transition(label='Community Meet')
WasteManage = Transition(label='Waste Manage')
YieldReport = Transition(label='Yield Report')

# Define the silent transition
skip = SilentTransition()

# Define the exclusive choice (XOR) for Pest Control and Growth Monitor
xor = OperatorPOWL(operator=Operator.XOR, children=[PestControl, GrowthMonitor])

# Define the loop for Community Meet and Waste Manage
loop = OperatorPOWL(operator=Operator.LOOP, children=[CommunityMeet, WasteManage])

# Define the partial order
root = StrictPartialOrder(nodes=[SiteSurvey, LoadTest, SoilSample, WaterCheck, DesignPlan, BedSetup, IrrigationInstall, ClimateSetup, SeedSelection, PlantingPhase, xor, HarvestPrep, loop, YieldReport])

# Add dependencies to the partial order
root.order.add_edge(SiteSurvey, LoadTest)
root.order.add_edge(SiteSurvey, SoilSample)
root.order.add_edge(SiteSurvey, WaterCheck)
root.order.add_edge(LoadTest, DesignPlan)
root.order.add_edge(SoilSample, DesignPlan)
root.order.add_edge(WaterCheck, DesignPlan)
root.order.add_edge(DesignPlan, BedSetup)
root.order.add_edge(BedSetup, IrrigationInstall)
root.order.add_edge(IrrigationInstall, ClimateSetup)
root.order.add_edge(ClimateSetup, SeedSelection)
root.order.add_edge(SeedSelection, PlantingPhase)
root.order.add_edge(PlantingPhase, xor)
root.order.add_edge(xor, HarvestPrep)
root.order.add_edge(HarvestPrep, loop)
root.order.add_edge(loop, YieldReport)

print(root)