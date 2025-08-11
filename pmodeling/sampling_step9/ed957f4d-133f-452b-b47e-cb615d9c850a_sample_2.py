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

# Define the silent activities
skip = SilentTransition()

# Define the loops and exclusive choices
loop_design = OperatorPOWL(operator=Operator.LOOP, children=[design_modules, prototype_build, test_durability])
loop_inventory = OperatorPOWL(operator=Operator.LOOP, children=[inventory_sync, pack_sustainably, route_optimize])
loop_engage = OperatorPOWL(operator=Operator.LOOP, children=[engage_community, collect_feedback, adjust_production])
loop_monitor = OperatorPOWL(operator=Operator.LOOP, children=[monitor_sensors, report_impact])

# Define the partial order
root = StrictPartialOrder(nodes=[source_materials, vet_suppliers, loop_design, loop_inventory, loop_engage, loop_monitor, secure_permits, map_habitats, micro_warehouse, partner_ngos, launch_campaign])

# Define the order
root.order.add_edge(source_materials, vet_suppliers)
root.order.add_edge(vet_suppliers, loop_design)
root.order.add_edge(loop_design, loop_inventory)
root.order.add_edge(loop_inventory, loop_engage)
root.order.add_edge(loop_engage, loop_monitor)
root.order.add_edge(loop_monitor, secure_permits)
root.order.add_edge(secure_permits, map_habitats)
root.order.add_edge(map_habitats, micro_warehouse)
root.order.add_edge(micro_warehouse, partner_ngos)
root.order.add_edge(partner_ngos, launch_campaign)

print(root)