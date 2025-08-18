import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities) for the POWL model
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

# Define the workflow using POWL operators
xor1 = OperatorPOWL(operator=Operator.XOR, children=[nutrient_mix, water_control])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[climate_adjust, sensor_monitor])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[lighting_tune, airflow_manage])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[health_scan, pest_control])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[harvest_timing, cold_storage])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[package_prep, delivery_plan])
xor7 = OperatorPOWL(operator=Operator.XOR, children=[feedback_loop, SilentTransition()])  # Silent transition for feedback loop

# Create the root POWL model
root = StrictPartialOrder(nodes=[seed_selection, germination_setup, xor1, xor2, xor3, xor4, xor5, xor6, xor7])
root.order.add_edge(seed_selection, germination_setup)
root.order.add_edge(germination_setup, xor1)
root.order.add_edge(xor1, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, xor5)
root.order.add_edge(xor5, xor6)
root.order.add_edge(xor6, xor7)
root.order.add_edge(xor7, feedback_loop)  # Connect feedback loop to the last XOR

# Print the root POWL model
print(root)