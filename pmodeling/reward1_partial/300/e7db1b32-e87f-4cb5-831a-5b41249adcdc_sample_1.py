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

# Define control-flow operators
xor = OperatorPOWL(operator=Operator.XOR, children=[harvesting_ops, predictive_check])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[data_analysis, predictive_check])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[waste_composting, water_recycling])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[eco_packaging, carbon_tracking])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[logistics_dispatch, carbon_tracking])

# Define the root of the POWL model
root = StrictPartialOrder(nodes=[seed_selection, ai_prediction, automated_planting, sensor_calibration, environment_adjust, nutrient_dosing, hydroponic_flow, robotic_pruning, health_monitor, xor, xor2, xor3, xor4, xor5])

# Define the partial order dependencies
root.order.add_edge(seed_selection, ai_prediction)
root.order.add_edge(seed_selection, automated_planting)
root.order.add_edge(ai_prediction, sensor_calibration)
root.order.add_edge(sensor_calibration, environment_adjust)
root.order.add_edge(environment_adjust, nutrient_dosing)
root.order.add_edge(nutrient_dosing, hydroponic_flow)
root.order.add_edge(hydroponic_flow, robotic_pruning)
root.order.add_edge(robotic_pruning, health_monitor)
root.order.add_edge(health_monitor, xor)
root.order.add_edge(xor, data_analysis)
root.order.add_edge(data_analysis, predictive_check)
root.order.add_edge(predictive_check, xor2)
root.order.add_edge(xor2, waste_composting)
root.order.add_edge(waste_composting, water_recycling)
root.order.add_edge(water_recycling, xor3)
root.order.add_edge(xor3, eco_packaging)
root.order.add_edge(eco_packaging, carbon_tracking)
root.order.add_edge(carbon_tracking, xor4)
root.order.add_edge(xor4, logistics_dispatch)
root.order.add_edge(logistics_dispatch, carbon_tracking)

print(root)