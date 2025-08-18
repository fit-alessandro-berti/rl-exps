import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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

skip = SilentTransition()

site_survey_to_permit_review = OperatorPOWL(operator=Operator.XOR, children=[permit_review, skip])
permit_review_to_design_layout = OperatorPOWL(operator=Operator.XOR, children=[design_layout, skip])
design_layout_to_system_assembly = OperatorPOWL(operator=Operator.XOR, children=[system_assembly, skip])
system_assembly_to_climate_setup = OperatorPOWL(operator=Operator.XOR, children=[climate_setup, skip])
climate_setup_to_nutrient_prep = OperatorPOWL(operator=Operator.XOR, children=[nutrient_prep, skip])
nutrient_prep_to_irrigation_test = OperatorPOWL(operator=Operator.XOR, children=[irrigation_test, skip])
irrigation_test_to_lighting_config = OperatorPOWL(operator=Operator.XOR, children=[lighting_config, skip])
lighting_config_to_energy_install = OperatorPOWL(operator=Operator.XOR, children=[energy_install, skip])
energy_install_to_sensor_setup = OperatorPOWL(operator=Operator.XOR, children=[sensor_setup, skip])
sensor_setup_to_automation_deploy = OperatorPOWL(operator=Operator.XOR, children=[automation_deploy, skip])
automation_deploy_to_crop_seeding = OperatorPOWL(operator=Operator.XOR, children=[crop_seeding, skip])
crop_seeding_to_waste_plan = OperatorPOWL(operator=Operator.XOR, children=[waste_plan, skip])
waste_plan_to_staff_training = OperatorPOWL(operator=Operator.XOR, children=[staff_training, skip])
staff_training_to_community_outreach = OperatorPOWL(operator=Operator.XOR, children=[community_outreach, skip])
community_outreach_to_yield_monitor = OperatorPOWL(operator=Operator.XOR, children=[yield_monitor, skip])
yield_monitor_to_maintenance_check = OperatorPOWL(operator=Operator.XOR, children=[maintenance_check, skip])

root = StrictPartialOrder(nodes=[
    site_survey,
    permit_review,
    design_layout,
    system_assembly,
    climate_setup,
    nutrient_prep,
    irrigation_test,
    lighting_config,
    energy_install,
    sensor_setup,
    automation_deploy,
    crop_seeding,
    waste_plan,
    staff_training,
    community_outreach,
    yield_monitor,
    maintenance_check
])
root.order.add_edge(site_survey, permit_review)
root.order.add_edge(permit_review, design_layout)
root.order.add_edge(design_layout, system_assembly)
root.order.add_edge(system_assembly, climate_setup)
root.order.add_edge(climate_setup, nutrient_prep)
root.order.add_edge(nutrient_prep, irrigation_test)
root.order.add_edge(irrigation_test, lighting_config)
root.order.add_edge(lighting_config, energy_install)
root.order.add_edge(energy_install, sensor_setup)
root.order.add_edge(sensor_setup, automation_deploy)
root.order.add_edge(automation_deploy, crop_seeding)
root.order.add_edge(crop_seeding, waste_plan)
root.order.add_edge(waste_plan, staff_training)
root.order.add_edge(staff_training, community_outreach)
root.order.add_edge(community_outreach, yield_monitor)
root.order.add_edge(yield_monitor, maintenance_check)