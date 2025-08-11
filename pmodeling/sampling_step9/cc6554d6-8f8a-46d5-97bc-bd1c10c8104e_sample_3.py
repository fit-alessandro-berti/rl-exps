import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
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

skip = SilentTransition()

# Define the loop nodes
risk_assess_loop = OperatorPOWL(operator=Operator.LOOP, children=[risk_assess, supplier_audit, inventory_scan, route_optimize, order_prioritize, contract_review])
delay_monitor_loop = OperatorPOWL(operator=Operator.LOOP, children=[delay_monitor, shipment_reroute, cost_analyze, compliance_check, alternative_engage, inventory_reallocate])
performance_track_loop = OperatorPOWL(operator=Operator.LOOP, children=[performance_track, feedback_loop, strategy_update])

# Define the choice nodes
xor = OperatorPOWL(operator=Operator.XOR, children=[delay_monitor_loop, performance_track_loop])

# Define the root node
root = StrictPartialOrder(nodes=[risk_assess_loop, delay_monitor_loop, performance_track_loop, xor])
root.order.add_edge(risk_assess_loop, xor)
root.order.add_edge(delay_monitor_loop, xor)
root.order.add_edge(performance_track_loop, xor)

# Print the root node
print(root)