import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
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

# Define control flow structures
xor_light_nutrient = OperatorPOWL(operator=Operator.XOR, children=[light_sourcing, nutrient_order])
xor_climate_grow = OperatorPOWL(operator=Operator.XOR, children=[climate_setup, growth_planning])
xor_seed_irrig = OperatorPOWL(operator=Operator.XOR, children=[seed_planting, irrigation_check])
xor_pest_energy = OperatorPOWL(operator=Operator.XOR, children=[pest_monitoring, energy_tracking])
xor_test_data = OperatorPOWL(operator=Operator.XOR, children=[quality_testing, data_analysis])
xor_repair_packaging = OperatorPOWL(operator=Operator.XOR, children=[equipment_repair, packaging_prep])
xor_update_delivery = OperatorPOWL(operator=Operator.XOR, children=[inventory_update, delivery_scheduling])
xor_feedback_forecast = OperatorPOWL(operator=Operator.XOR, children=[customer_feedback, market_forecast])

# Define the root POWL model
root = StrictPartialOrder(nodes=[xor_light_nutrient, xor_climate_grow, xor_seed_irrig, xor_pest_energy, xor_test_data, xor_repair_packaging, xor_update_delivery, xor_feedback_forecast])
root.order.add_edge(xor_light_nutrient, xor_climate_grow)
root.order.add_edge(xor_climate_grow, xor_seed_irrig)
root.order.add_edge(xor_seed_irrig, xor_pest_energy)
root.order.add_edge(xor_pest_energy, xor_test_data)
root.order.add_edge(xor_test_data, xor_repair_packaging)
root.order.add_edge(xor_repair_packaging, xor_update_delivery)
root.order.add_edge(xor_update_delivery, xor_feedback_forecast)