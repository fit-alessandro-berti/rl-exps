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

# Define the loop for cross-validation
cross_validation_loop = OperatorPOWL(operator=Operator.LOOP, children=[
    pilot_launch,
    feedback_gather,
    design_adapt,
    compliance_check,
    scaling_plan,
    ip_management,
    market_sync,
    partner_review
])

# Define the main process
main_process = StrictPartialOrder(nodes=[
    opportunity_scan,
    idea_workshop,
    concept_merge,
    resource_align,
    prototype_build,
    feasibility_test,
    cross_validation_loop
])

# Add dependencies between nodes
main_process.order.add_edge(opportunity_scan, idea_workshop)
main_process.order.add_edge(idea_workshop, concept_merge)
main_process.order.add_edge(concept_merge, resource_align)
main_process.order.add_edge(resource_align, prototype_build)
main_process.order.add_edge(prototype_build, feasibility_test)
main_process.order.add_edge(feasibility_test, cross_validation_loop)

# Set the root of the POWL model
root = main_process