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

# Define silent transitions (empty labels)
skip = SilentTransition()

# Define partial order nodes
permit_review_node = OperatorPOWL(operator=Operator.XOR, children=[permit_review, skip])
site_survey_node = OperatorPOWL(operator=Operator.XOR, children=[site_survey, skip])
design_layout_node = OperatorPOWL(operator=Operator.XOR, children=[design_layout, skip])
system_assembly_node = OperatorPOWL(operator=Operator.XOR, children=[system_assembly, skip])
climate_setup_node = OperatorPOWL(operator=Operator.XOR, children=[climate_setup, skip])
nutrient_prep_node = OperatorPOWL(operator=Operator.XOR, children=[nutrient_prep, skip])
irrigation_test_node = OperatorPOWL(operator=Operator.XOR, children=[irrigation_test, skip])
lighting_config_node = OperatorPOWL(operator=Operator.XOR, children=[lighting_config, skip])
energy_install_node = OperatorPOWL(operator=Operator.XOR, children=[energy_install, skip])
sensor_setup_node = OperatorPOWL(operator=Operator.XOR, children=[sensor_setup, skip])
automation_deploy_node = OperatorPOWL(operator=Operator.XOR, children=[automation_deploy, skip])
crop_seeding_node = OperatorPOWL(operator=Operator.XOR, children=[crop_seeding, skip])
waste_plan_node = OperatorPOWL(operator=Operator.XOR, children=[waste_plan, skip])
staff_training_node = OperatorPOWL(operator=Operator.XOR, children=[staff_training, skip])
community_outreach_node = OperatorPOWL(operator=Operator.XOR, children=[community_outreach, skip])
yield_monitor_node = OperatorPOWL(operator=Operator.XOR, children=[yield_monitor, skip])
maintenance_check_node = OperatorPOWL(operator=Operator.XOR, children=[maintenance_check, skip])

# Define partial order
root = StrictPartialOrder(nodes=[
    permit_review_node,
    site_survey_node,
    design_layout_node,
    system_assembly_node,
    climate_setup_node,
    nutrient_prep_node,
    irrigation_test_node,
    lighting_config_node,
    energy_install_node,
    sensor_setup_node,
    automation_deploy_node,
    crop_seeding_node,
    waste_plan_node,
    staff_training_node,
    community_outreach_node,
    yield_monitor_node,
    maintenance_check_node
])

# Define dependencies
root.order.add_edge(permit_review_node, site_survey_node)
root.order.add_edge(site_survey_node, design_layout_node)
root.order.add_edge(design_layout_node, system_assembly_node)
root.order.add_edge(system_assembly_node, climate_setup_node)
root.order.add_edge(climate_setup_node, nutrient_prep_node)
root.order.add_edge(nutrient_prep_node, irrigation_test_node)
root.order.add_edge(irrigation_test_node, lighting_config_node)
root.order.add_edge(lighting_config_node, energy_install_node)
root.order.add_edge(energy_install_node, sensor_setup_node)
root.order.add_edge(sensor_setup_node, automation_deploy_node)
root.order.add_edge(automation_deploy_node, crop_seeding_node)
root.order.add_edge(crop_seeding_node, waste_plan_node)
root.order.add_edge(waste_plan_node, staff_training_node)
root.order.add_edge(staff_training_node, community_outreach_node)
root.order.add_edge(community_outreach_node, yield_monitor_node)
root.order.add_edge(yield_monitor_node, maintenance_check_node)

print(root)