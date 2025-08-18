import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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

xor1 = OperatorPOWL(operator=Operator.XOR, children=[delay_monitor, alternative_engage])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[compliance_check, feedback_loop])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[inventory_reallocate, strategy_update])
loop = OperatorPOWL(operator=Operator.LOOP, children=[risk_assess, supplier_audit, inventory_scan, route_optimize, order_prioritize, contract_review, xor1, xor2, xor3])

root = StrictPartialOrder(nodes=[demand_forecast, loop])
root.order.add_edge(demand_forecast, loop)

print(root)