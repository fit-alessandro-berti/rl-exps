import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

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

# Define the process
loop = OperatorPOWL(operator=Operator.LOOP, children=[secure_permits, vet_suppliers, design_modules, prototype_build, test_durability])
xor1 = OperatorPOWL(operator=Operator.XOR, children=[map_habitats, micro_warehouse])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[inventory_sync, pack_sustainably])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[route_optimize, engage_community])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[collect_feedback, adjust_production])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[partner_ngos, launch_campaign])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[monitor_sensors, report_impact])

root = StrictPartialOrder(nodes=[loop, xor1, xor2, xor3, xor4, xor5, xor6])
root.order.add_edge(loop, xor1)
root.order.add_edge(loop, xor2)
root.order.add_edge(loop, xor3)
root.order.add_edge(loop, xor4)
root.order.add_edge(loop, xor5)
root.order.add_edge(loop, xor6)

print(root)