import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

site_survey = Transition(label='Site Survey')
rack_design = Transition(label='Rack Design')
system_setup = Transition(label='System Setup')
climate_calibrate = Transition(label='Climate Calibrate')
nutrient_prep = Transition(label='Nutrient Prep')
crop_select = Transition(label='Crop Select')
seed_germinate = Transition(label='Seed Germinate')
sensor_deploy = Transition(label='Sensor Deploy')
pest_control = Transition(label='Pest Control')
harvest_automate = Transition(label='Harvest Automate')
quality_check = Transition(label='Quality Check')
pack_produce = Transition(label='Pack Produce')
data_analyze = Transition(label='Data Analyze')
engage_community = Transition(label='Engage Community')
logistics_plan = Transition(label='Logistics Plan')

skip = SilentTransition()

# Create a loop for the modular rack design and system setup
loop = OperatorPOWL(operator=Operator.LOOP, children=[rack_design, system_setup])

# Create an XOR for the climate calibrate and nutrient prep
xor = OperatorPOWL(operator=Operator.XOR, children=[climate_calibrate, nutrient_prep])

# Create an XOR for the crop select and seed germinate
crop_germinate_xor = OperatorPOWL(operator=Operator.XOR, children=[crop_select, seed_germinate])

# Create a loop for the pest control and sensor deploy
pest_sensor_loop = OperatorPOWL(operator=Operator.LOOP, children=[pest_control, sensor_deploy])

# Create an XOR for the harvest automate and quality check
harvest_quality_xor = OperatorPOWL(operator=Operator.XOR, children=[harvest_automate, quality_check])

# Create a loop for the pack produce and data analyze
pack_analyze_loop = OperatorPOWL(operator=Operator.LOOP, children=[pack_produce, data_analyze])

# Create an XOR for the engage community and logistics plan
community_logistics_xor = OperatorPOWL(operator=Operator.XOR, children=[engage_community, logistics_plan])

# Create the root POWL model
root = StrictPartialOrder(nodes=[loop, crop_germinate_xor, pest_sensor_loop, harvest_quality_xor, pack_analyze_loop, community_logistics_xor])
root.order.add_edge(loop, crop_germinate_xor)
root.order.add_edge(loop, pest_sensor_loop)
root.order.add_edge(loop, harvest_quality_xor)
root.order.add_edge(loop, pack_analyze_loop)
root.order.add_edge(loop, community_logistics_xor)
root.order.add_edge(crop_germinate_xor, pest_sensor_loop)
root.order.add_edge(crop_germinate_xor, harvest_quality_xor)
root.order.add_edge(pest_sensor_loop, pack_analyze_loop)
root.order.add_edge(pest_sensor_loop, community_logistics_xor)
root.order.add_edge(harvest_quality_xor, pack_analyze_loop)
root.order.add_edge(harvest_quality_xor, community_logistics_xor)
root.order.add_edge(pack_analyze_loop, community_logistics_xor)

print(root)