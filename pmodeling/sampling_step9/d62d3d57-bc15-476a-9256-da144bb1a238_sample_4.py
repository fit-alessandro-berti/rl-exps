import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

SiteSurvey = Transition(label='Site Survey')
StructureAssess = Transition(label='Structure Assess')
SystemDesign = Transition(label='System Design')
CropSelect = Transition(label='Crop Select')
PermitObtain = Transition(label='Permit Obtain')
EnviroSetup = Transition(label='Enviro Setup')
IrrigationPlan = Transition(label='Irrigation Plan')
SensorInstall = Transition(label='Sensor Install')
AICalibration = Transition(label='AI Calibration')
StaffTrain = Transition(label='Staff Train')
NutrientMix = Transition(label='Nutrient Mix')
PestMonitor = Transition(label='Pest Monitor')
YieldAnalyze = Transition(label='Yield Analyze')
MarketAlign = Transition(label='Market Align')
LaunchFarm = Transition(label='Launch Farm')

skip = SilentTransition()
loop = OperatorPOWL(operator=Operator.LOOP, children=[SiteSurvey, StructureAssess, SystemDesign, CropSelect, PermitObtain, EnviroSetup, IrrigationPlan, SensorInstall, AICalibration, StaffTrain, NutrientMix, PestMonitor, YieldAnalyze, MarketAlign, LaunchFarm])
xor = OperatorPOWL(operator=Operator.XOR, children=[skip, loop])

root = StrictPartialOrder(nodes=[xor])
root.order.add_edge(loop, xor)