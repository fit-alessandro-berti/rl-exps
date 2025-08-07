import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
demand_forecast   = Transition(label='Demand Forecast')
risk_assess       = Transition(label='Risk Assess')
supplier_audit    = Transition(label='Supplier Audit')
inventory_scan    = Transition(label='Inventory Scan')
route_optimize    = Transition(label='Route Optimize')
order_prioritize  = Transition(label='Order Prioritize')
contract_review   = Transition(label='Contract Review')
delay_monitor     = Transition(label='Delay Monitor')
shipment_reroute  = Transition(label='Shipment Reroute')
cost_analyze      = Transition(label='Cost Analyze')
compliance_check  = Transition(label='Compliance Check')
alternative_engage= Transition(label='Alternative Engage')
inventory_realloc = Transition(label='Inventory Reallocate')
performance_track = Transition(label='Performance Track')
feedback_loop     = Transition(label='Feedback Loop')
strategy_update   = Transition(label='Strategy Update')

# Define the inner loop body (one cycle of the continuous adjustment cycle)
body = StrictPartialOrder(nodes=[
    delay_monitor,
    shipment_reroute,
    cost_analyze,
    compliance_check,
    alternative_engage,
    inventory_realloc
])
body.order.add_edge(delay_monitor, shipment_reroute)
body.order.add_edge(shipment_reroute, cost_analyze)
body.order.add_edge(cost_analyze, compliance_check)
body.order.add_edge(compliance_check, alternative_engage)
body.order.add_edge(alternative_engage, inventory_realloc)

# Define the LOOP operator: perform the body then optionally repeat
continuous_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[body, feedback_loop]
)

# Assemble the overall partial order
root = StrictPartialOrder(nodes=[
    demand_forecast,
    risk_assess,
    supplier_audit,
    inventory_scan,
    route_optimize,
    order_prioritize,
    contract_review,
    continuous_loop,
    performance_track,
    strategy_update
])

# Define the control-flow dependencies
root.order.add_edge(demand_forecast, risk_assess)
root.order.add_edge(risk_assess, supplier_audit)
root.order.add_edge(supplier_audit, inventory_scan)
root.order.add_edge(inventory_scan, route_optimize)
root.order.add_edge(route_optimize, order_prioritize)
root.order.add_edge(order_prioritize, contract_review)
root.order.add_edge(contract_review, continuous_loop)
root.order.add_edge(continuous_loop, performance_track)
root.order.add_edge(performance_track, strategy_update)