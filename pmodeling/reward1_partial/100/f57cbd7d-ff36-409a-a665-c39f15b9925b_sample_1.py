import pm4py

# Define the transitions (activities) with their labels
trend_scan = pm4py.objects.powl.obj.Transition(label='Trend Scan')
idea_sprint = pm4py.objects.powl.obj.Transition(label='Idea Sprint')
feasibility_check = pm4py.objects.powl.obj.Transition(label='Feasibility Check')
risk_review = pm4py.objects.powl.obj.Transition(label='Risk Review')
tech_prototype = pm4py.objects.powl.obj.Transition(label='Tech Prototype')
market_simulate = pm4py.objects.powl.obj.Transition(label='Market Simulate')
stakeholder_align = pm4py.objects.powl.obj.Transition(label='Stakeholder Align')
budget_adjust = pm4py.objects.powl.obj.Transition(label='Budget Adjust')
talent_source = pm4py.objects.powl.obj.Transition(label='Talent Source')
pilot_launch = pm4py.objects.powl.obj.Transition(label='Pilot Launch')
data_refine = pm4py.objects.powl.obj.Transition(label='Data Refine')
scale_analysis = pm4py.objects.powl.obj.Transition(label='Scale Analysis')
integration_plan = pm4py.objects.powl.obj.Transition(label='Integration Plan')
change_manage = pm4py.objects.powl.obj.Transition(label='Change Manage')
knowledge_transfer = pm4py.objects.powl.obj.Transition(label='Knowledge Transfer')

# Define the loop and choice nodes
loop_node = pm4py.objects.powl.obj.OperatorPOWL(
    operator=pm4py.objects.powl.obj.Operator.LOOP, children=[feasibility_check, risk_review, tech_prototype, market_simulate, stakeholder_align]
)
xor_node = pm4py.objects.powl.obj.OperatorPOWL(
    operator=pm4py.objects.powl.obj.Operator.XOR, children=[budget_adjust, talent_source, pilot_launch]
)
xor_node2 = pm4py.objects.powl.obj.OperatorPOWL(
    operator=pm4py.objects.powl.obj.Operator.XOR, children=[data_refine, scale_analysis, integration_plan]
)
xor_node3 = pm4py.objects.powl.obj.OperatorPOWL(
    operator=pm4py.objects.powl.obj.Operator.XOR, children=[change_manage, knowledge_transfer]
)

# Construct the strict partial order with defined nodes and their dependencies
root = pm4py.objects.powl.obj.StrictPartialOrder(
    nodes=[trend_scan, idea_sprint, loop_node, xor_node, xor_node2, xor_node3]
)

# Add edges to the partial order
root.order.add_edge(trend_scan, idea_sprint)
root.order.add_edge(idea_sprint, loop_node)
root.order.add_edge(loop_node, xor_node)
root.order.add_edge(xor_node, xor_node2)
root.order.add_edge(xor_node2, xor_node3)
root.order.add_edge(xor_node3, change_manage)

print(root)