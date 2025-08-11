import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
Site_Survey = Transition(label='Site Survey')
Design_Modules = Transition(label='Design Modules')
Source_Materials = Transition(label='Source Materials')
Install_Framework = Transition(label='Install Framework')
Setup_Irrigation = Transition(label='Setup Irrigation')
Integrate_Sensors = Transition(label='Integrate Sensors')
Configure_AI = Transition(label='Configure AI')
Select_Crops = Transition(label='Select Crops')
Calibrate_Climate = Transition(label='Calibrate Climate')
Plant_Seed = Transition(label='Plant Seeds')
Monitor_Growth = Transition(label='Monitor Growth')
Manage_Pests = Transition(label='Manage Pests')
Recycle_Waste = Transition(label='Recycle Waste')
Engage_Community = Transition(label='Engage Community')
Ensure_Compliance = Transition(label='Ensure Compliance')
Distribute_Produce = Transition(label='Distribute Produce')

skip = SilentTransition()
loop = OperatorPOWL(operator=Operator.LOOP, children=[Site_Survey, Design_Modules])
xor = OperatorPOWL(operator=Operator.XOR, children=[Source_Materials, skip])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[Install_Framework, xor])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[Setup_Irrigation, xor2])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[Integrate_Sensors, xor3])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[Configure_AI, xor4])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[Select_Crops, xor5])
xor7 = OperatorPOWL(operator=Operator.XOR, children=[Calibrate_Climate, xor6])
xor8 = OperatorPOWL(operator=Operator.XOR, children=[Plant_Seed, xor7])
xor9 = OperatorPOWL(operator=Operator.XOR, children=[Monitor_Growth, xor8])
xor10 = OperatorPOWL(operator=Operator.XOR, children=[Manage_Pests, xor9])
xor11 = OperatorPOWL(operator=Operator.XOR, children=[Recycle_Waste, xor10])
xor12 = OperatorPOWL(operator=Operator.XOR, children=[Engage_Community, xor11])
xor13 = OperatorPOWL(operator=Operator.XOR, children=[Ensure_Compliance, xor12])
xor14 = OperatorPOWL(operator=Operator.XOR, children=[Distribute_Produce, xor13])

root = StrictPartialOrder(nodes=[loop, xor14])
root.order.add_edge(loop, xor14)

# Print the root of the POWL model
print(root)