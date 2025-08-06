import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
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

# Define silent transitions (if any)
skip = SilentTransition()

# Define partial order nodes
site_survey_to_climate_scan = OperatorPOWL(operator=Operator.XOR, children=[site_survey, climate_scan])
climate_scan_to_module_setup = OperatorPOWL(operator=Operator.XOR, children=[climate_scan, module_setup])
module_setup_to_crop_choice = OperatorPOWL(operator=Operator.XOR, children=[module_setup, crop_choice])
crop_choice_to_nutrient_feed = OperatorPOWL(operator=Operator.XOR, children=[crop_choice, nutrient_feed])
nutrient_feed_to_pest_control = OperatorPOWL(operator=Operator.XOR, children=[nutrient_feed, pest_control])
pest_control_to_energy_audit = OperatorPOWL(operator=Operator.XOR, children=[pest_control, energy_audit])
energy_audit_to_waste_cycle = OperatorPOWL(operator=Operator.XOR, children=[energy_audit, waste_cycle])
waste_cycle_to_growth_track = OperatorPOWL(operator=Operator.XOR, children=[waste_cycle, growth_track])
growth_track_to_demand_plan = OperatorPOWL(operator=Operator.XOR, children=[growth_track, demand_plan])
demand_plan_to_community_link = OperatorPOWL(operator=Operator.XOR, children=[demand_plan, community_link])
community_link_to_regulation_check = OperatorPOWL(operator=Operator.XOR, children=[community_link, regulation_check])
regulation_check_to_supply_sync = OperatorPOWL(operator=Operator.XOR, children=[regulation_check, supply_sync])
supply_sync_to_system_upgrade = OperatorPOWL(operator=Operator.XOR, children=[supply_sync, system_upgrade])
system_upgrade_to_data_backup = OperatorPOWL(operator=Operator.XOR, children=[system_upgrade, data_backup])

# Define the root partial order
root = StrictPartialOrder(nodes=[
    site_survey_to_climate_scan,
    climate_scan_to_module_setup,
    module_setup_to_crop_choice,
    crop_choice_to_nutrient_feed,
    nutrient_feed_to_pest_control,
    pest_control_to_energy_audit,
    energy_audit_to_waste_cycle,
    waste_cycle_to_growth_track,
    growth_track_to_demand_plan,
    demand_plan_to_community_link,
    community_link_to_regulation_check,
    regulation_check_to_supply_sync,
    supply_sync_to_system_upgrade,
    system_upgrade_to_data_backup
])

# Add dependencies between nodes
root.order.add_edge(site_survey_to_climate_scan, climate_scan_to_module_setup)
root.order.add_edge(climate_scan_to_module_setup, module_setup_to_crop_choice)
root.order.add_edge(module_setup_to_crop_choice, crop_choice_to_nutrient_feed)
root.order.add_edge(crop_choice_to_nutrient_feed, nutrient_feed_to_pest_control)
root.order.add_edge(nutrient_feed_to_pest_control, pest_control_to_energy_audit)
root.order.add_edge(pest_control_to_energy_audit, energy_audit_to_waste_cycle)
root.order.add_edge(energy_audit_to_waste_cycle, waste_cycle_to_growth_track)
root.order.add_edge(waste_cycle_to_growth_track, growth_track_to_demand_plan)
root.order.add_edge(growth_track_to_demand_plan, demand_plan_to_community_link)
root.order.add_edge(demand_plan_to_community_link, community_link_to_regulation_check)
root.order.add_edge(community_link_to_regulation_check, regulation_check_to_supply_sync)
root.order.add_edge(regulation_check_to_supply_sync, supply_sync_to_system_upgrade)
root.order.add_edge(supply_sync_to_system_upgrade, system_upgrade_to_data_backup)

# Print the final POWL model
print(root)