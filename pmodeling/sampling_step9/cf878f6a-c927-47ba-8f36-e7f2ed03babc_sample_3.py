import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

SiteAssess = Transition(label='Site Assess')
ZoningCheck = Transition(label='Zoning Check')
DesignFarm = Transition(label='Design Farm')
ProcureGear = Transition(label='Procure Gear')
InstallSystems = Transition(label='Install Systems')
SetupSensors = Transition(label='Setup Sensors')
SelectCrops = Transition(label='Select Crops')
PrepareSeeds = Transition(label='Prepare Seeds')
MixNutrients = Transition(label='Mix Nutrients')
MonitorGrowth = Transition(label='Monitor Growth')
AdjustClimate = Transition(label='Adjust Climate')
RoboticHarvest = Transition(label='Robotic Harvest')
GradeQuality = Transition(label='Grade Quality')
PackProduce = Transition(label='Pack Produce')
ManageLogistics = Transition(label='Manage Logistics')
MarketProducts = Transition(label='Market Products')
RecycleWaste = Transition(label='Recycle Waste')
AuditSystems = Transition(label='Audit Systems')

skip = SilentTransition()
loop = OperatorPOWL(operator=Operator.LOOP, children=[SiteAssess, ZoningCheck, DesignFarm, ProcureGear, InstallSystems, SetupSensors, SelectCrops, PrepareSeeds, MixNutrients, MonitorGrowth, AdjustClimate, RoboticHarvest, GradeQuality, PackProduce, ManageLogistics, MarketProducts, RecycleWaste, AuditSystems])
xor = OperatorPOWL(operator=Operator.XOR, children=[skip])

root = StrictPartialOrder(nodes=[loop, xor])
root.order.add_edge(loop, xor)