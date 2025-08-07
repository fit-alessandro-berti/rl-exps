import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
trend_scan    = Transition(label='Trend Scan')
idea_sprint   = Transition(label='Idea Sprint')
feasibility   = Transition(label='Feasibility Check')
risk_review   = Transition(label='Risk Review')
tech_proto    = Transition(label='Tech Prototype')
market_sim    = Transition(label='Market Simulate')
stakeholder   = Transition(label='Stakeholder Align')
budget_adj    = Transition(label='Budget Adjust')
talent_source = Transition(label='Talent Source')
pilot_launch  = Transition(label='Pilot Launch')
data_refine   = Transition(label='Data Refine')
scale_analysis= Transition(label='Scale Analysis')
integration   = Transition(label='Integration Plan')
change_manage = Transition(label='Change Manage')
knowledge    = Transition(label='Knowledge Transfer')

# Define the iterative refinement loop: Pilot Launch -> Data Refine -> repeat
loop_body = StrictPartialOrder(nodes=[data_refine])
loop_body.order.add_edge(data_refine, pilot_launch)
refinement_loop = OperatorPOWL(operator=Operator.LOOP, children=[pilot_launch, loop_body])

# Build the overall partial order
root = StrictPartialOrder(
    nodes=[
        trend_scan,
        idea_sprint,
        feasibility,
        risk_review,
        tech_proto,
        market_sim,
        stakeholder,
        budget_adj,
        talent_source,
        refinement_loop,
        scale_analysis,
        integration,
        change_manage,
        knowledge
    ]
)

# Add the control-flow dependencies
root.order.add_edge(trend_scan, idea_sprint)
root.order.add_edge(idea_sprint, feasibility)
root.order.add_edge(idea_sprint, risk_review)
root.order.add_edge(feasibility, tech_proto)
root.order.add_edge(risk_review, tech_proto)
root.order.add_edge(tech_proto, market_sim)
root.order.add_edge(tech_proto, stakeholder)
root.order.add_edge(market_sim, refinement_loop)
root.order.add_edge(stakeholder, refinement_loop)
root.order.add_edge(refinement_loop, scale_analysis)
root.order.add_edge(scale_analysis, integration)
root.order.add_edge(integration, change_manage)
root.order.add_edge(integration, knowledge)
root.order.add_edge(change_manage, knowledge)

# Optional: if you want to add explicit dependencies between the refinement loop and the budget/talent source
# root.order.add_edge(refinement_loop, budget_adj)
# root.order.add_edge(refinement_loop, talent_source)