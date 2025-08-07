import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
seed_sourcing    = Transition(label='Seed Sourcing')
germination      = Transition(label='Germination Check')
nutrient_mix     = Transition(label='Nutrient Mix')
automated_planting = Transition(label='Automated Planting')
climate_control  = Transition(label='Climate Control')
crop_scanning    = Transition(label='Crop Scanning')
pest_monitoring  = Transition(label='Pest Monitoring')
growth_analysis  = Transition(label='Growth Analysis')
robotic_harvest  = Transition(label='Robotic Harvest')
quality_sort     = Transition(label='Quality Sort')
eco_packaging    = Transition(label='Eco Packaging')
blockchain_track = Transition(label='Blockchain Track')
route_planning   = Transition(label='Route Planning')
feedback_collect = Transition(label='Feedback Collect')
waste_recycling  = Transition(label='Waste Recycling')
data_analytics   = Transition(label='Data Analytics')
demand_forecast  = Transition(label='Demand Forecast')
maintenance_alert = Transition(label='Maintenance Alert')

# Build the core growth sequence as a partial order
growth = StrictPartialOrder(nodes=[
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
])
growth.order.add_edge(nutrient_mix, automated_planting)
growth.order.add_edge(automated_planting, climate_control)
growth.order.add_edge(climate_control, crop_scanning)
growth.order.add_edge(crop_scanning, pest_monitoring)
growth.order.add_edge(pest_monitoring, growth_analysis)
growth.order.add_edge(growth_analysis, robotic_harvest)
growth.order.add_edge(robotic_harvest, quality_sort)
growth.order.add_edge(quality_sort, eco_packaging)
growth.order.add_edge(eco_packaging, blockchain_track)
growth.order.add_edge(blockchain_track, route_planning)
growth.order.add_edge(route_planning, feedback_collect)
growth.order.add_edge(feedback_collect, waste_recycling)
growth.order.add_edge(waste_recycling, data_analytics)
growth.order.add_edge(data_analytics, demand_forecast)
growth.order.add_edge(demand_forecast, maintenance_alert)

# Loop: after each crop cycle, do demand forecast, maintenance alert, then repeat
loop = OperatorPOWL(operator=Operator.LOOP, children=[growth, demand_forecast])

# Build the full process as a strict partial order
root = StrictPartialOrder(nodes=[
    seed_sourcing,
    loop
])
root.order.add_edge(seed_sourcing, loop)