import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
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

# Define the relationships between activities
# Define the relationships between activities
Trend_Scan = OperatorPOWL(operator=Operator.SILENT, children=[Opportunity_Map])
Opportunity_Map = OperatorPOWL(operator=Operator.XOR, children=[Expert_Gather, Trend_Scan])
Expert_Gather = OperatorPOWL(operator=Operator.LOOP, children=[Idea_Sprint])
Idea_Sprint = OperatorPOWL(operator=Operator.LOOP, children=[Proto_Build])
Proto_Build = OperatorPOWL(operator=Operator.LOOP, children=[User_Feedback])
User_Feedback = OperatorPOWL(operator=Operator.LOOP, children=[Risk_Review])
Risk_Review = OperatorPOWL(operator=Operator.LOOP, children=[IP_Audit])
IP_Audit = OperatorPOWL(operator=Operator.LOOP, children=[Pilot_Launch])
Pilot_Launch = OperatorPOWL(operator=Operator.LOOP, children=[Stakeholder_Meet])
Stakeholder_Meet = OperatorPOWL(operator=Operator.LOOP, children=[Resource_Shift])
Resource_Shift = OperatorPOWL(operator=Operator.LOOP, children=[Scale_Up])
Scale_Up = OperatorPOWL(operator=Operator.LOOP, children=[Impact_Assess])
Impact_Assess = OperatorPOWL(operator=Operator.LOOP, children=[Knowledge_Share])
Knowledge_Share = OperatorPOWL(operator=Operator.LOOP, children=[Monitor_Trends])

# Define the root of the POWL model
root = StrictPartialOrder(nodes=[Trend_Scan, Opportunity_Map, Expert_Gather, Idea_Sprint, Proto_Build, User_Feedback, Risk_Review, IP_Audit, Pilot_Launch, Stakeholder_Meet, Resource_Shift, Scale_Up, Impact_Assess, Knowledge_Share, Monitor_Trends])
root.order.add_edge(Trend_Scan, Opportunity_Map)
root.order.add_edge(Opportunity_Map, Expert_Gather)
root.order.add_edge(Expert_Gather, Idea_Sprint)
root.order.add_edge(Idea_Sprint, Proto_Build)
root.order.add_edge(Proto_Build, User_Feedback)
root.order.add_edge(User_Feedback, Risk_Review)
root.order.add_edge(Risk_Review, IP_Audit)
root.order.add_edge(IP_Audit, Pilot_Launch)
root.order.add_edge(Pilot_Launch, Stakeholder_Meet)
root.order.add_edge(Stakeholder_Meet, Resource_Shift)
root.order.add_edge(Resource_Shift, Scale_Up)
root.order.add_edge(Scale_Up, Impact_Assess)
root.order.add_edge(Impact_Assess, Knowledge_Share)
root.order.add_edge(Knowledge_Share, Monitor_Trends)

# Print the POWL model
print(root)