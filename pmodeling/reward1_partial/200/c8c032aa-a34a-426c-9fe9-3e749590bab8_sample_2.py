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

# Define silent transitions (empty labels)
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

# Define loops and choices
light_sourcing_loop = OperatorPOWL(operator=Operator.LOOP, children=[light_sourcing, skip_light_sourcing])
nutrient_order_loop = OperatorPOWL(operator=Operator.LOOP, children=[nutrient_order, skip_nutrient_order])
climate_setup_loop = OperatorPOWL(operator=Operator.LOOP, children=[climate_setup, skip_climate_setup])
growth_planning_loop = OperatorPOWL(operator=Operator.LOOP, children=[growth_planning, skip_growth_planning])
seed_planting_loop = OperatorPOWL(operator=Operator.LOOP, children=[seed_planting, skip_seed_planting])
irrigation_check_loop = OperatorPOWL(operator=Operator.LOOP, children=[irrigation_check, skip_irrigation_check])
pest_monitoring_loop = OperatorPOWL(operator=Operator.LOOP, children=[pest_monitoring, skip_pest_monitoring])
energy_tracking_loop = OperatorPOWL(operator=Operator.LOOP, children=[energy_tracking, skip_energy_tracking])
quality_testing_loop = OperatorPOWL(operator=Operator.LOOP, children=[quality_testing, skip_quality_testing])
data_analysis_loop = OperatorPOWL(operator=Operator.LOOP, children=[data_analysis, skip_data_analysis])
equipment_repair_loop = OperatorPOWL(operator=Operator.LOOP, children=[equipment_repair, skip_equipment_repair])
packaging_prep_loop = OperatorPOWL(operator=Operator.LOOP, children=[packaging_prep, skip_packaging_prep])
inventory_update_loop = OperatorPOWL(operator=Operator.LOOP, children=[inventory_update, skip_inventory_update])
delivery_scheduling_loop = OperatorPOWL(operator=Operator.LOOP, children=[delivery_scheduling, skip_delivery_scheduling])
customer_feedback_loop = OperatorPOWL(operator=Operator.LOOP, children=[customer_feedback, skip_customer_feedback])
market_forecast_loop = OperatorPOWL(operator=Operator.LOOP, children=[market_forecast, skip_market_forecast])

# Define XOR choices
light_sourcing_choice = OperatorPOWL(operator=Operator.XOR, children=[light_sourcing, skip_light_sourcing])
nutrient_order_choice = OperatorPOWL(operator=Operator.XOR, children=[nutrient_order, skip_nutrient_order])
climate_setup_choice = OperatorPOWL(operator=Operator.XOR, children=[climate_setup, skip_climate_setup])
growth_planning_choice = OperatorPOWL(operator=Operator.XOR, children=[growth_planning, skip_growth_planning])
seed_planting_choice = OperatorPOWL(operator=Operator.XOR, children=[seed_planting, skip_seed_planting])
irrigation_check_choice = OperatorPOWL(operator=Operator.XOR, children=[irrigation_check, skip_irrigation_check])
pest_monitoring_choice = OperatorPOWL(operator=Operator.XOR, children=[pest_monitoring, skip_pest_monitoring])
energy_tracking_choice = OperatorPOWL(operator=Operator.XOR, children=[energy_tracking, skip_energy_tracking])
quality_testing_choice = OperatorPOWL(operator=Operator.XOR, children=[quality_testing, skip_quality_testing])
data_analysis_choice = OperatorPOWL(operator=Operator.XOR, children=[data_analysis, skip_data_analysis])
equipment_repair_choice = OperatorPOWL(operator=Operator.XOR, children=[equipment_repair, skip_equipment_repair])
packaging_prep_choice = OperatorPOWL(operator=Operator.XOR, children=[packaging_prep, skip_packaging_prep])
inventory_update_choice = OperatorPOWL(operator=Operator.XOR, children=[inventory_update, skip_inventory_update])
delivery_scheduling_choice = OperatorPOWL(operator=Operator.XOR, children=[delivery_scheduling, skip_delivery_scheduling])
customer_feedback_choice = OperatorPOWL(operator=Operator.XOR, children=[customer_feedback, skip_customer_feedback])
market_forecast_choice = OperatorPOWL(operator=Operator.XOR, children=[market_forecast, skip_market_forecast])

# Define the root node
root = StrictPartialOrder(
    nodes=[
        light_sourcing_loop,
        nutrient_order_loop,
        climate_setup_loop,
        growth_planning_loop,
        seed_planting_loop,
        irrigation_check_loop,
        pest_monitoring_loop,
        energy_tracking_loop,
        quality_testing_loop,
        data_analysis_loop,
        equipment_repair_loop,
        packaging_prep_loop,
        inventory_update_loop,
        delivery_scheduling_loop,
        customer_feedback_loop,
        market_forecast_loop,
        light_sourcing_choice,
        nutrient_order_choice,
        climate_setup_choice,
        growth_planning_choice,
        seed_planting_choice,
        irrigation_check_choice,
        pest_monitoring_choice,
        energy_tracking_choice,
        quality_testing_choice,
        data_analysis_choice,
        equipment_repair_choice,
        packaging_prep_choice,
        inventory_update_choice,
        delivery_scheduling_choice,
        customer_feedback_choice,
        market_forecast_choice
    ]
)

# Define dependencies (edges)
root.order.add_edge(light_sourcing_loop, light_sourcing_choice)
root.order.add_edge(nutrient_order_loop, nutrient_order_choice)
root.order.add_edge(climate_setup_loop, climate_setup_choice)
root.order.add_edge(growth_planning_loop, growth_planning_choice)
root.order.add_edge(seed_planting_loop, seed_planting_choice)
root.order.add_edge(irrigation_check_loop, irrigation_check_choice)
root.order.add_edge(pest_monitoring_loop, pest_monitoring_choice)
root.order.add_edge(energy_tracking_loop, energy_tracking_choice)
root.order.add_edge(quality_testing_loop, quality_testing_choice)
root.order.add_edge(data_analysis_loop, data_analysis_choice)
root.order.add_edge(equipment_repair_loop, equipment_repair_choice)
root.order.add_edge(packaging_prep_loop, packaging_prep_choice)
root.order.add_edge(inventory_update_loop, inventory_update_choice)
root.order.add_edge(delivery_scheduling_loop, delivery_scheduling_choice)
root.order.add_edge(customer_feedback_loop, customer_feedback_choice)
root.order.add_edge(market_forecast_loop, market_forecast_choice)

# Print the root node
print(root)