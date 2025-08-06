import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
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

# Define the workflow
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[permit_review, data_sync, quality_check, market_launch])
xor1 = OperatorPOWL(operator=Operator.XOR, children=[enviro_setup, sensor_install])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[pest_control, feedback_loop])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[structure_build, nutrient_mix])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[design_draft, plant_robots])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[site_survey, market_launch])
root = StrictPartialOrder(nodes=[loop1, xor1, xor2, xor3, xor4, xor5])
root.order.add_edge(loop1, xor1)
root.order.add_edge(xor1, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, xor5)
root.order.add_edge(xor5, loop1)