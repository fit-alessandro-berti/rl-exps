import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions
Trend_Scan = Transition(label='Trend Scan')
Opportunity_Map = Transition(label='Opportunity Map')
Expert_Gather = Transition(label='Expert Gather')
Idea_Sprint = Transition(label='Idea Sprint')
Proto_Build = Transition(label='Proto Build')
User_Feedback = Transition(label='User Feedback')
Risk_Review = Transition(label='Risk Review')
IP_Audit = Transition(label='IP Audit')
Pilot_Launch = Transition(label='Pilot Launch')
Stakeholder_Meet = Transition(label='Stakeholder Meet')
Resource_Shift = Transition(label='Resource Shift')
Scale_Up = Transition(label='Scale Up')
Impact_Assess = Transition(label='Impact Assess')
Knowledge_Share = Transition(label='Knowledge Share')
Monitor_Trends = Transition(label='Monitor Trends')

# Define silent transitions
skip = SilentTransition()

# Define loops
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[Idea_Sprint, Proto_Build])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[Risk_Review, IP_Audit])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[Pilot_Launch, Stakeholder_Meet, Resource_Shift])
loop4 = OperatorPOWL(operator=Operator.LOOP, children=[Scale_Up, Impact_Assess, Knowledge_Share])
loop5 = OperatorPOWL(operator=Operator.LOOP, children=[Monitor_Trends])

# Define XORs
xor1 = OperatorPOWL(operator=Operator.XOR, children=[Trend_Scan, skip])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[Opportunity_Map, Expert_Gather])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[Proto_Build, User_Feedback])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[Risk_Review, IP_Audit])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[Pilot_Launch, Stakeholder_Meet, Resource_Shift])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[Scale_Up, Impact_Assess, Knowledge_Share])
xor7 = OperatorPOWL(operator=Operator.XOR, children=[Monitor_Trends])

# Define root
root = StrictPartialOrder(nodes=[xor1, xor2, loop1, xor3, loop2, xor4, loop3, xor5, loop4, xor6, loop5, xor7])
root.order.add_edge(xor1, loop1)
root.order.add_edge(xor2, loop1)
root.order.add_edge(loop1, xor3)
root.order.add_edge(xor3, loop2)
root.order.add_edge(loop2, xor4)
root.order.add_edge(xor4, loop3)
root.order.add_edge(loop3, xor5)
root.order.add_edge(xor5, loop4)
root.order.add_edge(loop4, xor6)
root.order.add_edge(xor6, loop5)
root.order.add_edge(loop5, xor7)
root.order.add_edge(xor7, loop5)