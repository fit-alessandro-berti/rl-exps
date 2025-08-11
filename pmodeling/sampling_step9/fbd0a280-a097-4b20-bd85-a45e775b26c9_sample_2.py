import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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

skip = SilentTransition()

# Define the workflow structure
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[seed_selection, germination_setup])
xor1 = OperatorPOWL(operator=Operator.XOR, children=[nutrient_mix, skip])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[water_control, climate_adjust])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[sensor_monitor, lighting_tune])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[airflow_manage, health_scan])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[pest_control, skip])
loop4 = OperatorPOWL(operator=Operator.LOOP, children=[harvest_timing, cold_storage])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[package_prep, skip])
loop5 = OperatorPOWL(operator=Operator.LOOP, children=[delivery_plan, feedback_loop])

# Define the partial order
root = StrictPartialOrder(nodes=[loop1, xor1, loop2, xor2, loop3, xor3, loop4, xor4, loop5])
root.order.add_edge(loop1, xor1)
root.order.add_edge(xor1, loop2)
root.order.add_edge(loop2, xor2)
root.order.add_edge(xor2, loop3)
root.order.add_edge(loop3, xor3)
root.order.add_edge(xor3, loop4)
root.order.add_edge(loop4, xor4)
root.order.add_edge(xor4, loop5)

print(root)