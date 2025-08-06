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

# Define the partial order
root = StrictPartialOrder(
    nodes=[
        seed_sourcing,
        germination_check,
        nutrient_mix,
        automated_planting,
        climate_control,
        crop_scanning,
        pest_monitoring,
        growth_analysis,
        robotic_harvest,
        quality_sort,
        eco_packaging,
        blockchain_track,
        route_planning,
        feedback_collect,
        waste_recycling,
        data_analytics,
        demand_forecast,
        maintenance_alert
    ],
    order=[
        # Seed Sourcing
        (seed_sourcing, germination_check),
        # Germination Check
        (germination_check, nutrient_mix),
        (germination_check, automated_planting),
        # Nutrient Mix
        (nutrient_mix, automated_planting),
        # Automated Planting
        (automated_planting, climate_control),
        # Climate Control
        (climate_control, crop_scanning),
        (climate_control, pest_monitoring),
        # Crop Scanning
        (crop_scanning, growth_analysis),
        # Pest Monitoring
        (pest_monitoring, growth_analysis),
        # Growth Analysis
        (growth_analysis, robotic_harvest),
        # Robotic Harvest
        (robotic_harvest, quality_sort),
        # Quality Sort
        (quality_sort, eco_packaging),
        # Eco Packaging
        (eco_packaging, blockchain_track),
        # Blockchain Track
        (blockchain_track, route_planning),
        # Route Planning
        (route_planning, feedback_collect),
        # Feedback Collect
        (feedback_collect, waste_recycling),
        # Waste Recycling
        (waste_recycling, data_analytics),
        # Data Analytics
        (data_analytics, demand_forecast),
        # Demand Forecast
        (demand_forecast, maintenance_alert)
    ]
)

# Add dependencies
root.order.add_edge(seed_sourcing, germination_check)
root.order.add_edge(germination_check, nutrient_mix)
root.order.add_edge(germination_check, automated_planting)
root.order.add_edge(nutrient_mix, automated_planting)
root.order.add_edge(automated_planting, climate_control)
root.order.add_edge(climate_control, crop_scanning)
root.order.add_edge(climate_control, pest_monitoring)
root.order.add_edge(crop_scanning, growth_analysis)
root.order.add_edge(pest_monitoring, growth_analysis)
root.order.add_edge(growth_analysis, robotic_harvest)
root.order.add_edge(robotic_harvest, quality_sort)
root.order.add_edge(quality_sort, eco_packaging)
root.order.add_edge(eco_packaging, blockchain_track)
root.order.add_edge(blockchain_track, route_planning)
root.order.add_edge(route_planning, feedback_collect)
root.order.add_edge(feedback_collect, waste_recycling)
root.order.add_edge(waste_recycling, data_analytics)
root.order.add_edge(data_analytics, demand_forecast)
root.order.add_edge(demand_forecast, maintenance_alert)