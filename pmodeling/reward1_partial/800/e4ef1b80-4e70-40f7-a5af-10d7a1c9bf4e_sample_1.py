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

# Define the process tree
opportunity_scan_to_idea_workshop = OperatorPOWL(operator=Operator.XOR, children=[idea_workshop, SilentTransition()])
idea_workshop_to_concept_merge = OperatorPOWL(operator=Operator.XOR, children=[concept_merge, SilentTransition()])
concept_merge_to_resource_align = OperatorPOWL(operator=Operator.XOR, children=[resource_align, SilentTransition()])
resource_align_to_prototype_build = OperatorPOWL(operator=Operator.XOR, children=[prototype_build, SilentTransition()])
prototype_build_to_feasibility_test = OperatorPOWL(operator=Operator.XOR, children=[feasibility_test, SilentTransition()])
feasibility_test_to_pilot_launch = OperatorPOWL(operator=Operator.XOR, children=[pilot_launch, SilentTransition()])
pilot_launch_to_feedback_gather = OperatorPOWL(operator=Operator.XOR, children=[feedback_gather, SilentTransition()])
feedback_gather_to_design_adapt = OperatorPOWL(operator=Operator.XOR, children=[design_adapt, SilentTransition()])
design_adapt_to_compliance_check = OperatorPOWL(operator=Operator.XOR, children=[compliance_check, SilentTransition()])
compliance_check_to_scaling_plan = OperatorPOWL(operator=Operator.XOR, children=[scaling_plan, SilentTransition()])
scaling_plan_to_ip_management = OperatorPOWL(operator=Operator.XOR, children=[ip_management, SilentTransition()])
ip_management_to_market_sync = OperatorPOWL(operator=Operator.XOR, children=[market_sync, SilentTransition()])
market_sync_to_partner_review = OperatorPOWL(operator=Operator.XOR, children=[partner_review, SilentTransition()])
partner_review_to_exit_strategy = OperatorPOWL(operator=Operator.XOR, children=[exit_strategy, SilentTransition()])

# Define the partial order
root = StrictPartialOrder(nodes=[opportunity_scan, idea_workshop, concept_merge, resource_align, prototype_build, feasibility_test, pilot_launch, feedback_gather, design_adapt, compliance_check, scaling_plan, ip_management, market_sync, partner_review, exit_strategy])
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

# Print the root model
print(root)