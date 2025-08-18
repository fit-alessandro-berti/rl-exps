import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
source_materials = Transition(label='Source Materials')
vet_suppliers = Transition(label='Vet Suppliers')
design_modules = Transition(label='Design Modules')
prototype_build = Transition(label='Prototype Build')
test_durability = Transition(label='Test Durability')
secure_permits = Transition(label='Secure Permits')
map_habitats = Transition(label='Map Habitats')
micro_warehouse = Transition(label='Micro Warehouse')
inventory_sync = Transition(label='Inventory Sync')
pack_sustainably = Transition(label='Pack Sustainably')
route_optimize = Transition(label='Route Optimize')
engage_community = Transition(label='Engage Community')
collect_feedback = Transition(label='Collect Feedback')
adjust_production = Transition(label='Adjust Production')
partner_ngo = Transition(label='Partner NGOs')
launch_campaign = Transition(label='Launch Campaign')
monitor_sensors = Transition(label='Monitor Sensors')
report_impact = Transition(label='Report Impact')

# Define choices and loops
vet_and_design = OperatorPOWL(operator=Operator.XOR, children=[vet_suppliers, design_modules])
build_and_test = OperatorPOWL(operator=Operator.XOR, children=[prototype_build, test_durability])
secure_and_map = OperatorPOWL(operator=Operator.XOR, children=[secure_permits, map_habitats])
micro_warehouse_loop = OperatorPOWL(operator=Operator.LOOP, children=[micro_warehouse, inventory_sync])
pack_and_optimize = OperatorPOWL(operator=Operator.XOR, children=[pack_sustainably, route_optimize])
engage_and_collect = OperatorPOWL(operator=Operator.XOR, children=[engage_community, collect_feedback])
adjust_and_partners = OperatorPOWL(operator=Operator.XOR, children=[adjust_production, partner_ngo])
launch_and_monitor = OperatorPOWL(operator=Operator.XOR, children=[launch_campaign, monitor_sensors])
report_and_impact = OperatorPOWL(operator=Operator.XOR, children=[report_impact])

# Define the partial order
root = StrictPartialOrder(nodes=[
    vet_and_design,
    build_and_test,
    secure_and_map,
    micro_warehouse_loop,
    pack_and_optimize,
    engage_and_collect,
    adjust_and_partners,
    launch_and_monitor,
    report_and_impact
])

# Add edges
root.order.add_edge(vet_and_design, build_and_test)
root.order.add_edge(build_and_test, secure_and_map)
root.order.add_edge(secure_and_map, micro_warehouse_loop)
root.order.add_edge(micro_warehouse_loop, pack_and_optimize)
root.order.add_edge(pack_and_optimize, engage_and_collect)
root.order.add_edge(engage_and_collect, adjust_and_partners)
root.order.add_edge(adjust_and_partners, launch_and_monitor)
root.order.add_edge(launch_and_monitor, report_and_impact)

print(root)