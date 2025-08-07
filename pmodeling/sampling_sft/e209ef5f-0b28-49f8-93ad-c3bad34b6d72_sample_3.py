import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
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

# Continuous monitoring loop: Sensor Deploy -> Irrigation Adjust -> Nutrient Feed
monitoring_po = StrictPartialOrder(nodes=[sensor_deploy, irrigation_adjust, nutrient_feed])
monitoring_po.order.add_edge(sensor_deploy, irrigation_adjust)
monitoring_po.order.add_edge(irrigation_adjust, nutrient_feed)

# Pest management: Pest Scouting -> Pest Predict
pest_po = StrictPartialOrder(nodes=[pest_scouting, pest_predict])
pest_po.order.add_edge(pest_scouting, pest_predict)

# Community loop: Workshop Host -> Crop Rotate -> Waste Compost -> Water Recycle
community_po = StrictPartialOrder(nodes=[workshop_host, crop_rotate, waste_compost, water_recycle])
community_po.order.add_edge(workshop_host, crop_rotate)
community_po.order.add_edge(crop_rotate, waste_compost)
community_po.order.add_edge(waste_compost, water_recycle)

# Main process as a loop: 
#   Site Mapping -> Soil Analyze -> Bed Setup -> Crop Select -> monitoring_po -> pest_po -> community_po -> data_analyze -> cycle_refine -> resource_share -> yield_report
main_loop = OperatorPOWL(operator=Operator.LOOP, children=[
    site_mapping,
    soil_analyze,
    bed_setup,
    crop_select,
    monitoring_po,
    pest_po,
    community_po,
    data_analyze,
    cycle_refine,
    resource_share,
    yield_report
])

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    site_mapping,
    soil_analyze,
    bed_setup,
    crop_select,
    sensor_deploy,
    irrigation_adjust,
    nutrient_feed,
    pest_scouting,
    pest_predict,
    workshop_host,
    crop_rotate,
    waste_compost,
    water_recycle,
    data_analyze,
    cycle_refine,
    resource_share,
    yield_report
])

# Define the control-flow edges
root.order.add_edge(site_mapping, soil_analyze)
root.order.add_edge(soil_analyze, bed_setup)
root.order.add_edge(bed_setup, crop_select)
root.order.add_edge(crop_select, monitoring_po)
root.order.add_edge(monitoring_po, pest_po)
root.order.add_edge(pest_po, community_po)
root.order.add_edge(community_po, data_analyze)
root.order.add_edge(data_analyze, cycle_refine)
root.order.add_edge(cycle_refine, resource_share)
root.order.add_edge(resource_share, yield_report)
root.order.add_edge(yield_report, main_loop)