import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions (activities)
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

# Define silent transitions
skip = SilentTransition()

# Define loop nodes and exclusive choice nodes
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[Prototype_Build, Expert_Review])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[Feasibility_Check, Risk_Assess])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[Pilot_Launch, Data_Capture])
loop4 = OperatorPOWL(operator=Operator.LOOP, children=[Performance_Review, Scale_Plan])
loop5 = OperatorPOWL(operator=Operator.LOOP, children=[Resource_Align, Learn_Share])
loop6 = OperatorPOWL(operator=Operator.LOOP, children=[Culture_Embed])

xor1 = OperatorPOWL(operator=Operator.XOR, children=[Idea_Harvest, skip])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[Workshop_Host, skip])

# Create the root model
root = StrictPartialOrder(nodes=[Trend_Scan, xor1, xor2, loop1, loop2, loop3, loop4, loop5, loop6])
root.order.add_edge(Trend_Scan, xor1)
root.order.add_edge(Trend_Scan, xor2)
root.order.add_edge(xor1, loop1)
root.order.add_edge(xor2, loop2)
root.order.add_edge(loop1, loop3)
root.order.add_edge(loop2, loop4)
root.order.add_edge(loop3, loop5)
root.order.add_edge(loop4, loop6)
root.order.add_edge(loop5, Culture_Embed)