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

seed_sourcing_to_germination_check = OperatorPOWL(operator=Operator.XOR, children=[seed_sourcing, germination_check])
germination_check_to_nutrient_mix = OperatorPOWL(operator=Operator.XOR, children=[germination_check, nutrient_mix])
nutrient_mix_to_automated_planting = OperatorPOWL(operator=Operator.XOR, children=[nutrient_mix, automated_planting])
automated_planting_to_climate_control = OperatorPOWL(operator=Operator.XOR, children=[automated_planting, climate_control])
climate_control_to_crop_scanning = OperatorPOWL(operator=Operator.XOR, children=[climate_control, crop_scanning])
crop_scanning_to_pest_monitoring = OperatorPOWL(operator=Operator.XOR, children=[crop_scanning, pest_monitoring])
pest_monitoring_to_growth_analysis = OperatorPOWL(operator=Operator.XOR, children=[pest_monitoring, growth_analysis])
growth_analysis_to_robotic_harvest = OperatorPOWL(operator=Operator.XOR, children=[growth_analysis, robotic_harvest])
robotic_harvest_to_quality_sort = OperatorPOWL(operator=Operator.XOR, children=[robotic_harvest, quality_sort])
quality_sort_to_eco_packaging = OperatorPOWL(operator=Operator.XOR, children=[quality_sort, eco_packaging])
eco_packaging_to_blockchain_track = OperatorPOWL(operator=Operator.XOR, children=[eco_packaging, blockchain_track])
blockchain_track_to_route_planning = OperatorPOWL(operator=Operator.XOR, children=[blockchain_track, route_planning])
route_planning_to_feedback_collect = OperatorPOWL(operator=Operator.XOR, children=[route_planning, feedback_collect])
feedback_collect_to_waste_recycling = OperatorPOWL(operator=Operator.XOR, children=[feedback_collect, waste_recycling])
waste_recycling_to_data_analytics = OperatorPOWL(operator=Operator.XOR, children=[waste_recycling, data_analytics])
data_analytics_to_demand_forecast = OperatorPOWL(operator=Operator.XOR, children=[data_analytics, demand_forecast])
demand_forecast_to_maintenance_alert = OperatorPOWL(operator=Operator.XOR, children=[demand_forecast, maintenance_alert])

root = StrictPartialOrder(nodes=[
    seed_sourcing_to_germination_check,
    germination_check_to_nutrient_mix,
    nutrient_mix_to_automated_planting,
    automated_planting_to_climate_control,
    climate_control_to_crop_scanning,
    crop_scanning_to_pest_monitoring,
    pest_monitoring_to_growth_analysis,
    growth_analysis_to_robotic_harvest,
    robotic_harvest_to_quality_sort,
    quality_sort_to_eco_packaging,
    eco_packaging_to_blockchain_track,
    blockchain_track_to_route_planning,
    route_planning_to_feedback_collect,
    feedback_collect_to_waste_recycling,
    waste_recycling_to_data_analytics,
    data_analytics_to_demand_forecast,
    demand_forecast_to_maintenance_alert
])