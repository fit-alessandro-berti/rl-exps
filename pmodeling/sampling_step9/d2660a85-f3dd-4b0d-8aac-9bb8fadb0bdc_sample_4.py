import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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

skip = SilentTransition()
loop = OperatorPOWL(operator=Operator.LOOP, children=[SiteSurvey, DesignLayout, InstallModules, SetControls, SelectCrops, ConfigureIrrigation, SetupLighting, DeploySensors, TrainStaff, StartCultivation, MonitorGrowth, ManagePests, HarvestCrops, PackProduce, DistributeGoods])
root = StrictPartialOrder(nodes=[loop])
root.order.add_edge(loop, loop)