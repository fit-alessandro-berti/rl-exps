import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
light_sourcing    = Transition(label='Light Sourcing')
nutrient_order    = Transition(label='Nutrient Order')
climate_setup     = Transition(label='Climate Setup')
growth_planning   = Transition(label='Growth Planning')
seed_planting     = Transition(label='Seed Planting')
irrigation_check  = Transition(label='Irrigation Check')
pest_monitoring   = Transition(label='Pest Monitoring')
energy_tracking   = Transition(label='Energy Tracking')
quality_testing   = Transition(label='Quality Testing')
data_analysis     = Transition(label='Data Analysis')
equipment_repair  = Transition(label='Equipment Repair')
packaging_prep    = Transition(label='Packaging Prep')
inventory_update  = Transition(label='Inventory Update')
delivery_scheduling = Transition(label='Delivery Scheduling')
customer_feedback = Transition(label='Customer Feedback')
market_forecast   = Transition(label='Market Forecast')

# Silent transition for loop body (data analysis -> equipment repair -> quality testing)
skip = SilentTransition()

# Loop: analyze data, then optionally repair equipment and re-test, repeat until exit
loop = OperatorPOWL(operator=Operator.LOOP, children=[data_analysis, skip])

# Build the partial order
root = StrictPartialOrder(nodes=[
    light_sourcing, nutrient_order, climate_setup, growth_planning,
    seed_planting, irrigation_check, pest_monitoring, energy_tracking,
    loop, quality_testing, packaging_prep, inventory_update,
    delivery_scheduling, customer_feedback, market_forecast
])

# Add control-flow edges
root.order.add_edge(light_sourcing, nutrient_order)
root.order.add_edge(nutrient_order, climate_setup)
root.order.add_edge(climate_setup, growth_planning)
root.order.add_edge(growth_planning, seed_planting)
root.order.add_edge(seed_planting, irrigation_check)
root.order.add_edge(irrigation_check, pest_monitoring)
root.order.add_edge(pest_monitoring, energy_tracking)
root.order.add_edge(energy_tracking, loop)
root.order.add_edge(loop, quality_testing)
root.order.add_edge(quality_testing, packaging_prep)
root.order.add_edge(packaging_prep, inventory_update)
root.order.add_edge(inventory_update, delivery_scheduling)
root.order.add_edge(delivery_scheduling, customer_feedback)
root.order.add_edge(customer_feedback, market_forecast)

# For the loop, add the repair and re-test sequence
root.order.add_edge(loop, equipment_repair)
root.order.add_edge(equipment_repair, quality_testing)