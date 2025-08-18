from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions (activities)
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

# Define exclusive choice nodes
xor_site_survey = OperatorPOWL(operator=Operator.XOR, children=[permit_review, site_survey])
xor_design_layout = OperatorPOWL(operator=Operator.XOR, children=[system_assembly, design_layout])
xor_system_assembly = OperatorPOWL(operator=Operator.XOR, children=[climate_setup, system_assembly])
xor_climate_setup = OperatorPOWL(operator=Operator.XOR, children=[nutrient_prep, climate_setup])
xor_nutrient_prep = OperatorPOWL(operator=Operator.XOR, children=[irrigation_test, nutrient_prep])
xor_irrigation_test = OperatorPOWL(operator=Operator.XOR, children=[lighting_config, irrigation_test])
xor_lighting_config = OperatorPOWL(operator=Operator.XOR, children=[energy_install, lighting_config])
xor_energy_install = OperatorPOWL(operator=Operator.XOR, children=[sensor_setup, energy_install])
xor_sensor_setup = OperatorPOWL(operator=Operator.XOR, children=[automation_deploy, sensor_setup])
xor_automation_deploy = OperatorPOWL(operator=Operator.XOR, children=[crop_seeding, automation_deploy])
xor_crop_seeding = OperatorPOWL(operator=Operator.XOR, children=[waste_plan, crop_seeding])
xor_waste_plan = OperatorPOWL(operator=Operator.XOR, children=[staff_training, waste_plan])
xor_staff_training = OperatorPOWL(operator=Operator.XOR, children=[community_outreach, staff_training])
xor_community_outreach = OperatorPOWL(operator=Operator.XOR, children=[yield_monitor, community_outreach])
xor_yield_monitor = OperatorPOWL(operator=Operator.XOR, children=[maintenance_check, yield_monitor])

# Define partial order
root = StrictPartialOrder(nodes=[
    xor_site_survey,
    xor_design_layout,
    xor_system_assembly,
    xor_climate_setup,
    xor_nutrient_prep,
    xor_irrigation_test,
    xor_lighting_config,
    xor_energy_install,
    xor_sensor_setup,
    xor_automation_deploy,
    xor_crop_seeding,
    xor_waste_plan,
    xor_staff_training,
    xor_community_outreach,
    xor_yield_monitor,
    xor_yield_monitor
])

# Define dependencies between nodes
root.order.add_edge(xor_site_survey, xor_design_layout)
root.order.add_edge(xor_design_layout, xor_system_assembly)
root.order.add_edge(xor_system_assembly, xor_climate_setup)
root.order.add_edge(xor_climate_setup, xor_nutrient_prep)
root.order.add_edge(xor_nutrient_prep, xor_irrigation_test)
root.order.add_edge(xor_irrigation_test, xor_lighting_config)
root.order.add_edge(xor_lighting_config, xor_energy_install)
root.order.add_edge(xor_energy_install, xor_sensor_setup)
root.order.add_edge(xor_sensor_setup, xor_automation_deploy)
root.order.add_edge(xor_automation_deploy, xor_crop_seeding)
root.order.add_edge(xor_crop_seeding, xor_waste_plan)
root.order.add_edge(xor_waste_plan, xor_staff_training)
root.order.add_edge(xor_staff_training, xor_community_outreach)
root.order.add_edge(xor_community_outreach, xor_yield_monitor)
root.order.add_edge(xor_yield_monitor, xor_yield_monitor)

print(root)