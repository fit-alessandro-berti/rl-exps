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

seed_selection_xor = OperatorPOWL(operator=Operator.XOR, children=[germination_setup, seed_selection])
nutrient_mix_xor = OperatorPOWL(operator=Operator.XOR, children=[water_control, nutrient_mix])
climate_adjust_xor = OperatorPOWL(operator=Operator.XOR, children=[sensor_monitor, climate_adjust])
lighting_tune_xor = OperatorPOWL(operator=Operator.XOR, children=[health_scan, lighting_tune])
airflow_manage_xor = OperatorPOWL(operator=Operator.XOR, children=[pest_control, airflow_manage])
harvest_timing_xor = OperatorPOWL(operator=Operator.XOR, children=[cold_storage, harvest_timing])
package_prep_xor = OperatorPOWL(operator=Operator.XOR, children=[package_prep, harvest_timing])
delivery_plan_xor = OperatorPOWL(operator=Operator.XOR, children=[feedback_loop, delivery_plan])

root = StrictPartialOrder(nodes=[
    seed_selection_xor, nutrient_mix_xor, climate_adjust_xor, lighting_tune_xor, airflow_manage_xor,
    harvest_timing_xor, package_prep_xor, delivery_plan_xor
])
root.order.add_edge(seed_selection_xor, nutrient_mix_xor)
root.order.add_edge(nutrient_mix_xor, climate_adjust_xor)
root.order.add_edge(climate_adjust_xor, sensor_monitor)
root.order.add_edge(sensor_monitor, lighting_tune)
root.order.add_edge(lighting_tune, pest_control)
root.order.add_edge(pest_control, airflow_manage)
root.order.add_edge(airflow_manage, harvest_timing)
root.order.add_edge(harvest_timing, cold_storage)
root.order.add_edge(cold_storage, package_prep)
root.order.add_edge(package_prep, harvest_timing)
root.order.add_edge(harvest_timing, delivery_plan)
root.order.add_edge(delivery_plan, feedback_loop)