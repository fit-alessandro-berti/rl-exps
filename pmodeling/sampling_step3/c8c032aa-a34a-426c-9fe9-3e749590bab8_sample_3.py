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

# Define the process as a Strict Partial Order
root = StrictPartialOrder(nodes=[
    light_sourcing,
    nutrient_order,
    climate_setup,
    growth_planning,
    seed_planting,
    irrigation_check,
    pest_monitoring,
    energy_tracking,
    quality_testing,
    data_analysis,
    equipment_repair,
    packaging_prep,
    inventory_update,
    delivery_scheduling,
    customer_feedback,
    market_forecast
])

# Define dependencies between activities
root.order.add_edge(light_sourcing, nutrient_order)
root.order.add_edge(nutrient_order, climate_setup)
root.order.add_edge(climate_setup, growth_planning)
root.order.add_edge(growth_planning, seed_planting)
root.order.add_edge(seed_planting, irrigation_check)
root.order.add_edge(irrigation_check, pest_monitoring)
root.order.add_edge(pest_monitoring, energy_tracking)
root.order.add_edge(energy_tracking, quality_testing)
root.order.add_edge(quality_testing, data_analysis)
root.order.add_edge(data_analysis, equipment_repair)
root.order.add_edge(equipment_repair, packaging_prep)
root.order.add_edge(packaging_prep, inventory_update)
root.order.add_edge(inventory_update, delivery_scheduling)
root.order.add_edge(delivery_scheduling, customer_feedback)
root.order.add_edge(customer_feedback, market_forecast)

# Print the final model
print(root)