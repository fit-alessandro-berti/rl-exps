import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
qm_model = Transition(label='Quantum Modeling')
data_enc = Transition(label='Data Encoding')
route_sim = Transition(label='Route Simulation')
demand_f = Transition(label='Demand Forecast')
supplier_sync = Transition(label='Supplier Sync')
entangle_nodes = Transition(label='Entangle Nodes')
risk_anal = Transition(label='Risk Analysis')
inventory_scan = Transition(label='Inventory Scan')
latency_check = Transition(label='Latency Check')
transport_plan = Transition(label='Transport Plan')
quantum_comp = Transition(label='Quantum Compute')
scenario_test = Transition(label='Scenario Test')
resource_align = Transition(label='Resource Align')
protocol_upd = Transition(label='Protocol Update')
feedback_loop = Transition(label='Feedback Loop')
cost_opt = Transition(label='Cost Optimize')
impact_rev = Transition(label='Impact Review')

# Loop for iterative quantum compute and scenario testing
loop_po = StrictPartialOrder(nodes=[
    quantum_comp, scenario_test, resource_align, protocol_upd, feedback_loop
])
loop_po.order.add_edge(quantum_comp, scenario_test)
loop_po.order.add_edge(scenario_test, resource_align)
loop_po.order.add_edge(resource_align, protocol_upd)
loop_po.order.add_edge(protocol_upd, feedback_loop)
loop_po.order.add_edge(feedback_loop, quantum_comp)

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    qm_model, data_enc, route_sim, demand_f, supplier_sync,
    entangle_nodes, risk_anal, inventory_scan, latency_check,
    transport_plan, loop_po, cost_opt, impact_rev
])

# Define the control-flow dependencies
root.order.add_edge(qm_model, data_enc)
root.order.add_edge(data_enc, route_sim)
root.order.add_edge(route_sim, demand_f)
root.order.add_edge(demand_f, supplier_sync)
root.order.add_edge(supplier_sync, entangle_nodes)
root.order.add_edge(entangle_nodes, risk_anal)
root.order.add_edge(risk_anal, inventory_scan)
root.order.add_edge(inventory_scan, latency_check)
root.order.add_edge(latency_check, transport_plan)
root.order.add_edge(transport_plan, loop_po)
root.order.add_edge(loop_po, cost_opt)
root.order.add_edge(cost_opt, impact_rev)

print(root)