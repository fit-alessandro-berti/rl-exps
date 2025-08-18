import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
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

# Define partial order nodes
partial_order = StrictPartialOrder(nodes=[source_materials, vet_suppliers, design_modules, prototype_build, test_durability, secure_permits, map_habitats, micro_warehouse, inventory_sync, pack_sustainably, route_optimize, engage_community, collect_feedback, adjust_production, partner_ngos, launch_campaign, monitor_sensors, report_impact])

# Define dependencies between nodes
partial_order.order.add_edge(source_materials, vet_suppliers)
partial_order.order.add_edge(vet_suppliers, design_modules)
partial_order.order.add_edge(design_modules, prototype_build)
partial_order.order.add_edge(prototype_build, test_durability)
partial_order.order.add_edge(test_durability, secure_permits)
partial_order.order.add_edge(secure_permits, map_habitats)
partial_order.order.add_edge(map_habitats, micro_warehouse)
partial_order.order.add_edge(micro_warehouse, inventory_sync)
partial_order.order.add_edge(inventory_sync, pack_sustainably)
partial_order.order.add_edge(pack_sustainably, route_optimize)
partial_order.order.add_edge(route_optimize, engage_community)
partial_order.order.add_edge(engage_community, collect_feedback)
partial_order.order.add_edge(collect_feedback, adjust_production)
partial_order.order.add_edge(adjust_production, partner_ngos)
partial_order.order.add_edge(partner_ngos, launch_campaign)
partial_order.order.add_edge(launch_campaign, monitor_sensors)
partial_order.order.add_edge(monitor_sensors, report_impact)

# Set 'root' variable to the partial order model
root = partial_order