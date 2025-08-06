import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define the activities
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

# Define the operators
xor1 = OperatorPOWL(operator=Operator.XOR, children=[ai_prediction, sensor_calibration])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[environment_adjust, nutrient_dosing])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[hydroponic_flow, robotic_pruning])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[health_monitor, predictive_check])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[waste_composting, water_recycling])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[eco_packaging, carbon_tracking])
xor7 = OperatorPOWL(operator=Operator.XOR, children=[logistics_dispatch])

# Define the partial order
root = StrictPartialOrder(nodes=[xor1, xor2, xor3, xor4, xor5, xor6, xor7])

# Add the edges
root.order.add_edge(xor1, xor2)
root.order.add_edge(xor1, xor3)
root.order.add_edge(xor1, xor4)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor2, xor4)
root.order.add_edge(xor3, xor5)
root.order.add_edge(xor3, xor6)
root.order.add_edge(xor4, xor7)
root.order.add_edge(xor5, xor7)
root.order.add_edge(xor6, xor7)

# Print the root model
print(root)