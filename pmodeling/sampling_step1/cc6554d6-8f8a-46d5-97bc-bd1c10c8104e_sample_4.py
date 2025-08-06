from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions
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

# Define silent transitions
skip = SilentTransition()

# Define loop nodes
supplier_audit_loop = OperatorPOWL(operator=Operator.LOOP, children=[supplier_audit, inventory_scan])
contract_review_loop = OperatorPOWL(operator=Operator.LOOP, children=[contract_review, delay_monitor])
delay_monitor_loop = OperatorPOWL(operator=Operator.LOOP, children=[delay_monitor, order_prioritize])
route_optimize_loop = OperatorPOWL(operator=Operator.LOOP, children=[route_optimize, cost_analyze])
cost_analyze_loop = OperatorPOWL(operator=Operator.LOOP, children=[cost_analyze, compliance_check])
compliance_check_loop = OperatorPOWL(operator=Operator.LOOP, children=[compliance_check, alternative_engage])
alternative_engage_loop = OperatorPOWL(operator=Operator.LOOP, children=[alternative_engage, inventory_reallocate])
inventory_reallocate_loop = OperatorPOWL(operator=Operator.LOOP, children=[inventory_reallocate, performance_track])
performance_track_loop = OperatorPOWL(operator=Operator.LOOP, children=[performance_track, feedback_loop])
feedback_loop_loop = OperatorPOWL(operator=Operator.LOOP, children=[feedback_loop, strategy_update])

# Define root
root = StrictPartialOrder(nodes=[demand_forecast, risk_assess, supplier_audit_loop, contract_review_loop, delay_monitor_loop, route_optimize_loop, cost_analyze_loop, compliance_check_loop, alternative_engage_loop, inventory_reallocate_loop, performance_track_loop, feedback_loop_loop])
root.order.add_edge(demand_forecast, risk_assess)
root.order.add_edge(risk_assess, supplier_audit_loop)
root.order.add_edge(supplier_audit_loop, contract_review_loop)
root.order.add_edge(contract_review_loop, delay_monitor_loop)
root.order.add_edge(delay_monitor_loop, route_optimize_loop)
root.order.add_edge(route_optimize_loop, cost_analyze_loop)
root.order.add_edge(cost_analyze_loop, compliance_check_loop)
root.order.add_edge(compliance_check_loop, alternative_engage_loop)
root.order.add_edge(alternative_engage_loop, inventory_reallocate_loop)
root.order.add_edge(inventory_reallocate_loop, performance_track_loop)
root.order.add_edge(performance_track_loop, feedback_loop_loop)
root.order.add_edge(feedback_loop_loop, strategy_update)