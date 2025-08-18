import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define transitions with their respective labels
trend_scan = Transition(label='Trend Scan')
idea_sprint = Transition(label='Idea Sprint')
feasibility_check = Transition(label='Feasibility Check')
risk_review = Transition(label='Risk Review')
tech_prototype = Transition(label='Tech Prototype')
market_simulate = Transition(label='Market Simulate')
stakeholder_align = Transition(label='Stakeholder Align')
budget_adjust = Transition(label='Budget Adjust')
talent_source = Transition(label='Talent Source')
pilot_launch = Transition(label='Pilot Launch')
data_refine = Transition(label='Data Refine')
scale_analysis = Transition(label='Scale Analysis')
integration_plan = Transition(label='Integration Plan')
change_manage = Transition(label='Change Manage')
knowledge_transfer = Transition(label='Knowledge Transfer')

# Define silent transitions
skip = SilentTransition()

# Define exclusive choice (XOR) for stakeholder align and budget adjust
xor = OperatorPOWL(operator=Operator.XOR, children=[stakeholder_align, budget_adjust])

# Define exclusive choice (XOR) for pilot launch and data refine
xor2 = OperatorPOWL(operator=Operator.XOR, children=[pilot_launch, data_refine])

# Define loop for tech prototype and market simulate
loop = OperatorPOWL(operator=Operator.LOOP, children=[tech_prototype, market_simulate])

# Define the root POWL model
root = StrictPartialOrder(nodes=[
    trend_scan, idea_sprint, feasibility_check, risk_review, skip, loop, xor2, xor, tech_prototype, market_simulate,
    stakeholder_align, budget_adjust, pilot_launch, data_refine, scale_analysis, integration_plan, change_manage,
    knowledge_transfer
])

# Add edges to define the partial order relationships
root.order.add_edge(trend_scan, idea_sprint)
root.order.add_edge(idea_sprint, feasibility_check)
root.order.add_edge(feasibility_check, risk_review)
root.order.add_edge(risk_review, skip)
root.order.add_edge(skip, loop)
root.order.add_edge(loop, xor2)
root.order.add_edge(xor2, xor)
root.order.add_edge(xor, tech_prototype)
root.order.add_edge(xor, market_simulate)
root.order.add_edge(tech_prototype, stakeholder_align)
root.order.add_edge(market_simulate, budget_adjust)
root.order.add_edge(budget_adjust, xor2)
root.order.add_edge(xor2, pilot_launch)
root.order.add_edge(xor2, data_refine)
root.order.add_edge(pilot_launch, scale_analysis)
root.order.add_edge(data_refine, integration_plan)
root.order.add_edge(scale_analysis, change_manage)
root.order.add_edge(integration_plan, knowledge_transfer)

print(root)