import pm4py
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

skip = SilentTransition()

# Define the POWL model structure
xor1 = OperatorPOWL(operator=Operator.XOR, children=[pest_monitoring, skip])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[quality_testing, skip])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[data_analysis, skip])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[equipment_repair, skip])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[packaging_prep, skip])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[delivery_scheduling, skip])
xor7 = OperatorPOWL(operator=Operator.XOR, children=[customer_feedback, skip])
xor8 = OperatorPOWL(operator=Operator.XOR, children=[market_forecast, skip])

loop1 = OperatorPOWL(operator=Operator.LOOP, children=[light_sourcing, nutrient_order, climate_setup])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[growth_planning, seed_planting, irrigation_check])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[xor1, xor2, xor3, xor4, xor5, xor6, xor7, xor8])

root = StrictPartialOrder(nodes=[loop1, loop2, loop3])
root.order.add_edge(loop1, loop2)
root.order.add_edge(loop2, loop3)

# Print the POWL model
print(root)