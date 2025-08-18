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

# Define the partial order structure
root = StrictPartialOrder(nodes=[
    site_analysis,
    sensor_setup,
    data_capture,
    ai_prediction,
    community_poll,
    irrigation_adjust,
    nutrient_mix,
    pest_control,
    soil_testing,
    biochar_apply,
    microbial_add,
    automated_harvest,
    yield_review,
    waste_process,
    feedback_loop
])

# Define the dependencies between activities
root.order.add_edge(site_analysis, sensor_setup)
root.order.add_edge(sensor_setup, data_capture)
root.order.add_edge(data_capture, ai_prediction)
root.order.add_edge(ai_prediction, community_poll)
root.order.add_edge(community_poll, irrigation_adjust)
root.order.add_edge(irrigation_adjust, nutrient_mix)
root.order.add_edge(nutrient_mix, pest_control)
root.order.add_edge(pest_control, soil_testing)
root.order.add_edge(soil_testing, biochar_apply)
root.order.add_edge(biochar_apply, microbial_add)
root.order.add_edge(microbial_add, automated_harvest)
root.order.add_edge(automated_harvest, yield_review)
root.order.add_edge(yield_review, waste_process)
root.order.add_edge(waste_process, feedback_loop)

# Print the root of the POWL model
print(root)