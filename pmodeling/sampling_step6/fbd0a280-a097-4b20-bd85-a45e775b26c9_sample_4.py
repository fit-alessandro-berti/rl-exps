import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define each activity as a Transition object
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

# Define the partial order
root = StrictPartialOrder(nodes=[
    seed_selection,
    germination_setup,
    nutrient_mix,
    water_control,
    climate_adjust,
    sensor_monitor,
    lighting_tune,
    airflow_manage,
    health_scan,
    pest_control,
    harvest_timing,
    cold_storage,
    package_prep,
    delivery_plan,
    feedback_loop
])

# Define the dependencies between activities
root.order.add_edge(seed_selection, germination_setup)
root.order.add_edge(seed_selection, nutrient_mix)
root.order.add_edge(seed_selection, water_control)
root.order.add_edge(seed_selection, climate_adjust)
root.order.add_edge(seed_selection, sensor_monitor)
root.order.add_edge(seed_selection, lighting_tune)
root.order.add_edge(seed_selection, airflow_manage)
root.order.add_edge(seed_selection, health_scan)
root.order.add_edge(seed_selection, pest_control)
root.order.add_edge(seed_selection, harvest_timing)
root.order.add_edge(seed_selection, cold_storage)
root.order.add_edge(seed_selection, package_prep)
root.order.add_edge(seed_selection, delivery_plan)
root.order.add_edge(seed_selection, feedback_loop)

# Now, 'root' contains the POWL model for the urban vertical farming process.