import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
SiteSurvey = Transition(label='Site Survey')
StructureAssess = Transition(label='Structure Assess')
SystemDesign = Transition(label='System Design')
CropSelect = Transition(label='Crop Select')
PermitObtain = Transition(label='Permit Obtain')
EnviroSetup = Transition(label='Enviro Setup')
IrrigationPlan = Transition(label='Irrigation Plan')
SensorInstall = Transition(label='Sensor Install')
AI_Calibration = Transition(label='AI Calibration')
StaffTrain = Transition(label='Staff Train')
NutrientMix = Transition(label='Nutrient Mix')
PestMonitor = Transition(label='Pest Monitor')
YieldAnalyze = Transition(label='Yield Analyze')
MarketAlign = Transition(label='Market Align')
LaunchFarm = Transition(label='Launch Farm')

# Define silent transitions
skip = SilentTransition()

# Define loop for nutrient mix and pest monitor
loop_nutrient = OperatorPOWL(operator=Operator.LOOP, children=[NutrientMix, PestMonitor])
loop_nutrient.order.add_edge(NutrientMix, PestMonitor)

# Define XOR for staff train and nutrient mix
xor_staff = OperatorPOWL(operator=Operator.XOR, children=[StaffTrain, skip])
xor_staff.order.add_edge(StaffTrain, skip)

# Define XOR for yield analyze and market align
xor_yield = OperatorPOWL(operator=Operator.XOR, children=[YieldAnalyze, MarketAlign])
xor_yield.order.add_edge(YieldAnalyze, MarketAlign)

# Define root POWL model
root = StrictPartialOrder(nodes=[SiteSurvey, StructureAssess, SystemDesign, CropSelect, PermitObtain, EnviroSetup, IrrigationPlan, SensorInstall, AI_Calibration, xor_staff, loop_nutrient, xor_yield, LaunchFarm])
root.order.add_edge(SiteSurvey, StructureAssess)
root.order.add_edge(StructureAssess, SystemDesign)
root.order.add_edge(SystemDesign, CropSelect)
root.order.add_edge(CropSelect, PermitObtain)
root.order.add_edge(PermitObtain, EnviroSetup)
root.order.add_edge(EnviroSetup, IrrigationPlan)
root.order.add_edge(IrrigationPlan, SensorInstall)
root.order.add_edge(SensorInstall, AI_Calibration)
root.order.add_edge(AI_Calibration, xor_staff)
root.order.add_edge(xor_staff, loop_nutrient)
root.order.add_edge(loop_nutrient, xor_yield)
root.order.add_edge(xor_yield, LaunchFarm)

print(root)