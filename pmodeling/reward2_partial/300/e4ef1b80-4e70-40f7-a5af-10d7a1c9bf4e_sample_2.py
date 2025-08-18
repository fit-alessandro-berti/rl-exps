import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities) with their names
Opportunity_Scan = Transition(label='Opportunity Scan')
Idea_Workshop = Transition(label='Idea Workshop')
Concept_Merge = Transition(label='Concept Merge')
Resource_Align = Transition(label='Resource Align')
Prototype_Build = Transition(label='Prototype Build')
Feasibility_Test = Transition(label='Feasibility Test')
Pilot_Launch = Transition(label='Pilot Launch')
Feedback_Gather = Transition(label='Feedback Gather')
Design_Adapt = Transition(label='Design Adapt')
Compliance_Check = Transition(label='Compliance Check')
Scaling_Plan = Transition(label='Scaling Plan')
IP_Management = Transition(label='IP Management')
Market_Sync = Transition(label='Market Sync')
Partner_Review = Transition(label='Partner Review')
Exit_Strategy = Transition(label='Exit Strategy')

# Define the partial order
root = StrictPartialOrder(nodes=[
    Opportunity_Scan,
    Idea_Workshop,
    Concept_Merge,
    Resource_Align,
    Prototype_Build,
    Feasibility_Test,
    Pilot_Launch,
    Feedback_Gather,
    Design_Adapt,
    Compliance_Check,
    Scaling_Plan,
    IP_Management,
    Market_Sync,
    Partner_Review,
    Exit_Strategy
])

# Define the dependencies between the activities
root.order.add_edge(Opportunity_Scan, Idea_Workshop)
root.order.add_edge(Idea_Workshop, Concept_Merge)
root.order.add_edge(Concept_Merge, Resource_Align)
root.order.add_edge(Resource_Align, Prototype_Build)
root.order.add_edge(Prototype_Build, Feasibility_Test)
root.order.add_edge(Feasibility_Test, Pilot_Launch)
root.order.add_edge(Pilot_Launch, Feedback_Gather)
root.order.add_edge(Feedback_Gather, Design_Adapt)
root.order.add_edge(Design_Adapt, Compliance_Check)
root.order.add_edge(Compliance_Check, Scaling_Plan)
root.order.add_edge(Scaling_Plan, IP_Management)
root.order.add_edge(IP_Management, Market_Sync)
root.order.add_edge(Market_Sync, Partner_Review)
root.order.add_edge(Partner_Review, Exit_Strategy)

# Print the final POWL model
print(root)