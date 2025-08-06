import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
site_survey = Transition(label='Site Survey')
permit_review = Transition(label='Permit Review')
design_layout = Transition(label='Design Layout')
system_assembly = Transition(label='System Assembly')
climate_setup = Transition(label='Climate Setup')
nutrient_prep = Transition(label='Nutrient Prep')
irrigation_test = Transition(label='Irrigation Test')
lighting_config = Transition(label='Lighting Config')
energy_install = Transition(label='Energy Install')
sensor_setup = Transition(label='Sensor Setup')
automation_deploy = Transition(label='Automation Deploy')
crop_seeding = Transition(label='Crop Seeding')
waste_plan = Transition(label='Waste Plan')
staff_training = Transition(label='Staff Training')
community_outreach = Transition(label='Community Outreach')
yield_monitor = Transition(label='Yield Monitor')
maintenance_check = Transition(label='Maintenance Check')

# Define silent transitions
skip = SilentTransition()

# Define exclusive choice for permit review and site survey
permit_review_xor_site_survey = OperatorPOWL(operator=Operator.XOR, children=[permit_review, site_survey])

# Define exclusive choice for design layout and system assembly
design_layout_xor_system_assembly = OperatorPOWL(operator=Operator.XOR, children=[design_layout, system_assembly])

# Define exclusive choice for climate setup and nutrient prep
climate_setup_xor_nutrient_prep = OperatorPOWL(operator=Operator.XOR, children=[climate_setup, nutrient_prep])

# Define exclusive choice for irrigation test and lighting config
irrigation_test_xor_lighting_config = OperatorPOWL(operator=Operator.XOR, children=[irrigation_test, lighting_config])

# Define exclusive choice for energy install and sensor setup
energy_install_xor_sensor_setup = OperatorPOWL(operator=Operator.XOR, children=[energy_install, sensor_setup])

# Define exclusive choice for automation deploy and crop seeding
automation_deploy_xor_crop_seeding = OperatorPOWL(operator=Operator.XOR, children=[automation_deploy, crop_seeding])

# Define exclusive choice for waste plan and staff training
waste_plan_xor_staff_training = OperatorPOWL(operator=Operator.XOR, children=[waste_plan, staff_training])

# Define exclusive choice for community outreach and yield monitor
community_outreach_xor_yield_monitor = OperatorPOWL(operator=Operator.XOR, children=[community_outreach, yield_monitor])

# Define exclusive choice for maintenance check
maintenance_check_xor = OperatorPOWL(operator=Operator.XOR, children=[maintenance_check])

# Define loop for maintenance check
maintenance_check_loop = OperatorPOWL(operator=Operator.LOOP, children=[maintenance_check_xor])

# Define exclusive choice for maintenance check loop and community outreach or yield monitor
maintenance_check_loop_xor_community_outreach_yield_monitor = OperatorPOWL(operator=Operator.XOR, children=[maintenance_check_loop, community_outreach_xor_yield_monitor])

# Define root POWL model
root = StrictPartialOrder(nodes=[permit_review_xor_site_survey, design_layout_xor_system_assembly, climate_setup_xor_nutrient_prep, irrigation_test_xor_lighting_config, energy_install_xor_sensor_setup, automation_deploy_xor_crop_seeding, waste_plan_xor_staff_training, maintenance_check_loop_xor_community_outreach_yield_monitor])
root.order.add_edge(permit_review_xor_site_survey, design_layout_xor_system_assembly)
root.order.add_edge(design_layout_xor_system_assembly, climate_setup_xor_nutrient_prep)
root.order.add_edge(climate_setup_xor_nutrient_prep, irrigation_test_xor_lighting_config)
root.order.add_edge(irrigation_test_xor_lighting_config, energy_install_xor_sensor_setup)
root.order.add_edge(energy_install_xor_sensor_setup, automation_deploy_xor_crop_seeding)
root.order.add_edge(automation_deploy_xor_crop_seeding, waste_plan_xor_staff_training)
root.order.add_edge(waste_plan_xor_staff_training, maintenance_check_loop_xor_community_outreach_yield_monitor)