import pm4py
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

# Define the partial order
root = StrictPartialOrder(nodes=[
    demand_forecast, risk_assess, supplier_audit, inventory_scan, route_optimize, order_prioritize,
    contract_review, delay_monitor, shipment_reroute, cost_analyze, compliance_check, alternative_engage,
    inventory_reallocate, performance_track, feedback_loop, strategy_update
])

# Define dependencies
root.order.add_edge(demand_forecast, risk_assess)
root.order.add_edge(demand_forecast, supplier_audit)
root.order.add_edge(demand_forecast, inventory_scan)
root.order.add_edge(demand_forecast, route_optimize)
root.order.add_edge(demand_forecast, order_prioritize)
root.order.add_edge(demand_forecast, contract_review)
root.order.add_edge(demand_forecast, delay_monitor)
root.order.add_edge(demand_forecast, shipment_reroute)
root.order.add_edge(demand_forecast, cost_analyze)
root.order.add_edge(demand_forecast, compliance_check)
root.order.add_edge(demand_forecast, alternative_engage)
root.order.add_edge(demand_forecast, inventory_reallocate)
root.order.add_edge(demand_forecast, performance_track)
root.order.add_edge(demand_forecast, feedback_loop)
root.order.add_edge(demand_forecast, strategy_update)

# Print the root of the POWL model
print(root)