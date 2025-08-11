import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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

# Define silent transitions (tau labels)
skip = SilentTransition()

# Define exclusive choice operators
xor1 = OperatorPOWL(operator=Operator.XOR, children=[seed_selection, ai_prediction])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[automated_planting, sensor_calibration])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[environment_adjust, nutrient_dosing])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[hydroponic_flow, robotic_pruning])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[health_monitor, harvesting_ops])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[data_analysis, predictive_check])
xor7 = OperatorPOWL(operator=Operator.XOR, children=[waste_composting, water_recycling])
xor8 = OperatorPOWL(operator=Operator.XOR, children=[eco_packaging, carbon_tracking])
xor9 = OperatorPOWL(operator=Operator.XOR, children=[logistics_dispatch])

# Define loop operators
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[xor1, xor2])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[xor3, xor4])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[xor5, xor6])
loop4 = OperatorPOWL(operator=Operator.LOOP, children=[xor7, xor8])
loop5 = OperatorPOWL(operator=Operator.LOOP, children=[xor9])

# Define the root of the POWL model
root = StrictPartialOrder(nodes=[loop1, loop2, loop3, loop4, loop5])
root.order.add_edge(loop1, xor2)
root.order.add_edge(loop1, xor3)
root.order.add_edge(loop1, xor4)
root.order.add_edge(loop2, xor5)
root.order.add_edge(loop2, xor6)
root.order.add_edge(loop3, xor7)
root.order.add_edge(loop3, xor8)
root.order.add_edge(loop4, xor9)

print(root)