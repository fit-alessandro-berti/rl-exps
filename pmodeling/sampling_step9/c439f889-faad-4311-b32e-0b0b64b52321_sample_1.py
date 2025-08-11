import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
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

# Define the silent transition
skip = SilentTransition()

# Define the loops and XORs
seed_loop = OperatorPOWL(operator=Operator.LOOP, children=[seed_sourcing, farm_scheduling])
farm_loop = OperatorPOWL(operator=Operator.LOOP, children=[sensor_monitoring, nutrient_cycling])
pest_loop = OperatorPOWL(operator=Operator.LOOP, children=[pest_inspection, harvest_timing])
quality_loop = OperatorPOWL(operator=Operator.LOOP, children=[quality_check, eco_packaging])
storage_loop = OperatorPOWL(operator=Operator.LOOP, children=[storage_allocation, order_processing])
route_loop = OperatorPOWL(operator=Operator.LOOP, children=[route_planning, vehicle_dispatch])
feedback_loop = OperatorPOWL(operator=Operator.LOOP, children=[customer_feedback, demand_analysis])
waste_loop = OperatorPOWL(operator=Operator.LOOP, children=[waste_management, community_outreach])

# Define the XORs
xor1 = OperatorPOWL(operator=Operator.XOR, children=[seed_loop, skip])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[pest_loop, skip])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[quality_loop, skip])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[storage_loop, skip])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[route_loop, skip])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[feedback_loop, skip])
xor7 = OperatorPOWL(operator=Operator.XOR, children=[waste_loop, skip])

# Define the root POWL model
root = StrictPartialOrder(nodes=[xor1, xor2, xor3, xor4, xor5, xor6, xor7])
root.order.add_edge(xor1, xor2)
root.order.add_edge(xor1, xor3)
root.order.add_edge(xor1, xor4)
root.order.add_edge(xor1, xor5)
root.order.add_edge(xor1, xor6)
root.order.add_edge(xor1, xor7)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor2, xor4)
root.order.add_edge(xor2, xor5)
root.order.add_edge(xor2, xor6)
root.order.add_edge(xor2, xor7)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor3, xor5)
root.order.add_edge(xor3, xor6)
root.order.add_edge(xor3, xor7)
root.order.add_edge(xor4, xor5)
root.order.add_edge(xor4, xor6)
root.order.add_edge(xor4, xor7)
root.order.add_edge(xor5, xor6)
root.order.add_edge(xor5, xor7)
root.order.add_edge(xor6, xor7)