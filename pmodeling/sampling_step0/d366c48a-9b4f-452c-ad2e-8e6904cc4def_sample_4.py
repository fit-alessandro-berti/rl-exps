import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
site_survey = Transition(label='Site Survey')
climate_scan = Transition(label='Climate Scan')
module_setup = Transition(label='Module Setup')
crop_choice = Transition(label='Crop Choice')
nutrient_feed = Transition(label='Nutrient Feed')
pest_control = Transition(label='Pest Control')
energy_audit = Transition(label='Energy Audit')
waste_cycle = Transition(label='Waste Cycle')
growth_track = Transition(label='Growth Track')
demand_plan = Transition(label='Demand Plan')
community_link = Transition(label='Community Link')
regulation_check = Transition(label='Regulation Check')
supply_sync = Transition(label='Supply Sync')
system_upgrade = Transition(label='System Upgrade')
data_backup = Transition(label='Data Backup')
skip = SilentTransition()

# Define the process tree
site_survey_tree = OperatorPOWL(operator=Operator.PO, children=[climate_scan])
climate_scan_tree = OperatorPOWL(operator=Operator.XOR, children=[module_setup, skip])
module_setup_tree = OperatorPOWL(operator=Operator.XOR, children=[crop_choice, skip])
crop_choice_tree = OperatorPOWL(operator=Operator.XOR, children=[nutrient_feed, skip])
nutrient_feed_tree = OperatorPOWL(operator=Operator.XOR, children=[pest_control, skip])
pest_control_tree = OperatorPOWL(operator=Operator.XOR, children=[energy_audit, skip])
energy_audit_tree = OperatorPOWL(operator=Operator.XOR, children=[waste_cycle, skip])
waste_cycle_tree = OperatorPOWL(operator=Operator.XOR, children=[growth_track, skip])
growth_track_tree = OperatorPOWL(operator=Operator.XOR, children=[demand_plan, skip])
demand_plan_tree = OperatorPOWL(operator=Operator.XOR, children=[community_link, skip])
community_link_tree = OperatorPOWL(operator=Operator.XOR, children=[regulation_check, skip])
regulation_check_tree = OperatorPOWL(operator=Operator.XOR, children=[supply_sync, skip])
supply_sync_tree = OperatorPOWL(operator=Operator.XOR, children=[system_upgrade, skip])
system_upgrade_tree = OperatorPOWL(operator=Operator.XOR, children=[data_backup, skip])

# Define the partial order
root = StrictPartialOrder(nodes=[site_survey_tree, climate_scan_tree, module_setup_tree, crop_choice_tree, nutrient_feed_tree, pest_control_tree, energy_audit_tree, waste_cycle_tree, growth_track_tree, demand_plan_tree, community_link_tree, regulation_check_tree, supply_sync_tree, system_upgrade_tree, data_backup_tree])
root.order.add_edge(site_survey_tree, climate_scan_tree)
root.order.add_edge(climate_scan_tree, module_setup_tree)
root.order.add_edge(module_setup_tree, crop_choice_tree)
root.order.add_edge(crop_choice_tree, nutrient_feed_tree)
root.order.add_edge(nutrient_feed_tree, pest_control_tree)
root.order.add_edge(pest_control_tree, energy_audit_tree)
root.order.add_edge(energy_audit_tree, waste_cycle_tree)
root.order.add_edge(waste_cycle_tree, growth_track_tree)
root.order.add_edge(growth_track_tree, demand_plan_tree)
root.order.add_edge(demand_plan_tree, community_link_tree)
root.order.add_edge(community_link_tree, regulation_check_tree)
root.order.add_edge(regulation_check_tree, supply_sync_tree)
root.order.add_edge(supply_sync_tree, system_upgrade_tree)
root.order.add_edge(system_upgrade_tree, data_backup_tree)

# Print the root
print(root)