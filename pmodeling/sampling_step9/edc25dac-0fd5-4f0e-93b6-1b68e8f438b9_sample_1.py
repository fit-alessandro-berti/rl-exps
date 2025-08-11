import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions
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
skip = SilentTransition()
loop = OperatorPOWL(operator=Operator.LOOP, children=[load_assess, permit_review, site_survey, design_layout, soil_mix, install_beds, irrigation_set, climate_test, sensor_deploy, energy_setup, crop_select, plant_seeding, community_meet, compliance_check, growth_monitor, harvest_plan, waste_recycle])
xor = OperatorPOWL(operator=Operator.XOR, children=[skip])
root = StrictPartialOrder(nodes=[loop, xor])
root.order.add_edge(loop, xor)