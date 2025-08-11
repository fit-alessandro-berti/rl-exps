import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
seed_selection = Transition(label='Seed Selection')
germination_setup = Transition(label='Germination Setup')
nutrient_mix = Transition(label='Nutrient Mix')
water_control = Transition(label='Water Control')
climate_adjust = Transition(label='Climate Adjust')
sensor_monitor = Transition(label='Sensor Monitor')
lighting_tune = Transition(label='Lighting Tune')
airflow_manage = Transition(label='Airflow Manage')
health_scan = Transition(label='Health Scan')
pest_control = Transition(label='Pest Control')
harvest_timing = Transition(label='Harvest Timing')
cold_storage = Transition(label='Cold Storage')
package_prep = Transition(label='Package Prep')
delivery_plan = Transition(label='Delivery Plan')
feedback_loop = Transition(label='Feedback Loop')

# Define silent transitions
skip = SilentTransition()

# Define the POWL model
loop_climate = OperatorPOWL(operator=Operator.LOOP, children=[climate_adjust, sensor_monitor])
loop_lighting = OperatorPOWL(operator=Operator.LOOP, children=[lighting_tune, airflow_manage])
loop_health = OperatorPOWL(operator=Operator.LOOP, children=[health_scan, pest_control])

xor_harvest = OperatorPOWL(operator=Operator.XOR, children=[harvest_timing, skip])
xor_storage = OperatorPOWL(operator=Operator.XOR, children=[cold_storage, package_prep])

loop_delivery = OperatorPOWL(operator=Operator.LOOP, children=[delivery_plan, feedback_loop])

root = StrictPartialOrder(nodes=[loop_climate, loop_lighting, loop_health, xor_harvest, xor_storage, loop_delivery])

# Define dependencies between nodes
root.order.add_edge(loop_climate, loop_lighting)
root.order.add_edge(loop_climate, loop_health)
root.order.add_edge(loop_lighting, loop_health)
root.order.add_edge(xor_harvest, xor_storage)
root.order.add_edge(loop_delivery, xor_storage)
root.order.add_edge(loop_delivery, loop_health)

# Print the POWL model
print(root)