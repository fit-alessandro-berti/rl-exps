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

# Define silent transitions
skip = SilentTransition()

# Define loops and choices
loop_farm_scheduling = OperatorPOWL(operator=Operator.LOOP, children=[farm_scheduling, pest_inspection])
loop_sensor_monitoring = OperatorPOWL(operator=Operator.LOOP, children=[sensor_monitoring, quality_check])
loop_nutrient_cycling = OperatorPOWL(operator=Operator.LOOP, children=[nutrient_cycling, waste_management])
loop_crop_forecasting = OperatorPOWL(operator=Operator.LOOP, children=[crop_forecasting, demand_analysis])
loop_vehicle_dispatch = OperatorPOWL(operator=Operator.LOOP, children=[vehicle_dispatch, community_outreach])

xor_order_processing = OperatorPOWL(operator=Operator.XOR, children=[order_processing, skip])
xor_route_planning = OperatorPOWL(operator=Operator.XOR, children=[route_planning, skip])

xor_storage_allocation = OperatorPOWL(operator=Operator.XOR, children=[storage_allocation, skip])

# Define the root POWL model
root = StrictPartialOrder(nodes=[
    loop_farm_scheduling, loop_sensor_monitoring, loop_nutrient_cycling, loop_crop_forecasting,
    loop_vehicle_dispatch, xor_order_processing, xor_route_planning, xor_storage_allocation,
    seed_sourcing, eco_packaging, community_outreach
])

# Add edges to the order
root.order.add_edge(loop_farm_scheduling, loop_sensor_monitoring)
root.order.add_edge(loop_sensor_monitoring, loop_nutrient_cycling)
root.order.add_edge(loop_nutrient_cycling, loop_crop_forecasting)
root.order.add_edge(loop_crop_forecasting, loop_vehicle_dispatch)
root.order.add_edge(loop_vehicle_dispatch, xor_order_processing)
root.order.add_edge(xor_order_processing, xor_route_planning)
root.order.add_edge(xor_route_planning, xor_storage_allocation)
root.order.add_edge(xor_storage_allocation, seed_sourcing)
root.order.add_edge(seed_sourcing, eco_packaging)
root.order.add_edge(eco_packaging, community_outreach)

# Print the root POWL model
print(root)