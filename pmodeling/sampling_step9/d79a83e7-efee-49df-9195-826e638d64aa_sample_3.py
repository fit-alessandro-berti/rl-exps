import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
site_survey = Transition(label='Site Survey')
env_assessment = Transition(label='Env Assessment')
reg_compliance = Transition(label='Reg Compliance')
modular_setup = Transition(label='Modular Setup')
crop_selection = Transition(label='Crop Selection')
iot_integration = Transition(label='IoT Integration')
nutrient_flow = Transition(label='Nutrient Flow')
light_calibration = Transition(label='Light Calibration')
staff_training = Transition(label='Staff Training')
pest_control = Transition(label='Pest Control')
market_strategy = Transition(label='Market Strategy')
logistics_plan = Transition(label='Logistics Plan')
yield_analysis = Transition(label='Yield Analysis')
data_review = Transition(label='Data Review')
community_engage = Transition(label='Community Engage')

# Define the silent transitions (tau labels)
skip = SilentTransition()

# Define the loop nodes
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[modular_setup, env_assessment])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[reg_compliance, site_survey])

# Define the exclusive choice nodes
xor1 = OperatorPOWL(operator=Operator.XOR, children=[pest_control, skip])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[staff_training, skip])

# Define the partial order
root = StrictPartialOrder(nodes=[loop1, loop2, xor1, xor2, site_survey, env_assessment, reg_compliance, modular_setup, crop_selection, iot_integration, nutrient_flow, light_calibration, staff_training, pest_control, market_strategy, logistics_plan, yield_analysis, data_review, community_engage])

# Define the dependencies between the nodes
root.order.add_edge(loop1, loop2)
root.order.add_edge(loop1, xor1)
root.order.add_edge(loop1, xor2)
root.order.add_edge(loop2, loop1)
root.order.add_edge(loop2, xor1)
root.order.add_edge(loop2, xor2)
root.order.add_edge(xor1, loop1)
root.order.add_edge(xor1, loop2)
root.order.add_edge(xor2, loop1)
root.order.add_edge(xor2, loop2)

# Print the root POWL model
print(root)