import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
seed_selection    = Transition(label='Seed Selection')
germination_setup = Transition(label='Germination Setup')
nutrient_mix      = Transition(label='Nutrient Mix')
water_control     = Transition(label='Water Control')
climate_adjust    = Transition(label='Climate Adjust')
sensor_monitor    = Transition(label='Sensor Monitor')
lighting_tune     = Transition(label='Lighting Tune')
airflow_manage    = Transition(label='Airflow Manage')
health_scan       = Transition(label='Health Scan')
pest_control      = Transition(label='Pest Control')
harvest_timing    = Transition(label='Harvest Timing')
cold_storage      = Transition(label='Cold Storage')
package_prep      = Transition(label='Package Prep')
delivery_plan     = Transition(label='Delivery Plan')
feedback_loop     = Transition(label='Feedback Loop')

# Build the monitoring sub-process: concurrent climate & sensor monitoring, then lighting & airflow tuning
monitoring = StrictPartialOrder(nodes=[sensor_monitor, climate_adjust, lighting_tune, airflow_manage])
monitoring.order.add_edge(sensor_monitor, climate_adjust)
monitoring.order.add_edge(lighting_tune, climate_adjust)
monitoring.order.add_edge(airflow_manage, climate_adjust)

# Build the adaptive sub-process: health scan followed by pest control
adaptive = StrictPartialOrder(nodes=[health_scan, pest_control])
adaptive.order.add_edge(health_scan, pest_control)

# Build the harvesting sub-process: harvest timing followed by cold storage and packaging
harvesting = StrictPartialOrder(nodes=[harvest_timing, cold_storage, package_prep])
harvesting.order.add_edge(harvest_timing, cold_storage)
harvesting.order.add_edge(cold_storage, package_prep)

# Build the final delivery sub-process: delivery plan and feedback loop
delivery = StrictPartialOrder(nodes=[delivery_plan, feedback_loop])
delivery.order.add_edge(delivery_plan, feedback_loop)

# Assemble the overall process as a partial order
root = StrictPartialOrder(nodes=[
    seed_selection,
    germination_setup,
    nutrient_mix,
    water_control,
    monitoring,
    adaptive,
    harvest_timing,
    cold_storage,
    package_prep,
    delivery
])

# Define the control-flow dependencies
root.order.add_edge(seed_selection,     germination_setup)
root.order.add_edge(germination_setup, nutrient_mix)
root.order.add_edge(germination_setup, water_control)
root.order.add_edge(nutrient_mix,       monitoring)
root.order.add_edge(water_control,      monitoring)
root.order.add_edge(monitoring,         adaptive)
root.order.add_edge(adaptive,           harvest_timing)
root.order.add_edge(harvest_timing,     cold_storage)
root.order.add_edge(harvest_timing,     package_prep)
root.order.add_edge(cold_storage,       delivery)
root.order.add_edge(package_prep,       delivery)