import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
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

# Define the choice of activities
xor1 = OperatorPOWL(operator=Operator.XOR, children=[Trend_Scan, skip])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[Idea_Harvest, skip])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[Workshop_Host, skip])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[Concept_Filter, skip])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[Prototype_Build, skip])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[Expert_Review, skip])
xor7 = OperatorPOWL(operator=Operator.XOR, children=[Feasibility_Check, skip])
xor8 = OperatorPOWL(operator=Operator.XOR, children=[Risk_Assess, skip])
xor9 = OperatorPOWL(operator=Operator.XOR, children=[Pilot_Launch, skip])
xor10 = OperatorPOWL(operator=Operator.XOR, children=[Data_Capture, skip])
xor11 = OperatorPOWL(operator=Operator.XOR, children=[Performance_Review, skip])
xor12 = OperatorPOWL(operator=Operator.XOR, children=[Scale_Plan, skip])
xor13 = OperatorPOWL(operator=Operator.XOR, children=[Resource_Align, skip])
xor14 = OperatorPOWL(operator=Operator.XOR, children=[Learn_Share, skip])
xor15 = OperatorPOWL(operator=Operator.XOR, children=[Culture_Embed, skip])

# Define the loop nodes
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[xor1, xor2])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[xor3, xor4])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[xor5, xor6])
loop4 = OperatorPOWL(operator=Operator.LOOP, children=[xor7, xor8])
loop5 = OperatorPOWL(operator=Operator.LOOP, children=[xor9, xor10])
loop6 = OperatorPOWL(operator=Operator.LOOP, children=[xor11, xor12])
loop7 = OperatorPOWL(operator=Operator.LOOP, children=[xor13, xor14])
loop8 = OperatorPOWL(operator=Operator.LOOP, children=[xor15, skip])

# Define the root of the POWL model
root = StrictPartialOrder(nodes=[loop1, loop2, loop3, loop4, loop5, loop6, loop7, loop8])
root.order.add_edge(loop1, xor2)
root.order.add_edge(loop2, xor3)
root.order.add_edge(loop3, xor4)
root.order.add_edge(loop4, xor5)
root.order.add_edge(loop5, xor6)
root.order.add_edge(loop6, xor7)
root.order.add_edge(loop7, xor8)
root.order.add_edge(loop8, xor15)