import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
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

# Define control-flow operators
xor = OperatorPOWL(operator=Operator.XOR, children=[opportunity_scan, idea_workshop])
exclusive_choice = OperatorPOWL(operator=Operator.EXCLUSIVE_CHOICE, children=[concept_merge, resource_align])
loop = OperatorPOWL(operator=Operator.LOOP, children=[prototype_build, feasibility_test, pilot_launch, feedback_gather, design_adapt, compliance_check, scaling_plan, ip_management, market_sync, partner_review, exit_strategy])

# Define the root POWL model
root = StrictPartialOrder(nodes=[xor, exclusive_choice, loop])
root.order.add_edge(xor, exclusive_choice)
root.order.add_edge(exclusive_choice, loop)

# Print the root POWL model
print(root)