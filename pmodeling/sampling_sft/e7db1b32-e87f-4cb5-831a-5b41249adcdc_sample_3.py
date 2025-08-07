import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
seed_sel = Transition(label='Seed Selection')
ai_pred = Transition(label='AI Prediction')
auto_plant = Transition(label='Automated Planting')
sensor_calib = Transition(label='Sensor Calibration')
env_adjust = Transition(label='Environment Adjust')
nutrient_dose = Transition(label='Nutrient Dosing')
hydro_flow = Transition(label='Hydroponic Flow')
robot_prune = Transition(label='Robotic Pruning')
health_monitor = Transition(label='Health Monitor')
harvest_ops = Transition(label='Harvesting Ops')
data_analysis = Transition(label='Data Analysis')
predict_check = Transition(label='Predictive Check')
waste_comp = Transition(label='Waste Composting')
water_recycle = Transition(label='Water Recycling')
eco_packaging = Transition(label='Eco Packaging')
carbon_track = Transition(label='Carbon Tracking')
logistics_dispatch = Transition(label='Logistics Dispatch')

# Loop for continuous environmental adjustments, nutrient dosing, and hydro flow
loop_env = OperatorPOWL(operator=Operator.LOOP, children=[env_adjust, nutrient_dose, hydro_flow])

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    seed_sel, ai_pred, auto_plant,
    loop_env,
    robot_prune, health_monitor, harvest_ops,
    data_analysis, predict_check,
    waste_comp, water_recycle, eco_packaging, carbon_track, logistics_dispatch
])

# Define the control-flow dependencies
root.order.add_edge(seed_sel, ai_pred)
root.order.add_edge(ai_pred, auto_plant)

root.order.add_edge(auto_plant, loop_env)

# Body of the loop: pruning, health monitoring, harvesting
root.order.add_edge(loop_env, robot_prune)
root.order.add_edge(robot_prune, health_monitor)
root.order.add_edge(health_monitor, harvest_ops)

# After harvesting, analysis and predictive checks
root.order.add_edge(harvest_ops, data_analysis)
root.order.add_edge(data_analysis, predict_check)

# Finally, waste recycling, packaging, tracking, and logistics dispatch
root.order.add_edge(predict_check, waste_comp)
root.order.add_edge(waste_comp, water_recycle)
root.order.add_edge(water_recycle, eco_packaging)
root.order.add_edge(eco_packaging, carbon_track)
root.order.add_edge(carbon_track, logistics_dispatch)