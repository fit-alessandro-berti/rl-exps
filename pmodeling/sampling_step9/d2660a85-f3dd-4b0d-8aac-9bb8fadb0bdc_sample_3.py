import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
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

# Define silent transitions for empty labels
skip = SilentTransition()

# Define exclusive choice (XOR) for staff training and cultivation
xor = OperatorPOWL(operator=Operator.XOR, children=[TrainStaff, StartCultivation])

# Define loop for pest management
loop = OperatorPOWL(operator=Operator.LOOP, children=[ManagePests, skip])

# Define the root POWL model
root = StrictPartialOrder(nodes=[SiteSurvey, DesignLayout, InstallModules, SetControls, SelectCrops, ConfigureIrrigation, SetupLighting, DeploySensors, xor, loop, HarvestCrops, PackProduce, DistributeGoods])

# Define dependencies between transitions
root.order.add_edge(SiteSurvey, DesignLayout)
root.order.add_edge(DesignLayout, InstallModules)
root.order.add_edge(InstallModules, SetControls)
root.order.add_edge(SetControls, SelectCrops)
root.order.add_edge(SelectCrops, ConfigureIrrigation)
root.order.add_edge(ConfigureIrrigation, SetupLighting)
root.order.add_edge(SetupLighting, DeploySensors)
root.order.add_edge(DeploySensors, xor)
root.order.add_edge(xor, loop)
root.order.add_edge(loop, ManagePests)
root.order.add_edge(ManagePests, loop)
root.order.add_edge(ManagePests, skip)
root.order.add_edge(skip, ManagePests)
root.order.add_edge(ManagePests, loop)
root.order.add_edge(HarvestCrops, PackProduce)
root.order.add_edge(PackProduce, DistributeGoods)