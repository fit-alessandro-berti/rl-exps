import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all transitions
soil_analyze   = Transition(label='Soil Analyze')
site_mapping   = Transition(label='Site Mapping')
bed_setup      = Transition(label='Bed Setup')
crop_select    = Transition(label='Crop Select')
sensor_deploy  = Transition(label='Sensor Deploy')
pest_scouting  = Transition(label='Pest Scouting')
pest_predict   = Transition(label='Pest Predict')
irrigation_adj = Transition(label='Irrigation Adjust')
nutrient_feed  = Transition(label='Nutrient Feed')
workshop_host  = Transition(label='Workshop Host')
crop_rotate    = Transition(label='Crop Rotate')
waste_compost  = Transition(label='Waste Compost')
water_recycle  = Transition(label='Water Recycle')
data_analyze   = Transition(label='Data Analyze')
cycle_refine   = Transition(label='Cycle Refine')
resource_share = Transition(label='Resource Share')
yield_report   = Transition(label='Yield Report')

# Loop body for sensor monitoring & pest management
loop_body = StrictPartialOrder(nodes=[
    sensor_deploy, pest_scouting, pest_predict,
    irrigation_adj, nutrient_feed
])
loop_body.order.add_edge(sensor_deploy, pest_scouting)
loop_body.order.add_edge(pest_scouting, pest_predict)
loop_body.order.add_edge(pest_predict, irrigation_adj)
loop_body.order.add_edge(pest_predict, nutrient_feed)

# LOOP: do sensor monitoring & pest management, then optionally repeat
loop = OperatorPOWL(operator=Operator.LOOP, children=[loop_body, loop_body])

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    soil_analyze, site_mapping, bed_setup,
    crop_select, loop,
    workshop_host, crop_rotate,
    waste_compost, water_recycle,
    data_analyze, cycle_refine,
    resource_share, yield_report
])
root.order.add_edge(soil_analyze, site_mapping)
root.order.add_edge(site_mapping, bed_setup)
root.order.add_edge(bed_setup, crop_select)
root.order.add_edge(crop_select, loop)
root.order.add_edge(loop, workshop_host)
root.order.add_edge(workshop_host, crop_rotate)
root.order.add_edge(crop_rotate, waste_compost)
root.order.add_edge(crop_rotate, water_recycle)
root.order.add_edge(waste_compost, data_analyze)
root.order.add_edge(water_recycle, data_analyze)
root.order.add_edge(data_analyze, cycle_refine)
root.order.add_edge(cycle_refine, resource_share)
root.order.add_edge(resource_share, yield_report)