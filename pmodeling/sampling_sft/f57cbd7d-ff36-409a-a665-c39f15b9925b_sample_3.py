import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
trend_scan      = Transition(label='Trend Scan')
idea_sprint     = Transition(label='Idea Sprint')
feasibility_chk = Transition(label='Feasibility Check')
risk_review     = Transition(label='Risk Review')
tech_prototype  = Transition(label='Tech Prototype')
market_simulate = Transition(label='Market Simulate')
stakeholder_align = Transition(label='Stakeholder Align')
budget_adjust   = Transition(label='Budget Adjust')
talent_source   = Transition(label='Talent Source')
pilot_launch    = Transition(label='Pilot Launch')
data_refine     = Transition(label='Data Refine')
scale_analysis  = Transition(label='Scale Analysis')
integration_plan = Transition(label='Integration Plan')
change_manage   = Transition(label='Change Manage')
knowledge_transfer = Transition(label='Knowledge Transfer')

# Build the prototyping & validation sub-process (A)
prototyping = StrictPartialOrder(nodes=[tech_prototype, market_simulate, stakeholder_align, data_refine])
prototyping.order.add_edge(tech_prototype, market_simulate)
prototyping.order.add_edge(market_simulate, stakeholder_align)
prototyping.order.add_edge(stakeholder_align, data_refine)

# Build the resource allocation sub-process (B)
resource_alloc = StrictPartialOrder(nodes=[budget_adjust, talent_source])
resource_alloc.order.add_edge(budget_adjust, talent_source)

# Build the main process as a loop: do prototyping & validation, then optionally do resource allocation and repeat
main_body = StrictPartialOrder(nodes=[prototyping, resource_alloc])
main_body.order.add_edge(prototyping, resource_alloc)

loop = OperatorPOWL(operator=Operator.LOOP, children=[main_body, resource_alloc])

# Build the final sequence after the loop
final_seq = StrictPartialOrder(nodes=[scale_analysis, integration_plan, change_manage, knowledge_transfer])
final_seq.order.add_edge(loop, scale_analysis)
final_seq.order.add_edge(scale_analysis, integration_plan)
final_seq.order.add_edge(integration_plan, change_manage)
final_seq.order.add_edge(change_manage, knowledge_transfer)

# Assemble the overall root process
root = StrictPartialOrder(nodes=[
    trend_scan,
    idea_sprint,
    feasibility_chk,
    risk_review,
    loop,
    final_seq
])
root.order.add_edge(trend_scan, idea_sprint)
root.order.add_edge(idea_sprint, feasibility_chk)
root.order.add_edge(feasibility_chk, risk_review)
root.order.add_edge(risk_review, loop)
root.order.add_edge(loop, final_seq)