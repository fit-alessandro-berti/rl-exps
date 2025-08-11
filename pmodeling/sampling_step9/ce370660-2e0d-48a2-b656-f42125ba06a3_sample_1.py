import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

StructuralCheck = Transition(label='Structural Check')
PermitApply = Transition(label='Permit Apply')
DesignLayout = Transition(label='Design Layout')
SoilPrep = Transition(label='Soil Prep')
BedInstall = Transition(label='Bed Install')
IrrigationSetup = Transition(label='Irrigation Setup')
SensorMount = Transition(label='Sensor Mount')
SolarConnect = Transition(label='Solar Connect')
SeedOrder = Transition(label='Seed Order')
NutrientMix = Transition(label='Nutrient Mix')
CommunityMeet = Transition(label='Community Meet')
StaffTrain = Transition(label='Staff Train')
PlantCrop = Transition(label='Plant Crop')
MaintenancePlan = Transition(label='Maintenance Plan')
HarvestSchedule = Transition(label='Harvest Schedule')
WasteManage = Transition(label='Waste Manage')

skip = SilentTransition()

# Structural Check
# Permit Apply
# Design Layout
# Soil Prep
# Bed Install
# Irrigation Setup
# Sensor Mount
# Solar Connect
# Seed Order
# Nutrient Mix
# Community Meet
# Staff Train
# Plant Crop
# Maintenance Plan
# Harvest Schedule
# Waste Manage

loop1 = OperatorPOWL(operator=Operator.LOOP, children=[StructuralCheck, PermitApply])
xor1 = OperatorPOWL(operator=Operator.XOR, children=[DesignLayout, skip])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[SoilPrep, xor1])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[BedInstall, xor2])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[IrrigationSetup, xor3])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[SensorMount, xor4])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[SolarConnect, xor5])
xor7 = OperatorPOWL(operator=Operator.XOR, children=[SeedOrder, xor6])
xor8 = OperatorPOWL(operator=Operator.XOR, children=[NutrientMix, xor7])
xor9 = OperatorPOWL(operator=Operator.XOR, children=[CommunityMeet, xor8])
xor10 = OperatorPOWL(operator=Operator.XOR, children=[StaffTrain, xor9])
xor11 = OperatorPOWL(operator=Operator.XOR, children=[PlantCrop, xor10])
xor12 = OperatorPOWL(operator=Operator.XOR, children=[MaintenancePlan, xor11])
xor13 = OperatorPOWL(operator=Operator.XOR, children=[HarvestSchedule, xor12])
xor14 = OperatorPOWL(operator=Operator.XOR, children=[WasteManage, xor13])

root = StrictPartialOrder(nodes=[loop1, xor14])
root.order.add_edge(loop1, xor14)