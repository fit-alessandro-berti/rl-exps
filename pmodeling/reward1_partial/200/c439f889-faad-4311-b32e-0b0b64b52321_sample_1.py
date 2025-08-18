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

skip = SilentTransition()
xor = OperatorPOWL(operator=Operator.XOR, children=[waste_management, community_outreach])

loop1 = OperatorPOWL(operator=Operator.LOOP, children=[pest_inspection, crop_forecasting, sensor_monitoring])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[quality_check, eco_packaging, storage_allocation])

root = StrictPartialOrder(nodes=[seed_sourcing, farm_scheduling, loop1, loop2, order_processing, route_planning, vehicle_dispatch, customer_feedback, demand_analysis, xor])
root.order.add_edge(seed_sourcing, farm_scheduling)
root.order.add_edge(farm_scheduling, loop1)
root.order.add_edge(loop1, loop2)
root.order.add_edge(loop2, order_processing)
root.order.add_edge(order_processing, route_planning)
root.order.add_edge(route_planning, vehicle_dispatch)
root.order.add_edge(vehicle_dispatch, customer_feedback)
root.order.add_edge(customer_feedback, demand_analysis)
root.order.add_edge(demand_analysis, xor)