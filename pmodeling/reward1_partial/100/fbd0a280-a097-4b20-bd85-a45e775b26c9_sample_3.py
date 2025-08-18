import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions
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

# Define transitions for concurrent activities
sensor_monitor_and_health_scan = OperatorPOWL(operator=Operator.XOR, children=[sensor_monitor, health_scan])
pest_control_and_pest_control = OperatorPOWL(operator=Operator.XOR, children=[pest_control, pest_control])
harvest_and_cold_storage = OperatorPOWL(operator=Operator.XOR, children=[harvest_timing, cold_storage])

# Define loop for sensor monitoring and health scanning
loop = OperatorPOWL(operator=Operator.LOOP, children=[sensor_monitor_and_health_scan])

# Define partial order for the entire process
root = StrictPartialOrder(nodes=[seed_selection, germination_setup, nutrient_mix, water_control, climate_adjust, loop, pest_control_and_pest_control, harvest_and_cold_storage, package_prep, delivery_plan, feedback_loop])
root.order.add_edge(seed_selection, germination_setup)
root.order.add_edge(germination_setup, nutrient_mix)
root.order.add_edge(nutrient_mix, water_control)
root.order.add_edge(water_control, climate_adjust)
root.order.add_edge(climate_adjust, loop)
root.order.add_edge(loop, pest_control_and_pest_control)
root.order.add_edge(pest_control_and_pest_control, harvest_and_cold_storage)
root.order.add_edge(harvest_and_cold_storage, package_prep)
root.order.add_edge(package_prep, delivery_plan)
root.order.add_edge(delivery_plan, feedback_loop)