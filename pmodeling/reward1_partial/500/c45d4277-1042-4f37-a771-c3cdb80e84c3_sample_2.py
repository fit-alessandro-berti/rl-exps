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
root = StrictPartialOrder(
    nodes=[
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
    ],
    order=[
        (Trend_Scan, Opportunity_Map),
        (Opportunity_Map, Expert_Gather),
        (Expert_Gather, Idea_Sprint),
        (Idea_Sprint, Proto_Build),
        (Proto_Build, User_Feedback),
        (User_Feedback, Risk_Review),
        (Risk_Review, IP_Audit),
        (IP_Audit, Pilot_Launch),
        (Pilot_Launch, Stakeholder_Meet),
        (Stakeholder_Meet, Resource_Shift),
        (Resource_Shift, Scale_Up),
        (Scale_Up, Impact_Assess),
        (Impact_Assess, Knowledge_Share),
        (Knowledge_Share, Monitor_Trends)
    ]
)