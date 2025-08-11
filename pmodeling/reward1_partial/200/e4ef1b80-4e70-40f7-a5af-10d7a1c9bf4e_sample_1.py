from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define the transitions
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

# Define the loop node
loop_node = OperatorPOWL(operator=Operator.LOOP, children=[
    opportunity_scan, idea_workshop, concept_merge, resource_align, prototype_build,
    feasibility_test, pilot_launch, feedback_gather, design_adapt, compliance_check,
    scaling_plan, ip_management, market_sync, partner_review, exit_strategy
])

# Define the partial order
root = StrictPartialOrder(nodes=[loop_node])