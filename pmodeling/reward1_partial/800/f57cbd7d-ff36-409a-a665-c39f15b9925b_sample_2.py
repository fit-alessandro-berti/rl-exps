import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
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

# Define the control-flow operators
xor = OperatorPOWL(operator=Operator.XOR, children=[feasibility_check, risk_review])
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[tech_prototype, market_simulate, stakeholder_align])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[budget_adjust, talent_source])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[pilot_launch, data_refine])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[scale_analysis, integration_plan])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[change_manage, knowledge_transfer])

# Define the root model
root = StrictPartialOrder(nodes=[trend_scan, idea_sprint, xor, loop1, xor2, loop2, xor3, loop3])
root.order.add_edge(trend_scan, idea_sprint)
root.order.add_edge(idea_sprint, xor)
root.order.add_edge(xor, loop1)
root.order.add_edge(loop1, xor)
root.order.add_edge(xor, xor2)
root.order.add_edge(xor2, loop2)
root.order.add_edge(loop2, xor)
root.order.add_edge(xor, xor3)
root.order.add_edge(xor3, loop3)
root.order.add_edge(loop3, xor)