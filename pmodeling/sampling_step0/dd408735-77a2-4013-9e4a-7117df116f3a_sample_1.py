import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator
# Define the activities
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

# Define the partial order
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[SiteAssess, StructureCheck, SoilTest, ClimateEval, PermitObtain])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[DesignLayout, SeedSourcing, IrrigationSet, NutrientMix, PestControl])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[SensorInstall, StaffTrain])
loop4 = OperatorPOWL(operator=Operator.LOOP, children=[CropPlanting, YieldMonitor, MarketSetup])
loop5 = OperatorPOWL(operator=Operator.LOOP, children=[Maintenance, WasteManage])

xor = OperatorPOWL(operator=Operator.XOR, children=[loop1, loop2, loop3, loop4, loop5])
root = StrictPartialOrder(nodes=[xor])
root.order.add_edge(loop1, xor)
root.order.add_edge(loop2, xor)
root.order.add_edge(loop3, xor)
root.order.add_edge(loop4, xor)
root.order.add_edge(loop5, xor)