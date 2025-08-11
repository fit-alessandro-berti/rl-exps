import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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

skip = SilentTransition()
loop = OperatorPOWL(operator=Operator.LOOP, children=[SiteSurvey, LoadTest, SoilSample, WaterCheck, DesignPlan, BedSetup, IrrigationInstall, ClimateSetup, SeedSelection, PlantingPhase, PestControl, GrowthMonitor, HarvestPrep, CommunityMeet, WasteManage, YieldReport])
xor = OperatorPOWL(operator=Operator.XOR, children=[skip, skip])
root = StrictPartialOrder(nodes=[loop, xor])
root.order.add_edge(loop, xor)