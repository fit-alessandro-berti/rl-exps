import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define each activity as a Transition object
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

# Define the control-flow operators
exclusive_choice = OperatorPOWL(operator=Operator.XOR, children=[vet_suppliers, design_modules, prototype_build, test_durability, secure_permits, map_habitats])
loop = OperatorPOWL(operator=Operator.LOOP, children=[micro_warehouse, inventory_sync, pack_sustainably, route_optimize, engage_community, collect_feedback, adjust_production, partner_ngos, launch_campaign, monitor_sensors, report_impact])

# Create the POWL model
root = StrictPartialOrder(nodes=[source_materials, exclusive_choice, loop])
root.order.add_edge(source_materials, exclusive_choice)
root.order.add_edge(exclusive_choice, loop)

# Print the root of the POWL model
print(root)