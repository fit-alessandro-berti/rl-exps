from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for each activity
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

# Create the root POWL model
root = StrictPartialOrder(nodes=[site_survey, permit_review, design_layout, system_assembly, climate_setup, nutrient_prep, irrigation_test, lighting_config, energy_install, sensor_setup, automation_deploy, crop_seeding, waste_plan, staff_training, community_outreach, yield_monitor, maintenance_check])

# Define the order of execution
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