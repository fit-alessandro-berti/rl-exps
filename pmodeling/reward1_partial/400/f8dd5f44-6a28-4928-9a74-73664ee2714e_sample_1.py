import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
seed_selection = Transition(label='Seed Selection')
nutrient_mix = Transition(label='Nutrient Mix')
environment_setup = Transition(label='Environment Setup')
sensor_deployment = Transition(label='Sensor Deployment')
growth_monitoring = Transition(label='Growth Monitoring')
pest_detection = Transition(label='Pest Detection')
automated_harvest = Transition(label='Automated Harvest')
quality_check = Transition(label='Quality Check')
packaging_prep = Transition(label='Packaging Prep')
biodegradable_pack = Transition(label='Biodegradable Pack')
inventory_sync = Transition(label='Inventory Sync')
demand_forecast = Transition(label='Demand Forecast')
micro_fulfillment = Transition(label='Micro Fulfillment')
local_dispatch = Transition(label='Local Dispatch')
consumer_feedback = Transition(label='Consumer Feedback')
crop_adjustment = Transition(label='Crop Adjustment')

# Define operators and partial order
xor = OperatorPOWL(operator=Operator.XOR, children=[crop_adjustment, seed_selection])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[environment_setup, sensor_deployment])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[growth_monitoring, pest_detection])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[automated_harvest, quality_check])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[packaging_prep, biodegradable_pack])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[inventory_sync, demand_forecast])
xor7 = OperatorPOWL(operator=Operator.XOR, children=[micro_fulfillment, local_dispatch])
xor8 = OperatorPOWL(operator=Operator.XOR, children=[consumer_feedback, crop_adjustment])

root = StrictPartialOrder(nodes=[xor, xor2, xor3, xor4, xor5, xor6, xor7, xor8])
root.order.add_edge(xor, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, xor5)
root.order.add_edge(xor5, xor6)
root.order.add_edge(xor6, xor7)
root.order.add_edge(xor7, xor8)
root.order.add_edge(xor8, xor)