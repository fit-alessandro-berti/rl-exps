import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities with their exact names
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

# Define the control flow operators
xor_demand_risk = OperatorPOWL(operator=Operator.XOR, children=[demand_forecast, risk_assess])
xor_audit_scan = OperatorPOWL(operator=Operator.XOR, children=[supplier_audit, inventory_scan])
xor_optimize_prioritize = OperatorPOWL(operator=Operator.XOR, children=[route_optimize, order_prioritize])
xor_contract_review = OperatorPOWL(operator=Operator.XOR, children=[contract_review, delay_monitor])
xor_reroute_analyze = OperatorPOWL(operator=Operator.XOR, children=[shipment_reroute, cost_analyze])
xor_check_engage = OperatorPOWL(operator=Operator.XOR, children=[compliance_check, alternative_engage])
xor_reallocate_track = OperatorPOWL(operator=Operator.XOR, children=[inventory_reallocate, performance_track])
xor_feedback_update = OperatorPOWL(operator=Operator.XOR, children=[feedback_loop, strategy_update])

# Create the root node as a partial order
root = StrictPartialOrder(nodes=[xor_demand_risk, xor_audit_scan, xor_optimize_prioritize, xor_contract_review, xor_reroute_analyze, xor_check_engage, xor_reallocate_track, xor_feedback_update])

# Define the dependencies between nodes
root.order.add_edge(xor_demand_risk, xor_audit_scan)
root.order.add_edge(xor_audit_scan, xor_optimize_prioritize)
root.order.add_edge(xor_optimize_prioritize, xor_contract_review)
root.order.add_edge(xor_contract_review, xor_reroute_analyze)
root.order.add_edge(xor_reroute_analyze, xor_check_engage)
root.order.add_edge(xor_check_engage, xor_reallocate_track)
root.order.add_edge(xor_reallocate_track, xor_feedback_update)