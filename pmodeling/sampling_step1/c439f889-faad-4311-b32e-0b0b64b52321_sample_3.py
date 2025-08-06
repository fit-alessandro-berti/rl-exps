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

# Define the control flow operators
xor = OperatorPOWL(operator=Operator.XOR, children=[pest_inspection, quality_check])
loop = OperatorPOWL(operator=Operator.LOOP, children=[storage_allocation, order_processing])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[route_planning, vehicle_dispatch])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[customer_feedback, demand_analysis])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[waste_management, community_outreach])

# Create the root node of the POWL model
root = StrictPartialOrder(nodes=[seed_sourcing, farm_scheduling, sensor_monitoring, nutrient_cycling, crop_forecasting, xor, loop, xor2, xor3, xor4])

# Define the dependencies between nodes
root.order.add_edge(seed_sourcing, farm_scheduling)
root.order.add_edge(farm_scheduling, sensor_monitoring)
root.order.add_edge(sensor_monitoring, nutrient_cycling)
root.order.add_edge(nutrient_cycling, crop_forecasting)
root.order.add_edge(crop_forecasting, xor)
root.order.add_edge(xor, loop)
root.order.add_edge(loop, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)

# Print the root node of the POWL model
print(root)