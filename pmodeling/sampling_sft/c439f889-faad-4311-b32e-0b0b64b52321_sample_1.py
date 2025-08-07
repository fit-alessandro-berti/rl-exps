import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
seed_sourcing = Transition(label='Seed Sourcing')
farm_scheduling = Transition(label='Farm Scheduling')
sensor_monitoring = Transition(label='Sensor Monitoring')
nutrient_cycling = Transition(label='Nutrient Cycling')
crop_forecasting = Transition(label='Crop Forecasting')
pest_inspection = Transition(label='Pest Inspection')
harvest_timing = Transition(label='Harvest Timing')
quality_check = Transition(label='Quality Check')
eco_packaging = Transition(label='Eco Packaging')
storage_allocation = Transition(label='Storage Allocation')
order_processing = Transition(label='Order Processing')
route_planning = Transition(label='Route Planning')
vehicle_dispatch = Transition(label='Vehicle Dispatch')
customer_feedback = Transition(label='Customer Feedback')
demand_analysis = Transition(label='Demand Analysis')
waste_management = Transition(label='Waste Management')
community_outreach = Transition(label='Community Outreach')

# Define the main production & distribution sequence
main_seq = StrictPartialOrder(nodes=[
    seed_sourcing,
    farm_scheduling,
    sensor_monitoring,
    nutrient_cycling,
    crop_forecasting,
    pest_inspection,
    harvest_timing,
    quality_check,
    eco_packaging,
    storage_allocation,
    order_processing,
    route_planning,
    vehicle_dispatch
])
main_seq.order.add_edge(seed_sourcing, farm_scheduling)
main_seq.order.add_edge(farm_scheduling, sensor_monitoring)
main_seq.order.add_edge(sensor_monitoring, nutrient_cycling)
main_seq.order.add_edge(nutrient_cycling, crop_forecasting)
main_seq.order.add_edge(crop_forecasting, pest_inspection)
main_seq.order.add_edge(pest_inspection, harvest_timing)
main_seq.order.add_edge(harvest_timing, quality_check)
main_seq.order.add_edge(quality_check, eco_packaging)
main_seq.order.add_edge(eco_packaging, storage_allocation)
main_seq.order.add_edge(storage_allocation, order_processing)
main_seq.order.add_edge(order_processing, route_planning)
main_seq.order.add_edge(route_planning, vehicle_dispatch)

# Define the loop for community outreach and demand analysis
community_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[community_outreach, demand_analysis]
)

# Assemble the root partial order
root = StrictPartialOrder(nodes=[
    main_seq,
    community_loop,
    waste_management
])
root.order.add_edge(main_seq, community_loop)
root.order.add_edge(community_loop, waste_management)

# Print the root model for verification
print(root)