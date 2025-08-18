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

# Define loops and choices
sensor_monitor_loop = OperatorPOWL(operator=Operator.LOOP, children=[sensor_monitor])
airflow_manage_loop = OperatorPOWL(operator=Operator.LOOP, children=[airflow_manage])
pest_control_loop = OperatorPOWL(operator=Operator.LOOP, children=[pest_control])
feedback_loop_choice = OperatorPOWL(operator=Operator.XOR, children=[feedback_loop])

# Define the root process
root = StrictPartialOrder(nodes=[
    seed_selection,
    germination_setup,
    nutrient_mix,
    water_control,
    climate_adjust,
    sensor_monitor_loop,
    lighting_tune,
    airflow_manage_loop,
    health_scan,
    pest_control_loop,
    harvest_timing,
    cold_storage,
    package_prep,
    delivery_plan,
    feedback_loop_choice
])

# Add edges to the root process
root.order.add_edge(seed_selection, germination_setup)
root.order.add_edge(germination_setup, nutrient_mix)
root.order.add_edge(nutrient_mix, water_control)
root.order.add_edge(water_control, climate_adjust)
root.order.add_edge(climate_adjust, sensor_monitor_loop)
root.order.add_edge(sensor_monitor_loop, airflow_manage_loop)
root.order.add_edge(airflow_manage_loop, health_scan)
root.order.add_edge(health_scan, pest_control_loop)
root.order.add_edge(pest_control_loop, harvest_timing)
root.order.add_edge(harvest_timing, cold_storage)
root.order.add_edge(cold_storage, package_prep)
root.order.add_edge(package_prep, delivery_plan)
root.order.add_edge(delivery_plan, feedback_loop_choice)
root.order.add_edge(feedback_loop_choice, seed_selection)

print(root)