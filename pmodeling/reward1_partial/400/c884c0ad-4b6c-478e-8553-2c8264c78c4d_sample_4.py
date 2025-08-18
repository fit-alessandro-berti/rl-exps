from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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

# Process flow
seed_sourcing_node = StrictPartialOrder(nodes=[seed_sourcing])
germination_check_node = StrictPartialOrder(nodes=[germination_check])
nutrient_mix_node = StrictPartialOrder(nodes=[nutrient_mix])
automated_planting_node = StrictPartialOrder(nodes=[automated_planting])
climate_control_node = StrictPartialOrder(nodes=[climate_control])
crop_scanning_node = StrictPartialOrder(nodes=[crop_scanning])
pest_monitoring_node = StrictPartialOrder(nodes=[pest_monitoring])
growth_analysis_node = StrictPartialOrder(nodes=[growth_analysis])
robotic_harvest_node = StrictPartialOrder(nodes=[robotic_harvest])
quality_sort_node = StrictPartialOrder(nodes=[quality_sort])
eco_packaging_node = StrictPartialOrder(nodes=[eco_packaging])
blockchain_track_node = StrictPartialOrder(nodes=[blockchain_track])
route_planning_node = StrictPartialOrder(nodes=[route_planning])
feedback_collect_node = StrictPartialOrder(nodes=[feedback_collect])
waste_recycling_node = StrictPartialOrder(nodes=[waste_recycling])
data_analytics_node = StrictPartialOrder(nodes=[data_analytics])
demand_forecast_node = StrictPartialOrder(nodes=[demand_forecast])
maintenance_alert_node = StrictPartialOrder(nodes=[maintenance_alert])

# Define the partial order graph
root = StrictPartialOrder(nodes=[
    seed_sourcing_node,
    germination_check_node,
    nutrient_mix_node,
    automated_planting_node,
    climate_control_node,
    crop_scanning_node,
    pest_monitoring_node,
    growth_analysis_node,
    robotic_harvest_node,
    quality_sort_node,
    eco_packaging_node,
    blockchain_track_node,
    route_planning_node,
    feedback_collect_node,
    waste_recycling_node,
    data_analytics_node,
    demand_forecast_node,
    maintenance_alert_node
])

# Define the partial order relationships
root.order.add_edge(seed_sourcing_node, germination_check_node)
root.order.add_edge(seed_sourcing_node, nutrient_mix_node)
root.order.add_edge(germination_check_node, automated_planting_node)
root.order.add_edge(automated_planting_node, climate_control_node)
root.order.add_edge(climate_control_node, crop_scanning_node)
root.order.add_edge(crop_scanning_node, pest_monitoring_node)
root.order.add_edge(pest_monitoring_node, growth_analysis_node)
root.order.add_edge(growth_analysis_node, robotic_harvest_node)
root.order.add_edge(robotic_harvest_node, quality_sort_node)
root.order.add_edge(quality_sort_node, eco_packaging_node)
root.order.add_edge(eco_packaging_node, blockchain_track_node)
root.order.add_edge(blockchain_track_node, route_planning_node)
root.order.add_edge(route_planning_node, feedback_collect_node)
root.order.add_edge(feedback_collect_node, waste_recycling_node)
root.order.add_edge(waste_recycling_node, data_analytics_node)
root.order.add_edge(data_analytics_node, demand_forecast_node)
root.order.add_edge(demand_forecast_node, maintenance_alert_node)

# Print the root POWL model
print(root)