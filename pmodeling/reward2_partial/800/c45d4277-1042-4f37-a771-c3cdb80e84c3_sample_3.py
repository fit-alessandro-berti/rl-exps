import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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

# Define the POWL model
root = StrictPartialOrder(nodes=[
    Trend_Scan,
    Opportunity_Map,
    Expert_Gather,
    Idea_Sprint,
    Proto_Build,
    User_Feedback,
    Risk_Review,
    IP_Audit,
    Pilot_Launch,
    Stakeholder_Meet,
    Resource_Shift,
    Scale_Up,
    Impact_Assess,
    Knowledge_Share,
    Monitor_Trends
])

# Define the dependencies
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

# Print the root model
print(root)