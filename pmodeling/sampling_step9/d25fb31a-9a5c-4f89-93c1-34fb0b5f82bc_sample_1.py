import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

Assess_Structure = Transition(label='Assess Structure')
Analyze_Environment = Transition(label='Analyze Environment')
Design_Modules = Transition(label='Design Modules')
Procure_Materials = Transition(label='Procure Materials')
Install_Irrigation = Transition(label='Install Irrigation')
Set_Sensors = Transition(label='Set Sensors')
Select_Seeds = Transition(label='Select Seeds')
Schedule_Planting = Transition(label='Schedule Planting')
Monitor_Growth = Transition(label='Monitor Growth')
Collect_Data = Transition(label='Collect Data')
Manage_Pests = Transition(label='Manage Pests')
Harvest_Crops = Transition(label='Harvest Crops')
Coordinate_Sales = Transition(label='Coordinate Sales')
Compost_Waste = Transition(label='Compost Waste')
Review_Feedback = Transition(label='Review Feedback')

skip = SilentTransition()

loop = OperatorPOWL(operator=Operator.LOOP, children=[Assess_Structure, Analyze_Environment])
xor = OperatorPOWL(operator=Operator.XOR, children=[Design_Modules, skip])
root = StrictPartialOrder(nodes=[loop, xor])
root.order.add_edge(loop, xor)

root.order.add_edge(xor, Procure_Materials)
root.order.add_edge(xor, Install_Irrigation)
root.order.add_edge(xor, Set_Sensors)
root.order.add_edge(xor, Select_Seeds)
root.order.add_edge(xor, Schedule_Planting)
root.order.add_edge(xor, Monitor_Growth)
root.order.add_edge(xor, Collect_Data)
root.order.add_edge(xor, Manage_Pests)
root.order.add_edge(xor, Harvest_Crops)
root.order.add_edge(xor, Coordinate_Sales)
root.order.add_edge(xor, Compost_Waste)
root.order.add_edge(xor, Review_Feedback)