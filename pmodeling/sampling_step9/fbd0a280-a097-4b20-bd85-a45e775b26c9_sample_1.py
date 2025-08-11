import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
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

# Define the partial order nodes
sensor_monitor_node = OperatorPOWL(operator=Operator.PARTIAL_ORDER, children=[sensor_monitor, lighting_tune, airflow_manage])
nutrient_mix_node = OperatorPOWL(operator=Operator.PARTIAL_ORDER, children=[nutrient_mix, water_control])
harvest_timing_node = OperatorPOWL(operator=Operator.PARTIAL_ORDER, children=[harvest_timing, cold_storage, package_prep, delivery_plan])

# Define the loop nodes
germination_loop = OperatorPOWL(operator=Operator.LOOP, children=[germination_setup])
climate_adjust_loop = OperatorPOWL(operator=Operator.LOOP, children=[climate_adjust])
pest_control_loop = OperatorPOWL(operator=Operator.LOOP, children=[pest_control])

# Define the XOR node for feedback loop
xor_node = OperatorPOWL(operator=Operator.XOR, children=[feedback_loop, SilentTransition()])

# Define the root of the POWL model
root = StrictPartialOrder(nodes=[germination_loop, nutrient_mix_node, climate_adjust_loop, pest_control_loop, sensor_monitor_node, harvest_timing_node, xor_node])
root.order.add_edge(germination_loop, nutrient_mix_node)
root.order.add_edge(nutrient_mix_node, climate_adjust_loop)
root.order.add_edge(climate_adjust_loop, pest_control_loop)
root.order.add_edge(sensor_monitor_node, harvest_timing_node)
root.order.add_edge(harvest_timing_node, xor_node)