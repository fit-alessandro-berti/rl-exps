import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
site_analysis = Transition(label='Site Analysis')
sensor_setup = Transition(label='Sensor Setup')
data_capture = Transition(label='Data Capture')
ai_prediction = Transition(label='AI Prediction')
community_poll = Transition(label='Community Poll')
irrigation_adjust = Transition(label='Irrigation Adjust')
nutrient_mix = Transition(label='Nutrient Mix')
pest_control = Transition(label='Pest Control')
soil_testing = Transition(label='Soil Testing')
biochar_apply = Transition(label='Biochar Apply')
microbial_add = Transition(label='Microbial Add')
automated_harvest = Transition(label='Automated Harvest')
yield_review = Transition(label='Yield Review')
waste_process = Transition(label='Waste Process')
feedback_loop = Transition(label='Feedback Loop')

# Define silent transitions for empty labels
skip = SilentTransition()

# Define loop nodes
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[soil_testing, microbial_add])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[biochar_apply, nutrient_mix])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[pest_control, irrigation_adjust])

# Define exclusive choice nodes
xor1 = OperatorPOWL(operator=Operator.XOR, children=[site_analysis, sensor_setup])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[data_capture, ai_prediction])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[community_poll, feedback_loop])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[yield_review, waste_process])

# Define the root POWL model
root = StrictPartialOrder(nodes=[xor1, xor2, xor3, xor4, loop1, loop2, loop3])
root.order.add_edge(xor1, loop1)
root.order.add_edge(xor2, loop2)
root.order.add_edge(xor3, loop3)
root.order.add_edge(xor4, loop1)
root.order.add_edge(loop1, xor1)
root.order.add_edge(loop2, xor2)
root.order.add_edge(loop3, xor3)
root.order.add_edge(loop1, xor4)

# Print the root POWL model
print(root)