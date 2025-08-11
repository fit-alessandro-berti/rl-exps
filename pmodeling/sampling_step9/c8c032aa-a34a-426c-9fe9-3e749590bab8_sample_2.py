import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model for the complex and atypical supply chain management process
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
skip = SilentTransition()
loop = OperatorPOWL(operator=Operator.LOOP, children=[light_sourcing, nutrient_order, climate_setup, growth_planning, seed_planting, irrigation_check, pest_monitoring, energy_tracking, quality_testing, data_analysis, equipment_repair, packaging_prep, inventory_update, delivery_scheduling, customer_feedback, market_forecast])
xor = OperatorPOWL(operator=Operator.XOR, children=[market_forecast, skip])
root = StrictPartialOrder(nodes=[loop, xor])
root.order.add_edge(loop, xor)

# Print the final POWL model
print(root)