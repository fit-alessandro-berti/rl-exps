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

# Define silent transitions for empty labels
skip = SilentTransition()

# Define the process tree structure
seed_selection_to_ai = OperatorPOWL(operator=Operator.XOR, children=[seed_selection, ai_prediction])
ai_to_planting = OperatorPOWL(operator=Operator.XOR, children=[ai_prediction, automated_planting])
planting_to_calibration = OperatorPOWL(operator=Operator.XOR, children=[automated_planting, sensor_calibration])
calibration_to_adjust = OperatorPOWL(operator=Operator.XOR, children=[sensor_calibration, environment_adjust])
adjust_to_dosing = OperatorPOWL(operator=Operator.XOR, children=[environment_adjust, nutrient_dosing])
dosing_to_flow = OperatorPOWL(operator=Operator.XOR, children=[nutrient_dosing, hydroponic_flow])
flow_to_pruning = OperatorPOWL(operator=Operator.XOR, children=[hydroponic_flow, robotic_pruning])
pruning_to_monitor = OperatorPOWL(operator=Operator.XOR, children=[robotic_pruning, health_monitor])
monitor_to_harvest = OperatorPOWL(operator=Operator.XOR, children=[health_monitor, harvesting_ops])
harvest_to_analysis = OperatorPOWL(operator=Operator.XOR, children=[harvesting_ops, data_analysis])
analysis_to_check = OperatorPOWL(operator=Operator.XOR, children=[data_analysis, predictive_check])
check_to_composting = OperatorPOWL(operator=Operator.XOR, children=[predictive_check, waste_composting])
composting_to_recycling = OperatorPOWL(operator=Operator.XOR, children=[waste_composting, water_recycling])
recycling_to_packaging = OperatorPOWL(operator=Operator.XOR, children=[water_recycling, eco_packaging])
packaging_to_tracking = OperatorPOWL(operator=Operator.XOR, children=[eco_packaging, carbon_tracking])
tracking_to_dispatch = OperatorPOWL(operator=Operator.XOR, children=[carbon_tracking, logistics_dispatch])

# Create the partial order structure
root = StrictPartialOrder(nodes=[seed_selection_to_ai, ai_to_planting, planting_to_calibration, calibration_to_adjust, adjust_to_dosing, dosing_to_flow, flow_to_pruning, pruning_to_monitor, monitor_to_harvest, harvest_to_analysis, analysis_to_check, check_to_composting, composting_to_recycling, recycling_to_packaging, packaging_to_tracking, tracking_to_dispatch])

# Define the partial order dependencies
root.order.add_edge(seed_selection_to_ai, ai_to_planting)
root.order.add_edge(ai_to_planting, planting_to_calibration)
root.order.add_edge(planting_to_calibration, calibration_to_adjust)
root.order.add_edge(calibration_to_adjust, adjust_to_dosing)
root.order.add_edge(adjust_to_dosing, dosing_to_flow)
root.order.add_edge(dosing_to_flow, flow_to_pruning)
root.order.add_edge(flow_to_pruning, pruning_to_monitor)
root.order.add_edge(pruning_to_monitor, monitor_to_harvest)
root.order.add_edge(monitor_to_harvest, harvest_to_analysis)
root.order.add_edge(harvest_to_analysis, analysis_to_check)
root.order.add_edge(analysis_to_check, check_to_composting)
root.order.add_edge(check_to_composting, composting_to_recycling)
root.order.add_edge(composting_to_recycling, recycling_to_packaging)
root.order.add_edge(recycling_to_packaging, packaging_to_tracking)
root.order.add_edge(packaging_to_tracking, tracking_to_dispatch)

print(root)