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

# Loop for continuous AI prediction, community poll, and adjustment
loop_body = StrictPartialOrder(nodes=[
    ai_prediction,
    community_poll,
    irrigation_adj,
    nutrient_mix,
    pest_control
])
loop_body.order.add_edge(ai_prediction, community_poll)
loop_body.order.add_edge(community_poll, irrigation_adj)
loop_body.order.add_edge(community_poll, nutrient_mix)
loop_body.order.add_edge(community_poll, pest_control)

loop = OperatorPOWL(operator=Operator.LOOP, children=[data_capture, loop_body])

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    site_analysis,
    sensor_setup,
    loop,
    soil_testing,
    biochar_apply,
    microbial_add,
    automated_harvest,
    yield_review,
    waste_process,
    feedback_loop
])
root.order.add_edge(site_analysis, sensor_setup)
root.order.add_edge(sensor_setup, loop)
root.order.add_edge(loop, soil_testing)
root.order.add_edge(soil_testing, biochar_apply)
root.order.add_edge(soil_testing, microbial_add)
root.order.add_edge(biochar_apply, automated_harvest)
root.order.add_edge(biochar_apply, waste_process)
root.order.add_edge(microbial_add, automated_harvest)
root.order.add_edge(microbial_add, waste_process)
root.order.add_edge(automated_harvest, yield_review)
root.order.add_edge(waste_process, feedback_loop)
root.order.add_edge(feedback_loop, loop)