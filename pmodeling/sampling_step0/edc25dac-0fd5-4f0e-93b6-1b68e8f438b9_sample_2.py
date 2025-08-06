import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for each activity
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

# Define silent transitions
skip1 = SilentTransition()
skip2 = SilentTransition()
skip3 = SilentTransition()
skip4 = SilentTransition()

# Define exclusive choice nodes
xor1 = OperatorPOWL(operator=Operator.XOR, children=[soil_mix, skip1])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[irrigation_set, skip2])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[climate_test, skip3])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[sensor_deploy, skip4])

# Define the loop node
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[crop_select, plant_seeding])

# Define the partial order
root = StrictPartialOrder(nodes=[load_assess, permit_review, site_survey, design_layout, xor1, xor2, xor3, xor4, loop1, community_meet, compliance_check, growth_monitor, harvest_plan, waste_recycle])

# Define the order between the nodes
root.order.add_edge(load_assess, permit_review)
root.order.add_edge(permit_review, site_survey)
root.order.add_edge(site_survey, design_layout)
root.order.add_edge(design_layout, xor1)
root.order.add_edge(xor1, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, loop1)
root.order.add_edge(loop1, community_meet)
root.order.add_edge(community_meet, compliance_check)
root.order.add_edge(compliance_check, growth_monitor)
root.order.add_edge(growth_monitor, harvest_plan)
root.order.add_edge(harvest_plan, waste_recycle)

# Print the final result
print(root)