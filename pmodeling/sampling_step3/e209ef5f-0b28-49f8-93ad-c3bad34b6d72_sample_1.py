import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
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

# Create a StrictPartialOrder model with all the defined transitions
root = StrictPartialOrder(nodes=[
    soil_analyze, site_mapping, bed_setup, crop_select, sensor_deploy,
    irrigation_adjust, nutrient_feed, pest_scouting, pest_predict,
    workshop_host, crop_rotate, waste_compost, water_recycle, data_analyze,
    cycle_refine, resource_share, yield_report
])

# Define the partial order dependencies
root.order.add_edge(soil_analyze, site_mapping)
root.order.add_edge(site_mapping, bed_setup)
root.order.add_edge(bed_setup, crop_select)
root.order.add_edge(crop_select, sensor_deploy)
root.order.add_edge(sensor_deploy, irrigation_adjust)
root.order.add_edge(irrigation_adjust, nutrient_feed)
root.order.add_edge(nutrient_feed, pest_scouting)
root.order.add_edge(pest_scouting, pest_predict)
root.order.add_edge(pest_predict, workshop_host)
root.order.add_edge(workshop_host, crop_rotate)
root.order.add_edge(crop_rotate, waste_compost)
root.order.add_edge(waste_compost, water_recycle)
root.order.add_edge(water_recycle, data_analyze)
root.order.add_edge(data_analyze, cycle_refine)
root.order.add_edge(cycle_refine, resource_share)
root.order.add_edge(resource_share, yield_report)

print(root)