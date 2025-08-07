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

# Define the partial order
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

# Add dependencies if any (not specified in the problem statement)
# For example, if 'Light Sourcing' should precede 'Nutrient Order':
# root.order.add_edge(light_sourcing, nutrient_order)

# Print the root POWL model (for demonstration purposes)
print(root)