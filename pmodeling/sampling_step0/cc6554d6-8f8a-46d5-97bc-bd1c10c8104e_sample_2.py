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

# Define the loops
risk_assess_loop = OperatorPOWL(operator=Operator.LOOP, children=[risk_assess])
delay_monitor_loop = OperatorPOWL(operator=Operator.LOOP, children=[delay_monitor])

# Define the exclusive choices
inventory_scan_xor = OperatorPOWL(operator=Operator.XOR, children=[inventory_scan, delay_monitor])
order_prioritize_xor = OperatorPOWL(operator=Operator.XOR, children=[order_prioritize, inventory_scan])
contract_review_xor = OperatorPOWL(operator=Operator.XOR, children=[contract_review, delay_monitor])
cost_analyze_xor = OperatorPOWL(operator=Operator.XOR, children=[cost_analyze, delay_monitor])
compliance_check_xor = OperatorPOWL(operator=Operator.XOR, children=[compliance_check, delay_monitor])
alternative_engage_xor = OperatorPOWL(operator=Operator.XOR, children=[alternative_engage, delay_monitor])
inventory_reallocate_xor = OperatorPOWL(operator=Operator.XOR, children=[inventory_reallocate, delay_monitor])
performance_track_xor = OperatorPOWL(operator=Operator.XOR, children=[performance_track, delay_monitor])

# Define the partial order
root = StrictPartialOrder(nodes=[demand_forecast, risk_assess_loop, supplier_audit, inventory_scan_xor, order_prioritize_xor, contract_review_xor, delay_monitor_loop, shipment_reroute, cost_analyze_xor, compliance_check_xor, alternative_engage_xor, inventory_reallocate_xor, performance_track_xor, feedback_loop, strategy_update])
root.order.add_edge(demand_forecast, risk_assess_loop)
root.order.add_edge(demand_forecast, supplier_audit)
root.order.add_edge(risk_assess_loop, inventory_scan_xor)
root.order.add_edge(risk_assess_loop, order_prioritize_xor)
root.order.add_edge(order_prioritize_xor, contract_review_xor)
root.order.add_edge(order_prioritize_xor, delay_monitor_loop)
root.order.add_edge(delay_monitor_loop, shipment_reroute)
root.order.add_edge(delay_monitor_loop, cost_analyze_xor)
root.order.add_edge(delay_monitor_loop, compliance_check_xor)
root.order.add_edge(delay_monitor_loop, alternative_engage_xor)
root.order.add_edge(delay_monitor_loop, inventory_reallocate_xor)
root.order.add_edge(delay_monitor_loop, performance_track_xor)
root.order.add_edge(delay_monitor_loop, feedback_loop)
root.order.add_edge(feedback_loop, strategy_update)

# Print the POWL model
print(root)