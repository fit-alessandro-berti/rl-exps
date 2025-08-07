import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for the POWL model
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

# Define the partial order with dependencies
root = StrictPartialOrder(nodes=[source_materials, vet_suppliers, design_modules, prototype_build, test_durability, secure_permits, map_habitats, micro_warehouse, inventory_sync, pack_sustainably, route_optimize, engage_community, collect_feedback, adjust_production, partner_ngos, launch_campaign, monitor_sensors, report_impact])

# Add dependencies
root.order.add_edge(source_materials, vet_suppliers)
root.order.add_edge(source_materials, design_modules)
root.order.add_edge(source_materials, prototype_build)
root.order.add_edge(source_materials, test_durability)
root.order.add_edge(source_materials, secure_permits)
root.order.add_edge(source_materials, map_habitats)
root.order.add_edge(source_materials, micro_warehouse)
root.order.add_edge(source_materials, inventory_sync)
root.order.add_edge(source_materials, pack_sustainably)
root.order.add_edge(source_materials, route_optimize)
root.order.add_edge(source_materials, engage_community)
root.order.add_edge(source_materials, collect_feedback)
root.order.add_edge(source_materials, adjust_production)
root.order.add_edge(source_materials, partner_ngos)
root.order.add_edge(source_materials, launch_campaign)
root.order.add_edge(source_materials, monitor_sensors)
root.order.add_edge(source_materials, report_impact)

# Now 'root' contains the POWL model for the process