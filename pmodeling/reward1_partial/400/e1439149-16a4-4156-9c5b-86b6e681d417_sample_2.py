import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
Trend_Scan = Transition(label='Trend Scan')
Idea_Harvest = Transition(label='Idea Harvest')
Workshop_Host = Transition(label='Workshop Host')
Concept_Filter = Transition(label='Concept Filter')
Prototype_Build = Transition(label='Prototype Build')
Expert_Review = Transition(label='Expert Review')
Feasibility_Check = Transition(label='Feasibility Check')
Risk_Assess = Transition(label='Risk Assess')
Pilot_Launch = Transition(label='Pilot Launch')
Data_Capture = Transition(label='Data Capture')
Performance_Review = Transition(label='Performance Review')
Scale_Plan = Transition(label='Scale Plan')
Resource_Align = Transition(label='Resource Align')
Learn_Share = Transition(label='Learn Share')
Culture_Embed = Transition(label='Culture Embed')

# Define silent transitions (tau labels)
skip = SilentTransition()

# Define the POWL model
loop = OperatorPOWL(operator=Operator.LOOP, children=[Trend_Scan, Idea_Harvest, Workshop_Host])
xor = OperatorPOWL(operator=Operator.XOR, children=[Concept_Filter, Prototype_Build])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[Expert_Review, Feasibility_Check])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[Risk_Assess, Pilot_Launch])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[Data_Capture, Performance_Review])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[Scale_Plan, Resource_Align])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[Learn_Share, Culture_Embed])

# Construct the root of the POWL model
root = StrictPartialOrder(nodes=[loop, xor, xor2, xor3, xor4, xor5, xor6])
root.order.add_edge(loop, xor)
root.order.add_edge(xor, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, xor5)
root.order.add_edge(xor5, xor6)