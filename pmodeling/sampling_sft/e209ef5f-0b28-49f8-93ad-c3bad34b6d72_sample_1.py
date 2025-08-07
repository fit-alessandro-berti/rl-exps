import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
soil_analyze    = Transition(label='Soil Analyze')
site_mapping    = Transition(label='Site Mapping')
bed_setup       = Transition(label='Bed Setup')
crop_select     = Transition(label='Crop Select')
sensor_deploy   = Transition(label='Sensor Deploy')
irrigation_adj  = Transition(label='Irrigation Adjust')
nutrient_feed   = Transition(label='Nutrient Feed')
pest_scouting   = Transition(label='Pest Scouting')
pest_predict    = Transition(label='Pest Predict')
workshop_host   = Transition(label='Workshop Host')
crop_rotate     = Transition(label='Crop Rotate')
waste_compost   = Transition(label='Waste Compost')
water_recycle   = Transition(label='Water Recycle')
data_analyze    = Transition(label='Data Analyze')
cycle_refine    = Transition(label='Cycle Refine')
resource_share  = Transition(label='Resource Share')
yield_report    = Transition(label='Yield Report')

# Define the loop for continuous monitoring and adjustment
monitor_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[pest_scouting, pest_predict]
)

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    soil_analyze, site_mapping, bed_setup, crop_select,
    sensor_deploy, irrigation_adj, nutrient_feed,
    monitor_loop,
    crop_rotate,
    waste_compost, water_recycle,
    data_analyze, cycle_refine, resource_share,
    yield_report
])

# Define the control-flow dependencies
root.order.add_edge(soil_analyze, site_mapping)
root.order.add_edge(site_mapping, bed_setup)
root.order.add_edge(bed_setup, crop_select)
root.order.add_edge(crop_select, sensor_deploy)
root.order.add_edge(sensor_deploy, irrigation_adj)
root.order.add_edge(irrigation_adj, nutrient_feed)

# After the initial setup, the monitoring loop can start concurrently
root.order.add_edge(soil_analyze, monitor_loop)
root.order.add_edge(site_mapping, monitor_loop)
root.order.add_edge(bed_setup, monitor_loop)
root.order.add_edge(crop_select, monitor_loop)
root.order.add_edge(sensor_deploy, monitor_loop)
root.order.add_edge(irrigation_adj, monitor_loop)
root.order.add_edge(nutrient_feed, monitor_loop)

# After monitoring, the rest of the cycle can proceed in parallel
root.order.add_edge(monitor_loop, crop_rotate)
root.order.add_edge(monitor_loop, waste_compost)
root.order.add_edge(monitor_loop, water_recycle)

# Parallelize the resource management and reporting steps
root.order.add_edge(waste_compost, data_analyze)
root.order.add_edge(water_recycle, data_analyze)
root.order.add_edge(data_analyze, cycle_refine)
root.order.add_edge(cycle_refine, resource_share)
root.order.add_edge(resource_share, yield_report)

# Finally, the cycle is completed with the yield report
root.order.add_edge(yield_report, yield_report)  # loop back for another cycle