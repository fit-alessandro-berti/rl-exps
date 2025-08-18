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

# Define the POWL operators
xor1 = OperatorPOWL(operator=Operator.XOR, children=[delay_monitor, shipment_reroute])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[cost_analyze, alternative_engage])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[compliance_check, inventory_reallocate])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[performance_track, strategy_update])

# Define the POWL partial order
root = StrictPartialOrder(nodes=[demand_forecast, risk_assess, supplier_audit, inventory_scan, route_optimize, order_prioritize, contract_review, xor1, xor2, xor3, xor4, feedback_loop, strategy_update])

# Define the order dependencies
root.order.add_edge(demand_forecast, risk_assess)
root.order.add_edge(risk_assess, supplier_audit)
root.order.add_edge(supplier_audit, inventory_scan)
root.order.add_edge(inventory_scan, route_optimize)
root.order.add_edge(route_optimize, order_prioritize)
root.order.add_edge(order_prioritize, contract_review)
root.order.add_edge(contract_review, xor1)
root.order.add_edge(xor1, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, feedback_loop)
root.order.add_edge(feedback_loop, strategy_update)