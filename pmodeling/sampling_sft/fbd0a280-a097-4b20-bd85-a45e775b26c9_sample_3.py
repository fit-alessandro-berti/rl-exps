import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define the basic activities
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

# Build the monitoring & control partial order
monitoring_po = StrictPartialOrder(nodes=[sensor_monitor, lighting_tune, airflow_manage])
monitoring_po.order.add_edge(sensor_monitor, lighting_tune)
monitoring_po.order.add_edge(sensor_monitor, airflow_manage)

control_po = StrictPartialOrder(nodes=[climate_adjust, health_scan, pest_control])
control_po.order.add_edge(climate_adjust, health_scan)
control_po.order.add_edge(climate_adjust, pest_control)

# Loop for continuous monitoring & control
monitoring_loop = OperatorPOWL(operator=Operator.LOOP, children=[monitoring_po, monitoring_po])
control_loop = OperatorPOWL(operator=Operator.LOOP, children=[control_po, control_po])

# Assemble the overall process
root = StrictPartialOrder(nodes=[
    seed_selection,
    germination_setup,
    nutrient_mix,
    water_control,
    climate_adjust,
    monitoring_loop,
    health_scan,
    pest_control,
    harvest_timing,
    cold_storage,
    package_prep,
    delivery_plan,
    feedback_loop
])

# Define the control & monitoring dependencies
root.order.add_edge(seed_selection,     germination_setup)
root.order.add_edge(germination_setup, nutrient_mix)
root.order.add_edge(germination_setup, water_control)
root.order.add_edge(nutrient_mix,       climate_adjust)
root.order.add_edge(water_control,      climate_adjust)
root.order.add_edge(climate_adjust,     monitoring_loop)

# Harvest timing must wait for control & monitoring to finish
root.order.add_edge(monitoring_loop, harvest_timing)
root.order.add_edge(control_loop, harvest_timing)

# After harvest, proceed to cold storage and packaging
root.order.add_edge(harvest_timing, cold_storage)
root.order.add_edge(harvest_timing, package_prep)

# Packaging must wait for cold storage
root.order.add_edge(cold_storage, package_prep)

# Delivery plan and feedback loop can start concurrently with packaging
root.order.add_edge(package_prep, delivery_plan)
root.order.add_edge(package_prep, feedback_loop)

# Feedback loop must finish before the cycle repeats
root.order.add_edge(feedback_loop, seed_selection)