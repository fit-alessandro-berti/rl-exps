import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions
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

# Define loops and exclusive choices
site_analysis_loop = OperatorPOWL(operator=Operator.LOOP, children=[site_analysis, sensor_setup])
sensor_setup_loop = OperatorPOWL(operator=Operator.LOOP, children=[sensor_setup, data_capture])
data_capture_loop = OperatorPOWL(operator=Operator.LOOP, children=[data_capture, ai_prediction])
ai_prediction_loop = OperatorPOWL(operator=Operator.LOOP, children=[ai_prediction, community_poll])
community_poll_loop = OperatorPOWL(operator=Operator.LOOP, children=[community_poll, irrigation_adjust])
irrigation_adjust_loop = OperatorPOWL(operator=Operator.LOOP, children=[irrigation_adjust, nutrient_mix])
nutrient_mix_loop = OperatorPOWL(operator=Operator.LOOP, children=[nutrient_mix, pest_control])
pest_control_loop = OperatorPOWL(operator=Operator.LOOP, children=[pest_control, soil_testing])
soil_testing_loop = OperatorPOWL(operator=Operator.LOOP, children=[soil_testing, biochar_apply])
biochar_apply_loop = OperatorPOWL(operator=Operator.LOOP, children=[biochar_apply, microbial_add])
microbial_add_loop = OperatorPOWL(operator=Operator.LOOP, children=[microbial_add, automated_harvest])
automated_harvest_loop = OperatorPOWL(operator=Operator.LOOP, children=[automated_harvest, yield_review])
yield_review_loop = OperatorPOWL(operator=Operator.LOOP, children=[yield_review, waste_process])
waste_process_loop = OperatorPOWL(operator=Operator.LOOP, children=[waste_process, feedback_loop])

# Create the root POWL model
root = StrictPartialOrder(nodes=[site_analysis_loop, sensor_setup_loop, data_capture_loop, ai_prediction_loop, community_poll_loop, irrigation_adjust_loop, nutrient_mix_loop, pest_control_loop, soil_testing_loop, biochar_apply_loop, microbial_add_loop, automated_harvest_loop, yield_review_loop, waste_process_loop, feedback_loop])
root.order.add_edge(site_analysis_loop, sensor_setup_loop)
root.order.add_edge(sensor_setup_loop, data_capture_loop)
root.order.add_edge(data_capture_loop, ai_prediction_loop)
root.order.add_edge(ai_prediction_loop, community_poll_loop)
root.order.add_edge(community_poll_loop, irrigation_adjust_loop)
root.order.add_edge(irrigation_adjust_loop, nutrient_mix_loop)
root.order.add_edge(nutrient_mix_loop, pest_control_loop)
root.order.add_edge(pest_control_loop, soil_testing_loop)
root.order.add_edge(soil_testing_loop, biochar_apply_loop)
root.order.add_edge(biochar_apply_loop, microbial_add_loop)
root.order.add_edge(microbial_add_loop, automated_harvest_loop)
root.order.add_edge(automated_harvest_loop, yield_review_loop)
root.order.add_edge(yield_review_loop, waste_process_loop)
root.order.add_edge(waste_process_loop, feedback_loop)