import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
light_sourcing     = Transition(label='Light Sourcing')
nutrient_order     = Transition(label='Nutrient Order')
climate_setup      = Transition(label='Climate Setup')
growth_planning    = Transition(label='Growth Planning')
seed_planting      = Transition(label='Seed Planting')
irrigation_check   = Transition(label='Irrigation Check')
pest_monitoring    = Transition(label='Pest Monitoring')
energy_tracking    = Transition(label='Energy Tracking')
quality_testing    = Transition(label='Quality Testing')
data_analysis      = Transition(label='Data Analysis')
equipment_repair   = Transition(label='Equipment Repair')
packaging_prep     = Transition(label='Packaging Prep')
inventory_update   = Transition(label='Inventory Update')
delivery_scheduling= Transition(label='Delivery Scheduling')
customer_feedback  = Transition(label='Customer Feedback')
market_forecast    = Transition(label='Market Forecast')

# Define the main production sequence as a partial order
production = StrictPartialOrder(nodes=[
    light_sourcing, nutrient_order, climate_setup, growth_planning,
    seed_planting, irrigation_check, pest_monitoring, energy_tracking,
    quality_testing, data_analysis, equipment_repair, packaging_prep,
    inventory_update, delivery_scheduling
])
# Define the control-flow dependencies
dependencies = [
    (light_sourcing,   nutrient_order),
    (light_sourcing,   climate_setup),
    (nutrient_order,   growth_planning),
    (climate_setup,    growth_planning),
    (growth_planning,  seed_planting),
    (seed_planting,    irrigation_check),
    (irrigation_check, pest_monitoring),
    (pest_monitoring,  energy_tracking),
    (energy_tracking,  quality_testing),
    (quality_testing,  data_analysis),
    (data_analysis,    equipment_repair),
    (equipment_repair, packaging_prep),
    (packaging_prep,   inventory_update),
    (inventory_update, delivery_scheduling)
]
for src, tgt in dependencies:
    production.order.add_edge(src, tgt)

# Define the loop for iterative quality testing and data analysis
loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[quality_testing, data_analysis]
)

# Build the root partial order including the main production and the loop
root = StrictPartialOrder(nodes=[
    production, loop, market_forecast, customer_feedback
])
root.order.add_edge(production, loop)
root.order.add_edge(loop, market_forecast)
root.order.add_edge(loop, customer_feedback)

# Print the root model for verification
print(root)