import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

SiteSurvey = Transition(label='Site Survey')
PermitFiling = Transition(label='Permit Filing')
StructurePrep = Transition(label='Structure Prep')
SystemInstall = Transition(label='System Install')
NutrientMix = Transition(label='Nutrient Mix')
SensorSetup = Transition(label='Sensor Setup')
AIcalibration = Transition(label='AI Calibration')
SeedSourcing = Transition(label='Seed Sourcing')
StaffTraining = Transition(label='Staff Training')
EnergyConnect = Transition(label='Energy Connect')
WaterCycle = Transition(label='Water Cycle')
GrowthMonitor = Transition(label='Growth Monitor')
WasteAudit = Transition(label='Waste Audit')
CommunityMeet = Transition(label='Community Meet')
DataReview = Transition(label='Data Review')
YieldForecast = Transition(label='Yield Forecast')

skip = SilentTransition()

# Establishing Vertical Farming Facility
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[SiteSurvey, PermitFiling, StructurePrep, SystemInstall])
xor1 = OperatorPOWL(operator=Operator.XOR, children=[NutrientMix, skip])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[SensorSetup, AIcalibration])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[SeedSourcing, StaffTraining])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[EnergyConnect, skip])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[WaterCycle, skip])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[GrowthMonitor, skip])
xor7 = OperatorPOWL(operator=Operator.XOR, children=[WasteAudit, skip])
xor8 = OperatorPOWL(operator=Operator.XOR, children=[CommunityMeet, skip])
xor9 = OperatorPOWL(operator=Operator.XOR, children=[DataReview, YieldForecast])

root = StrictPartialOrder(nodes=[loop1, xor1, xor2, xor3, xor4, xor5, xor6, xor7, xor8, xor9])
root.order.add_edge(loop1, xor1)
root.order.add_edge(loop1, xor2)
root.order.add_edge(loop1, xor3)
root.order.add_edge(loop1, xor4)
root.order.add_edge(loop1, xor5)
root.order.add_edge(loop1, xor6)
root.order.add_edge(loop1, xor7)
root.order.add_edge(loop1, xor8)
root.order.add_edge(loop1, xor9)

print(root)