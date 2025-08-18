from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
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

# Define exclusive choice for pest inspection and quality check
pest_inspection_or_quality_check = OperatorPOWL(operator=Operator.XOR, children=[pest_inspection, quality_check])

# Define loop for sensor monitoring and nutrient cycling
sensor_monitoring_nutrient_cycling = OperatorPOWL(operator=Operator.LOOP, children=[sensor_monitoring, nutrient_cycling])

# Define exclusive choice for crop forecasting and pest inspection or quality check
crop_forecasting_or_pest_inspection_or_quality_check = OperatorPOWL(operator=Operator.XOR, children=[crop_forecasting, pest_inspection_or_quality_check])

# Define loop for storage allocation and order processing
storage_allocation_order_processing = OperatorPOWL(operator=Operator.LOOP, children=[storage_allocation, order_processing])

# Define exclusive choice for route planning and vehicle dispatch
route_planning_or_vehicle_dispatch = OperatorPOWL(operator=Operator.XOR, children=[route_planning, vehicle_dispatch])

# Define loop for customer feedback and demand analysis
customer_feedback_demand_analysis = OperatorPOWL(operator=Operator.LOOP, children=[customer_feedback, demand_analysis])

# Define loop for waste management and community outreach
waste_management_community_outreach = OperatorPOWL(operator=Operator.LOOP, children=[waste_management, community_outreach])

# Define partial order with dependencies
root = StrictPartialOrder(nodes=[
    seed_sourcing,
    farm_scheduling,
    sensor_monitoring_nutrient_cycling,
    crop_forecasting_or_pest_inspection_or_quality_check,
    storage_allocation_order_processing,
    route_planning_or_vehicle_dispatch,
    customer_feedback_demand_analysis,
    waste_management_community_outreach
])
root.order.add_edge(seed_sourcing, farm_scheduling)
root.order.add_edge(farm_scheduling, sensor_monitoring_nutrient_cycling)
root.order.add_edge(sensor_monitoring_nutrient_cycling, crop_forecasting_or_pest_inspection_or_quality_check)
root.order.add_edge(crop_forecasting_or_pest_inspection_or_quality_check, storage_allocation_order_processing)
root.order.add_edge(storage_allocation_order_processing, route_planning_or_vehicle_dispatch)
root.order.add_edge(route_planning_or_vehicle_dispatch, customer_feedback_demand_analysis)
root.order.add_edge(customer_feedback_demand_analysis, waste_management_community_outreach)