import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
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

# Define silent transitions
skip = SilentTransition()

# Define loops and XORs
loop_site_survey = OperatorPOWL(operator=Operator.LOOP, children=[site_survey, skip])
loop_climate_calibrate = OperatorPOWL(operator=Operator.LOOP, children=[climate_calibrate, skip])
loop_pest_control = OperatorPOWL(operator=Operator.LOOP, children=[pest_control, skip])
loop_logistics_plan = OperatorPOWL(operator=Operator.LOOP, children=[logistics_plan, skip])

xor_sensor_deploy = OperatorPOWL(operator=Operator.XOR, children=[sensor_deploy, skip])

xor_data_analyze = OperatorPOWL(operator=Operator.XOR, children=[data_analyze, skip])

xor_engage_community = OperatorPOWL(operator=Operator.XOR, children=[engage_community, skip])

root = StrictPartialOrder(nodes=[loop_site_survey, loop_climate_calibrate, loop_pest_control, loop_logistics_plan, xor_sensor_deploy, xor_data_analyze, xor_engage_community, rack_design, system_setup, nutrient_prep, crop_select, seed_germinate, harvest_automate, quality_check, pack_produce])
root.order.add_edge(loop_site_survey, rack_design)
root.order.add_edge(loop_climate_calibrate, system_setup)
root.order.add_edge(loop_pest_control, nutrient_prep)
root.order.add_edge(loop_logistics_plan, crop_select)
root.order.add_edge(xor_sensor_deploy, seed_germinate)
root.order.add_edge(xor_data_analyze, quality_check)
root.order.add_edge(xor_engage_community, pack_produce)

print(root)