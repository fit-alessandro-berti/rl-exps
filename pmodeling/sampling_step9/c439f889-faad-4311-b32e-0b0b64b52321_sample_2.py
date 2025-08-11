import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
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

# Define exclusive choice for seed sourcing and farm scheduling
xor_seed_scheduling = OperatorPOWL(operator=Operator.XOR, children=[seed_sourcing, farm_scheduling])

# Define loop for sensor monitoring, nutrient cycling, and crop forecasting
loop_sensor_cycling = OperatorPOWL(operator=Operator.LOOP, children=[sensor_monitoring, nutrient_cycling, crop_forecasting])

# Define exclusive choice for pest inspection and harvest timing
xor_pest_harvest = OperatorPOWL(operator=Operator.XOR, children=[pest_inspection, harvest_timing])

# Define exclusive choice for quality check and eco packaging
xor_quality_packaging = OperatorPOWL(operator=Operator.XOR, children=[quality_check, eco_packaging])

# Define loop for order processing, route planning, and vehicle dispatch
loop_order_dispatch = OperatorPOWL(operator=Operator.LOOP, children=[order_processing, route_planning, vehicle_dispatch])

# Define loop for customer feedback and demand analysis
loop_feedback_demand = OperatorPOWL(operator=Operator.LOOP, children=[customer_feedback, demand_analysis])

# Define loop for waste management and community outreach
loop_waste_community = OperatorPOWL(operator=Operator.LOOP, children=[waste_management, community_outreach])

# Define partial order for the entire process
root = StrictPartialOrder(nodes=[xor_seed_scheduling, loop_sensor_cycling, xor_pest_harvest, xor_quality_packaging, loop_order_dispatch, loop_feedback_demand, loop_waste_community])

# Define dependencies
root.order.add_edge(xor_seed_scheduling, loop_sensor_cycling)
root.order.add_edge(loop_sensor_cycling, xor_pest_harvest)
root.order.add_edge(xor_pest_harvest, xor_quality_packaging)
root.order.add_edge(xor_quality_packaging, loop_order_dispatch)
root.order.add_edge(loop_order_dispatch, loop_feedback_demand)
root.order.add_edge(loop_feedback_demand, loop_waste_community)

print(root)