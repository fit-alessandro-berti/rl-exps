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

xor1 = OperatorPOWL(operator=Operator.XOR, children=[pest_inspection, quality_check])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[storage_allocation, order_processing])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[route_planning, vehicle_dispatch])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[customer_feedback, demand_analysis])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[waste_management, community_outreach])

loop = OperatorPOWL(operator=Operator.LOOP, children=[seed_sourcing, farm_scheduling, sensor_monitoring, nutrient_cycling, crop_forecasting, xor1])

root = StrictPartialOrder(nodes=[loop, xor2, xor3, xor4, xor5])
root.order.add_edge(loop, xor2)
root.order.add_edge(loop, xor3)
root.order.add_edge(loop, xor4)
root.order.add_edge(loop, xor5)