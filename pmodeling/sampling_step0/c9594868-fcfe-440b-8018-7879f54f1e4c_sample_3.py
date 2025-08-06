import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
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

# Define silent activities
skip = SilentTransition()

# Define the process
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[site_survey, load_test, permit_review])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[design_layout, material_sourcing, soil_prep])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[hydroponic_setup, community_meet, crop_select])
loop4 = OperatorPOWL(operator=Operator.LOOP, children=[sensor_install, water_testing, pest_control])
loop5 = OperatorPOWL(operator=Operator.LOOP, children=[growth_monitor, harvest_plan, market_launch])
loop6 = OperatorPOWL(operator=Operator.LOOP, children=[feedback_collect, skip])

xor1 = OperatorPOWL(operator=Operator.XOR, children=[loop1, loop2])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[xor1, loop3])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[xor2, loop4])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[xor3, loop5])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[xor4, loop6])

root = StrictPartialOrder(nodes=[xor1, xor2, xor3, xor4, xor5])
root.order.add_edge(xor1, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, xor5)

print(root)