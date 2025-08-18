import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities) in the POWL model
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

# Define the partial order
root = StrictPartialOrder(nodes=[
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
    vehicle_dispatch,
    customer_feedback,
    demand_analysis,
    waste_management,
    community_outreach
])

# Define the dependencies (partial order edges) between the transitions
root.order.add_edge(seed_sourcing, farm_scheduling)
root.order.add_edge(farm_scheduling, sensor_monitoring)
root.order.add_edge(sensor_monitoring, nutrient_cycling)
root.order.add_edge(nutrient_cycling, crop_forecasting)
root.order.add_edge(crop_forecasting, pest_inspection)
root.order.add_edge(pest_inspection, harvest_timing)
root.order.add_edge(harvest_timing, quality_check)
root.order.add_edge(quality_check, eco_packaging)
root.order.add_edge(eco_packaging, storage_allocation)
root.order.add_edge(storage_allocation, order_processing)
root.order.add_edge(order_processing, route_planning)
root.order.add_edge(route_planning, vehicle_dispatch)
root.order.add_edge(vehicle_dispatch, customer_feedback)
root.order.add_edge(customer_feedback, demand_analysis)
root.order.add_edge(demand_analysis, waste_management)
root.order.add_edge(waste_management, community_outreach)

# Print the root POWL model
print(root)