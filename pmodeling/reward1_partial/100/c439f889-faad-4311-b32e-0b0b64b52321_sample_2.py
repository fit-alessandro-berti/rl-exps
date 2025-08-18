import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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

# Define exclusive choices
exclusive_choice_1 = OperatorPOWL(operator=Operator.XOR, children=[pest_inspection, quality_check])
exclusive_choice_2 = OperatorPOWL(operator=Operator.XOR, children=[storage_allocation, order_processing])
exclusive_choice_3 = OperatorPOWL(operator=Operator.XOR, children=[route_planning, vehicle_dispatch])
exclusive_choice_4 = OperatorPOWL(operator=Operator.XOR, children=[customer_feedback, demand_analysis])
exclusive_choice_5 = OperatorPOWL(operator=Operator.XOR, children=[waste_management, community_outreach])

# Define loops
loop_1 = OperatorPOWL(operator=Operator.LOOP, children=[sensor_monitoring, exclusive_choice_1])
loop_2 = OperatorPOWL(operator=Operator.LOOP, children=[nutrient_cycling, exclusive_choice_2])
loop_3 = OperatorPOWL(operator=Operator.LOOP, children=[crop_forecasting, exclusive_choice_3])
loop_4 = OperatorPOWL(operator=Operator.LOOP, children=[exclusive_choice_4, exclusive_choice_5])

# Define the root node
root = StrictPartialOrder(nodes=[seed_sourcing, farm_scheduling, loop_1, loop_2, loop_3, loop_4])
root.order.add_edge(seed_sourcing, farm_scheduling)
root.order.add_edge(farm_scheduling, loop_1)
root.order.add_edge(loop_1, loop_2)
root.order.add_edge(loop_2, loop_3)
root.order.add_edge(loop_3, loop_4)
root.order.add_edge(loop_4, exclusive_choice_4)
root.order.add_edge(exclusive_choice_4, exclusive_choice_5)

print(root)