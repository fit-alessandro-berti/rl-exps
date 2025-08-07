import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
demand_forecast    = Transition(label='Demand Forecast')
risk_assess        = Transition(label='Risk Assess')
supplier_audit     = Transition(label='Supplier Audit')
inventory_scan     = Transition(label='Inventory Scan')
contract_review    = Transition(label='Contract Review')
delay_monitor      = Transition(label='Delay Monitor')
route_optimize     = Transition(label='Route Optimize')
order_prioritize   = Transition(label='Order Prioritize')
shipment_reroute   = Transition(label='Shipment Reroute')
cost_analyze       = Transition(label='Cost Analyze')
compliance_check   = Transition(label='Compliance Check')
alternative_engage = Transition(label='Alternative Engage')
inventory_realloc  = Transition(label='Inventory Reallocate')
performance_track  = Transition(label='Performance Track')
feedback_loop      = Transition(label='Feedback Loop')
strategy_update    = Transition(label='Strategy Update')

# Define the core update loop: 
#   1. Delay Monitor (monitoring for disruptions)
#   2. Route Optimize (adjusting routes)
#   3. Order Prioritize (re-prioritizing orders)
#   4. Shipment Reroute (rerouting shipments)
#   5. Cost Analyze (evaluating costs)
#   6. Compliance Check (complying with regulations)
#   7. Alternative Engage (engaging with alternatives)
#   8. Inventory Reallocate (re-allocating inventory)
#   9. Performance Track (tracking performance)
# 10. Feedback Loop (capturing feedback for strategy update)

# Build the inner partial order for one iteration of the loop
inner_po = StrictPartialOrder(nodes=[
    delay_monitor,
    route_optimize,
    order_prioritize,
    shipment_reroute,
    cost_analyze,
    compliance_check,
    alternative_engage,
    inventory_realloc,
    performance_track
])
inner_po.order.add_edge(delay_monitor, route_optimize)
inner_po.order.add_edge(route_optimize, order_prioritize)
inner_po.order.add_edge(order_prioritize, shipment_reroute)
inner_po.order.add_edge(shipment_reroute, cost_analyze)
inner_po.order.add_edge(cost_analyze, compliance_check)
inner_po.order.add_edge(compliance_check, alternative_engage)
inner_po.order.add_edge(alternative_engage, inventory_realloc)
inner_po.order.add_edge(inventory_realloc, performance_track)

# Define the LOOP operator: execute the inner partial order, then optionally repeat
loop = OperatorPOWL(operator=Operator.LOOP, children=[inner_po, feedback_loop])

# Build the overall partial order with the initial setup followed by the loop
root = StrictPartialOrder(nodes=[
    demand_forecast,
    risk_assess,
    supplier_audit,
    inventory_scan,
    contract_review,
    loop,
    feedback_loop,
    strategy_update
])
root.order.add_edge(demand_forecast, risk_assess)
root.order.add_edge(risk_assess, supplier_audit)
root.order.add_edge(supplier_audit, inventory_scan)
root.order.add_edge(inventory_scan, contract_review)
root.order.add_edge(contract_review, loop)
root.order.add_edge(loop, feedback_loop)
root.order.add_edge(feedback_loop, strategy_update)