import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define each activity as a Transition
soil_analyze = Transition(label='Soil Analyze')
site_mapping = Transition(label='Site Mapping')
bed_setup = Transition(label='Bed Setup')
crop_select = Transition(label='Crop Select')
sensor_deploy = Transition(label='Sensor Deploy')
irrigation_adjust = Transition(label='Irrigation Adjust')
nutrient_feed = Transition(label='Nutrient Feed')
pest_scouting = Transition(label='Pest Scouting')
pest_predict = Transition(label='Pest Predict')
workshop_host = Transition(label='Workshop Host')
crop_rotate = Transition(label='Crop Rotate')
waste_compost = Transition(label='Waste Compost')
water_recycle = Transition(label='Water Recycle')
data_analyze = Transition(label='Data Analyze')
cycle_refine = Transition(label='Cycle Refine')
resource_share = Transition(label='Resource Share')
yield_report = Transition(label='Yield Report')

# Define the loop for sensor deployment and pest scouting
sensor_pest_loop = OperatorPOWL(operator=Operator.LOOP, children=[sensor_deploy, pest_scouting])

# Define the exclusive choice for pest prediction and workshop host
pest_prediction_workshop_choice = OperatorPOWL(operator=Operator.XOR, children=[pest_predict, workshop_host])

# Define the loop for waste composting and water recycling
waste_water_loop = OperatorPOWL(operator=Operator.LOOP, children=[waste_compost, water_recycle])

# Define the root POWL model with all activities and loops
root = StrictPartialOrder(nodes=[soil_analyze, site_mapping, bed_setup, crop_select, sensor_pest_loop, irrigation_adjust, nutrient_feed, pest_prediction_workshop_choice, crop_rotate, waste_water_loop, data_analyze, cycle_refine, resource_share, yield_report])

# Add dependencies between activities
root.order.add_edge(soil_analyze, site_mapping)
root.order.add_edge(site_mapping, bed_setup)
root.order.add_edge(bed_setup, crop_select)
root.order.add_edge(crop_select, sensor_pest_loop)
root.order.add_edge(sensor_pest_loop, irrigation_adjust)
root.order.add_edge(irrigation_adjust, nutrient_feed)
root.order.add_edge(nutrient_feed, pest_prediction_workshop_choice)
root.order.add_edge(pest_prediction_workshop_choice, crop_rotate)
root.order.add_edge(crop_rotate, waste_water_loop)
root.order.add_edge(waste_water_loop, data_analyze)
root.order.add_edge(data_analyze, cycle_refine)
root.order.add_edge(cycle_refine, resource_share)
root.order.add_edge(resource_share, yield_report)

# Print the root POWL model
print(root)