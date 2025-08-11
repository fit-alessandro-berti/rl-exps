import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
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
Skip = SilentTransition()

# Define the loop node for planting phase
loop = OperatorPOWL(operator=Operator.LOOP, children=[PlantingPhase, PestControl])

# Define exclusive choice for climate setup and design plan
xor = OperatorPOWL(operator=Operator.XOR, children=[ClimateSetup, DesignPlan])

# Define the root of the POWL model
root = StrictPartialOrder(nodes=[SiteSurvey, LoadTest, SoilSample, WaterCheck, xor, loop, BedSetup, IrrigationInstall, SeedSelection, GrowthMonitor, HarvestPrep, CommunityMeet, WasteManage, YieldReport])
root.order.add_edge(SiteSurvey, LoadTest)
root.order.add_edge(LoadTest, SoilSample)
root.order.add_edge(SoilSample, WaterCheck)
root.order.add_edge(WaterCheck, xor)
root.order.add_edge(xor, loop)
root.order.add_edge(loop, BedSetup)
root.order.add_edge(BedSetup, IrrigationInstall)
root.order.add_edge(IrrigationInstall, SeedSelection)
root.order.add_edge(SeedSelection, PlantingPhase)
root.order.add_edge(PlantingPhase, PestControl)
root.order.add_edge(PestControl, GrowthMonitor)
root.order.add_edge(GrowthMonitor, HarvestPrep)
root.order.add_edge(HarvestPrep, CommunityMeet)
root.order.add_edge(CommunityMeet, WasteManage)
root.order.add_edge(WasteManage, YieldReport)

print(root)