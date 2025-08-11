import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

SiteSurvey = Transition(label='Site Survey')
DesignLayout = Transition(label='Design Layout')
StructureBuild = Transition(label='Structure Build')
SystemInstall = Transition(label='System Install')
ClimateSetup = Transition(label='Climate Setup')
NutrientPrep = Transition(label='Nutrient Prep')
SeedGerminate = Transition(label='Seed Germinate')
PlantingPhase = Transition(label='Planting Phase')
SensorDeploy = Transition(label='Sensor Deploy')
PestControl = Transition(label='Pest Control')
WaterMonitor = Transition(label='Water Monitor')
DataAnalyze = Transition(label='Data Analyze')
StaffTrain = Transition(label='Staff Train')
YieldForecast = Transition(label='Yield Forecast')
CommunityMeet = Transition(label='Community Meet')
skip = SilentTransition()
loop = OperatorPOWL(operator=Operator.LOOP, children=[SiteSurvey, DesignLayout, StructureBuild, SystemInstall, ClimateSetup, NutrientPrep, SeedGerminate, PlantingPhase, SensorDeploy, PestControl, WaterMonitor, DataAnalyze, StaffTrain, YieldForecast, CommunityMeet])
xor = OperatorPOWL(operator=Operator.XOR, children=[skip])
root = StrictPartialOrder(nodes=[loop, xor])
root.order.add_edge(loop, xor)