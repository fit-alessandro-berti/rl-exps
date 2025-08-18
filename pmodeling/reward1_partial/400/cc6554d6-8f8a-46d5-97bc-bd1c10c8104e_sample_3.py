from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
demand_forecast = Transition(label='Demand Forecast')
risk_assess = Transition(label='Risk Assess')
supplier_audit = Transition(label='Supplier Audit')
inventory_scan = Transition(label='Inventory Scan')
route_optimize = Transition(label='Route Optimize')
order_prioritize = Transition(label='Order Prioritize')
contract_review = Transition(label='Contract Review')
delay_monitor = Transition(label='Delay Monitor')
shipment_reroute = Transition(label='Shipment Reroute')
cost_analyze = Transition(label='Cost Analyze')
compliance_check = Transition(label='Compliance Check')
alternative_engage = Transition(label='Alternative Engage')
inventory_reallocate = Transition(label='Inventory Reallocate')
performance_track = Transition(label='Performance Track')
feedback_loop = Transition(label='Feedback Loop')
strategy_update = Transition(label='Strategy Update')

# Define the process tree structure
xor1 = OperatorPOWL(operator=Operator.XOR, children=[delay_monitor, contract_review])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[compliance_check, alternative_engage])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[inventory_reallocate, performance_track])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[feedback_loop, strategy_update])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[route_optimize, order_prioritize])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[inventory_scan, supplier_audit])
xor7 = OperatorPOWL(operator=Operator.XOR, children=[risk_assess, demand_forecast])

# Define the partial order
root = StrictPartialOrder(nodes=[xor1, xor2, xor3, xor4, xor5, xor6, xor7])
root.order.add_edge(xor1, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, xor5)
root.order.add_edge(xor5, xor6)
root.order.add_edge(xor6, xor7)

print(root)