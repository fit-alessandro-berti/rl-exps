import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
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

# Build the loop for adaptive climate control
climate_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[sensor_monitor, climate_adjust]
)

# Build the loop for pest control and health assessment
pest_health_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[pest_control, health_scan]
)

# Build the main partial order
root = StrictPartialOrder(nodes=[
    seed_selection,
    germination_setup,
    nutrient_mix,
    water_control,
    climate_loop,
    lighting_tune,
    airflow_manage,
    pest_health_loop,
    harvest_timing,
    cold_storage,
    package_prep,
    delivery_plan,
    feedback_loop
])

# Define the control-flow dependencies
root.order.add_edge(seed_selection, germination_setup)
root.order.add_edge(germination_setup, nutrient_mix)
root.order.add_edge(germination_setup, water_control)
root.order.add_edge(nutrient_mix, climate_loop)
root.order.add_edge(water_control, climate_loop)
root.order.add_edge(climate_loop, lighting_tune)
root.order.add_edge(climate_loop, airflow_manage)
root.order.add_edge(lighting_tune, pest_health_loop)
root.order.add_edge(airflow_manage, pest_health_loop)
root.order.add_edge(pest_health_loop, harvest_timing)
root.order.add_edge(harvest_timing, cold_storage)
root.order.add_edge(cold_storage, package_prep)
root.order.add_edge(package_prep, delivery_plan)
root.order.add_edge(delivery_plan, feedback_loop)