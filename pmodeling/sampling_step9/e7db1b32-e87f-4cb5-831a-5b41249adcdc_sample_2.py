import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
seed_selection = Transition(label='Seed Selection')
ai_prediction = Transition(label='AI Prediction')
automated_planting = Transition(label='Automated Planting')
sensor_calibration = Transition(label='Sensor Calibration')
environment_adjustment = Transition(label='Environment Adjust')
nutrient_dosing = Transition(label='Nutrient Dosing')
hydroponic_flow = Transition(label='Hydroponic Flow')
robotic_pruning = Transition(label='Robotic Pruning')
health_monitoring = Transition(label='Health Monitor')
harvesting_ops = Transition(label='Harvesting Ops')
data_analysis = Transition(label='Data Analysis')
predictive_check = Transition(label='Predictive Check')
waste_composting = Transition(label='Waste Composting')
water_recycling = Transition(label='Water Recycling')
eco_packaging = Transition(label='Eco Packaging')
carbon_tracking = Transition(label='Carbon Tracking')
logistics_dispatch = Transition(label='Logistics Dispatch')

# Define the silent transitions
skip = SilentTransition()

# Define the sub-processes
predictive_subprocess = StrictPartialOrder(nodes=[predictive_check, health_monitoring])
harvesting_subprocess = StrictPartialOrder(nodes=[harvesting_ops, eco_packaging, carbon_tracking])
logistics_subprocess = StrictPartialOrder(nodes=[logistics_dispatch])

# Define the main process
seed_selection_to_ai_prediction = OperatorPOWL(operator=Operator.XOR, children=[seed_selection, ai_prediction])
ai_prediction_to_automated_planting = OperatorPOWL(operator=Operator.XOR, children=[ai_prediction, automated_planting])
automated_planting_to_sensor_calibration = OperatorPOWL(operator=Operator.XOR, children=[automated_planting, sensor_calibration])
sensor_calibration_to_environment_adjustment = OperatorPOWL(operator=Operator.XOR, children=[sensor_calibration, environment_adjustment])
environment_adjustment_to_nutrient_dosing = OperatorPOWL(operator=Operator.XOR, children=[environment_adjustment, nutrient_dosing])
nutrient_dosing_to_hydroponic_flow = OperatorPOWL(operator=Operator.XOR, children=[nutrient_dosing, hydroponic_flow])
hydroponic_flow_to_robotic_pruning = OperatorPOWL(operator=Operator.XOR, children=[hydroponic_flow, robotic_pruning])
robotic_pruning_to_health_monitoring = OperatorPOWL(operator=Operator.XOR, children=[robotic_pruning, health_monitoring])
health_monitoring_to_harvesting_ops = OperatorPOWL(operator=Operator.XOR, children=[health_monitoring, harvesting_ops])
harvesting_ops_to_eco_packaging = OperatorPOWL(operator=Operator.XOR, children=[harvesting_ops, eco_packaging])
eco_packaging_to_carbon_tracking = OperatorPOWL(operator=Operator.XOR, children=[eco_packaging, carbon_tracking])
carbon_tracking_to_logistics_dispatch = OperatorPOWL(operator=Operator.XOR, children=[carbon_tracking, logistics_dispatch])
logistics_dispatch_to_skip = OperatorPOWL(operator=Operator.XOR, children=[logistics_dispatch, skip])

# Define the main loop
main_loop = OperatorPOWL(operator=Operator.LOOP, children=[seed_selection_to_ai_prediction, ai_prediction_to_automated_planting, automated_planting_to_sensor_calibration, sensor_calibration_to_environment_adjustment, environment_adjustment_to_nutrient_dosing, nutrient_dosing_to_hydroponic_flow, hydroponic_flow_to_robotic_pruning, robotic_pruning_to_health_monitoring, health_monitoring_to_harvesting_ops, harvesting_ops_to_eco_packaging, eco_packaging_to_carbon_tracking, carbon_tracking_to_logistics_dispatch])

# Define the final loop
final_loop = OperatorPOWL(operator=Operator.LOOP, children=[main_loop, predictive_subprocess, harvesting_subprocess, logistics_subprocess])

# Define the root
root = StrictPartialOrder(nodes=[final_loop])
root.order.add_edge(final_loop, predictive_subprocess)
root.order.add_edge(final_loop, harvesting_subprocess)
root.order.add_edge(final_loop, logistics_subprocess)