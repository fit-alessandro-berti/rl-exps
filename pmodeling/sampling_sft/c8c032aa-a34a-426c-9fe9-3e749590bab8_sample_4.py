import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
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
delivery_scheduling = Transition(label='Delivery Scheduling')
inventory_update  = Transition(label='Inventory Update')
customer_feedback = Transition(label='Customer Feedback')
market_forecast   = Transition(label='Market Forecast')

# Silent transition for optional steps
skip = SilentTransition()

# Define the optional pest monitoring and equipment repair branches
# XOR: either do Pest Monitoring then Equipment Repair, or skip both
pest_xor = OperatorPOWL(operator=Operator.XOR, children=[pest_monitoring, equipment_repair])

# Define the main growth cycle as a strict partial order
growth_cycle = StrictPartialOrder(nodes=[
    irrigation_check,
    pest_xor,
    quality_testing,
    data_analysis
])
growth_cycle.order.add_edge(irrigation_check, pest_xor)
growth_cycle.order.add_edge(pest_xor, quality_testing)
growth_cycle.order.add_edge(quality_testing, data_analysis)

# Define the overall process as a strict partial order
root = StrictPartialOrder(nodes=[
    light_sourcing,
    nutrient_order,
    climate_setup,
    growth_planning,
    seed_planting,
    growth_cycle,
    packaging_prep,
    delivery_scheduling,
    inventory_update,
    customer_feedback,
    market_forecast
])

# Sequence the activities in the overall process
root.order.add_edge(light_sourcing, nutrient_order)
root.order.add_edge(nutrient_order, climate_setup)
root.order.add_edge(climate_setup, growth_planning)
root.order.add_edge(growth_planning, seed_planting)
root.order.add_edge(seed_planting, growth_cycle)
root.order.add_edge(growth_cycle, packaging_prep)
root.order.add_edge(packaging_prep, delivery_scheduling)
root.order.add_edge(delivery_scheduling, inventory_update)
root.order.add_edge(inventory_update, customer_feedback)
root.order.add_edge(customer_feedback, market_forecast)