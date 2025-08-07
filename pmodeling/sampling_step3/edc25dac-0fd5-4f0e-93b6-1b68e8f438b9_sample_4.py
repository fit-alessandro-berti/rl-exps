import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
load_assess = Transition(label='Load Assess')
permit_review = Transition(label='Permit Review')
site_survey = Transition(label='Site Survey')
design_layout = Transition(label='Design Layout')
soil_mix = Transition(label='Soil Mix')
install_beds = Transition(label='Install Beds')
irrigation_set = Transition(label='Irrigation Set')
climate_test = Transition(label='Climate Test')
sensor_deploy = Transition(label='Sensor Deploy')
energy_setup = Transition(label='Energy Setup')
crop_select = Transition(label='Crop Select')
plant_seeding = Transition(label='Plant Seeding')
community_meet = Transition(label='Community Meet')
compliance_check = Transition(label='Compliance Check')
growth_monitor = Transition(label='Growth Monitor')
harvest_plan = Transition(label='Harvest Plan')
waste_recycle = Transition(label='Waste Recycle')

# Define partial order
root = StrictPartialOrder(nodes=[load_assess, permit_review, site_survey, design_layout, soil_mix, install_beds, irrigation_set, climate_test, sensor_deploy, energy_setup, crop_select, plant_seeding, community_meet, compliance_check, growth_monitor, harvest_plan, waste_recycle])
root.order.add_edge(load_assess, permit_review)
root.order.add_edge(permit_review, site_survey)
root.order.add_edge(site_survey, design_layout)
root.order.add_edge(design_layout, soil_mix)
root.order.add_edge(soil_mix, install_beds)
root.order.add_edge(install_beds, irrigation_set)
root.order.add_edge(irrigation_set, climate_test)
root.order.add_edge(climate_test, sensor_deploy)
root.order.add_edge(sensor_deploy, energy_setup)
root.order.add_edge(energy_setup, crop_select)
root.order.add_edge(crop_select, plant_seeding)
root.order.add_edge(plant_seeding, community_meet)
root.order.add_edge(community_meet, compliance_check)
root.order.add_edge(compliance_check, growth_monitor)
root.order.add_edge(growth_monitor, harvest_plan)
root.order.add_edge(harvest_plan, waste_recycle)

# Save the final result in the variable 'root'