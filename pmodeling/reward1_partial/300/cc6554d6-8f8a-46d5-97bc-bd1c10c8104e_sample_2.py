import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions (activities)
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

# Define loops and choices
loop_1 = OperatorPOWL(operator=Operator.LOOP, children=[delay_monitor, inventory_scan])
loop_2 = OperatorPOWL(operator=Operator.LOOP, children=[route_optimize, order_prioritize])
loop_3 = OperatorPOWL(operator=Operator.LOOP, children=[supplier_audit, contract_review])
loop_4 = OperatorPOWL(operator=Operator.LOOP, children=[shipment_reroute, cost_analyze])
loop_5 = OperatorPOWL(operator=Operator.LOOP, children=[compliance_check, alternative_engage])
loop_6 = OperatorPOWL(operator=Operator.LOOP, children=[inventory_reallocate, performance_track])

xor_1 = OperatorPOWL(operator=Operator.XOR, children=[loop_1, loop_2])
xor_2 = OperatorPOWL(operator=Operator.XOR, children=[loop_3, loop_4])
xor_3 = OperatorPOWL(operator=Operator.XOR, children=[loop_5, loop_6])

root = StrictPartialOrder(nodes=[demand_forecast, risk_assess, xor_1, xor_2, xor_3, feedback_loop, strategy_update])
root.order.add_edge(demand_forecast, xor_1)
root.order.add_edge(risk_assess, xor_2)
root.order.add_edge(xor_1, xor_3)
root.order.add_edge(xor_2, feedback_loop)
root.order.add_edge(xor_3, strategy_update)