from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
root = StrictPartialOrder()

# Define the activities
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

# Define the control-flow operators
xor1 = OperatorPOWL(operator=Operator.XOR, children=[Expert_Gather, Idea_Sprint])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[Risk_Review, IP_Audit])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[Stakeholder_Meet, Resource_Shift])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[Impact_Assess, Knowledge_Share])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[Monitor_Trends, Trend_Scan])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[Proto_Build, User_Feedback])
xor7 = OperatorPOWL(operator=Operator.XOR, children=[Pilot_Launch, Scale_Up])

# Add the activities to the POWL model
root.add_transition(Trend_Scan)
root.add_transition(Opportunity_Map)
root.add_transition(Expert_Gather)
root.add_transition(Idea_Sprint)
root.add_transition(Proto_Build)
root.add_transition(User_Feedback)
root.add_transition(Risk_Review)
root.add_transition(IP_Audit)
root.add_transition(Pilot_Launch)
root.add_transition(Stakeholder_Meet)
root.add_transition(Resource_Shift)
root.add_transition(Scale_Up)
root.add_transition(Impact_Assess)
root.add_transition(Knowledge_Share)
root.add_transition(Monitor_Trends)

# Add the control-flow operators to the POWL model
root.add_operator(xor1)
root.add_operator(xor2)
root.add_operator(xor3)
root.add_operator(xor4)
root.add_operator(xor5)
root.add_operator(xor6)
root.add_operator(xor7)

# Add the dependencies between the activities and control-flow operators
root.add_edge(Trend_Scan, xor5)
root.add_edge(Opportunity_Map, xor5)
root.add_edge(Expert_Gather, xor1)
root.add_edge(Idea_Sprint, xor1)
root.add_edge(Proto_Build, xor6)
root.add_edge(User_Feedback, xor6)
root.add_edge(Risk_Review, xor2)
root.add_edge(IP_Audit, xor2)
root.add_edge(Stakeholder_Meet, xor3)
root.add_edge(Resource_Shift, xor3)
root.add_edge(Pilot_Launch, xor7)
root.add_edge(Scale_Up, xor7)
root.add_edge(Impact_Assess, xor4)
root.add_edge(Knowledge_Share, xor4)
root.add_edge(Monitor_Trends, xor5)

# Print the POWL model
print(root)