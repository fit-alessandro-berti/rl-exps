from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL nodes
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

# Define the POWL operators
xor = OperatorPOWL(operator=Operator.XOR, children=[pest_control, sensor_deploy])
loop = OperatorPOWL(operator=Operator.LOOP, children=[data_analyze, engage_community])
xor_loop = OperatorPOWL(operator=Operator.XOR, children=[climate_calibrate, loop])
xor_xor = OperatorPOWL(operator=Operator.XOR, children=[xor, xor_loop])
xor_xor_loop = OperatorPOWL(operator=Operator.XOR, children=[logistics_plan, xor_xor])
xor_xor_loop_loop = OperatorPOWL(operator=Operator.XOR, children=[nutrient_prep, xor_xor_loop])
xor_xor_loop_loop_loop = OperatorPOWL(operator=Operator.XOR, children=[crop_select, xor_xor_loop_loop])

# Define the POWL model
root = StrictPartialOrder(nodes=[site_survey, rack_design, system_setup, xor_xor_loop_loop_loop])
root.order.add_edge(site_survey, rack_design)
root.order.add_edge(rack_design, system_setup)
root.order.add_edge(system_setup, xor_xor_loop_loop_loop)

# Define the dependencies between nodes
root.order.add_edge(site_survey, xor_xor_loop_loop_loop)
root.order.add_edge(rack_design, xor_xor_loop_loop_loop)
root.order.add_edge(system_setup, xor_xor_loop_loop_loop)
root.order.add_edge(xor_xor_loop_loop_loop, xor)
root.order.add_edge(xor_xor_loop_loop_loop, loop)
root.order.add_edge(xor, xor_loop)
root.order.add_edge(xor_loop, xor_xor)
root.order.add_edge(xor_xor, xor_xor_loop)
root.order.add_edge(xor_xor_loop, logistics_plan)
root.order.add_edge(xor_xor_loop, xor_xor_loop_loop)
root.order.add_edge(xor_xor_loop_loop, nutrient_prep)
root.order.add_edge(xor_xor_loop_loop, crop_select)

# Return the root of the POWL model
print(root)