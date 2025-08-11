import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities)
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

# Define the silent transitions
skip = SilentTransition()

# Define the loop node for site survey and design layout
loop = OperatorPOWL(operator=Operator.LOOP, children=[SiteSurvey, DesignLayout])

# Define the exclusive choice node for modules and controls
xor = OperatorPOWL(operator=Operator.XOR, children=[InstallModules, SetControls])

# Define the exclusive choice node for irrigation and lighting
xor2 = OperatorPOWL(operator=Operator.XOR, children=[ConfigureIrrigation, SetupLighting])

# Define the exclusive choice node for sensors and staff training
xor3 = OperatorPOWL(operator=Operator.XOR, children=[DeploySensors, TrainStaff])

# Define the exclusive choice node for cultivation and monitoring
xor4 = OperatorPOWL(operator=Operator.XOR, children=[StartCultivation, MonitorGrowth])

# Define the exclusive choice node for pest management and harvest
xor5 = OperatorPOWL(operator=Operator.XOR, children=[ManagePests, HarvestCrops])

# Define the exclusive choice node for packing and distribution
xor6 = OperatorPOWL(operator=Operator.XOR, children=[PackProduce, DistributeGoods])

# Define the root of the POWL model
root = StrictPartialOrder(nodes=[loop, xor, xor2, xor3, xor4, xor5, xor6])

# Add edges to the root
root.order.add_edge(loop, xor)
root.order.add_edge(xor, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, xor5)
root.order.add_edge(xor5, xor6)

# Print the root
print(root)