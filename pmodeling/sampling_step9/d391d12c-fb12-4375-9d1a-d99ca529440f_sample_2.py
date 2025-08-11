import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
site_survey = Transition(label='Site Survey')
climate_check = Transition(label='Climate Check')
soil_testing = Transition(label='Soil Testing')
media_select = Transition(label='Media Select')
design_layout = Transition(label='Design Layout')
hydro_setup = Transition(label='Hydro Setup')
nutrient_mix = Transition(label='Nutrient Mix')
sensor_install = Transition(label='Sensor Install')
regulation_review = Transition(label='Regulation Review')
permit_apply = Transition(label='Permit Apply')
stakeholder_meet = Transition(label='Stakeholder Meet')
community_train = Transition(label='Community Train')
plant_seed = Transition(label='Plant Seed')
monitor_growth = Transition(label='Monitor Growth')
adjust_controls = Transition(label='Adjust Controls')
harvest_plan = Transition(label='Harvest Plan')
waste_recycle = Transition(label='Waste Recycle')
feedback_loop = Transition(label='Feedback Loop')

# Define the silent transition
skip = SilentTransition()

# Define the exclusive choice
xor = OperatorPOWL(operator=Operator.XOR, children=[feedback_loop, skip])

# Define the loop
loop = OperatorPOWL(operator=Operator.LOOP, children=[site_survey, climate_check, soil_testing, media_select, design_layout, hydro_setup, nutrient_mix, sensor_install, regulation_review, permit_apply, stakeholder_meet, community_train, plant_seed, monitor_growth, adjust_controls, harvest_plan, waste_recycle])

# Define the root
root = StrictPartialOrder(nodes=[loop, xor])
root.order.add_edge(loop, xor)

print(root)