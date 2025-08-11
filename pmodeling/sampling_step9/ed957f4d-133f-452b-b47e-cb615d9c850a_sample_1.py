import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
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

# Define the relationships between activities
exclusive_choice1 = OperatorPOWL(operator=Operator.XOR, children=[vet_suppliers, source_materials])
exclusive_choice2 = OperatorPOWL(operator=Operator.XOR, children=[design_modules, exclusive_choice1])
exclusive_choice3 = OperatorPOWL(operator=Operator.XOR, children=[prototype_build, exclusive_choice2])
exclusive_choice4 = OperatorPOWL(operator=Operator.XOR, children=[test_durability, exclusive_choice3])
exclusive_choice5 = OperatorPOWL(operator=Operator.XOR, children=[secure_permits, exclusive_choice4])
exclusive_choice6 = OperatorPOWL(operator=Operator.XOR, children=[map_habitats, exclusive_choice5])
exclusive_choice7 = OperatorPOWL(operator=Operator.XOR, children=[micro_warehouse, exclusive_choice6])
exclusive_choice8 = OperatorPOWL(operator=Operator.XOR, children=[inventory_sync, exclusive_choice7])
exclusive_choice9 = OperatorPOWL(operator=Operator.XOR, children=[pack_sustainably, exclusive_choice8])
exclusive_choice10 = OperatorPOWL(operator=Operator.XOR, children=[route_optimize, exclusive_choice9])
exclusive_choice11 = OperatorPOWL(operator=Operator.XOR, children=[engage_community, exclusive_choice10])
exclusive_choice12 = OperatorPOWL(operator=Operator.XOR, children=[collect_feedback, exclusive_choice11])
exclusive_choice13 = OperatorPOWL(operator=Operator.XOR, children=[adjust_production, exclusive_choice12])
exclusive_choice14 = OperatorPOWL(operator=Operator.XOR, children=[partner_ngos, exclusive_choice13])
exclusive_choice15 = OperatorPOWL(operator=Operator.XOR, children=[launch_campaign, exclusive_choice14])
exclusive_choice16 = OperatorPOWL(operator=Operator.XOR, children=[monitor_sensors, exclusive_choice15])
exclusive_choice17 = OperatorPOWL(operator=Operator.XOR, children=[report_impact, exclusive_choice16])

# Define the loop node
loop_node = OperatorPOWL(operator=Operator.LOOP, children=[exclusive_choice17])

# Define the root
root = StrictPartialOrder(nodes=[loop_node])

# Define the order of execution
root.order.add_edge(loop_node, exclusive_choice17)

# Print the root
print(root)