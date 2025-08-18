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

root = StrictPartialOrder(nodes=[
    SiteAssess,
    ZoningCheck,
    DesignFarm,
    ProcureGear,
    InstallSystems,
    SetupSensors,
    SelectCrops,
    PrepareSeeds,
    MixNutrients,
    MonitorGrowth,
    AdjustClimate,
    RoboticHarvest,
    GradeQuality,
    PackProduce,
    ManageLogistics,
    MarketProducts,
    RecycleWaste,
    AuditSystems
])

root.order.add_edge(SiteAssess, ZoningCheck)
root.order.add_edge(ZoningCheck, DesignFarm)
root.order.add_edge(DesignFarm, ProcureGear)
root.order.add_edge(ProcureGear, InstallSystems)
root.order.add_edge(InstallSystems, SetupSensors)
root.order.add_edge(SetupSensors, SelectCrops)
root.order.add_edge(SelectCrops, PrepareSeeds)
root.order.add_edge(PrepareSeeds, MixNutrients)
root.order.add_edge(MixNutrients, MonitorGrowth)
root.order.add_edge(MonitorGrowth, AdjustClimate)
root.order.add_edge(AdjustClimate, RoboticHarvest)
root.order.add_edge(RoboticHarvest, GradeQuality)
root.order.add_edge(GradeQuality, PackProduce)
root.order.add_edge(PackProduce, ManageLogistics)
root.order.add_edge(ManageLogistics, MarketProducts)
root.order.add_edge(MarketProducts, RecycleWaste)
root.order.add_edge(RecycleWaste, AuditSystems)