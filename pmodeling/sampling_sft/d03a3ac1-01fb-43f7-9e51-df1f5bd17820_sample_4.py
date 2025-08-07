import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
site_analysis    = Transition(label='Site Analysis')
sensor_setup     = Transition(label='Sensor Setup')
data_capture     = Transition(label='Data Capture')
ai_prediction    = Transition(label='AI Prediction')
community_poll   = Transition(label='Community Poll')
irrigation_adj   = Transition(label='Irrigation Adjust')
nutrient_mix     = Transition(label='Nutrient Mix')
pest_control     = Transition(label='Pest Control')
soil_testing     = Transition(label='Soil Testing')
biochar_apply    = Transition(label='Biochar Apply')
microbial_add    = Transition(label='Microbial Add')
automated_harvest= Transition(label='Automated Harvest')
yield_review     = Transition(label='Yield Review')
waste_process    = Transition(label='Waste Process')
feedback_loop    = Transition(label='Feedback Loop')

# Build the loop body: AI Prediction -> Community Poll -> Feedback Loop
loop_body = StrictPartialOrder(nodes=[ai_prediction, community_poll, feedback_loop])
loop_body.order.add_edge(ai_prediction, community_poll)
loop_body.order.add_edge(community_poll, feedback_loop)

# Define the LOOP operator: do Data Capture, then either exit or repeat loop_body and Data Capture
loop = OperatorPOWL(operator=Operator.LOOP, children=[data_capture, loop_body])

# Assemble the top-level partial order
root = StrictPartialOrder(nodes=[
    site_analysis,
    sensor_setup,
    loop,
    irrigation_adj,
    nutrient_mix,
    pest_control,
    soil_testing,
    biochar_apply,
    microbial_add,
    automated_harvest,
    yield_review,
    waste_process
])

# Define the control-flow dependencies
root.order.add_edge(site_analysis, sensor_setup)
root.order.add_edge(sensor_setup, loop)
root.order.add_edge(loop, irrigation_adj)
root.order.add_edge(loop, nutrient_mix)
root.order.add_edge(loop, pest_control)
root.order.add_edge(loop, soil_testing)
root.order.add_edge(loop, biochar_apply)
root.order.add_edge(loop, microbial_add)
root.order.add_edge(loop, automated_harvest)
root.order.add_edge(loop, yield_review)
root.order.add_edge(loop, waste_process)

print(root)