import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define activities
seed_sourcing     = Transition(label='Seed Sourcing')
germination_check = Transition(label='Germination Check')
nutrient_mix      = Transition(label='Nutrient Mix')
automated_planting= Transition(label='Automated Planting')
climate_control   = Transition(label='Climate Control')
crop_scanning     = Transition(label='Crop Scanning')
pest_monitoring   = Transition(label='Pest Monitoring')
growth_analysis   = Transition(label='Growth Analysis')
robo_harvest      = Transition(label='Robotic Harvest')
quality_sort      = Transition(label='Quality Sort')
eco_packaging     = Transition(label='Eco Packaging')
blockchain_track  = Transition(label='Blockchain Track')
route_planning    = Transition(label='Route Planning')
feedback_collect  = Transition(label='Feedback Collect')
waste_recycling   = Transition(label='Waste Recycling')
demand_forecast   = Transition(label='Demand Forecast')
maintenance_alert = Transition(label='Maintenance Alert')

# Build the partial order
root = StrictPartialOrder(nodes=[
    seed_sourcing,
    germination_check,
    nutrient_mix,
    automated_planting,
    climate_control,
    crop_scanning,
    pest_monitoring,
    growth_analysis,
    robo_harvest,
    quality_sort,
    eco_packaging,
    blockchain_track,
    route_planning,
    feedback_collect,
    waste_recycling,
    demand_forecast,
    maintenance_alert
])

# Define the control-flow dependencies
root.order.add_edge(seed_sourcing, germination_check)
root.order.add_edge(germination_check, nutrient_mix)
root.order.add_edge(nutrient_mix, automated_planting)
root.order.add_edge(automated_planting, climate_control)
root.order.add_edge(climate_control, crop_scanning)
root.order.add_edge(crop_scanning, pest_monitoring)
root.order.add_edge(pest_monitoring, growth_analysis)
root.order.add_edge(growth_analysis, robo_harvest)
root.order.add_edge(robo_harvest, quality_sort)
root.order.add_edge(quality_sort, eco_packaging)
root.order.add_edge(eco_packaging, blockchain_track)
root.order.add_edge(blockchain_track, route_planning)
root.order.add_edge(route_planning, feedback_collect)
root.order.add_edge(feedback_collect, waste_recycling)
root.order.add_edge(waste_recycling, demand_forecast)
root.order.add_edge(demand_forecast, maintenance_alert)

# The maintenance alert loop is not strictly sequential but can be modeled as a loop
# in the partial order graph, so we add it as a child to the demand forecast
loop_body = StrictPartialOrder(nodes=[maintenance_alert])
loop = OperatorPOWL(operator=Operator.LOOP, children=[demand_forecast, loop_body])
root.order.add_edge(demand_forecast, loop)

# Print the root model
print(root)