import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
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

# Build the main cycle as a partial order
main_cycle = StrictPartialOrder(nodes=[
    site_analysis, sensor_setup, data_capture,
    ai_prediction, community_poll,
    irrigation_adj, nutrient_mix, pest_control,
    soil_testing, biochar_apply, microbial_add,
    automated_harvest, yield_review, waste_process
])

# Sequence of data capture -> AI prediction
main_cycle.order.add_edge(data_capture, ai_prediction)

# Community poll then either adjust irrigation or nutrient mix
main_cycle.order.add_edge(community_poll, irrigation_adj)
main_cycle.order.add_edge(community_poll, nutrient_mix)

# Parallel irrigation and nutrient mix after community poll
main_cycle.order.add_edge(irrigation_adj, yield_review)
main_cycle.order.add_edge(nutrient_mix, yield_review)

# Pest control and soil testing after AI prediction
main_cycle.order.add_edge(ai_prediction, pest_control)
main_cycle.order.add_edge(ai_prediction, soil_testing)

# Biochar and microbial add after soil testing
main_cycle.order.add_edge(soil_testing, biochar_apply)
main_cycle.order.add_edge(soil_testing, microbial_add)

# Harvesting after yield review
main_cycle.order.add_edge(yield_review, automated_harvest)

# Waste processing after automated harvest
main_cycle.order.add_edge(automated_harvest, waste_process)

# Feedback loop at the end
main_cycle.order.add_edge(yield_review, feedback_loop)

# Assemble the overall process as a loop: do the main cycle, then optionally do feedback and repeat
root = OperatorPOWL(operator=Operator.LOOP, children=[main_cycle, feedback_loop])