import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

SiteSurvey = Transition(label='Site Survey')
ZoningCheck = Transition(label='Zoning Check')
DesignLayout = Transition(label='Design Layout')
SystemOrder = Transition(label='System Order')
StructureBuild = Transition(label='Structure Build')
InstallHydroponics = Transition(label='Install Hydroponics')
CalibrateSensors = Transition(label='Calibrate Sensors')
SelectCrops = Transition(label='Select Crops')
PlantSeeding = Transition(label='Plant Seeding')
MonitorGrowth = Transition(label='Monitor Growth')
ManagePests = Transition(label='Manage Pests')
ScheduleHarvest = Transition(label='Schedule Harvest')
PackageProduce = Transition(label='Package Produce')
LocalDelivery = Transition(label='Local Delivery')
AnalyzeData = Transition(label='Analyze Data')

skip = SilentTransition()

loop1 = OperatorPOWL(operator=Operator.LOOP, children=[SiteSurvey, ZoningCheck])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[DesignLayout, SystemOrder, StructureBuild])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[InstallHydroponics, CalibrateSensors, SelectCrops, PlantSeeding, MonitorGrowth, ManagePests])
loop4 = OperatorPOWL(operator=Operator.LOOP, children=[ScheduleHarvest, PackageProduce, LocalDelivery])
xor = OperatorPOWL(operator=Operator.XOR, children=[AnalyzeData, skip])

root = StrictPartialOrder(nodes=[loop1, loop2, loop3, loop4, xor])
root.order.add_edge(loop1, loop2)
root.order.add_edge(loop2, loop3)
root.order.add_edge(loop3, loop4)
root.order.add_edge(loop4, xor)