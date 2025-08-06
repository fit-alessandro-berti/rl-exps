import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
root = StrictPartialOrder()

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

# Define choices and loops
site_mapping_choice = OperatorPOWL(operator=Operator.XOR, children=[site_mapping, soil_analyze])
bed_setup_choice = OperatorPOWL(operator=Operator.XOR, children=[bed_setup, sensor_deploy])
crop_select_choice = OperatorPOWL(operator=Operator.XOR, children=[crop_select, irrigation_adjust])
nutrient_feed_choice = OperatorPOWL(operator=Operator.XOR, children=[nutrient_feed, nutrient_feed])
pest_scouting_choice = OperatorPOWL(operator=Operator.XOR, children=[pest_scouting, pest_predict])
workshop_host_choice = OperatorPOWL(operator=Operator.XOR, children=[workshop_host, workshop_host])
crop_rotate_choice = OperatorPOWL(operator=Operator.XOR, children=[crop_rotate, crop_rotate])
waste_compost_choice = OperatorPOWL(operator=Operator.XOR, children=[waste_compost, waste_compost])
water_recycle_choice = OperatorPOWL(operator=Operator.XOR, children=[water_recycle, water_recycle])
data_analyze_choice = OperatorPOWL(operator=Operator.XOR, children=[data_analyze, data_analyze])
cycle_refine_choice = OperatorPOWL(operator=Operator.XOR, children=[cycle_refine, cycle_refine])
resource_share_choice = OperatorPOWL(operator=Operator.XOR, children=[resource_share, resource_share])
yield_report_choice = OperatorPOWL(operator=Operator.XOR, children=[yield_report, yield_report])

# Define loops
bed_setup_loop = OperatorPOWL(operator=Operator.LOOP, children=[bed_setup_choice, bed_setup_choice])
pest_scouting_loop = OperatorPOWL(operator=Operator.LOOP, children=[pest_scouting_choice, pest_scouting_choice])
crop_rotate_loop = OperatorPOWL(operator=Operator.LOOP, children=[crop_rotate_choice, crop_rotate_choice])
waste_compost_loop = OperatorPOWL(operator=Operator.LOOP, children=[waste_compost_choice, waste_compost_choice])
water_recycle_loop = OperatorPOWL(operator=Operator.LOOP, children=[water_recycle_choice, water_recycle_choice])
data_analyze_loop = OperatorPOWL(operator=Operator.LOOP, children=[data_analyze_choice, data_analyze_choice])
cycle_refine_loop = OperatorPOWL(operator=Operator.LOOP, children=[cycle_refine_choice, cycle_refine_choice])
resource_share_loop = OperatorPOWL(operator=Operator.LOOP, children=[resource_share_choice, resource_share_choice])
yield_report_loop = OperatorPOWL(operator=Operator.LOOP, children=[yield_report_choice, yield_report_choice])

# Define the partial order
root.nodes = [site_mapping_choice, bed_setup_loop, crop_select_choice, nutrient_feed_choice, pest_scouting_loop, workshop_host_choice, crop_rotate_loop, waste_compost_loop, water_recycle_loop, data_analyze_loop, cycle_refine_loop, resource_share_loop, yield_report_loop]

# Define dependencies
root.order.add_edge(site_mapping_choice, bed_setup_loop)
root.order.add_edge(bed_setup_loop, crop_select_choice)
root.order.add_edge(crop_select_choice, nutrient_feed_choice)
root.order.add_edge(nutrient_feed_choice, pest_scouting_loop)
root.order.add_edge(pest_scouting_loop, workshop_host_choice)
root.order.add_edge(workshop_host_choice, crop_rotate_loop)
root.order.add_edge(crop_rotate_loop, waste_compost_loop)
root.order.add_edge(waste_compost_loop, water_recycle_loop)
root.order.add_edge(water_recycle_loop, data_analyze_loop)
root.order.add_edge(data_analyze_loop, cycle_refine_loop)
root.order.add_edge(cycle_refine_loop, resource_share_loop)
root.order.add_edge(resource_share_loop, yield_report_loop)

# Print the final POWL model
print(root)