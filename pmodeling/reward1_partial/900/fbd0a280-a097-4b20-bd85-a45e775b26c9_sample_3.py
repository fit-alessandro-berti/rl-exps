import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
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

# Define the workflow
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[seed_selection, germination_setup])
xor1 = OperatorPOWL(operator=Operator.XOR, children=[nutrient_mix, water_control])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[climate_adjust, sensor_monitor])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[lighting_tune, airflow_manage])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[health_scan, pest_control])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[harvest_timing, cold_storage])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[package_prep, delivery_plan])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[feedback_loop])

# Create the root of the POWL model
root = StrictPartialOrder(nodes=[loop1, xor1, loop2, xor2, xor3, loop3, xor4, xor5])
root.order.add_edge(loop1, xor1)
root.order.add_edge(xor1, loop2)
root.order.add_edge(loop2, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, loop3)
root.order.add_edge(loop3, xor4)
root.order.add_edge(xor4, xor5)

# Print the POWL model
print(root)