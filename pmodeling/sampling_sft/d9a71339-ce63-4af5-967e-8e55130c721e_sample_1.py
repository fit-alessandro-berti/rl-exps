import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
site_survey      = Transition(label='Site Survey')
structural_check = Transition(label='Structural Check')
modular_install  = Transition(label='Modular Install')
hydroponic_setup = Transition(label='Hydroponic Setup')
nutrient_mix     = Transition(label='Nutrient Mix')
sensor_setup     = Transition(label='Sensor Setup')
ai_training      = Transition(label='AI Training')
data_capture     = Transition(label='Data Capture')
maintenance_plan = Transition(label='Maintenance Plan')
pest_scan        = Transition(label='Pest Scan')
growth_monitor   = Transition(label='Growth Monitor')
harvest_sync     = Transition(label='Harvest Sync')
quality_test     = Transition(label='Quality Test')
package_prep     = Transition(label='Package Prep')
logistics_plan   = Transition(label='Logistics Plan')

# Build the core sequential workflow as a strict partial order
core_workflow = StrictPartialOrder(nodes=[
    site_survey,
    structural_check,
    modular_install,
    hydroponic_setup,
    nutrient_mix,
    sensor_setup,
    ai_training,
    data_capture,
    maintenance_plan,
    pest_scan,
    growth_monitor,
    harvest_sync,
    quality_test,
    package_prep,
    logistics_plan
])

# Add sequential edges
core_workflow.order.add_edge(site_survey,    structural_check)
core_workflow.order.add_edge(structural_check, modular_install)
core_workflow.order.add_edge(modular_install, hydroponic_setup)
core_workflow.order.add_edge(hydroponic_setup, nutrient_mix)
core_workflow.order.add_edge(nutrient_mix, sensor_setup)
core_workflow.order.add_edge(sensor_setup, ai_training)
core_workflow.order.add_edge(ai_training, data_capture)
core_workflow.order.add_edge(data_capture, maintenance_plan)
core_workflow.order.add_edge(maintenance_plan, pest_scan)
core_workflow.order.add_edge(pest_scan, growth_monitor)
core_workflow.order.add_edge(growth_monitor, harvest_sync)
core_workflow.order.add_edge(harvest_sync, quality_test)
core_workflow.order.add_edge(quality_test, package_prep)
core_workflow.order.add_edge(package_prep, logistics_plan)

# Loop for ongoing data acquisition and maintenance
loop_body = StrictPartialOrder(nodes=[data_capture, maintenance_plan])
loop_body.order.add_edge(data_capture, maintenance_plan)
loop = OperatorPOWL(operator=Operator.LOOP, children=[loop_body, loop_body])

# Build the full root partial order
root = StrictPartialOrder(nodes=[
    site_survey,
    structural_check,
    modular_install,
    hydroponic_setup,
    nutrient_mix,
    sensor_setup,
    ai_training,
    loop,
    pest_scan,
    growth_monitor,
    harvest_sync,
    quality_test,
    package_prep,
    logistics_plan
])

# Add sequential edges before the loop
root.order.add_edge(site_survey,    structural_check)
root.order.add_edge(structural_check, modular_install)
root.order.add_edge(modular_install, hydroponic_setup)
root.order.add_edge(hydroponic_setup, nutrient_mix)
root.order.add_edge(nutrient_mix, sensor_setup)
root.order.add_edge(sensor_setup, ai_training)

# Add the loop after the initial setup
root.order.add_edge(ai_training, loop)

# Add sequential edges after the loop
root.order.add_edge(loop, pest_scan)
root.order.add_edge(pest_scan, growth_monitor)
root.order.add_edge(growth_monitor, harvest_sync)
root.order.add_edge(harvest_sync, quality_test)
root.order.add_edge(quality_test, package_prep)
root.order.add_edge(package_prep, logistics_plan)

print(root)