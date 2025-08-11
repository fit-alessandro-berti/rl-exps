from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
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

# Define the control flow
xor1 = OperatorPOWL(operator=Operator.XOR, children=[light_sourcing, nutrient_order, climate_setup])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[growth_planning, seed_planting])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[irrigation_check, pest_monitoring])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[energy_tracking, quality_testing])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[data_analysis, equipment_repair])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[packaging_prep, inventory_update])
xor7 = OperatorPOWL(operator=Operator.XOR, children=[delivery_scheduling, customer_feedback])
xor8 = OperatorPOWL(operator=Operator.XOR, children=[market_forecast, customer_feedback])

# Define the partial order
root = StrictPartialOrder(nodes=[xor1, xor2, xor3, xor4, xor5, xor6, xor7, xor8])
root.order.add_edge(xor1, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, xor5)
root.order.add_edge(xor5, xor6)
root.order.add_edge(xor6, xor7)
root.order.add_edge(xor7, xor8)