import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities
seed_selection    = Transition(label='Seed Selection')
ai_prediction     = Transition(label='AI Prediction')
auto_planting     = Transition(label='Automated Planting')
sensor_calibration= Transition(label='Sensor Calibration')
env_adjust        = Transition(label='Environment Adjust')
nutrient_dosing   = Transition(label='Nutrient Dosing')
hydro_flow        = Transition(label='Hydroponic Flow')
robot_pruning     = Transition(label='Robotic Pruning')
health_monitor    = Transition(label='Health Monitor')
harvesting_ops    = Transition(label='Harvesting Ops')
data_analysis     = Transition(label='Data Analysis')
predictive_check  = Transition(label='Predictive Check')
waste_composting  = Transition(label='Waste Composting')
water_recycling   = Transition(label='Water Recycling')
eco_packaging     = Transition(label='Eco Packaging')
carbon_tracking   = Transition(label='Carbon Tracking')
logistics_dispatch= Transition(label='Logistics Dispatch')

# Silent transition for loop exit
skip = SilentTransition()

# 1) Sensor calibration + environment adjust in parallel
sensor_po = StrictPartialOrder(nodes=[sensor_calibration, env_adjust])
# No order edges => they can run in parallel

# 2) Nutrient dosing -> hydroponic flow in parallel
nutrient_po = StrictPartialOrder(nodes=[nutrient_dosing, hydro_flow])
nutrient_po.order.add_edge(nutrient_dosing, hydro_flow)

# 3) Robotic pruning -> health monitoring in parallel
robot_po = StrictPartialOrder(nodes=[robot_pruning, health_monitor])
robot_po.order.add_edge(robot_pruning, health_monitor)

# 4) Harvesting ops -> data analysis in parallel
harvest_po = StrictPartialOrder(nodes=[harvesting_ops, data_analysis])
harvest_po.order.add_edge(harvesting_ops, data_analysis)

# 5) Waste composting -> water recycling in parallel
waste_po = StrictPartialOrder(nodes=[waste_composting, water_recycling])
waste_po.order.add_edge(waste_composting, water_recycling)

# 6) Eco packaging -> carbon tracking in parallel
eco_po = StrictPartialOrder(nodes=[eco_packaging, carbon_tracking])
eco_po.order.add_edge(eco_packaging, carbon_tracking)

# 7) Predictive check -> logistics dispatch in parallel
predictive_po = StrictPartialOrder(nodes=[predictive_check, logistics_dispatch])
predictive_po.order.add_edge(predictive_check, logistics_dispatch)

# 8) Main execution sequence: 
#   - AI Prediction
#   - Auto Planting
#   - sensor_po (calibration + adjust)
#   - nutrient_po (dosing + flow)
#   - robot_po (pruning + monitor)
#   - harvest_po (ops + analysis)
#   - waste_po (compost + recycle)
#   - eco_po (packaging + tracking)
#   - predictive_po (check + dispatch)
main_seq = StrictPartialOrder(nodes=[
    ai_prediction,
    auto_planting,
    sensor_po,
    nutrient_po,
    robot_po,
    harvest_po,
    waste_po,
    eco_po,
    predictive_po
])
main_seq.order.add_edge(ai_prediction, auto_planting)
main_seq.order.add_edge(auto_planting, sensor_po)
main_seq.order.add_edge(sensor_po, nutrient_po)
main_seq.order.add_edge(nutrient_po, robot_po)
main_seq.order.add_edge(robot_po, harvest_po)
main_seq.order.add_edge(harvest_po, waste_po)
main_seq.order.add_edge(waste_po, eco_po)
main_seq.order.add_edge(eco_po, predictive_po)

# Loop: do main_seq, then either exit or do skip (no-op) then main_seq again
loop = OperatorPOWL(operator=Operator.LOOP, children=[main_seq, skip])

# Final root model: the loop
root = loop