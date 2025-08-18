import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions
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

# Define exclusive choice
exclusive_choice = OperatorPOWL(operator=Operator.XOR, children=[
    tech_prototype,
    market_simulate,
    stakeholder_align,
    pilot_launch,
    data_refine,
    scale_analysis,
    integration_plan,
    change_manage,
    knowledge_transfer
])

# Define loop for risk review and feasibility check
loop = OperatorPOWL(operator=Operator.LOOP, children=[risk_review, feasibility_check])

# Define root POWL model
root = StrictPartialOrder(nodes=[trend_scan, idea_sprint, loop, exclusive_choice])
root.order.add_edge(trend_scan, idea_sprint)
root.order.add_edge(idea_sprint, loop)
root.order.add_edge(loop, exclusive_choice)