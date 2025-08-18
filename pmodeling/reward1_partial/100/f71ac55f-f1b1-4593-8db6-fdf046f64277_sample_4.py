from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities)
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

# Define the silent transitions (for simplicity, we'll assume they are not used in this context)
skip = SilentTransition()

# Define the process tree structure
site_survey_tree = OperatorPOWL(operator=Operator.LOOP, children=[site_survey, permit_review, design_layout])
permit_review_tree = OperatorPOWL(operator=Operator.LOOP, children=[permit_review, design_layout, system_assembly])
design_layout_tree = OperatorPOWL(operator=Operator.LOOP, children=[design_layout, system_assembly, climate_setup])
system_assembly_tree = OperatorPOWL(operator=Operator.LOOP, children=[system_assembly, climate_setup, nutrient_prep])
climate_setup_tree = OperatorPOWL(operator=Operator.LOOP, children=[climate_setup, nutrient_prep, irrigation_test])
nutrient_prep_tree = OperatorPOWL(operator=Operator.LOOP, children=[nutrient_prep, irrigation_test, lighting_config])
irrigation_test_tree = OperatorPOWL(operator=Operator.LOOP, children=[irrigation_test, lighting_config, energy_install])
lighting_config_tree = OperatorPOWL(operator=Operator.LOOP, children=[lighting_config, energy_install, sensor_setup])
energy_install_tree = OperatorPOWL(operator=Operator.LOOP, children=[energy_install, sensor_setup, automation_deploy])
sensor_setup_tree = OperatorPOWL(operator=Operator.LOOP, children=[sensor_setup, automation_deploy, crop_seeding])
automation_deploy_tree = OperatorPOWL(operator=Operator.LOOP, children=[automation_deploy, crop_seeding, waste_plan])
crop_seeding_tree = OperatorPOWL(operator=Operator.LOOP, children=[crop_seeding, waste_plan, staff_training])
waste_plan_tree = OperatorPOWL(operator=Operator.LOOP, children=[waste_plan, staff_training, community_outreach])
staff_training_tree = OperatorPOWL(operator=Operator.LOOP, children=[staff_training, community_outreach, yield_monitor])
community_outreach_tree = OperatorPOWL(operator=Operator.LOOP, children=[community_outreach, yield_monitor, maintenance_check])
yield_monitor_tree = OperatorPOWL(operator=Operator.LOOP, children=[yield_monitor, maintenance_check, skip])
maintenance_check_tree = OperatorPOWL(operator=Operator.LOOP, children=[maintenance_check, skip, skip])

# Create the root Partial Order
root = StrictPartialOrder(nodes=[
    site_survey_tree, permit_review_tree, design_layout_tree, system_assembly_tree, climate_setup_tree,
    nutrient_prep_tree, irrigation_test_tree, lighting_config_tree, energy_install_tree, sensor_setup_tree,
    automation_deploy_tree, crop_seeding_tree, waste_plan_tree, staff_training_tree, community_outreach_tree,
    yield_monitor_tree, maintenance_check_tree
])

# Define the dependencies
root.order.add_edge(site_survey_tree, permit_review_tree)
root.order.add_edge(permit_review_tree, design_layout_tree)
root.order.add_edge(design_layout_tree, system_assembly_tree)
root.order.add_edge(system_assembly_tree, climate_setup_tree)
root.order.add_edge(climate_setup_tree, nutrient_prep_tree)
root.order.add_edge(nutrient_prep_tree, irrigation_test_tree)
root.order.add_edge(irrigation_test_tree, lighting_config_tree)
root.order.add_edge(lighting_config_tree, energy_install_tree)
root.order.add_edge(energy_install_tree, sensor_setup_tree)
root.order.add_edge(sensor_setup_tree, automation_deploy_tree)
root.order.add_edge(automation_deploy_tree, crop_seeding_tree)
root.order.add_edge(crop_seeding_tree, waste_plan_tree)
root.order.add_edge(waste_plan_tree, staff_training_tree)
root.order.add_edge(staff_training_tree, community_outreach_tree)
root.order.add_edge(community_outreach_tree, yield_monitor_tree)
root.order.add_edge(yield_monitor_tree, maintenance_check_tree)

# Output the root
print(root)