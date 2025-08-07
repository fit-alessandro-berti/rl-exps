import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define the atomic activities
trend_scan      = Transition(label='Trend Scan')
idea_sprint     = Transition(label='Idea Sprint')
feasibility     = Transition(label='Feasibility Check')
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

# Build the partial order
root = StrictPartialOrder(nodes=[
    trend_scan,
    idea_sprint,
    feasibility,
    risk_review,
    tech_prototype,
    market_simulate,
    stakeholder_align,
    budget_adjust,
    talent_source,
    pilot_launch,
    data_refine,
    scale_analysis,
    integration_plan,
    change_manage,
    knowledge_transfer
])

# Define the control-flow dependencies
root.order.add_edge(trend_scan, idea_sprint)
root.order.add_edge(idea_sprint, feasibility)
root.order.add_edge(idea_sprint, risk_review)
root.order.add_edge(feasibility, tech_prototype)
root.order.add_edge(risk_review, tech_prototype)
root.order.add_edge(tech_prototype, market_simulate)
root.order.add_edge(market_simulate, stakeholder_align)
root.order.add_edge(stakeholder_align, budget_adjust)
root.order.add_edge(budget_adjust, talent_source)
root.order.add_edge(talent_source, pilot_launch)
root.order.add_edge(pilot_launch, data_refine)
root.order.add_edge(data_refine, data_refine)  # Parallel data refinement
root.order.add_edge(data_refine, scale_analysis)
root.order.add_edge(scale_analysis, integration_plan)
root.order.add_edge(integration_plan, change_manage)
root.order.add_edge(change_manage, knowledge_transfer)

# Close the loop with a silent transition to represent the end
root.order.add_edge(knowledge_transfer, knowledge_transfer)