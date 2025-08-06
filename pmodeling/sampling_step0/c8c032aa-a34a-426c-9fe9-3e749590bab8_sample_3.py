import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities)
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

# Define the silent transitions (empty labels)
skip_light_sourcing = SilentTransition()
skip_nutrient_order = SilentTransition()
skip_climate_setup = SilentTransition()
skip_growth_planning = SilentTransition()
skip_seed_planting = SilentTransition()
skip_irrigation_check = SilentTransition()
skip_pest_monitoring = SilentTransition()
skip_energy_tracking = SilentTransition()
skip_quality_testing = SilentTransition()
skip_data_analysis = SilentTransition()
skip_equipment_repair = SilentTransition()
skip_packaging_prep = SilentTransition()
skip_inventory_update = SilentTransition()
skip_delivery_scheduling = SilentTransition()
skip_customer_feedback = SilentTransition()
skip_market_forecast = SilentTransition()

# Define the choice operators
xor_light_sourcing = OperatorPOWL(operator=Operator.XOR, children=[light_sourcing, skip_light_sourcing])
xor_nutrient_order = OperatorPOWL(operator=Operator.XOR, children=[nutrient_order, skip_nutrient_order])
xor_climate_setup = OperatorPOWL(operator=Operator.XOR, children=[climate_setup, skip_climate_setup])
xor_growth_planning = OperatorPOWL(operator=Operator.XOR, children=[growth_planning, skip_growth_planning])
xor_seed_planting = OperatorPOWL(operator=Operator.XOR, children=[seed_planting, skip_seed_planting])
xor_irrigation_check = OperatorPOWL(operator=Operator.XOR, children=[irrigation_check, skip_irrigation_check])
xor_pest_monitoring = OperatorPOWL(operator=Operator.XOR, children=[pest_monitoring, skip_pest_monitoring])
xor_energy_tracking = OperatorPOWL(operator=Operator.XOR, children=[energy_tracking, skip_energy_tracking])
xor_quality_testing = OperatorPOWL(operator=Operator.XOR, children=[quality_testing, skip_quality_testing])
xor_data_analysis = OperatorPOWL(operator=Operator.XOR, children=[data_analysis, skip_data_analysis])
xor_equipment_repair = OperatorPOWL(operator=Operator.XOR, children=[equipment_repair, skip_equipment_repair])
xor_packaging_prep = OperatorPOWL(operator=Operator.XOR, children=[packaging_prep, skip_packaging_prep])
xor_inventory_update = OperatorPOWL(operator=Operator.XOR, children=[inventory_update, skip_inventory_update])
xor_delivery_scheduling = OperatorPOWL(operator=Operator.XOR, children=[delivery_scheduling, skip_delivery_scheduling])
xor_customer_feedback = OperatorPOWL(operator=Operator.XOR, children=[customer_feedback, skip_customer_feedback])
xor_market_forecast = OperatorPOWL(operator=Operator.XOR, children=[market_forecast, skip_market_forecast])

# Define the loop operators
loop_light_sourcing = OperatorPOWL(operator=Operator.LOOP, children=[light_sourcing, skip_light_sourcing])
loop_nutrient_order = OperatorPOWL(operator=Operator.LOOP, children=[nutrient_order, skip_nutrient_order])
loop_climate_setup = OperatorPOWL(operator=Operator.LOOP, children=[climate_setup, skip_climate_setup])
loop_growth_planning = OperatorPOWL(operator=Operator.LOOP, children=[growth_planning, skip_growth_planning])
loop_seed_planting = OperatorPOWL(operator=Operator.LOOP, children=[seed_planting, skip_seed_planting])
loop_irrigation_check = OperatorPOWL(operator=Operator.LOOP, children=[irrigation_check, skip_irrigation_check])
loop_pest_monitoring = OperatorPOWL(operator=Operator.LOOP, children=[pest_monitoring, skip_pest_monitoring])
loop_energy_tracking = OperatorPOWL(operator=Operator.LOOP, children=[energy_tracking, skip_energy_tracking])
loop_quality_testing = OperatorPOWL(operator=Operator.LOOP, children=[quality_testing, skip_quality_testing])
loop_data_analysis = OperatorPOWL(operator=Operator.LOOP, children=[data_analysis, skip_data_analysis])
loop_equipment_repair = OperatorPOWL(operator=Operator.LOOP, children=[equipment_repair, skip_equipment_repair])
loop_packaging_prep = OperatorPOWL(operator=Operator.LOOP, children=[packaging_prep, skip_packaging_prep])
loop_inventory_update = OperatorPOWL(operator=Operator.LOOP, children=[inventory_update, skip_inventory_update])
loop_delivery_scheduling = OperatorPOWL(operator=Operator.LOOP, children=[delivery_scheduling, skip_delivery_scheduling])
loop_customer_feedback = OperatorPOWL(operator=Operator.LOOP, children=[customer_feedback, skip_customer_feedback])
loop_market_forecast = OperatorPOWL(operator=Operator.LOOP, children=[market_forecast, skip_market_forecast])

# Define the root POWL model
root = StrictPartialOrder(nodes=[
    loop_light_sourcing,
    xor_light_sourcing,
    loop_nutrient_order,
    xor_nutrient_order,
    loop_climate_setup,
    xor_climate_setup,
    loop_growth_planning,
    xor_growth_planning,
    loop_seed_planting,
    xor_seed_planting,
    loop_irrigation_check,
    xor_irrigation_check,
    loop_pest_monitoring,
    xor_pest_monitoring,
    loop_energy_tracking,
    xor_energy_tracking,
    loop_quality_testing,
    xor_quality_testing,
    loop_data_analysis,
    xor_data_analysis,
    loop_equipment_repair,
    xor_equipment_repair,
    loop_packaging_prep,
    xor_packaging_prep,
    loop_inventory_update,
    xor_inventory_update,
    loop_delivery_scheduling,
    xor_delivery_scheduling,
    loop_customer_feedback,
    xor_customer_feedback,
    loop_market_forecast,
    xor_market_forecast
])

# Define the partial order
root.order.add_edge(loop_light_sourcing, xor_light_sourcing)
root.order.add_edge(loop_nutrient_order, xor_nutrient_order)
root.order.add_edge(loop_climate_setup, xor_climate_setup)
root.order.add_edge(loop_growth_planning, xor_growth_planning)
root.order.add_edge(loop_seed_planting, xor_seed_planting)
root.order.add_edge(loop_irrigation_check, xor_irrigation_check)
root.order.add_edge(loop_pest_monitoring, xor_pest_monitoring)
root.order.add_edge(loop_energy_tracking, xor_energy_tracking)
root.order.add_edge(loop_quality_testing, xor_quality_testing)
root.order.add_edge(loop_data_analysis, xor_data_analysis)
root.order.add_edge(loop_equipment_repair, xor_equipment_repair)
root.order.add_edge(loop_packaging_prep, xor_packaging_prep)
root.order.add_edge(loop_inventory_update, xor_inventory_update)
root.order.add_edge(loop_delivery_scheduling, xor_delivery_scheduling)
root.order.add_edge(loop_customer_feedback, xor_customer_feedback)
root.order.add_edge(loop_market_forecast, xor_market_forecast)

# Save the final result in the variable 'root'