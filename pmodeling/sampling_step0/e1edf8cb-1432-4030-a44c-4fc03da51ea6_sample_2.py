import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

SiteSurvey = Transition(label='Site Survey')
StructuralCheck = Transition(label='Structural Check')
EnvControl = Transition(label='Env Control')
HydroSetup = Transition(label='Hydro Setup')
CropSelect = Transition(label='Crop Select')
IoTInstall = Transition(label='IoT Install')
SensorCalibrate = Transition(label='Sensor Calibrate')
WaterCycle = Transition(label='Water Cycle')
NutrientMix = Transition(label='Nutrient Mix')
LightingAdjust = Transition(label='Lighting Adjust')
StaffTrain = Transition(label='Staff Train')
WasteManage = Transition(label='Waste Manage')
EnergyAudit = Transition(label='Energy Audit')
HarvestPlan = Transition(label='Harvest Plan')
DeliverySetup = Transition(label='Delivery Setup')
MarketAlign = Transition(label='Market Align')

loop1 = OperatorPOWL(operator=Operator.LOOP, children=[SiteSurvey, StructuralCheck])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[EnvControl, HydroSetup])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[CropSelect, IoTInstall])
loop4 = OperatorPOWL(operator=Operator.LOOP, children=[SensorCalibrate, WaterCycle])
loop5 = OperatorPOWL(operator=Operator.LOOP, children=[NutrientMix, LightingAdjust])
loop6 = OperatorPOWL(operator=Operator.LOOP, children=[StaffTrain, WasteManage])
loop7 = OperatorPOWL(operator=Operator.LOOP, children=[EnergyAudit, HarvestPlan])
loop8 = OperatorPOWL(operator=Operator.LOOP, children=[DeliverySetup, MarketAlign])

xor1 = OperatorPOWL(operator=Operator.XOR, children=[loop1, loop2])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[loop3, loop4])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[loop5, loop6])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[loop7, loop8])

root = StrictPartialOrder(nodes=[xor1, xor2, xor3, xor4])
root.order.add_edge(xor1, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)