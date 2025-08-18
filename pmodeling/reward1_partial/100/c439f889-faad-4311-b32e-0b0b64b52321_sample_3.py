import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions
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

# Define the exclusive choice operators
sensor_monitoring_and_nutrient_cycling = OperatorPOWL(operator=Operator.XOR, children=[sensor_monitoring, nutrient_cycling])
pest_inspection_and_harvest_timing = OperatorPOWL(operator=Operator.XOR, children=[pest_inspection, harvest_timing])
quality_check_and_eco_packaging = OperatorPOWL(operator=Operator.XOR, children=[quality_check, eco_packaging])
storage_allocation_and_order_processing = OperatorPOWL(operator=Operator.XOR, children=[storage_allocation, order_processing])
route_planning_and_vehicle_dispatch = OperatorPOWL(operator=Operator.XOR, children=[route_planning, vehicle_dispatch])

# Define the loop nodes
farm_scheduling_loop = OperatorPOWL(operator=Operator.LOOP, children=[farm_scheduling, pest_inspection_and_harvest_timing])
crop_forecasting_and_customer_feedback = OperatorPOWL(operator=Operator.LOOP, children=[crop_forecasting, customer_feedback])
demand_analysis_and_waste_management = OperatorPOWL(operator=Operator.LOOP, children=[demand_analysis, waste_management])

# Define the partial order
root = StrictPartialOrder(nodes=[farm_scheduling_loop, crop_forecasting_and_customer_feedback, demand_analysis_and_waste_management, storage_allocation_and_order_processing, route_planning_and_vehicle_dispatch, sensor_monitoring_and_nutrient_cycling, pest_inspection_and_harvest_timing, quality_check_and_eco_packaging, community_outreach])
root.order.add_edge(farm_scheduling_loop, crop_forecasting_and_customer_feedback)
root.order.add_edge(crop_forecasting_and_customer_feedback, demand_analysis_and_waste_management)
root.order.add_edge(demand_analysis_and_waste_management, storage_allocation_and_order_processing)
root.order.add_edge(storage_allocation_and_order_processing, route_planning_and_vehicle_dispatch)
root.order.add_edge(route_planning_and_vehicle_dispatch, sensor_monitoring_and_nutrient_cycling)
root.order.add_edge(sensor_monitoring_and_nutrient_cycling, pest_inspection_and_harvest_timing)
root.order.add_edge(pest_inspection_and_harvest_timing, quality_check_and_eco_packaging)
root.order.add_edge(quality_check_and_eco_packaging, community_outreach)