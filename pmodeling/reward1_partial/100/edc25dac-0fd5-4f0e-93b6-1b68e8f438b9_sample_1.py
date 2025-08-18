import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities with their labels
activities = ['Load Assess', 'Permit Review', 'Site Survey', 'Design Layout', 'Soil Mix', 'Install Beds', 'Irrigation Set', 'Climate Test', 'Sensor Deploy', 'Energy Setup', 'Crop Select', 'Plant Seeding', 'Community Meet', 'Compliance Check', 'Growth Monitor', 'Harvest Plan', 'Waste Recycle']

# Create transitions for each activity
transitions = [Transition(label=activity) for activity in activities]

# Define the process steps using OperatorPOWL
load_assess = OperatorPOWL(operator=Operator.XOR, children=[transitions[0], SilentTransition()])
permit_review = OperatorPOWL(operator=Operator.XOR, children=[transitions[1], SilentTransition()])
site_survey = OperatorPOWL(operator=Operator.XOR, children=[transitions[2], SilentTransition()])
design_layout = OperatorPOWL(operator=Operator.XOR, children=[transitions[3], SilentTransition()])
soil_mix = OperatorPOWL(operator=Operator.XOR, children=[transitions[4], SilentTransition()])
install_beds = OperatorPOWL(operator=Operator.XOR, children=[transitions[5], SilentTransition()])
irrigation_set = OperatorPOWL(operator=Operator.XOR, children=[transitions[6], SilentTransition()])
climate_test = OperatorPOWL(operator=Operator.XOR, children=[transitions[7], SilentTransition()])
sensor_deploy = OperatorPOWL(operator=Operator.XOR, children=[transitions[8], SilentTransition()])
energy_setup = OperatorPOWL(operator=Operator.XOR, children=[transitions[9], SilentTransition()])
crop_select = OperatorPOWL(operator=Operator.XOR, children=[transitions[10], SilentTransition()])
plant_seeding = OperatorPOWL(operator=Operator.XOR, children=[transitions[11], SilentTransition()])
community_meet = OperatorPOWL(operator=Operator.XOR, children=[transitions[12], SilentTransition()])
compliance_check = OperatorPOWL(operator=Operator.XOR, children=[transitions[13], SilentTransition()])
growth_monitor = OperatorPOWL(operator=Operator.XOR, children=[transitions[14], SilentTransition()])
harvest_plan = OperatorPOWL(operator=Operator.XOR, children=[transitions[15], SilentTransition()])
waste_recycle = OperatorPOWL(operator=Operator.XOR, children=[transitions[16], SilentTransition()])

# Create a partial order with the defined nodes
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

# Define the dependencies between the nodes
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

# Print the root to verify the model
print(root)