import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
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

# Define the control-flow operators
xor_light_sourcing = OperatorPOWL(operator=Operator.XOR, children=[light_sourcing, nutrient_order])
xor_climate_setup = OperatorPOWL(operator=Operator.XOR, children=[climate_setup, growth_planning])
xor_seed_planting = OperatorPOWL(operator=Operator.XOR, children=[seed_planting, irrigation_check])
xor_pest_monitoring = OperatorPOWL(operator=Operator.XOR, children=[pest_monitoring, energy_tracking])
xor_quality_testing = OperatorPOWL(operator=Operator.XOR, children=[quality_testing, data_analysis])
xor_equipment_repair = OperatorPOWL(operator=Operator.XOR, children=[equipment_repair, packaging_prep])
xor_inventory_update = OperatorPOWL(operator=Operator.XOR, children=[inventory_update, delivery_scheduling])
xor_customer_feedback = OperatorPOWL(operator=Operator.XOR, children=[customer_feedback, market_forecast])

# Define the loop for unexpected events
loop_unexpected_events = OperatorPOWL(operator=Operator.LOOP, children=[xor_light_sourcing, xor_climate_setup, xor_seed_planting, xor_pest_monitoring, xor_quality_testing, xor_equipment_repair, xor_inventory_update, xor_customer_feedback])

# Define the root node
root = StrictPartialOrder(nodes=[loop_unexpected_events])
root.order.add_edge(loop_unexpected_events, xor_light_sourcing)
root.order.add_edge(loop_unexpected_events, xor_climate_setup)
root.order.add_edge(loop_unexpected_events, xor_seed_planting)
root.order.add_edge(loop_unexpected_events, xor_pest_monitoring)
root.order.add_edge(loop_unexpected_events, xor_quality_testing)
root.order.add_edge(loop_unexpected_events, xor_equipment_repair)
root.order.add_edge(loop_unexpected_events, xor_inventory_update)
root.order.add_edge(loop_unexpected_events, xor_customer_feedback)

# Print the root node
print(root)