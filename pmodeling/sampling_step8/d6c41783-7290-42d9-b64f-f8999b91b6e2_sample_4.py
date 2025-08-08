from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions
q_model = Transition(label='Quantum Modeling')
data_enc = Transition(label='Data Encoding')
route_sim = Transition(label='Route Simulation')
demand_f = Transition(label='Demand Forecast')
sup_sync = Transition(label='Supplier Sync')
ent_nodes = Transition(label='Entangle Nodes')
risk_an = Transition(label='Risk Analysis')
inv_scan = Transition(label='Inventory Scan')
lat_check = Transition(label='Latency Check')
transport_p = Transition(label='Transport Plan')
quant_com = Transition(label='Quantum Compute')
scenario_t = Transition(label='Scenario Test')
res_align = Transition(label='Resource Align')
proto_upd = Transition(label='Protocol Update')
feedback_l = Transition(label='Feedback Loop')
cost_opt = Transition(label='Cost Optimize')
impact_rev = Transition(label='Impact Review')

# Define partial order
root = StrictPartialOrder(nodes=[q_model, data_enc, route_sim, demand_f, sup_sync, ent_nodes, risk_an, inv_scan, lat_check, transport_p, quant_com, scenario_t, res_align, proto_upd, feedback_l, cost_opt, impact_rev])

# Define order dependencies
root.order.add_edge(q_model, data_enc)
root.order.add_edge(data_enc, route_sim)
root.order.add_edge(route_sim, demand_f)
root.order.add_edge(demand_f, sup_sync)
root.order.add_edge(sup_sync, ent_nodes)
root.order.add_edge(ent_nodes, risk_an)
root.order.add_edge(risk_an, inv_scan)
root.order.add_edge(inv_scan, lat_check)
root.order.add_edge(lat_check, transport_p)
root.order.add_edge(transport_p, quant_com)
root.order.add_edge(quant_com, scenario_t)
root.order.add_edge(scenario_t, res_align)
root.order.add_edge(res_align, proto_upd)
root.order.add_edge(proto_upd, feedback_l)
root.order.add_edge(feedback_l, cost_opt)
root.order.add_edge(cost_opt, impact_rev)

print(root)