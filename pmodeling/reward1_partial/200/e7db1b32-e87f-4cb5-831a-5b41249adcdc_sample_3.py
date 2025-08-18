import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
seed_selection = Transition(label='Seed Selection')
ai_prediction = Transition(label='AI Prediction')
automated_planting = Transition(label='Automated Planting')
sensor_calibration = Transition(label='Sensor Calibration')
environment_adjust = Transition(label='Environment Adjust')
nutrient_dosing = Transition(label='Nutrient Dosing')
hydroponic_flow = Transition(label='Hydroponic Flow')
robotic_pruning = Transition(label='Robotic Pruning')
health_monitor = Transition(label='Health Monitor')
harvesting_ops = Transition(label='Harvesting Ops')
data_analysis = Transition(label='Data Analysis')
predictive_check = Transition(label='Predictive Check')
waste_composting = Transition(label='Waste Composting')
water_recycling = Transition(label='Water Recycling')
eco_packaging = Transition(label='Eco Packaging')
carbon_tracking = Transition(label='Carbon Tracking')
logistics_dispatch = Transition(label='Logistics Dispatch')

# Define silent transitions (for empty labels)
skip = SilentTransition()

# Define the POWL model structure
loop_seed_selection = OperatorPOWL(operator=Operator.LOOP, children=[seed_selection, ai_prediction])
xor_planting_environment = OperatorPOWL(operator=Operator.XOR, children=[automated_planting, sensor_calibration, environment_adjust])
loop_nutrient_dosing = OperatorPOWL(operator=Operator.LOOP, children=[nutrient_dosing, hydroponic_flow])
xor_pruning_monitoring = OperatorPOWL(operator=Operator.XOR, children=[robotic_pruning, health_monitor])
loop_harvesting_ops = OperatorPOWL(operator=Operator.LOOP, children=[harvesting_ops, data_analysis, predictive_check])
xor_waste_processing = OperatorPOWL(operator=Operator.XOR, children=[waste_composting, water_recycling])
loop_eco_packaging = OperatorPOWL(operator=Operator.LOOP, children=[eco_packaging, carbon_tracking])
xor_logistics_dispatch = OperatorPOWL(operator=Operator.XOR, children=[logistics_dispatch, skip])

# Create the root node with all activities as children
root = StrictPartialOrder(nodes=[loop_seed_selection, xor_planting_environment, loop_nutrient_dosing, xor_pruning_monitoring, loop_harvesting_ops, xor_waste_processing, loop_eco_packaging, xor_logistics_dispatch])
root.order.add_edge(loop_seed_selection, xor_planting_environment)
root.order.add_edge(xor_planting_environment, loop_nutrient_dosing)
root.order.add_edge(loop_nutrient_dosing, xor_pruning_monitoring)
root.order.add_edge(xor_pruning_monitoring, loop_harvesting_ops)
root.order.add_edge(loop_harvesting_ops, xor_waste_processing)
root.order.add_edge(xor_waste_processing, loop_eco_packaging)
root.order.add_edge(loop_eco_packaging, xor_logistics_dispatch)