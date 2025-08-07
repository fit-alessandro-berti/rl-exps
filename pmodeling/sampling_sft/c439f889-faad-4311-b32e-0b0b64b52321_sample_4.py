import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
seed_sourcing      = Transition(label='Seed Sourcing')
farm_scheduling    = Transition(label='Farm Scheduling')
sensor_monitoring  = Transition(label='Sensor Monitoring')
nutrient_cycling   = Transition(label='Nutrient Cycling')
crop_forecasting   = Transition(label='Crop Forecasting')
pest_inspection    = Transition(label='Pest Inspection')
harvest_timing     = Transition(label='Harvest Timing')
quality_check      = Transition(label='Quality Check')
eco_packaging      = Transition(label='Eco Packaging')
storage_allocation = Transition(label='Storage Allocation')
order_processing   = Transition(label='Order Processing')
route_planning     = Transition(label='Route Planning')
vehicle_dispatch   = Transition(label='Vehicle Dispatch')
customer_feedback  = Transition(label='Customer Feedback')
demand_analysis    = Transition(label='Demand Analysis')
waste_management   = Transition(label='Waste Management')
community_outreach = Transition(label='Community Outreach')

# Define the main production cycle as a partial order
main_cycle = StrictPartialOrder(nodes=[
    seed_sourcing,
    farm_scheduling,
    sensor_monitoring,
    nutrient_cycling,
    crop_forecasting,
    pest_inspection,
    harvest_timing,
    quality_check,
    eco_packaging,
    storage_allocation
])
# Sequence of activities in the production cycle
main_cycle.order.add_edge(seed_sourcing, farm_scheduling)
main_cycle.order.add_edge(farm_scheduling, sensor_monitoring)
main_cycle.order.add_edge(sensor_monitoring, nutrient_cycling)
main_cycle.order.add_edge(nutrient_cycling, crop_forecasting)
main_cycle.order.add_edge(crop_forecasting, pest_inspection)
main_cycle.order.add_edge(pest_inspection, harvest_timing)
main_cycle.order.add_edge(harvest_timing, quality_check)
main_cycle.order.add_edge(quality_check, eco_packaging)
main_cycle.order.add_edge(eco_packaging, storage_allocation)

# Define the delivery and feedback loop as a partial order
delivery_loop = StrictPartialOrder(nodes=[
    order_processing,
    route_planning,
    vehicle_dispatch,
    customer_feedback,
    demand_analysis,
    waste_management,
    community_outreach
])
delivery_loop.order.add_edge(order_processing, route_planning)
delivery_loop.order.add_edge(route_planning, vehicle_dispatch)
delivery_loop.order.add_edge(vehicle_dispatch, customer_feedback)
delivery_loop.order.add_edge(customer_feedback, demand_analysis)
delivery_loop.order.add_edge(demand_analysis, waste_management)
delivery_loop.order.add_edge(waste_management, community_outreach)

# Define the overall process as a choice between production and delivery
root = OperatorPOWL(operator=Operator.XOR, children=[main_cycle, delivery_loop])

print(root)