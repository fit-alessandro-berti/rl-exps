import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define transitions (activities)
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

# Define operators
xor = OperatorPOWL(operator=Operator.XOR, children=[crop_rotate, resource_share])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[waste_compost, water_recycle])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[pest_scouting, pest_predict])
loop = OperatorPOWL(operator=Operator.LOOP, children=[soil_analyze, site_mapping, bed_setup, crop_select, sensor_deploy, irrigation_adjust, nutrient_feed, xor3, xor2, yield_report])

# Construct the POWL model
root = StrictPartialOrder(nodes=[loop, xor])
root.order.add_edge(loop, xor)