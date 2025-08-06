import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator
# Define the activities
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

# Define the choices and loops
choice1 = OperatorPOWL(operator=Operator.XOR, children=[pest_control, nutrient_mix])
choice2 = OperatorPOWL(operator=Operator.XOR, children=[airflow_manage, climate_adjust])
choice3 = OperatorPOWL(operator=Operator.XOR, children=[lighting_tune, sensor_monitor])
choice4 = OperatorPOWL(operator=Operator.XOR, children=[harvest_timing, feedback_loop])
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[choice1, choice2, choice3, choice4])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[seed_selection, germination_setup])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[nutrient_mix, water_control])
loop4 = OperatorPOWL(operator=Operator.LOOP, children=[pest_control, health_scan])
loop5 = OperatorPOWL(operator=Operator.LOOP, children=[lighting_tune, airflow_manage])
loop6 = OperatorPOWL(operator=Operator.LOOP, children=[harvest_timing, feedback_loop])

# Define the root of the POWL model
root = StrictPartialOrder(nodes=[loop1, loop2, loop3, loop4, loop5, loop6])
root.order.add_edge(loop1, loop2)
root.order.add_edge(loop1, loop3)
root.order.add_edge(loop1, loop4)
root.order.add_edge(loop1, loop5)
root.order.add_edge(loop1, loop6)
root.order.add_edge(loop2, loop3)
root.order.add_edge(loop3, loop4)
root.order.add_edge(loop3, loop5)
root.order.add_edge(loop3, loop6)
root.order.add_edge(loop4, loop5)
root.order.add_edge(loop4, loop6)
root.order.add_edge(loop5, loop6)

# Return the root of the POWL model
return root