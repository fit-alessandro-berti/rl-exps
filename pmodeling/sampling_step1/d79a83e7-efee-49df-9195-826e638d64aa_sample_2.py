from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
activities = ['Site Survey', 'Env Assessment', 'Reg Compliance', 'Modular Setup', 'Crop Selection', 'IoT Integration', 'Nutrient Flow', 'Light Calibration', 'Staff Training', 'Pest Control', 'Market Strategy', 'Logistics Plan', 'Yield Analysis', 'Data Review', 'Community Engage']

# Create the transitions for each activity
transitions = [Transition(label=activity) for activity in activities]

# Create the loop node for yield analysis
yield_analysis_loop = OperatorPOWL(operator=Operator.LOOP, children=[transitions[-2], transitions[-1]])

# Create the xor node for pest control and data review
pest_control_data_xor = OperatorPOWL(operator=Operator.XOR, children=[transitions[-3], transitions[-4]])

# Create the partial order
root = StrictPartialOrder(nodes=transitions[:-2] + [yield_analysis_loop, pest_control_data_xor])
root.order.add_edge(transitions[-3], pest_control_data_xor)
root.order.add_edge(transitions[-4], pest_control_data_xor)
root.order.add_edge(yield_analysis_loop, pest_control_data_xor)
root.order.add_edge(yield_analysis_loop, transitions[-2])
root.order.add_edge(yield_analysis_loop, transitions[-1])