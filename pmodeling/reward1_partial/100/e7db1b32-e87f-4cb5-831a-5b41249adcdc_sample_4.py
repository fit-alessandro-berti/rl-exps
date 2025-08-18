import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities)
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

# Define the control flow operators
xor = OperatorPOWL(operator=Operator.XOR, children=[ai_prediction, automated_planting])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[sensor_calibration, environment_adjust])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[nutrient_dosing, hydroponic_flow])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[robotic_pruning, health_monitor])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[harvesting_ops, data_analysis])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[predictive_check, waste_composting])
xor7 = OperatorPOWL(operator=Operator.XOR, children=[water_recycling, eco_packaging])
xor8 = OperatorPOWL(operator=Operator.XOR, children=[carbon_tracking, logistics_dispatch])

# Define the loops
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[xor, xor2, xor3, xor4, xor5, xor6, xor7, xor8])

# Define the root
root = StrictPartialOrder(nodes=[loop1])