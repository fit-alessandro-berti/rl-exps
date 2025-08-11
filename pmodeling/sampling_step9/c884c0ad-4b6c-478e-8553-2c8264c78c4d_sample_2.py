import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
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

skip = SilentTransition()

# Define the partial order nodes
loop_seed_sourcing = OperatorPOWL(operator=Operator.LOOP, children=[seed_sourcing, germination_check])
xor_nutrient_mix = OperatorPOWL(operator=Operator.XOR, children=[nutrient_mix, skip])
loop_automated_planting = OperatorPOWL(operator=Operator.LOOP, children=[automated_planting, climate_control])
xor_crop_scanning = OperatorPOWL(operator=Operator.XOR, children=[crop_scanning, skip])
loop_pest_monitoring = OperatorPOWL(operator=Operator.LOOP, children=[pest_monitoring, growth_analysis])
xor_robotic_harvest = OperatorPOWL(operator=Operator.XOR, children=[robotic_harvest, skip])
xor_quality_sort = OperatorPOWL(operator=Operator.XOR, children=[quality_sort, skip])
xor_eco_packaging = OperatorPOWL(operator=Operator.XOR, children=[eco_packaging, skip])
xor_blockchain_track = OperatorPOWL(operator=Operator.XOR, children=[blockchain_track, skip])
xor_route_planning = OperatorPOWL(operator=Operator.XOR, children=[route_planning, skip])
xor_feedback_collect = OperatorPOWL(operator=Operator.XOR, children=[feedback_collect, skip])
xor_waste_recycling = OperatorPOWL(operator=Operator.XOR, children=[waste_recycling, skip])
xor_data_analytics = OperatorPOWL(operator=Operator.XOR, children=[data_analytics, skip])
xor_demand_forecast = OperatorPOWL(operator=Operator.XOR, children=[demand_forecast, skip])
xor_maintenance_alert = OperatorPOWL(operator=Operator.XOR, children=[maintenance_alert, skip])

# Define the root node
root = StrictPartialOrder(nodes=[loop_seed_sourcing, xor_nutrient_mix, loop_automated_planting, xor_crop_scanning, loop_pest_monitoring, xor_robotic_harvest, xor_quality_sort, xor_eco_packaging, xor_blockchain_track, xor_route_planning, xor_feedback_collect, xor_waste_recycling, xor_data_analytics, xor_demand_forecast, xor_maintenance_alert])
root.order.add_edge(loop_seed_sourcing, xor_nutrient_mix)
root.order.add_edge(loop_automated_planting, xor_crop_scanning)
root.order.add_edge(loop_pest_monitoring, xor_robotic_harvest)
root.order.add_edge(xor_quality_sort, xor_eco_packaging)
root.order.add_edge(xor_blockchain_track, xor_route_planning)
root.order.add_edge(xor_feedback_collect, xor_waste_recycling)
root.order.add_edge(xor_data_analytics, xor_demand_forecast)
root.order.add_edge(xor_maintenance_alert, xor_demand_forecast)

# Print the POWL model
print(root)