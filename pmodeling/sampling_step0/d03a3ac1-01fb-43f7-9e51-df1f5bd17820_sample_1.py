import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
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

# Define silent transitions
skip = SilentTransition()

# Define nodes and transitions for the process
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[site_analysis, sensor_setup])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[data_capture, ai_prediction])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[community_poll, irrigation_adjust])
loop4 = OperatorPOWL(operator=Operator.LOOP, children=[nutrient_mix, pest_control])
loop5 = OperatorPOWL(operator=Operator.LOOP, children=[soil_testing, biochar_apply])
loop6 = OperatorPOWL(operator=Operator.LOOP, children=[microbial_add, automated_harvest])
loop7 = OperatorPOWL(operator=Operator.LOOP, children=[yield_review, waste_process])

xor1 = OperatorPOWL(operator=Operator.XOR, children=[feedback_loop, skip])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[loop1, loop2])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[loop3, loop4])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[loop5, loop6])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[loop7, skip])

root = StrictPartialOrder(nodes=[xor1, xor2, xor3, xor4, xor5])
root.order.add_edge(xor1, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, xor5)
root.order.add_edge(xor5, xor1)

# Print the root node
print(root)