import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

SiteSelect = Transition(label='Site Select')
EnvAssess = Transition(label='Env Assess')
DesignModules = Transition(label='Design Modules')
HydroponicsSetup = Transition(label='Hydroponics Setup')
SoftwareDev = Transition(label='Software Dev')
SeedChoose = Transition(label='Seed Choose')
LEDInstall = Transition(label='LED Install')
TrainStaff = Transition(label='Train Staff')
ComplianceCheck = Transition(label='Compliance Check')
EngageCommunity = Transition(label='Engage Community')
PlantCrops = Transition(label='Plant Crops')
MonitorGrowth = Transition(label='Monitor Growth')
OptimizeYields = Transition(label='Optimize Yields')
WasteManage = Transition(label='Waste Manage')
EnergyAudit = Transition(label='Energy Audit')
WaterRecycle = Transition(label='Water Recycle')

skip = SilentTransition()

loop1 = OperatorPOWL(operator=Operator.LOOP, children=[SiteSelect, EnvAssess, DesignModules, HydroponicsSetup])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[SoftwareDev, SeedChoose, LEDInstall, TrainStaff])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[ComplianceCheck, EngageCommunity, PlantCrops, MonitorGrowth])
loop4 = OperatorPOWL(operator=Operator.LOOP, children=[OptimizeYields, WasteManage, EnergyAudit, WaterRecycle])

xor1 = OperatorPOWL(operator=Operator.XOR, children=[loop1, skip])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[loop2, skip])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[loop3, skip])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[loop4, skip])

root = StrictPartialOrder(nodes=[xor1, xor2, xor3, xor4])
root.order.add_edge(xor1, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)

print(root)