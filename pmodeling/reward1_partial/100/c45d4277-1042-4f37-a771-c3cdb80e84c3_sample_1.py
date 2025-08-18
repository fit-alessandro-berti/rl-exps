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

# Define partial order model
loop = OperatorPOWL(operator=Operator.LOOP, children=[Trend_Scan, Expert_Gather, Idea_Sprint, Proto_Build, User_Feedback, Risk_Review, IP_Audit, Pilot_Launch, Stakeholder_Meet, Resource_Shift, Scale_Up, Impact_Assess, Knowledge_Share, Monitor_Trends])
root = StrictPartialOrder(nodes=[loop])
root.order.add_edge(loop, loop)

print(root)