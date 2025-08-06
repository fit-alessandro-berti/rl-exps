import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
site_survey = Transition(label='Site Survey')
load_test = Transition(label='Load Test')
permit_review = Transition(label='Permit Review')
design_layout = Transition(label='Design Layout')
material_sourcing = Transition(label='Material Sourcing')
soil_prep = Transition(label='Soil Prep')
hydroponic_setup = Transition(label='Hydroponic Setup')
community_meet = Transition(label='Community Meet')
crop_select = Transition(label='Crop Select')
sensor_install = Transition(label='Sensor Install')
water_testing = Transition(label='Water Testing')
pest_control = Transition(label='Pest Control')
growth_monitor = Transition(label='Growth Monitor')
harvest_plan = Transition(label='Harvest Plan')
market_launch = Transition(label='Market Launch')
feedback_collect = Transition(label='Feedback Collect')

# Define silent transitions
skip = SilentTransition()

# Define the process flow
loop_1 = OperatorPOWL(operator=Operator.LOOP, children=[load_test, permit_review, design_layout, material_sourcing, soil_prep, hydroponic_setup])
loop_2 = OperatorPOWL(operator=Operator.LOOP, children=[community_meet, crop_select, sensor_install, water_testing, pest_control, growth_monitor])
loop_3 = OperatorPOWL(operator=Operator.LOOP, children=[harvest_plan, market_launch, feedback_collect])

# Construct the root model
root = StrictPartialOrder(nodes=[loop_1, loop_2, loop_3])
root.order.add_edge(loop_1, loop_2)
root.order.add_edge(loop_2, loop_3)

print(root)