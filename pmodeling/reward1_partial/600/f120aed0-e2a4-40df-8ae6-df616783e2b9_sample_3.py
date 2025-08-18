import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions
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

# Define loop for sensor deployment and pest control
sensor_pest_loop = OperatorPOWL(operator=Operator.LOOP, children=[sensor_deploy, pest_control])

# Define exclusive choice for crop selection and seed germination
crop_germinate_choice = OperatorPOWL(operator=Operator.XOR, children=[crop_select, seed_germinate])

# Define root POWL model
root = StrictPartialOrder(nodes=[site_survey, rack_design, system_setup, climate_calibrate, nutrient_prep, crop_germinate_choice, sensor_pest_loop, harvest_automate, quality_check, pack_produce, data_analyze, engage_community, logistics_plan])
root.order.add_edge(site_survey, rack_design)
root.order.add_edge(rack_design, system_setup)
root.order.add_edge(system_setup, climate_calibrate)
root.order.add_edge(climate_calibrate, nutrient_prep)
root.order.add_edge(nutrient_prep, crop_germinate_choice)
root.order.add_edge(crop_germinate_choice, sensor_pest_loop)
root.order.add_edge(sensor_pest_loop, harvest_automate)
root.order.add_edge(harvest_automate, quality_check)
root.order.add_edge(quality_check, pack_produce)
root.order.add_edge(pack_produce, data_analyze)
root.order.add_edge(data_analyze, engage_community)
root.order.add_edge(engage_community, logistics_plan)