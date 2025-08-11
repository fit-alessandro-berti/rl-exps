import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
opportunity_scan = Transition(label='Opportunity Scan')
idea_workshop = Transition(label='Idea Workshop')
concept_merge = Transition(label='Concept Merge')
resource_align = Transition(label='Resource Align')
prototype_build = Transition(label='Prototype Build')
feasibility_test = Transition(label='Feasibility Test')
pilot_launch = Transition(label='Pilot Launch')
feedback_gather = Transition(label='Feedback Gather')
design_adapt = Transition(label='Design Adapt')
compliance_check = Transition(label='Compliance Check')
scaling_plan = Transition(label='Scaling Plan')
ip_management = Transition(label='IP Management')
market_sync = Transition(label='Market Sync')
partner_review = Transition(label='Partner Review')
exit_strategy = Transition(label='Exit Strategy')

# Define the partial order
root = StrictPartialOrder(nodes=[
    opportunity_scan, idea_workshop, concept_merge, resource_align, prototype_build, feasibility_test, 
    pilot_launch, feedback_gather, design_adapt, compliance_check, scaling_plan, ip_management, 
    market_sync, partner_review, exit_strategy
])

# Define the dependencies
root.order.add_edge(opportunity_scan, idea_workshop)
root.order.add_edge(idea_workshop, concept_merge)
root.order.add_edge(concept_merge, resource_align)
root.order.add_edge(resource_align, prototype_build)
root.order.add_edge(prototype_build, feasibility_test)
root.order.add_edge(feasibility_test, pilot_launch)
root.order.add_edge(pilot_launch, feedback_gather)
root.order.add_edge(feedback_gather, design_adapt)
root.order.add_edge(design_adapt, compliance_check)
root.order.add_edge(compliance_check, scaling_plan)
root.order.add_edge(scaling_plan, ip_management)
root.order.add_edge(ip_management, market_sync)
root.order.add_edge(market_sync, partner_review)
root.order.add_edge(partner_review, exit_strategy)

# Print the final result
print(root)