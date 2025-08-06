import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

SiteAssess = Transition(label='Site Assess')
StructureCheck = Transition(label='Structure Check')
SoilTest = Transition(label='Soil Test')
ClimateEval = Transition(label='Climate Eval')
PermitObtain = Transition(label='Permit Obtain')
DesignLayout = Transition(label='Design Layout')
SeedSourcing = Transition(label='Seed Sourcing')
IrrigationSet = Transition(label='Irrigation Set')
NutrientMix = Transition(label='Nutrient Mix')
PestControl = Transition(label='Pest Control')
SensorInstall = Transition(label='Sensor Install')
StaffTrain = Transition(label='Staff Train')
CropPlanting = Transition(label='Crop Planting')
YieldMonitor = Transition(label='Yield Monitor')
MarketSetup = Transition(label='Market Setup')
Maintenance = Transition(label='Maintenance')
WasteManage = Transition(label='Waste Manage')

skip = SilentTransition()

loop1 = OperatorPOWL(operator=Operator.LOOP, children=[SiteAssess, StructureCheck, SoilTest, ClimateEval, PermitObtain])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[DesignLayout, SeedSourcing, IrrigationSet, NutrientMix, PestControl])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[SensorInstall, StaffTrain, CropPlanting])
loop4 = OperatorPOWL(operator=Operator.LOOP, children=[YieldMonitor, MarketSetup, Maintenance])
loop5 = OperatorPOWL(operator=Operator.LOOP, children=[WasteManage])

xor1 = OperatorPOWL(operator=Operator.XOR, children=[loop1, skip])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[loop2, skip])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[loop3, skip])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[loop4, skip])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[loop5, skip])

root = StrictPartialOrder(nodes=[xor1, xor2, xor3, xor4, xor5])
root.order.add_edge(xor1, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, xor5)

print(root)