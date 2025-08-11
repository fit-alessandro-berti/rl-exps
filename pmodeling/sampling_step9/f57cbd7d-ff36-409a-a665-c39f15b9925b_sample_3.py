import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
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

skip = SilentTransition()

# Define the process flow
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[feasibility_check, risk_review])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[tech_prototype, market_simulate, stakeholder_align])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[budget_adjust, talent_source])
loop4 = OperatorPOWL(operator=Operator.LOOP, children=[pilot_launch, data_refine])
loop5 = OperatorPOWL(operator=Operator.LOOP, children=[scale_analysis, integration_plan])
loop6 = OperatorPOWL(operator=Operator.LOOP, children=[change_manage, knowledge_transfer])

root = StrictPartialOrder(nodes=[loop1, loop2, loop3, loop4, loop5, loop6])
root.order.add_edge(loop1, loop2)
root.order.add_edge(loop2, loop3)
root.order.add_edge(loop3, loop4)
root.order.add_edge(loop4, loop5)
root.order.add_edge(loop5, loop6)