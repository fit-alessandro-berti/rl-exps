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

# Define the loop for automated processes
Automation_Loop = OperatorPOWL(operator=Operator.LOOP, children=[
    Integrate_Sensors,
    Configure_AI,
    Calibrate_Climate,
    Plant_Seed,
    Monitor_Growth,
    Manage_Pests,
    Recycle_Waste,
    Ensure_Compliance
])

# Define the XOR for community engagement and distribution
Community_Distribution_XOR = OperatorPOWL(operator=Operator.XOR, children=[
    Engage_Community,
    Distribute_Produce
])

# Define the root partial order
root = StrictPartialOrder(nodes=[Site_Survey, Design_Modules, Source_Materials, Install_Framework, Automation_Loop, Community_Distribution_XOR])
root.order.add_edge(Site_Survey, Design_Modules)
root.order.add_edge(Design_Modules, Source_Materials)
root.order.add_edge(Source_Materials, Install_Framework)
root.order.add_edge(Install_Framework, Automation_Loop)
root.order.add_edge(Automation_Loop, Community_Distribution_XOR)

print(root)