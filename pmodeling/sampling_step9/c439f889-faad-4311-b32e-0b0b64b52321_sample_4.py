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

# Define the control flow operators
xor = OperatorPOWL(operator=Operator.XOR, children=[seed_sourcing, farm_scheduling])
loop = OperatorPOWL(operator=Operator.LOOP, children=[sensor_monitoring, nutrient_cycling])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[crop_forecasting, pest_inspection])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[harvest_timing, quality_check])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[eco_packaging, storage_allocation])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[order_processing, route_planning])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[vehicle_dispatch, customer_feedback])
loop4 = OperatorPOWL(operator=Operator.LOOP, children=[demand_analysis, waste_management])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[community_outreach, waste_management])

# Define the root POWL model
root = StrictPartialOrder(nodes=[xor, loop, xor2, loop2, xor3, loop3, xor4, loop4, xor5])
root.order.add_edge(xor, loop)
root.order.add_edge(loop, xor2)
root.order.add_edge(xor2, loop2)
root.order.add_edge(loop2, xor3)
root.order.add_edge(xor3, loop3)
root.order.add_edge(loop3, xor4)
root.order.add_edge(xor4, loop4)
root.order.add_edge(loop4, xor5)
root.order.add_edge(xor5, loop4)