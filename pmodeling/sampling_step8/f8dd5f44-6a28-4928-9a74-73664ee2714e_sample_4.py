import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
seed_selection = Transition(label='Seed Selection')
nutrient_mix = Transition(label='Nutrient Mix')
env_setup = Transition(label='Environment Setup')
sensor_dep = Transition(label='Sensor Deployment')
growth_mon = Transition(label='Growth Monitoring')
pest_detect = Transition(label='Pest Detection')
auto_harvest = Transition(label='Automated Harvest')
quality_check = Transition(label='Quality Check')
packaging_prep = Transition(label='Packaging Prep')
biodegradable_pack = Transition(label='Biodegradable Pack')
inv_sync = Transition(label='Inventory Sync')
demand_forecast = Transition(label='Demand Forecast')
micro_fulfill = Transition(label='Micro Fulfillment')
local_dispatch = Transition(label='Local Dispatch')
consumer_feedback = Transition(label='Consumer Feedback')
crop_adjustment = Transition(label='Crop Adjustment')

# Define transitions
xor1 = OperatorPOWL(operator=Operator.XOR, children=[pest_detect, auto_harvest])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[quality_check, packaging_prep])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[biodegradable_pack, inv_sync])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[demand_forecast, micro_fulfill])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[local_dispatch, consumer_feedback])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[crop_adjustment, inv_sync])

# Define the partial order
root = StrictPartialOrder(nodes=[seed_selection, nutrient_mix, env_setup, sensor_dep, growth_mon, xor1, xor2, xor3, xor4, xor5, xor6])
root.order.add_edge(seed_selection, nutrient_mix)
root.order.add_edge(nutrient_mix, env_setup)
root.order.add_edge(env_setup, sensor_dep)
root.order.add_edge(sensor_dep, growth_mon)
root.order.add_edge(growth_mon, xor1)
root.order.add_edge(pest_detect, xor2)
root.order.add_edge(auto_harvest, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(quality_check, xor4)
root.order.add_edge(packaging_prep, xor4)
root.order.add_edge(xor4, xor5)
root.order.add_edge(biodegradable_pack, xor6)
root.order.add_edge(inv_sync, xor6)
root.order.add_edge(local_dispatch, consumer_feedback)
root.order.add_edge(consumer_feedback, inv_sync)
root.order.add_edge(crop_adjustment, inv_sync)