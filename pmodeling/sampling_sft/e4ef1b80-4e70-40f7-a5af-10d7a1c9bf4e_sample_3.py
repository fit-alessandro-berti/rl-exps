import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
op_scan    = Transition(label='Opportunity Scan')
idea_work  = Transition(label='Idea Workshop')
concept_m  = Transition(label='Concept Merge')
resource_a = Transition(label='Resource Align')
prototype  = Transition(label='Prototype Build')
feas_test  = Transition(label='Feasibility Test')
pilot_la   = Transition(label='Pilot Launch')
feedback   = Transition(label='Feedback Gather')
design_ad  = Transition(label='Design Adapt')
compliance = Transition(label='Compliance Check')
scaling_p  = Transition(label='Scaling Plan')
ip_manage  = Transition(label='IP Management')
market_s   = Transition(label='Market Sync')
partner_r  = Transition(label='Partner Review')
exit_s     = Transition(label='Exit Strategy')

# Define the iterative cycle: 
#   1. Opportunity Scan -> Idea Workshop -> Concept Merge -> Resource Align
#   2. Prototype Build -> Feasibility Test -> Pilot Launch -> Feedback Gather
#   3. Design Adapt -> Compliance Check -> Scaling Plan -> IP Management
#   4. Market Sync -> Partner Review -> Exit Strategy

cycle = StrictPartialOrder(nodes=[
    idea_work, concept_m, resource_a,
    prototype, feas_test, pilot_la, feedback,
    design_ad, compliance, scaling_p, ip_manage,
    market_s, partner_r, exit_s
])

cycle.order.add_edge(idea_work, concept_m)
cycle.order.add_edge(concept_m, resource_a)
cycle.order.add_edge(resource_a, prototype)
cycle.order.add_edge(prototype, feas_test)
cycle.order.add_edge(feas_test, pilot_la)
cycle.order.add_edge(pilot_la, feedback)
cycle.order.add_edge(feedback, design_ad)
cycle.order.add_edge(design_ad, compliance)
cycle.order.add_edge(compliance, scaling_p)
cycle.order.add_edge(scaling_p, ip_manage)
cycle.order.add_edge(ip_manage, market_s)
cycle.order.add_edge(market_s, partner_r)
cycle.order.add_edge(partner_r, exit_s)

# Loop the entire cycle until exit
loop = OperatorPOWL(operator=Operator.LOOP, children=[op_scan, cycle])

# Root of the overall process
root = loop