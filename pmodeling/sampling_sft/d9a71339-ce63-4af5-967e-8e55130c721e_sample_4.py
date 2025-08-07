import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define the atomic activities
site_survey     = Transition(label='Site Survey')
structural_check = Transition(label='Structural Check')
modular_install = Transition(label='Modular Install')
hydroponic_setup = Transition(label='Hydroponic Setup')
nutrient_mix    = Transition(label='Nutrient Mix')
sensor_setup    = Transition(label='Sensor Setup')
ai_training     = Transition(label='AI Training')
data_capture    = Transition(label='Data Capture')
maintenance_plan= Transition(label='Maintenance Plan')
pest_scan       = Transition(label='Pest Scan')
growth_monitor  = Transition(label='Growth Monitor')
harvest_sync    = Transition(label='Harvest Sync')
quality_test    = Transition(label='Quality Test')
package_prep    = Transition(label='Package Prep')
logistics_plan  = Transition(label='Logistics Plan')

# Define the concurrent monitoring and maintenance sequence
monitor_seq = StrictPartialOrder(nodes=[pest_scan, growth_monitor])
monitor_seq.order.add_edge(pest_scan, growth_monitor)

# Define the loop: do Data Capture, then either exit or do Monitor/Plan and Capture again
data_loop = OperatorPOWL(operator=Operator.LOOP, children=[data_capture, monitor_seq])

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    site_survey, structural_check, modular_install,
    hydroponic_setup, nutrient_mix, sensor_setup, ai_training,
    data_loop, maintenance_plan, harvest_sync, quality_test,
    package_prep, logistics_plan
])

# Define the control-flow dependencies
root.order.add_edge(site_survey, structural_check)
root.order.add_edge(structural_check, modular_install)
root.order.add_edge(modular_install, hydroponic_setup)
root.order.add_edge(hydroponic_setup, nutrient_mix)
root.order.add_edge(nutrient_mix, sensor_setup)
root.order.add_edge(sensor_setup, ai_training)
root.order.add_edge(ai_training, data_loop)
root.order.add_edge(data_loop, maintenance_plan)
root.order.add_edge(maintenance_plan, harvest_sync)
root.order.add_edge(harvest_sync, quality_test)
root.order.add_edge(quality_test, package_prep)
root.order.add_edge(package_prep, logistics_plan)

print(root)