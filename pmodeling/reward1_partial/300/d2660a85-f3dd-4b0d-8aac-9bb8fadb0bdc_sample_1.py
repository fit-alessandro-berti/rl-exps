import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities as transitions with their labels
SiteSurvey = Transition(label='Site Survey')
DesignLayout = Transition(label='Design Layout')
InstallModules = Transition(label='Install Modules')
SetControls = Transition(label='Set Controls')
SelectCrops = Transition(label='Select Crops')
ConfigureIrrigation = Transition(label='Configure Irrigation')
SetupLighting = Transition(label='Setup Lighting')
DeploySensors = Transition(label='Deploy Sensors')
TrainStaff = Transition(label='Train Staff')
StartCultivation = Transition(label='Start Cultivation')
MonitorGrowth = Transition(label='Monitor Growth')
ManagePests = Transition(label='Manage Pests')
HarvestCrops = Transition(label='Harvest Crops')
PackProduce = Transition(label='Pack Produce')
DistributeGoods = Transition(label='Distribute Goods')

# Define silent transitions for loop
skip = SilentTransition()

# Define partial order structure
root = StrictPartialOrder(nodes=[
    SiteSurvey,
    DesignLayout,
    InstallModules,
    SetControls,
    SelectCrops,
    ConfigureIrrigation,
    SetupLighting,
    DeploySensors,
    TrainStaff,
    StartCultivation,
    MonitorGrowth,
    ManagePests,
    HarvestCrops,
    PackProduce,
    DistributeGoods
])

# Define dependencies (partial order)
root.order.add_edge(SiteSurvey, DesignLayout)
root.order.add_edge(DesignLayout, InstallModules)
root.order.add_edge(InstallModules, SetControls)
root.order.add_edge(SetControls, SelectCrops)
root.order.add_edge(SelectCrops, ConfigureIrrigation)
root.order.add_edge(ConfigureIrrigation, SetupLighting)
root.order.add_edge(SetupLighting, DeploySensors)
root.order.add_edge(DeploySensors, TrainStaff)
root.order.add_edge(TrainStaff, StartCultivation)
root.order.add_edge(StartCultivation, MonitorGrowth)
root.order.add_edge(MonitorGrowth, ManagePests)
root.order.add_edge(ManagePests, HarvestCrops)
root.order.add_edge(HarvestCrops, PackProduce)
root.order.add_edge(PackProduce, DistributeGoods)

print(root)