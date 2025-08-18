import pm4py
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

# Define exclusive choice nodes
sensor_monitoring_and_nutrient_cycling = OperatorPOWL(operator=Operator.XOR, children=[sensor_monitoring, nutrient_cycling])
pest_inspection_and_crop_forecasting = OperatorPOWL(operator=Operator.XOR, children=[pest_inspection, crop_forecasting])
quality_check_and_harvest_timing = OperatorPOWL(operator=Operator.XOR, children=[quality_check, harvest_timing])
eco_packaging_and_storage_allocation = OperatorPOWL(operator=Operator.XOR, children=[eco_packaging, storage_allocation])
order_processing_and_route_planning = OperatorPOWL(operator=Operator.XOR, children=[order_processing, route_planning])
vehicle_dispatch_and_customer_feedback = OperatorPOWL(operator=Operator.XOR, children=[vehicle_dispatch, customer_feedback])
demand_analysis_and_waste_management = OperatorPOWL(operator=Operator.XOR, children=[demand_analysis, waste_management])
community_outreach_and_seed_sourcing = OperatorPOWL(operator=Operator.XOR, children=[community_outreach, seed_sourcing])

# Define loop nodes
farm_scheduling_loop = OperatorPOWL(operator=Operator.LOOP, children=[farm_scheduling])

# Define the root node
root = StrictPartialOrder(nodes=[
    farm_scheduling_loop,
    sensor_monitoring_and_nutrient_cycling,
    pest_inspection_and_crop_forecasting,
    quality_check_and_harvest_timing,
    eco_packaging_and_storage_allocation,
    order_processing_and_route_planning,
    vehicle_dispatch_and_customer_feedback,
    demand_analysis_and_waste_management,
    community_outreach_and_seed_sourcing
])

# Define dependencies between nodes
root.order.add_edge(farm_scheduling_loop, sensor_monitoring_and_nutrient_cycling)
root.order.add_edge(sensor_monitoring_and_nutrient_cycling, pest_inspection_and_crop_forecasting)
root.order.add_edge(pest_inspection_and_crop_forecasting, quality_check_and_harvest_timing)
root.order.add_edge(quality_check_and_harvest_timing, eco_packaging_and_storage_allocation)
root.order.add_edge(eco_packaging_and_storage_allocation, order_processing_and_route_planning)
root.order.add_edge(order_processing_and_route_planning, vehicle_dispatch_and_customer_feedback)
root.order.add_edge(vehicle_dispatch_and_customer_feedback, demand_analysis_and_waste_management)
root.order.add_edge(demand_analysis_and_waste_management, community_outreach_and_seed_sourcing)

print(root)