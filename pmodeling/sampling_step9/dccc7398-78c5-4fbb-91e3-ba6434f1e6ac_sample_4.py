import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions
site_survey = Transition(label='Site Survey')
design_draft = Transition(label='Design Draft')
permit_review = Transition(label='Permit Review')
structure_build = Transition(label='Structure Build')
enviro_setup = Transition(label='Enviro Setup')
nutrient_mix = Transition(label='Nutrient Mix')
seed_selection = Transition(label='Seed Selection')
plant_robots = Transition(label='Plant Robots')
sensor_install = Transition(label='Sensor Install')
data_sync = Transition(label='Data Sync')
growth_monitor = Transition(label='Growth Monitor')
pest_control = Transition(label='Pest Control')
harvest_plan = Transition(label='Harvest Plan')
quality_check = Transition(label='Quality Check')
market_launch = Transition(label='Market Launch')
feedback_loop = Transition(label='Feedback Loop')

# Define the silent transitions
skip = SilentTransition()

# Define the exclusive choice (XOR) for the activities
xor = OperatorPOWL(operator=Operator.XOR, children=[design_draft, permit_review, structure_build, enviro_setup, nutrient_mix, seed_selection, plant_robots, sensor_install, data_sync, growth_monitor, pest_control, harvest_plan, quality_check, market_launch, feedback_loop])

# Define the loop for the activities
loop = OperatorPOWL(operator=Operator.LOOP, children=[site_survey, xor])

# Define the root of the POWL model
root = StrictPartialOrder(nodes=[loop, xor])
root.order.add_edge(loop, xor)

# Print the root of the POWL model
print(root)