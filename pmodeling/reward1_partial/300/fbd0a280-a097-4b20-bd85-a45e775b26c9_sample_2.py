from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities) as POWL nodes
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

# Define the loop structure for monitoring and adjusting
monitor_loop = OperatorPOWL(operator=Operator.LOOP, children=[sensor_monitor, lighting_tune, airflow_manage])

# Define the choice structure for pest control and disease prevention strategies
pest_control_choice = OperatorPOWL(operator=Operator.XOR, children=[pest_control, feedback_loop])

# Define the root POWL model
root = StrictPartialOrder(nodes=[monitor_loop, pest_control_choice])
root.order.add_edge(monitor_loop, pest_control_choice)

print(root)