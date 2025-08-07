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

# Define the root of the POWL model
root = StrictPartialOrder(nodes=[
    load_assess,
    permit_review,
    site_survey,
    design_layout,
    soil_mix,
    install_beds,
    irrigation_set,
    climate_test,
    sensor_deploy,
    energy_setup,
    crop_select,
    plant_seeding,
    community_meet,
    compliance_check,
    growth_monitor,
    harvest_plan,
    waste_recycle
])

# No explicit ordering is needed as the activities are sequential in the process description
# However, if there were dependencies, they would be added here like:
# root.order.add_edge(load_assess, permit_review)
# root.order.add_edge(permit_review, site_survey)
# ...

print(root)