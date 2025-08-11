import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities)
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

# Define silent transitions (tau labels)
skip = SilentTransition()

# Define the loop nodes
soil_management = OperatorPOWL(operator=Operator.LOOP, children=[soil_testing, biochar_apply, microbial_add])
crop_management = OperatorPOWL(operator=Operator.LOOP, children=[site_analysis, sensor_setup, data_capture, ai_prediction, community_poll, irrigation_adjust, nutrient_mix, pest_control, soil_management, automated_harvest, yield_review, waste_process, feedback_loop])

# Define the partial order
root = StrictPartialOrder(nodes=[crop_management])
root.order.add_edge(crop_management, feedback_loop)

print(root)