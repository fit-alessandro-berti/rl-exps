import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
seed_sourcing = Transition(label='Seed Sourcing')
germination_check = Transition(label='Germination Check')
nutrient_mix = Transition(label='Nutrient Mix')
automated_planting = Transition(label='Automated Planting')
climate_control = Transition(label='Climate Control')
crop_scanning = Transition(label='Crop Scanning')
pest_monitoring = Transition(label='Pest Monitoring')
growth_analysis = Transition(label='Growth Analysis')
robotic_harvest = Transition(label='Robotic Harvest')
quality_sort = Transition(label='Quality Sort')
eco_packaging = Transition(label='Eco Packaging')
blockchain_track = Transition(label='Blockchain Track')
route_planning = Transition(label='Route Planning')
feedback_collect = Transition(label='Feedback Collect')
waste_recycling = Transition(label='Waste Recycling')
data_analytics = Transition(label='Data Analytics')
demand_forecast = Transition(label='Demand Forecast')
maintenance_alert = Transition(label='Maintenance Alert')

# Define the POWL model
loop_crop_health = OperatorPOWL(operator=Operator.LOOP, children=[crop_scanning, pest_monitoring, growth_analysis])
xor_routing = OperatorPOWL(operator=Operator.XOR, children=[route_planning, feedback_collect])
xor_waste = OperatorPOWL(operator=Operator.XOR, children=[waste_recycling, data_analytics])
xor_demand = OperatorPOWL(operator=Operator.XOR, children=[demand_forecast, maintenance_alert])

root = StrictPartialOrder(nodes=[seed_sourcing, germination_check, nutrient_mix, automated_planting, climate_control, loop_crop_health, xor_routing, eco_packaging, blockchain_track, xor_waste, xor_demand])
root.order.add_edge(loop_crop_health, xor_routing)
root.order.add_edge(loop_crop_health, xor_waste)
root.order.add_edge(loop_crop_health, xor_demand)

print(root)