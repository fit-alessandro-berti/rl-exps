import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
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

# Define the partial order
root = StrictPartialOrder(nodes=[
    SiteSurvey,
    StructureAssess,
    SystemDesign,
    CropSelect,
    PermitObtain,
    EnviroSetup,
    IrrigationPlan,
    SensorInstall,
    AICalibration,
    StaffTrain,
    NutrientMix,
    PestMonitor,
    YieldAnalyze,
    MarketAlign,
    LaunchFarm
])

# Define the order
root.order.add_edge(SiteSurvey, StructureAssess)
root.order.add_edge(StructureAssess, SystemDesign)
root.order.add_edge(SystemDesign, CropSelect)
root.order.add_edge(CropSelect, PermitObtain)
root.order.add_edge(PermitObtain, EnviroSetup)
root.order.add_edge(EnviroSetup, IrrigationPlan)
root.order.add_edge(IrrigationPlan, SensorInstall)
root.order.add_edge(SensorInstall, AICalibration)
root.order.add_edge(AICalibration, StaffTrain)
root.order.add_edge(StaffTrain, NutrientMix)
root.order.add_edge(NutrientMix, PestMonitor)
root.order.add_edge(PestMonitor, YieldAnalyze)
root.order.add_edge(YieldAnalyze, MarketAlign)
root.order.add_edge(MarketAlign, LaunchFarm)

print(root)