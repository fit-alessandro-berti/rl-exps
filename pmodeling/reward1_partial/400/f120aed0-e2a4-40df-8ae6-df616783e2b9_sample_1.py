import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
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

# Define the control-flow operators
xor = OperatorPOWL(operator=Operator.XOR, children=[pest_control, sensor_deploy])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[quality_check, pack_produce])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[logistics_plan, engage_community])
loop = OperatorPOWL(operator=Operator.LOOP, children=[climate_calibrate, nutrient_prep])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[seed_germinate, crop_select])
root = StrictPartialOrder(nodes=[site_survey, rack_design, system_setup, loop, xor, xor2, xor3])
root.order.add_edge(site_survey, rack_design)
root.order.add_edge(rack_design, system_setup)
root.order.add_edge(system_setup, loop)
root.order.add_edge(loop, xor)
root.order.add_edge(xor, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, loop)
root.order.add_edge(loop, xor4)
root.order.add_edge(xor4, loop)