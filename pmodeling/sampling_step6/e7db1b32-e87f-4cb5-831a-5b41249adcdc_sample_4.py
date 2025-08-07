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

# Define the root of the partial order
root = StrictPartialOrder(nodes=[
    seed_selection,
    ai_prediction,
    automated_planting,
    sensor_calibration,
    environment_adjust,
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

# Since there are no dependencies in the given process description, no edges are added to the root.