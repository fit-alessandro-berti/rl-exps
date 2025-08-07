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
root = StrictPartialOrder(nodes=[
    seed_selection,
    ai_prediction,
    automated_planting,
    sensor_calibration,
    environment_adjustment,
    nutrient_dosing,
    hydroponic_flow,
    robotic_pruning,
    health_monitor,
    harvesting_ops,
    data_analysis,
    predictive_check,
    waste_composting,
    water_recycling,
    eco_packaging,
    carbon_tracking,
    logistics_dispatch
])

# Define the dependencies
root.order.add_edge(seed_selection, ai_prediction)
root.order.add_edge(seed_selection, automated_planting)
root.order.add_edge(ai_prediction, sensor_calibration)
root.order.add_edge(ai_prediction, environment_adjustment)
root.order.add_edge(ai_prediction, nutrient_dosing)
root.order.add_edge(ai_prediction, hydroponic_flow)
root.order.add_edge(ai_prediction, robotic_pruning)
root.order.add_edge(ai_prediction, health_monitor)
root.order.add_edge(ai_prediction, harvesting_ops)
root.order.add_edge(health_monitor, data_analysis)
root.order.add_edge(health_monitor, predictive_check)
root.order.add_edge(harvesting_ops, waste_composting)
root.order.add_edge(harvesting_ops, water_recycling)
root.order.add_edge(harvesting_ops, eco_packaging)
root.order.add_edge(harvesting_ops, carbon_tracking)
root.order.add_edge(harvesting_ops, logistics_dispatch)

# Save the final result in the variable 'root'