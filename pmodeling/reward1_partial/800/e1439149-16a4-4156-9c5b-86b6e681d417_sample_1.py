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

# Define exclusive choice operators for the process
xor1 = OperatorPOWL(operator=Operator.XOR, children=[Idea_Harvest, skip])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[Workshop_Host, skip])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[Concept_Filter, skip])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[Prototype_Build, skip])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[Expert_Review, skip])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[Feasibility_Check, skip])
xor7 = OperatorPOWL(operator=Operator.XOR, children=[Risk_Assess, skip])
xor8 = OperatorPOWL(operator=Operator.XOR, children=[Pilot_Launch, skip])
xor9 = OperatorPOWL(operator=Operator.XOR, children=[Data_Capture, skip])
xor10 = OperatorPOWL(operator=Operator.XOR, children=[Performance_Review, skip])
xor11 = OperatorPOWL(operator=Operator.XOR, children=[Scale_Plan, skip])
xor12 = OperatorPOWL(operator=Operator.XOR, children=[Resource_Align, skip])
xor13 = OperatorPOWL(operator=Operator.XOR, children=[Learn_Share, skip])
xor14 = OperatorPOWL(operator=Operator.XOR, children=[Culture_Embed, skip])

# Define loop operators for the process
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[xor1, xor2])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[xor3, xor4])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[xor5, xor6])
loop4 = OperatorPOWL(operator=Operator.LOOP, children=[xor7, xor8])
loop5 = OperatorPOWL(operator=Operator.LOOP, children=[xor9, xor10])
loop6 = OperatorPOWL(operator=Operator.LOOP, children=[xor11, xor12])
loop7 = OperatorPOWL(operator=Operator.LOOP, children=[xor13, xor14])

# Define partial order for the process
root = StrictPartialOrder(nodes=[loop1, loop2, loop3, loop4, loop5, loop6, loop7])
root.order.add_edge(loop1, xor2)
root.order.add_edge(loop2, xor4)
root.order.add_edge(loop3, xor6)
root.order.add_edge(loop4, xor8)
root.order.add_edge(loop5, xor10)
root.order.add_edge(loop6, xor12)
root.order.add_edge(loop7, xor14)