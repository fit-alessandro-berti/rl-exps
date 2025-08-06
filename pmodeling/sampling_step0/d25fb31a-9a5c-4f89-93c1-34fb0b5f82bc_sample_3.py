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

xor1 = OperatorPOWL(operator=Operator.XOR, children=[Analyze_Environment, Procure_Materials])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[Design_Modules, Procure_Materials])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[Install_Irrigation, Procure_Materials])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[Set_Sensors, Procure_Materials])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[Select_Seeds, Procure_Materials])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[Schedule_Planting, Procure_Materials])
xor7 = OperatorPOWL(operator=Operator.XOR, children=[Monitor_Growth, Procure_Materials])
xor8 = OperatorPOWL(operator=Operator.XOR, children=[Collect_Data, Procure_Materials])
xor9 = OperatorPOWL(operator=Operator.XOR, children=[Manage_Pests, Procure_Materials])
xor10 = OperatorPOWL(operator=Operator.XOR, children=[Harvest_Crops, Procure_Materials])
xor11 = OperatorPOWL(operator=Operator.XOR, children=[Coordinate_Sales, Procure_Materials])
xor12 = OperatorPOWL(operator=Operator.XOR, children=[Compost_Waste, Procure_Materials])
xor13 = OperatorPOWL(operator=Operator.XOR, children=[Review_Feedback, Procure_Materials])

loop1 = OperatorPOWL(operator=Operator.LOOP, children=[xor1, xor2, xor3, xor4, xor5, xor6, xor7, xor8, xor9, xor10, xor11, xor12, xor13])

root = StrictPartialOrder(nodes=[Assess_Structure, loop1])
root.order.add_edge(Assess_Structure, loop1)