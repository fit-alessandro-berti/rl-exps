import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
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

# Define transitions
loop_soil_analyze = OperatorPOWL(operator=Operator.LOOP, children=[soil_analyze, site_mapping])
loop_bed_setup = OperatorPOWL(operator=Operator.LOOP, children=[bed_setup, crop_select])
loop_sensor_deploy = OperatorPOWL(operator=Operator.LOOP, children=[sensor_deploy, irrigation_adjust, nutrient_feed])
loop_pest_scouting = OperatorPOWL(operator=Operator.LOOP, children=[pest_scouting, pest_predict])
loop_workshop_host = OperatorPOWL(operator=Operator.LOOP, children=[workshop_host, crop_rotate])
loop_waste_compost = OperatorPOWL(operator=Operator.LOOP, children=[waste_compost, water_recycle])
loop_data_analyze = OperatorPOWL(operator=Operator.LOOP, children=[data_analyze, cycle_refine])
loop_resource_share = OperatorPOWL(operator=Operator.LOOP, children=[resource_share, yield_report])

# Create the POWL model
root = StrictPartialOrder(nodes=[loop_soil_analyze, loop_bed_setup, loop_sensor_deploy, loop_pest_scouting, loop_workshop_host, loop_waste_compost, loop_data_analyze, loop_resource_share])
root.order.add_edge(loop_soil_analyze, loop_bed_setup)
root.order.add_edge(loop_bed_setup, loop_sensor_deploy)
root.order.add_edge(loop_sensor_deploy, loop_pest_scouting)
root.order.add_edge(loop_pest_scouting, loop_workshop_host)
root.order.add_edge(loop_workshop_host, loop_waste_compost)
root.order.add_edge(loop_waste_compost, loop_data_analyze)
root.order.add_edge(loop_data_analyze, loop_resource_share)