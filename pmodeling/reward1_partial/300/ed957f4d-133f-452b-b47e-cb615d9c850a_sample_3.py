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

# Define the loop for micro-warehousing and inventory syncing
micro_warehousing_loop = OperatorPOWL(operator=Operator.LOOP, children=[micro_warehouse, inventory_sync])

# Define the exclusive choice for micro-warehousing or engaging the community
micro_warehousing_or_community = OperatorPOWL(operator=Operator.XOR, children=[micro_warehousing_loop, engage_community])

# Define the exclusive choice for adjusting production or partnering with NGOs
adjust_production_or_partnership = OperatorPOWL(operator=Operator.XOR, children=[adjust_production, partner_ngos])

# Define the process as a strict partial order
root = StrictPartialOrder(nodes=[
    source_materials, vet_suppliers, design_modules, prototype_build, test_durability, secure_permits, 
    map_habitats, micro_warehousing_or_community, collect_feedback, adjust_production_or_partnership, 
    launch_campaign, monitor_sensors, report_impact])

# Define the order of execution
root.order.add_edge(source_materials, vet_suppliers)
root.order.add_edge(vet_suppliers, design_modules)
root.order.add_edge(design_modules, prototype_build)
root.order.add_edge(prototype_build, test_durability)
root.order.add_edge(test_durability, secure_permits)
root.order.add_edge(secure_permits, map_habitats)
root.order.add_edge(map_habitats, micro_warehousing_or_community)
root.order.add_edge(micro_warehousing_or_community, collect_feedback)
root.order.add_edge(collect_feedback, adjust_production_or_partnership)
root.order.add_edge(adjust_production_or_partnership, launch_campaign)
root.order.add_edge(launch_campaign, monitor_sensors)
root.order.add_edge(monitor_sensors, report_impact)

# Print the root node
print(root)