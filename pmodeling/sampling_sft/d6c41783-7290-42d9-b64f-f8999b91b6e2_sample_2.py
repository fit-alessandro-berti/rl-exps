import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
qm_model = Transition(label='Quantum Modeling')
data_enc = Transition(label='Data Encoding')
route_sim = Transition(label='Route Simulation')
demand_fct = Transition(label='Demand Forecast')
supplier_sync = Transition(label='Supplier Sync')
entangle_nodes = Transition(label='Entangle Nodes')
risk_analysis = Transition(label='Risk Analysis')
inventory_scan = Transition(label='Inventory Scan')
latency_check = Transition(label='Latency Check')
transport_plan = Transition(label='Transport Plan')
quantum_compute = Transition(label='Quantum Compute')
scenario_test = Transition(label='Scenario Test')
resource_align = Transition(label='Resource Align')
protocol_update = Transition(label='Protocol Update')
feedback_loop = Transition(label='Feedback Loop')
cost_optimize = Transition(label='Cost Optimize')
impact_review = Transition(label='Impact Review')

# Loop: Quantum Compute -> Scenario Test, then either exit or do Feedback Loop -> Scenario Test again
loop_body = StrictPartialOrder(nodes=[feedback_loop, scenario_test])
loop_body.order.add_edge(feedback_loop, scenario_test)
quantum_loop = OperatorPOWL(operator=Operator.LOOP, children=[quantum_compute, loop_body])

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    qm_model, data_enc, route_sim, demand_fct, supplier_sync,
    entangle_nodes, risk_analysis, inventory_scan, latency_check,
    transport_plan, quantum_loop, scenario_test, resource_align,
    protocol_update, feedback_loop, cost_optimize, impact_review
])

# Define control-flow dependencies
root.order.add_edge(qm_model, data_enc)
root.order.add_edge(data_enc, route_sim)
root.order.add_edge(route_sim, demand_fct)
root.order.add_edge(demand_fct, supplier_sync)
root.order.add_edge(supplier_sync, entangle_nodes)
root.order.add_edge(entangle_nodes, risk_analysis)
root.order.add_edge(risk_analysis, inventory_scan)
root.order.add_edge(inventory_scan, latency_check)
root.order.add_edge(latency_check, transport_plan)
root.order.add_edge(transport_plan, quantum_loop)
root.order.add_edge(quantum_loop, scenario_test)
root.order.add_edge(scenario_test, resource_align)
root.order.add_edge(resource_align, protocol_update)
root.order.add_edge(protocol_update, feedback_loop)
root.order.add_edge(feedback_loop, scenario_test)
root.order.add_edge(scenario_test, cost_optimize)
root.order.add_edge(cost_optimize, impact_review)