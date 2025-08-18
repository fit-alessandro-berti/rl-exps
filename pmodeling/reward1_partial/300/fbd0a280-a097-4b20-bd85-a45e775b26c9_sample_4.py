import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define each activity as a transition
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

# Define the partial order structure
loop_1 = OperatorPOWL(operator=Operator.LOOP, children=[germination_setup, nutrient_mix, water_control, climate_adjust, sensor_monitor, lighting_tune, airflow_manage, health_scan, pest_control, harvest_timing])
loop_2 = OperatorPOWL(operator=Operator.LOOP, children=[cold_storage, package_prep, delivery_plan])
xor = OperatorPOWL(operator=Operator.XOR, children=[loop_1, loop_2])
xor_2 = OperatorPOWL(operator=Operator.XOR, children=[feedback_loop])

# Create the root of the POWL model
root = StrictPartialOrder(nodes=[loop_1, loop_2, xor, xor_2])
root.order.add_edge(loop_1, xor)
root.order.add_edge(loop_2, xor)
root.order.add_edge(xor, xor_2)

print(root)