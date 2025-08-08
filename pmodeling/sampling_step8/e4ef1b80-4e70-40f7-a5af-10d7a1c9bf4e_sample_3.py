import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define the activities
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

# Define the partial orders
opportunity_scan_to_idea_workshop = OperatorPOWL(operator=OperatorPOWL.Operator.EXCLUSIVE_CHOICE, children=[Opportunity_Scan, Idea_Workshop])
idea_workshop_to_concept_merge = OperatorPOWL(operator=OperatorPOWL.Operator.EXCLUSIVE_CHOICE, children=[Idea_Workshop, Concept_Merge])
concept_merge_to_resource_align = OperatorPOWL(operator=OperatorPOWL.Operator.EXCLUSIVE_CHOICE, children=[Concept_Merge, Resource_Align])
resource_align_to_prototype_build = OperatorPOWL(operator=OperatorPOWL.Operator.EXCLUSIVE_CHOICE, children=[Resource_Align, Prototype_Build])
prototype_build_to_feasibility_test = OperatorPOWL(operator=OperatorPOWL.Operator.EXCLUSIVE_CHOICE, children=[Prototype_Build, Feasibility_Test])
feasibility_test_to_pilot_launch = OperatorPOWL(operator=OperatorPOWL.Operator.EXCLUSIVE_CHOICE, children=[Feasibility_Test, Pilot_Launch])
pilot_launch_to_feedback_gather = OperatorPOWL(operator=OperatorPOWL.Operator.EXCLUSIVE_CHOICE, children=[Pilot_Launch, Feedback_Gather])
feedback_gather_to_design_adapt = OperatorPOWL(operator=OperatorPOWL.Operator.EXCLUSIVE_CHOICE, children=[Feedback_Gather, Design_Adapt])
design_adapt_to_compliance_check = OperatorPOWL(operator=OperatorPOWL.Operator.EXCLUSIVE_CHOICE, children=[Design_Adapt, Compliance_Check])
compliance_check_to_scaling_plan = OperatorPOWL(operator=OperatorPOWL.Operator.EXCLUSIVE_CHOICE, children=[Compliance_Check, Scaling_Plan])
scaling_plan_to_ip_management = OperatorPOWL(operator=OperatorPOWL.Operator.EXCLUSIVE_CHOICE, children=[Scaling_Plan, IP_Management])
ip_management_to_market_sync = OperatorPOWL(operator=OperatorPOWL.Operator.EXCLUSIVE_CHOICE, children=[IP_Management, Market_Sync])
market_sync_to_partner_review = OperatorPOWL(operator=OperatorPOWL.Operator.EXCLUSIVE_CHOICE, children=[Market_Sync, Partner_Review])
partner_review_to_exit_strategy = OperatorPOWL(operator=OperatorPOWL.Operator.EXCLUSIVE_CHOICE, children=[Partner_Review, Exit_Strategy])

# Define the partial order
root = StrictPartialOrder(nodes=[
    opportunity_scan_to_idea_workshop,
    idea_workshop_to_concept_merge,
    concept_merge_to_resource_align,
    resource_align_to_prototype_build,
    prototype_build_to_feasibility_test,
    feasibility_test_to_pilot_launch,
    pilot_launch_to_feedback_gather,
    feedback_gather_to_design_adapt,
    design_adapt_to_compliance_check,
    compliance_check_to_scaling_plan,
    scaling_plan_to_ip_management,
    ip_management_to_market_sync,
    market_sync_to_partner_review,
    partner_review_to_exit_strategy
])

# Add edges to the partial order
root.order.add_edge(opportunity_scan_to_idea_workshop, idea_workshop_to_concept_merge)
root.order.add_edge(idea_workshop_to_concept_merge, concept_merge_to_resource_align)
root.order.add_edge(concept_merge_to_resource_align, resource_align_to_prototype_build)
root.order.add_edge(resource_align_to_prototype_build, prototype_build_to_feasibility_test)
root.order.add_edge(prototype_build_to_feasibility_test, feasibility_test_to_pilot_launch)
root.order.add_edge(feasibility_test_to_pilot_launch, pilot_launch_to_feedback_gather)
root.order.add_edge(pilot_launch_to_feedback_gather, feedback_gather_to_design_adapt)
root.order.add_edge(feedback_gather_to_design_adapt, design_adapt_to_compliance_check)
root.order.add_edge(design_adapt_to_compliance_check, compliance_check_to_scaling_plan)
root.order.add_edge(compliance_check_to_scaling_plan, scaling_plan_to_ip_management)
root.order.add_edge(scaling_plan_to_ip_management, ip_management_to_market_sync)
root.order.add_edge(ip_management_to_market_sync, market_sync_to_partner_review)
root.order.add_edge(market_sync_to_partner_review, partner_review_to_exit_strategy)