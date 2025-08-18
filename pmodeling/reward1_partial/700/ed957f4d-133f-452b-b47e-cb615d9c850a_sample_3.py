from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define the transitions (activities) in the POWL model
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

# Define the control-flow operators
xor = OperatorPOWL(operator=Operator.XOR, children=[source_materials, vet_suppliers])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[design_modules, prototype_build, test_durability, secure_permits])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[map_habitats, micro_warehouse, inventory_sync])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[pack_sustainably, route_optimize, engage_community, collect_feedback])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[adjust_production, partner_ngo, launch_campaign])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[monitor_sensors, report_impact])

# Define the partial order
root = StrictPartialOrder(nodes=[xor, xor2, xor3, xor4, xor5, xor6])

# Define the dependencies between nodes
root.order.add_edge(xor, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, xor5)
root.order.add_edge(xor5, xor6)

# Print the final POWL model
print(root)