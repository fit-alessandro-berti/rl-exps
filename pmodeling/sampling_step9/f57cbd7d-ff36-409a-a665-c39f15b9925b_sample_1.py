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

# Define silent transitions
skip = SilentTransition()

# Define the process
loop = OperatorPOWL(operator=Operator.LOOP, children=[tech_prototype, market_simulate, stakeholder_align])
xor = OperatorPOWL(operator=Operator.XOR, children=[pilot_launch, data_refine])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[scale_analysis, integration_plan])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[change_manage, knowledge_transfer])
root = StrictPartialOrder(nodes=[loop, xor, xor2, xor3])
root.order.add_edge(loop, xor)
root.order.add_edge(loop, xor2)
root.order.add_edge(loop, xor3)
root.order.add_edge(xor, xor2)
root.order.add_edge(xor, xor3)
root.order.add_edge(xor2, xor3)