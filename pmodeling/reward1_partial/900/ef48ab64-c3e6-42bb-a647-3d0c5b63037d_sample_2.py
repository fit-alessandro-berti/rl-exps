import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for each activity
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

# Define the loop for the optimization cycle
loop = OperatorPOWL(operator=Operator.LOOP, children=[OptimizeYields, WasteManage, EnergyAudit, WaterRecycle])

# Define the partial order with all activities and the loop
root = StrictPartialOrder(nodes=[SiteSelect, EnvAssess, DesignModules, HydroponicsSetup, SoftwareDev, SeedChoose, LEDInstall, TrainStaff, ComplianceCheck, EngageCommunity, PlantCrops, MonitorGrowth, loop])

# Define the dependencies between activities
root.order.add_edge(SiteSelect, EnvAssess)
root.order.add_edge(EnvAssess, DesignModules)
root.order.add_edge(DesignModules, HydroponicsSetup)
root.order.add_edge(HydroponicsSetup, SoftwareDev)
root.order.add_edge(SoftwareDev, SeedChoose)
root.order.add_edge(SeedChoose, LEDInstall)
root.order.add_edge(LEDInstall, TrainStaff)
root.order.add_edge(TrainStaff, ComplianceCheck)
root.order.add_edge(ComplianceCheck, EngageCommunity)
root.order.add_edge(EngageCommunity, PlantCrops)
root.order.add_edge(PlantCrops, MonitorGrowth)
root.order.add_edge(MonitorGrowth, loop)