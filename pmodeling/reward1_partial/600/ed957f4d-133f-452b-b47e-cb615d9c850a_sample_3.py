import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition

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

# Define the relationships between activities
source_materials_to_vet_suppliers = OperatorPOWL(operator=Operator.XOR, children=[source_materials, vet_suppliers])
vet_suppliers_to_design_modules = OperatorPOWL(operator=Operator.XOR, children=[vet_suppliers, design_modules])
design_modules_to_prototype_build = OperatorPOWL(operator=Operator.XOR, children=[design_modules, prototype_build])
prototype_build_to_test_durability = OperatorPOWL(operator=Operator.XOR, children=[prototype_build, test_durability])
test_durability_to_secure_permits = OperatorPOWL(operator=Operator.XOR, children=[test_durability, secure_permits])
secure_permits_to_map_habitats = OperatorPOWL(operator=Operator.XOR, children=[secure_permits, map_habitats])
map_habitats_to_micro_warehouse = OperatorPOWL(operator=Operator.XOR, children=[map_habitats, micro_warehouse])
micro_warehouse_to_inventory_sync = OperatorPOWL(operator=Operator.XOR, children=[micro_warehouse, inventory_sync])
inventory_sync_to_pack_sustainably = OperatorPOWL(operator=Operator.XOR, children=[inventory_sync, pack_sustainably])
pack_sustainably_to_route_optimize = OperatorPOWL(operator=Operator.XOR, children=[pack_sustainably, route_optimize])
route_optimize_to_engage_community = OperatorPOWL(operator=Operator.XOR, children=[route_optimize, engage_community])
engage_community_to_collect_feedback = OperatorPOWL(operator=Operator.XOR, children=[engage_community, collect_feedback])
collect_feedback_to_adjust_production = OperatorPOWL(operator=Operator.XOR, children=[collect_feedback, adjust_production])
adjust_production_to_partner_ngos = OperatorPOWL(operator=Operator.XOR, children=[adjust_production, partner_ngos])
partner_ngos_to_launch_campaign = OperatorPOWL(operator=Operator.XOR, children=[partner_ngos, launch_campaign])
launch_campaign_to_monitor_sensors = OperatorPOWL(operator=Operator.XOR, children=[launch_campaign, monitor_sensors])
monitor_sensors_to_report_impact = OperatorPOWL(operator=Operator.XOR, children=[monitor_sensors, report_impact])

# Create a StrictPartialOrder to represent the overall process flow
root = StrictPartialOrder(nodes=[source_materials_to_vet_suppliers, vet_suppliers_to_design_modules, design_modules_to_prototype_build, prototype_build_to_test_durability, test_durability_to_secure_permits, secure_permits_to_map_habitats, map_habitats_to_micro_warehouse, micro_warehouse_to_inventory_sync, inventory_sync_to_pack_sustainably, pack_sustainably_to_route_optimize, route_optimize_to_engage_community, engage_community_to_collect_feedback, collect_feedback_to_adjust_production, adjust_production_to_partner_ngos, partner_ngos_to_launch_campaign, launch_campaign_to_monitor_sensors, monitor_sensors_to_report_impact])