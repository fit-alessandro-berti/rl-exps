from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model for the process
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
xor1 = OperatorPOWL(operator=Operator.XOR, children=[energy_tracking, data_analysis])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[equipment_repair, packaging_prep])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[inventory_update, delivery_scheduling])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[customer_feedback, market_forecast])

# Define the partial order
root = StrictPartialOrder(nodes=[light_sourcing, nutrient_order, climate_setup, growth_planning, seed_planting, irrigation_check, pest_monitoring, xor1, xor2, xor3, xor4])
root.order.add_edge(light_sourcing, nutrient_order)
root.order.add_edge(nutrient_order, climate_setup)
root.order.add_edge(climate_setup, growth_planning)
root.order.add_edge(growth_planning, seed_planting)
root.order.add_edge(seed_planting, irrigation_check)
root.order.add_edge(irrigation_check, pest_monitoring)
root.order.add_edge(pest_monitoring, xor1)
root.order.add_edge(xor1, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, root)

# Print the root of the POWL model
print(root)