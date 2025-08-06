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

# Define silent transitions
skip = SilentTransition()

# Define loop nodes
loop_farm_scheduling = OperatorPOWL(operator=Operator.LOOP, children=[farm_scheduling, pest_inspection])
loop_crop_forecasting = OperatorPOWL(operator=Operator.LOOP, children=[crop_forecasting, sensor_monitoring])
loop_nutrient_cycling = OperatorPOWL(operator=Operator.LOOP, children=[nutrient_cycling, quality_check])
loop_harvest_timing = OperatorPOWL(operator=Operator.LOOP, children=[harvest_timing, eco_packaging])
loop_storage_allocation = OperatorPOWL(operator=Operator.LOOP, children=[storage_allocation, order_processing])
loop_route_planning = OperatorPOWL(operator=Operator.LOOP, children=[route_planning, vehicle_dispatch])

# Define exclusive choice nodes
xor_customer_feedback = OperatorPOWL(operator=Operator.XOR, children=[customer_feedback, demand_analysis])
xor_waste_management = OperatorPOWL(operator=Operator.XOR, children=[waste_management, community_outreach])

# Define partial order
root = StrictPartialOrder(nodes=[
    loop_farm_scheduling,
    loop_crop_forecasting,
    loop_nutrient_cycling,
    loop_harvest_timing,
    loop_storage_allocation,
    loop_route_planning,
    xor_customer_feedback,
    xor_waste_management
])

# Add dependencies
root.order.add_edge(loop_farm_scheduling, loop_crop_forecasting)
root.order.add_edge(loop_crop_forecasting, loop_nutrient_cycling)
root.order.add_edge(loop_nutrient_cycling, loop_harvest_timing)
root.order.add_edge(loop_harvest_timing, loop_storage_allocation)
root.order.add_edge(loop_storage_allocation, loop_route_planning)
root.order.add_edge(loop_route_planning, xor_customer_feedback)
root.order.add_edge(xor_customer_feedback, xor_waste_management)
root.order.add_edge(xor_waste_management, root)