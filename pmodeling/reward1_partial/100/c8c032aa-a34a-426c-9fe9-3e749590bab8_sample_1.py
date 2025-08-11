import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities) in the POWL model
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

# Define the silent transitions
skip = SilentTransition()

# Define the choice nodes
light_nutrient_choice = OperatorPOWL(operator=Operator.XOR, children=[light_sourcing, nutrient_order])
climate_grow_choice = OperatorPOWL(operator=Operator.XOR, children=[climate_setup, growth_planning])
irrigation_pest_choice = OperatorPOWL(operator=Operator.XOR, children=[irrigation_check, pest_monitoring])
energy_data_choice = OperatorPOWL(operator=Operator.XOR, children=[energy_tracking, data_analysis])
repair_packaging_choice = OperatorPOWL(operator=Operator.XOR, children=[equipment_repair, packaging_prep])
update_delivery_choice = OperatorPOWL(operator=Operator.XOR, children=[inventory_update, delivery_scheduling])
feedback_forecast_choice = OperatorPOWL(operator=Operator.XOR, children=[customer_feedback, market_forecast])

# Define the loop nodes
growth_loop = OperatorPOWL(operator=Operator.LOOP, children=[seed_planting, irrigation_check, pest_monitoring])
inspection_loop = OperatorPOWL(operator=Operator.LOOP, children=[quality_testing, data_analysis])

# Define the root of the POWL model
root = StrictPartialOrder(nodes=[
    light_nutrient_choice,
    climate_grow_choice,
    irrigation_pest_choice,
    energy_data_choice,
    repair_packaging_choice,
    update_delivery_choice,
    feedback_forecast_choice,
    growth_loop,
    inspection_loop
])

# Define the dependencies between nodes
root.order.add_edge(light_nutrient_choice, climate_grow_choice)
root.order.add_edge(climate_grow_choice, irrigation_pest_choice)
root.order.add_edge(irrigation_pest_choice, energy_data_choice)
root.order.add_edge(energy_data_choice, repair_packaging_choice)
root.order.add_edge(repair_packaging_choice, update_delivery_choice)
root.order.add_edge(update_delivery_choice, feedback_forecast_choice)
root.order.add_edge(feedback_forecast_choice, growth_loop)
root.order.add_edge(growth_loop, inspection_loop)
root.order.add_edge(inspection_loop, growth_loop)

print(root)