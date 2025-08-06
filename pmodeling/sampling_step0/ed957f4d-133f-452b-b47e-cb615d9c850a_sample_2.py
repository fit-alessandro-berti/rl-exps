import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
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
partner_ngos = Transition(label='Partner NGOs')
launch_campaign = Transition(label='Launch Campaign')
monitor_sensors = Transition(label='Monitor Sensors')
report_impact = Transition(label='Report Impact')

# Define the choices and loops
vet_and_design = OperatorPOWL(operator=Operator.XOR, children=[vet_suppliers, design_modules])
prototype_and_test = OperatorPOWL(operator=Operator.XOR, children=[prototype_build, test_durability])
permits_and_habitats = OperatorPOWL(operator=Operator.XOR, children=[secure_permits, map_habitats])
micro_warehouse_loop = OperatorPOWL(operator=Operator.LOOP, children=[micro_warehouse])
inventory_sync_loop = OperatorPOWL(operator=Operator.LOOP, children=[inventory_sync])
pack_sustainably_loop = OperatorPOWL(operator=Operator.LOOP, children=[pack_sustainably])
route_optimize_loop = OperatorPOWL(operator=Operator.LOOP, children=[route_optimize])
engage_community_loop = OperatorPOWL(operator=Operator.LOOP, children=[engage_community])
collect_feedback_loop = OperatorPOWL(operator=Operator.LOOP, children=[collect_feedback])
adjust_production_loop = OperatorPOWL(operator=Operator.LOOP, children=[adjust_production])
partner_ngos_loop = OperatorPOWL(operator=Operator.LOOP, children=[partner_ngos])
launch_campaign_loop = OperatorPOWL(operator=Operator.LOOP, children=[launch_campaign])
monitor_sensors_loop = OperatorPOWL(operator=Operator.LOOP, children=[monitor_sensors])
report_impact_loop = OperatorPOWL(operator=Operator.LOOP, children=[report_impact])

# Define the partial order
root = StrictPartialOrder(nodes=[
    vet_and_design,
    prototype_and_test,
    permits_and_habitats,
    micro_warehouse_loop,
    inventory_sync_loop,
    pack_sustainably_loop,
    route_optimize_loop,
    engage_community_loop,
    collect_feedback_loop,
    adjust_production_loop,
    partner_ngos_loop,
    launch_campaign_loop,
    monitor_sensors_loop,
    report_impact_loop,
    source_materials
])

# Define the dependencies
root.order.add_edge(vet_and_design, prototype_and_test)
root.order.add_edge(prototype_and_test, permits_and_habitats)
root.order.add_edge(permits_and_habitats, micro_warehouse_loop)
root.order.add_edge(micro_warehouse_loop, inventory_sync_loop)
root.order.add_edge(inventory_sync_loop, pack_sustainably_loop)
root.order.add_edge(pack_sustainably_loop, route_optimize_loop)
root.order.add_edge(route_optimize_loop, engage_community_loop)
root.order.add_edge(engage_community_loop, collect_feedback_loop)
root.order.add_edge(collect_feedback_loop, adjust_production_loop)
root.order.add_edge(adjust_production_loop, partner_ngos_loop)
root.order.add_edge(partner_ngos_loop, launch_campaign_loop)
root.order.add_edge(launch_campaign_loop, monitor_sensors_loop)
root.order.add_edge(monitor_sensors_loop, report_impact_loop)
root.order.add_edge(report_impact_loop, source_materials)

print(root)