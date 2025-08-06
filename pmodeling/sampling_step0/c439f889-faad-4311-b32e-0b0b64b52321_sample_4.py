import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
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
partial_order = StrictPartialOrder(
    nodes=[seed_sourcing, farm_scheduling, sensor_monitoring, nutrient_cycling, crop_forecasting, pest_inspection,
           harvest_timing, quality_check, eco_packaging, storage_allocation, order_processing, route_planning,
           vehicle_dispatch, customer_feedback, demand_analysis, waste_management, community_outreach],
    order=set()
)

# Define the control-flow operators
xor1 = OperatorPOWL(operator=Operator.XOR, children=[sensor_monitoring, nutrient_cycling])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[pest_inspection, harvest_timing])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[quality_check, eco_packaging])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[storage_allocation, order_processing])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[route_planning, vehicle_dispatch])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[customer_feedback, demand_analysis])
xor7 = OperatorPOWL(operator=Operator.XOR, children=[waste_management, community_outreach])

# Define the partial order relationships
partial_order.order.add_edge(seed_sourcing, farm_scheduling)
partial_order.order.add_edge(farm_scheduling, sensor_monitoring)
partial_order.order.add_edge(sensor_monitoring, xor1)
partial_order.order.add_edge(nutrient_cycling, xor1)
partial_order.order.add_edge(xor1, crop_forecasting)
partial_order.order.add_edge(crop_forecasting, pest_inspection)
partial_order.order.add_edge(pest_inspection, xor2)
partial_order.order.add_edge(harvest_timing, xor2)
partial_order.order.add_edge(xor2, quality_check)
partial_order.order.add_edge(quality_check, eco_packaging)
partial_order.order.add_edge(eco_packaging, storage_allocation)
partial_order.order.add_edge(storage_allocation, order_processing)
partial_order.order.add_edge(order_processing, route_planning)
partial_order.order.add_edge(route_planning, vehicle_dispatch)
partial_order.order.add_edge(vehicle_dispatch, customer_feedback)
partial_order.order.add_edge(customer_feedback, demand_analysis)
partial_order.order.add_edge(demand_analysis, waste_management)
partial_order.order.add_edge(waste_management, community_outreach)

# Set the root
root = partial_order