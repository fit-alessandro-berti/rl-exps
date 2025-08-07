import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
qm_model   = Transition(label='Quantum Modeling')
data_enc   = Transition(label='Data Encoding')
route_sim  = Transition(label='Route Simulation')
demand_f   = Transition(label='Demand Forecast')
supply_sync= Transition(label='Supplier Sync')
entangle   = Transition(label='Entangle Nodes')
risk_an    = Transition(label='Risk Analysis')
inventory  = Transition(label='Inventory Scan')
latency    = Transition(label='Latency Check')
transport  = Transition(label='Transport Plan')
quant_comp = Transition(label='Quantum Compute')
scenario   = Transition(label='Scenario Test')
resource   = Transition(label='Resource Align')
protocol   = Transition(label='Protocol Update')
feedback   = Transition(label='Feedback Loop')
cost_opt   = Transition(label='Cost Optimize')
impact_rev = Transition(label='Impact Review')

# Define the loop body (one iteration of the main process)
body = StrictPartialOrder(nodes=[
    demand_f,
    supply_sync,
    entangle,
    risk_an,
    inventory,
    latency,
    transport,
    quant_comp,
    scenario,
    resource,
    protocol,
    feedback,
    cost_opt,
    impact_rev
])
# Sequential execution within one iteration
body.order.add_edge(demand_f, supply_sync)
body.order.add_edge(supply_sync, entangle)
body.order.add_edge(entangle, risk_an)
body.order.add_edge(risk_an, inventory)
body.order.add_edge(inventory, latency)
body.order.add_edge(latency, transport)
body.order.add_edge(transport, quant_comp)
body.order.add_edge(quant_comp, scenario)
body.order.add_edge(scenario, resource)
body.order.add_edge(resource, protocol)
body.order.add_edge(protocol, feedback)
body.order.add_edge(feedback, cost_opt)
body.order.add_edge(cost_opt, impact_rev)

# Loop: do the above body, then optionally do the feedback loop and repeat
loop = OperatorPOWL(operator=Operator.LOOP, children=[body, feedback])

# Assemble the overall partial order
root = StrictPartialOrder(nodes=[qm_model, data_enc, route_sim, loop])
root.order.add_edge(qm_model, data_enc)
root.order.add_edge(data_enc, route_sim)
root.order.add_edge(route_sim, loop)