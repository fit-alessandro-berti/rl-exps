import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for each activity
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

# Define the loop for pest inspection and quality check
pest_and_quality_loop = OperatorPOWL(operator=Operator.LOOP, children=[pest_inspection, quality_check])

# Define the exclusive choice for eco packaging and storage allocation
eco_packaging_or_storage = OperatorPOWL(operator=Operator.XOR, children=[eco_packaging, storage_allocation])

# Define the exclusive choice for order processing and route planning
order_processing_or_route_planning = OperatorPOWL(operator=Operator.XOR, children=[order_processing, route_planning])

# Define the exclusive choice for vehicle dispatch and community outreach
vehicle_dispatch_or_community_outreach = OperatorPOWL(operator=Operator.XOR, children=[vehicle_dispatch, community_outreach])

# Define the exclusive choice for waste management and customer feedback
waste_management_or_customer_feedback = OperatorPOWL(operator=Operator.XOR, children=[waste_management, customer_feedback])

# Define the exclusive choice for demand analysis and community outreach
demand_analysis_or_community_outreach = OperatorPOWL(operator=Operator.XOR, children=[demand_analysis, community_outreach])

# Define the partial order
root = StrictPartialOrder(nodes=[
    seed_sourcing, farm_scheduling, sensor_monitoring, nutrient_cycling, crop_forecasting, pest_and_quality_loop,
    eco_packaging_or_storage, order_processing_or_route_planning, vehicle_dispatch_or_community_outreach,
    waste_management_or_customer_feedback, demand_analysis_or_community_outreach
])

# Define the dependencies
root.order.add_edge(seed_sourcing, farm_scheduling)
root.order.add_edge(farm_scheduling, sensor_monitoring)
root.order.add_edge(sensor_monitoring, nutrient_cycling)
root.order.add_edge(nutrient_cycling, crop_forecasting)
root.order.add_edge(crop_forecasting, pest_inspection)
root.order.add_edge(pest_inspection, quality_check)
root.order.add_edge(pest_inspection, waste_management)
root.order.add_edge(quality_check, eco_packaging_or_storage)
root.order.add_edge(eco_packaging_or_storage, order_processing_or_route_planning)
root.order.add_edge(order_processing_or_route_planning, vehicle_dispatch_or_community_outreach)
root.order.add_edge(vehicle_dispatch_or_community_outreach, waste_management_or_customer_feedback)
root.order.add_edge(waste_management_or_customer_feedback, demand_analysis_or_community_outreach)
root.order.add_edge(demand_analysis_or_community_outreach, community_outreach)

print(root)