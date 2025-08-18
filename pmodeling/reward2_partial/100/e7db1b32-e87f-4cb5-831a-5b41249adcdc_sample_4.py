from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for each activity
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

# Define the partial order
root = StrictPartialOrder(nodes=[seed_selection, ai_prediction, automated_planting, sensor_calibration, environment_adjust, nutrient_dosing, hydroponic_flow, robotic_pruning, health_monitor, harvesting_ops, data_analysis, predictive_check, waste_composting, water_recycling, eco_packaging, carbon_tracking, logistics_dispatch])

# Define the order of execution
root.order.add_edge(seed_selection, ai_prediction)
root.order.add_edge(ai_prediction, automated_planting)
root.order.add_edge(automated_planting, sensor_calibration)
root.order.add_edge(sensor_calibration, environment_adjust)
root.order.add_edge(environment_adjust, nutrient_dosing)
root.order.add_edge(nutrient_dosing, hydroponic_flow)
root.order.add_edge(hydroponic_flow, robotic_pruning)
root.order.add_edge(robotic_pruning, health_monitor)
root.order.add_edge(health_monitor, harvesting_ops)
root.order.add_edge(harvesting_ops, data_analysis)
root.order.add_edge(data_analysis, predictive_check)
root.order.add_edge(predictive_check, waste_composting)
root.order.add_edge(waste_composting, water_recycling)
root.order.add_edge(water_recycling, eco_packaging)
root.order.add_edge(eco_packaging, carbon_tracking)
root.order.add_edge(carbon_tracking, logistics_dispatch)

print(root)