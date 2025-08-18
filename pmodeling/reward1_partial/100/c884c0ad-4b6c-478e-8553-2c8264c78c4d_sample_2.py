import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model for the process
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

# Define the loop and XOR nodes
loop_node = OperatorPOWL(operator=Operator.LOOP, children=[climate_control, pest_monitoring, growth_analysis, robotic_harvest, quality_sort])
xor_node = OperatorPOWL(operator=Operator.XOR, children=[waste_recycling, data_analytics, maintenance_alert])

# Define the root of the POWL model
root = StrictPartialOrder(nodes=[seed_sourcing, germination_check, nutrient_mix, automated_planting, loop_node, xor_node])
root.order.add_edge(seed_sourcing, germination_check)
root.order.add_edge(germination_check, nutrient_mix)
root.order.add_edge(nutrient_mix, automated_planting)
root.order.add_edge(automated_planting, loop_node)
root.order.add_edge(loop_node, xor_node)

# Print the root of the POWL model
print(root)