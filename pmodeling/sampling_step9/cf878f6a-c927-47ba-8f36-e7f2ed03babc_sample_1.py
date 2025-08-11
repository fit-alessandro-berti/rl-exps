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

# Define the loop for continuous monitoring and adjustment
monitorLoop = OperatorPOWL(operator=Operator.LOOP, children=[MonitorGrowth, AdjustClimate])

# Define the XOR for the two main paths: robotic harvest and manual harvest
harvestXor = OperatorPOWL(operator=Operator.XOR, children=[RoboticHarvest, skip])

# Define the XOR for the two main paths: pack and ship, or store
logisticsXor = OperatorPOWL(operator=Operator.XOR, children=[PackProduce, ManageLogistics])

# Define the XOR for the two main paths: market directly or through distributor
marketXor = OperatorPOWL(operator=Operator.XOR, children=[MarketProducts, skip])

# Define the loop for waste recycling
recycleLoop = OperatorPOWL(operator=Operator.LOOP, children=[RecycleWaste, skip])

# Define the XOR for the two main paths: audit and continue, or end
auditXor = OperatorPOWL(operator=Operator.XOR, children=[AuditSystems, skip])

# Create the root process
root = StrictPartialOrder(nodes=[SiteAssess, ZoningCheck, DesignFarm, ProcureGear, InstallSystems, SetupSensors, SelectCrops, PrepareSeeds, MixNutrients, monitorLoop, harvestXor, logisticsXor, marketXor, recycleLoop, auditXor])
root.order.add_edge(SiteAssess, ZoningCheck)
root.order.add_edge(ZoningCheck, DesignFarm)
root.order.add_edge(DesignFarm, ProcureGear)
root.order.add_edge(ProcureGear, InstallSystems)
root.order.add_edge(InstallSystems, SetupSensors)
root.order.add_edge(SetupSensors, SelectCrops)
root.order.add_edge(SelectCrops, PrepareSeeds)
root.order.add_edge(PrepareSeeds, MixNutrients)
root.order.add_edge(MixNutrients, monitorLoop)
root.order.add_edge(monitorLoop, harvestXor)
root.order.add_edge(harvestXor, logisticsXor)
root.order.add_edge(logisticsXor, marketXor)
root.order.add_edge(marketXor, recycleLoop)
root.order.add_edge(recycleLoop, auditXor)
root.order.add_edge(auditXor, SiteAssess)  # The loop will continue indefinitely, so we need to add an edge to break the cycle

print(root)