import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
light_sourcing = Transition(label='Light Sourcing')
nutrient_order = Transition(label='Nutrient Order')
climate_setup = Transition(label='Climate Setup')
growth_planning = Transition(label='Growth Planning')
seed_planting = Transition(label='Seed Planting')
irrigation_check = Transition(label='Irrigation Check')
pest_monitoring = Transition(label='Pest Monitoring')
energy_tracking = Transition(label='Energy Tracking')
quality_testing = Transition(label='Quality Testing')
data_analysis = Transition(label='Data Analysis')
equipment_repair = Transition(label='Equipment Repair')
packaging_prep = Transition(label='Packaging Prep')
inventory_update = Transition(label='Inventory Update')
delivery_scheduling = Transition(label='Delivery Scheduling')
customer_feedback = Transition(label='Customer Feedback')
market_forecast = Transition(label='Market Forecast')

# Define the control flow operators
xor1 = OperatorPOWL(operator=Operator.XOR, children=[light_sourcing, nutrient_order])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[climate_setup, growth_planning])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[seed_planting, irrigation_check])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[pest_monitoring, energy_tracking])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[quality_testing, data_analysis])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[equipment_repair, packaging_prep])
xor7 = OperatorPOWL(operator=Operator.XOR, children=[inventory_update, delivery_scheduling])
xor8 = OperatorPOWL(operator=Operator.XOR, children=[customer_feedback, market_forecast])

# Define the loop nodes
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[xor1, xor2])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[xor3, xor4])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[xor5, xor6])
loop4 = OperatorPOWL(operator=Operator.LOOP, children=[xor7, xor8])

# Define the root node
root = StrictPartialOrder(nodes=[loop1, loop2, loop3, loop4])
root.order.add_edge(loop1, xor1)
root.order.add_edge(loop1, xor2)
root.order.add_edge(loop2, xor3)
root.order.add_edge(loop2, xor4)
root.order.add_edge(loop3, xor5)
root.order.add_edge(loop3, xor6)
root.order.add_edge(loop4, xor7)
root.order.add_edge(loop4, xor8)

# Print the root node
print(root)