import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
site_analysis   = Transition(label='Site Analysis')
sensor_setup    = Transition(label='Sensor Setup')
data_capture    = Transition(label='Data Capture')
ai_prediction   = Transition(label='AI Prediction')
community_poll  = Transition(label='Community Poll')
irrigation_adj  = Transition(label='Irrigation Adjust')
nutrient_mix    = Transition(label='Nutrient Mix')
pest_control    = Transition(label='Pest Control')
soil_testing    = Transition(label='Soil Testing')
biochar_apply   = Transition(label='Biochar Apply')
microbial_add   = Transition(label='Microbial Add')
automated_harvest = Transition(label='Automated Harvest')
yield_review    = Transition(label='Yield Review')
waste_process   = Transition(label='Waste Process')
feedback_loop   = Transition(label='Feedback Loop')

# Define the feedback loop: after each automated harvest, do a yield review
# then optionally do a feedback loop and repeat
feedback_loop_body = StrictPartialOrder(nodes=[yield_review, feedback_loop])
feedback_loop_body.order.add_edge(yield_review, feedback_loop)

# Define the loop: Site Analysis -> Sensor Setup -> Data Capture -> AI Prediction
# then Community Poll -> Irrigation Adjust -> Nutrient Mix -> Pest Control -> Soil Testing
# then Biochar Apply -> Microbial Add -> Automated Harvest
# then optionally do the feedback loop body and repeat
body = StrictPartialOrder(nodes=[
    data_capture, ai_prediction,
    community_poll, irrigation_adj, nutrient_mix, pest_control, soil_testing,
    biochar_apply, microbial_add, automated_harvest
])
body.order.add_edge(data_capture, ai_prediction)
body.order.add_edge(community_poll, irrigation_adj)
body.order.add_edge(irrigation_adj, nutrient_mix)
body.order.add_edge(nutrient_mix, pest_control)
body.order.add_edge(pest_control, soil_testing)
body.order.add_edge(soil_testing, biochar_apply)
body.order.add_edge(biochar_apply, microbial_add)
body.order.add_edge(microbial_add, automated_harvest)

loop = OperatorPOWL(operator=Operator.LOOP, children=[body, feedback_loop_body])

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    site_analysis, sensor_setup,
    feedback_loop
])
root.order.add_edge(site_analysis, sensor_setup)
root.order.add_edge(sensor_setup, feedback_loop)