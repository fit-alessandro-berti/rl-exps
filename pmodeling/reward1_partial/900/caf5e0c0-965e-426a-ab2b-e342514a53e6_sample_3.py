import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for each activity
site_survey = Transition(label='Site Survey')
system_design = Transition(label='System Design')
climate_sim = Transition(label='Climate Sim')
seed_select = Transition(label='Seed Select')
module_setup = Transition(label='Module Setup')
nutrient_mix = Transition(label='Nutrient Mix')
water_cycle = Transition(label='Water Cycle')
energy_link = Transition(label='Energy Link')
sensor_install = Transition(label='Sensor Install')
pest_detect = Transition(label='Pest Detect')
growth_scan = Transition(label='Growth Scan')
data_sync = Transition(label='Data Sync')
community_meet = Transition(label='Community Meet')
reg_compliance = Transition(label='Reg Compliance')
system_test = Transition(label='System Test')
maintenance_plan = Transition(label='Maintenance Plan')

# Define the transitions as SilentTransitions
skip = SilentTransition()

# Define the process steps using POWL operators
# Site Survey --> System Design --> Climate Sim --> Seed Select --> Module Setup --> Nutrient Mix --> Water Cycle
site_survey_to_system_design = OperatorPOWL(operator=Operator.LOOP, children=[site_survey, system_design])
climate_sim_to_seed_select = OperatorPOWL(operator=Operator.XOR, children=[climate_sim, skip])
seed_select_to_module_setup = OperatorPOWL(operator=Operator.LOOP, children=[seed_select, module_setup])
module_setup_to_nutrient_mix = OperatorPOWL(operator=Operator.LOOP, children=[module_setup, nutrient_mix])
nutrient_mix_to_water_cycle = OperatorPOWL(operator=Operator.LOOP, children=[nutrient_mix, water_cycle])

# Energy Link --> Sensor Install --> Pest Detect --> Growth Scan
energy_link_to_sensor_install = OperatorPOWL(operator=Operator.LOOP, children=[energy_link, sensor_install])
sensor_install_to_pest_detect = OperatorPOWL(operator=Operator.LOOP, children=[sensor_install, pest_detect])
pest_detect_to_growth_scan = OperatorPOWL(operator=Operator.LOOP, children=[pest_detect, growth_scan])

# Data Sync --> Community Meet --> Reg Compliance
data_sync_to_community_meet = OperatorPOWL(operator=Operator.LOOP, children=[data_sync, community_meet])
community_meet_to_reg_compliance = OperatorPOWL(operator=Operator.LOOP, children=[community_meet, reg_compliance])

# System Test --> Maintenance Plan
system_test_to_maintenance_plan = OperatorPOWL(operator=Operator.LOOP, children=[system_test, maintenance_plan])

# Define the root partial order
root = StrictPartialOrder(nodes=[site_survey_to_system_design, climate_sim_to_seed_select, seed_select_to_module_setup, module_setup_to_nutrient_mix, nutrient_mix_to_water_cycle, energy_link_to_sensor_install, sensor_install_to_pest_detect, pest_detect_to_growth_scan, data_sync_to_community_meet, community_meet_to_reg_compliance, system_test_to_maintenance_plan])
root.order.add_edge(site_survey_to_system_design, climate_sim_to_seed_select)
root.order.add_edge(climate_sim_to_seed_select, seed_select_to_module_setup)
root.order.add_edge(seed_select_to_module_setup, module_setup_to_nutrient_mix)
root.order.add_edge(module_setup_to_nutrient_mix, nutrient_mix_to_water_cycle)
root.order.add_edge(nutrient_mix_to_water_cycle, energy_link_to_sensor_install)
root.order.add_edge(energy_link_to_sensor_install, sensor_install_to_pest_detect)
root.order.add_edge(sensor_install_to_pest_detect, pest_detect_to_growth_scan)
root.order.add_edge(pest_detect_to_growth_scan, data_sync_to_community_meet)
root.order.add_edge(data_sync_to_community_meet, community_meet_to_reg_compliance)
root.order.add_edge(community_meet_to_reg_compliance, system_test_to_maintenance_plan)