import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
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

# Loop for continuous monitoring & adjustment
monitor_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[pest_scouting, pest_predict]
)

# Build the top‐level partial order
root = StrictPartialOrder(nodes=[
    soil_analyze,
    site_mapping,
    bed_setup,
    crop_select,
    sensor_deploy,
    irrigation_adjust,
    nutrient_feed,
    monitor_loop,
    data_analyze,
    cycle_refine,
    resource_share,
    yield_report
])

# Sequential edges
root.order.add_edge(soil_analyze, site_mapping)
root.order.add_edge(site_mapping, bed_setup)
root.order.add_edge(bed_setup, crop_select)
root.order.add_edge(crop_select, sensor_deploy)
root.order.add_edge(sensor_deploy, irrigation_adjust)
root.order.add_edge(irrigation_adjust, nutrient_feed)
root.order.add_edge(nutrient_feed, monitor_loop)

# After the loop, continue with data analysis and cycle refinement
root.order.add_edge(monitor_loop, data_analyze)
root.order.add_edge(data_analyze, cycle_refine)

# Parallel resource sharing and yield reporting
root.order.add_edge(cycle_refine, resource_share)
root.order.add_edge(cycle_refine, yield_report)