import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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

light_sourcing_choice = OperatorPOWL(operator=Operator.XOR, children=[light_sourcing, skip])
nutrient_order_choice = OperatorPOWL(operator=Operator.XOR, children=[nutrient_order, skip])
climate_setup_choice = OperatorPOWL(operator=Operator.XOR, children=[climate_setup, skip])
growth_planning_choice = OperatorPOWL(operator=Operator.XOR, children=[growth_planning, skip])
seed_planting_choice = OperatorPOWL(operator=Operator.XOR, children=[seed_planting, skip])
irrigation_check_choice = OperatorPOWL(operator=Operator.XOR, children=[irrigation_check, skip])
pest_monitoring_choice = OperatorPOWL(operator=Operator.XOR, children=[pest_monitoring, skip])
energy_tracking_choice = OperatorPOWL(operator=Operator.XOR, children=[energy_tracking, skip])
quality_testing_choice = OperatorPOWL(operator=Operator.XOR, children=[quality_testing, skip])
data_analysis_choice = OperatorPOWL(operator=Operator.XOR, children=[data_analysis, skip])
equipment_repair_choice = OperatorPOWL(operator=Operator.XOR, children=[equipment_repair, skip])
packaging_prep_choice = OperatorPOWL(operator=Operator.XOR, children=[packaging_prep, skip])
inventory_update_choice = OperatorPOWL(operator=Operator.XOR, children=[inventory_update, skip])
delivery_scheduling_choice = OperatorPOWL(operator=Operator.XOR, children=[delivery_scheduling, skip])
customer_feedback_choice = OperatorPOWL(operator=Operator.XOR, children=[customer_feedback, skip])
market_forecast_choice = OperatorPOWL(operator=Operator.XOR, children=[market_forecast, skip])

root = StrictPartialOrder(nodes=[
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
])

root.order.add_edge(light_sourcing_choice, nutrient_order_choice)
root.order.add_edge(nutrient_order_choice, climate_setup_choice)
root.order.add_edge(climate_setup_choice, growth_planning_choice)
root.order.add_edge(growth_planning_choice, seed_planting_choice)
root.order.add_edge(seed_planting_choice, irrigation_check_choice)
root.order.add_edge(irrigation_check_choice, pest_monitoring_choice)
root.order.add_edge(pest_monitoring_choice, energy_tracking_choice)
root.order.add_edge(energy_tracking_choice, quality_testing_choice)
root.order.add_edge(quality_testing_choice, data_analysis_choice)
root.order.add_edge(data_analysis_choice, equipment_repair_choice)
root.order.add_edge(equipment_repair_choice, packaging_prep_choice)
root.order.add_edge(packaging_prep_choice, inventory_update_choice)
root.order.add_edge(inventory_update_choice, delivery_scheduling_choice)
root.order.add_edge(delivery_scheduling_choice, customer_feedback_choice)
root.order.add_edge(customer_feedback_choice, market_forecast_choice)