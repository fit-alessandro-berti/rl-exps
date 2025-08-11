from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
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

# Define the control flow operators
light_sourcing_nutrient_order = OperatorPOWL(operator=Operator.XOR, children=[light_sourcing, nutrient_order])
climate_setup_energy_tracking = OperatorPOWL(operator=Operator.XOR, children=[climate_setup, energy_tracking])
pest_monitoring_quality_testing = OperatorPOWL(operator=Operator.XOR, children=[pest_monitoring, quality_testing])
data_analysis_equipment_repair = OperatorPOWL(operator=Operator.XOR, children=[data_analysis, equipment_repair])
packaging_prep_inventory_update = OperatorPOWL(operator=Operator.XOR, children=[packaging_prep, inventory_update])
delivery_scheduling_customer_feedback = OperatorPOWL(operator=Operator.XOR, children=[delivery_scheduling, customer_feedback])
market_forecast_delivery_scheduling = OperatorPOWL(operator=Operator.XOR, children=[market_forecast, delivery_scheduling])

# Define the loop for data analysis
loop_data_analysis = OperatorPOWL(operator=Operator.LOOP, children=[data_analysis, equipment_repair])

# Define the partial order
root = StrictPartialOrder(nodes=[light_sourcing_nutrient_order, climate_setup_energy_tracking, pest_monitoring_quality_testing, loop_data_analysis, packaging_prep_inventory_update, delivery_scheduling_customer_feedback, market_forecast_delivery_scheduling])
root.order.add_edge(light_sourcing_nutrient_order, climate_setup_energy_tracking)
root.order.add_edge(climate_setup_energy_tracking, pest_monitoring_quality_testing)
root.order.add_edge(pest_monitoring_quality_testing, loop_data_analysis)
root.order.add_edge(loop_data_analysis, packaging_prep_inventory_update)
root.order.add_edge(packaging_prep_inventory_update, delivery_scheduling_customer_feedback)
root.order.add_edge(delivery_scheduling_customer_feedback, market_forecast_delivery_scheduling)