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
data_analysis      = Transition(label='Data Analysis')
quality_testing    = Transition(label='Quality Testing')
equipment_repair   = Transition(label='Equipment Repair')
packaging_prep     = Transition(label='Packaging Prep')
delivery_scheduling= Transition(label='Delivery Scheduling')
inventory_update   = Transition(label='Inventory Update')
customer_feedback  = Transition(label='Customer Feedback')
market_forecast    = Transition(label='Market Forecast')

# Define the loop body for recurring adjustments
loop_body = StrictPartialOrder(nodes=[
    irrigation_check,
    pest_monitoring,
    energy_tracking,
    data_analysis,
    quality_testing,
    equipment_repair
])
loop_body.order.add_edge(irrigation_check, pest_monitoring)
loop_body.order.add_edge(pest_monitoring, energy_tracking)
loop_body.order.add_edge(energy_tracking, data_analysis)
loop_body.order.add_edge(data_analysis, quality_testing)
loop_body.order.add_edge(quality_testing, equipment_repair)

# Define the loop: repeat the adjustment cycle after each quality test
loop = OperatorPOWL(operator=Operator.LOOP, children=[loop_body, data_analysis])

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    light_sourcing,
    nutrient_order,
    climate_setup,
    growth_planning,
    seed_planting,
    loop,
    packaging_prep,
    delivery_scheduling,
    inventory_update,
    customer_feedback,
    market_forecast
])

# Define the control-flow dependencies
root.order.add_edge(light_sourcing, nutrient_order)
root.order.add_edge(nutrient_order, climate_setup)
root.order.add_edge(climate_setup, growth_planning)
root.order.add_edge(growth_planning, seed_planting)
root.order.add_edge(seed_planting, loop)
root.order.add_edge(loop, packaging_prep)
root.order.add_edge(packaging_prep, delivery_scheduling)
root.order.add_edge(delivery_scheduling, inventory_update)
root.order.add_edge(inventory_update, customer_feedback)
root.order.add_edge(customer_feedback, market_forecast)