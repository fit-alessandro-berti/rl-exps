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

# Define silent transitions
skip = SilentTransition()

# Define loop and exclusive choice nodes
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[health_monitor, data_analysis])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[water_recycling, carbon_tracking])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[eco_packaging, logistics_dispatch])
xor1 = OperatorPOWL(operator=Operator.XOR, children=[sensor_calibration, environment_adjust])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[nutrient_dosing, hydroponic_flow])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[robotic_pruning, harvesting_ops])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[predictive_check, waste_composting])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[seed_selection, ai_prediction])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[automated_planting, skip])

# Define the root POWL model
root = StrictPartialOrder(nodes=[xor5, xor6, xor1, xor2, xor3, xor4, loop1, loop2, loop3])
root.order.add_edge(xor5, xor6)
root.order.add_edge(xor6, xor1)
root.order.add_edge(xor1, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, loop1)
root.order.add_edge(loop1, loop2)
root.order.add_edge(loop2, loop3)
root.order.add_edge(loop3, loop1)

print(root)