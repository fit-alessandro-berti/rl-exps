import pm4py
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

root = StrictPartialOrder(nodes=[
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
])

# No dependencies in the given process, so no need to add edges