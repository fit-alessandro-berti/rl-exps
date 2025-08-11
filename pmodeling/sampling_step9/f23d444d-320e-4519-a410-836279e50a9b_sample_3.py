import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

SiteSurvey = Transition(label='Site Survey')
SystemDesign = Transition(label='System Design')
ModuleBuild = Transition(label='Module Build')
NutrientMix = Transition(label='Nutrient Mix')
SeedSelection = Transition(label='Seed Selection')
PlantingPlan = Transition(label='Planting Plan')
IrrigationSetup = Transition(label='Irrigation Setup')
ClimateControl = Transition(label='Climate Control')
LightingAdjust = Transition(label='Lighting Adjust')
PestMonitor = Transition(label='Pest Monitor')
WasteCycle = Transition(label='Waste Cycle')
DataCapture = Transition(label='Data Capture')
YieldForecast = Transition(label='Yield Forecast')
RegulationCheck = Transition(label='Regulation Check')
CommunityMeet = Transition(label='Community Meet')
HarvestPrep = Transition(label='Harvest Prep')
MarketLink = Transition(label='Market Link')

skip = SilentTransition()
loop = OperatorPOWL(operator=Operator.LOOP, children=[SiteSurvey, SystemDesign, ModuleBuild, NutrientMix, SeedSelection, PlantingPlan, IrrigationSetup, ClimateControl, LightingAdjust, PestMonitor, WasteCycle, DataCapture, YieldForecast, RegulationCheck, CommunityMeet, HarvestPrep, MarketLink])
root = StrictPartialOrder(nodes=[loop])
root.order.add_edge(loop, loop)