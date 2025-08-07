import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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

# Define dependencies if any (not specified in the problem statement)
# root.order.add_edge(site_analysis, sensor_setup)
# root.order.add_edge(site_analysis, data_capture)
# root.order.add_edge(site_analysis, ai_prediction)
# root.order.add_edge(site_analysis, community_poll)
# root.order.add_edge(site_analysis, irrigation_adjust)
# root.order.add_edge(site_analysis, nutrient_mix)
# root.order.add_edge(site_analysis, pest_control)
# root.order.add_edge(site_analysis, soil_testing)
# root.order.add_edge(site_analysis, biochar_apply)
# root.order.add_edge(site_analysis, microbial_add)
# root.order.add_edge(site_analysis, automated_harvest)
# root.order.add_edge(site_analysis, yield_review)
# root.order.add_edge(site_analysis, waste_process)
# root.order.add_edge(site_analysis, feedback_loop)