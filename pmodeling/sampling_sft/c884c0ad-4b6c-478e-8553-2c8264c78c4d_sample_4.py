import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
seed_sourcing    = Transition(label='Seed Sourcing')
germination      = Transition(label='Germination Check')
nutrient_mix     = Transition(label='Nutrient Mix')
planting         = Transition(label='Automated Planting')
climate_control  = Transition(label='Climate Control')
crop_scanning    = Transition(label='Crop Scanning')
pest_monitoring  = Transition(label='Pest Monitoring')
growth_analysis  = Transition(label='Growth Analysis')
robo_harvest     = Transition(label='Robotic Harvest')
quality_sort     = Transition(label='Quality Sort')
eco_packaging    = Transition(label='Eco Packaging')
blockchain_track = Transition(label='Blockchain Track')
route_planning   = Transition(label='Route Planning')
feedback_collect = Transition(label='Feedback Collect')
waste_recycling  = Transition(label='Waste Recycling')
data_analytics   = Transition(label='Data Analytics')
demand_forecast  = Transition(label='Demand Forecast')
maintenance_alert= Transition(label='Maintenance Alert')

# Loop for continuous crop health monitoring
loop_body = StrictPartialOrder(nodes=[pest_monitoring, growth_analysis])
loop_body.order.add_edge(pest_monitoring, growth_analysis)
loop = OperatorPOWL(operator=Operator.LOOP, children=[crop_scanning, loop_body])

# Build the partial order
root = StrictPartialOrder(nodes=[
    seed_sourcing,
    germination,
    nutrient_mix,
    planting,
    climate_control,
    loop,
    robo_harvest,
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

# Define the control‐flow dependencies
root.order.add_edge(seed_sourcing,   germination)
root.order.add_edge(germination,    nutrient_mix)
root.order.add_edge(nutrient_mix,   planting)
root.order.add_edge(planting,       climate_control)
root.order.add_edge(climate_control, loop)
root.order.add_edge(loop,           robo_harvest)
root.order.add_edge(robo_harvest,   quality_sort)
root.order.add_edge(quality_sort,   eco_packaging)
root.order.add_edge(eco_packaging,  blockchain_track)
root.order.add_edge(blockchain_track, route_planning)
root.order.add_edge(route_planning, feedback_collect)
root.order.add_edge(feedback_collect, waste_recycling)
root.order.add_edge(waste_recycling, data_analytics)
root.order.add_edge(data_analytics, demand_forecast)
root.order.add_edge(demand_forecast, maintenance_alert)

# Print the root (for verification)
print(root)