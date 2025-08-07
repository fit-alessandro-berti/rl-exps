import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define all activities as transitions
site_survey      = Transition(label='Site Survey')
design_layout    = Transition(label='Design Layout')
sensor_deploy    = Transition(label='Sensor Deploy')
crop_select      = Transition(label='Crop Select')
system_install   = Transition(label='System Install')
energy_setup     = Transition(label='Energy Setup')
water_cycle      = Transition(label='Water Cycle')
pest_control     = Transition(label='Pest Control')
regulatory_check = Transition(label='Regulatory Check')
staff_training   = Transition(label='Staff Training')
data_configure   = Transition(label='Data Configure')
supply_plan      = Transition(label='Supply Plan')
harvest_schedule = Transition(label='Harvest Schedule')
quality_audit    = Transition(label='Quality Audit')
market_launch    = Transition(label='Market Launch')
feedback_loop    = Transition(label='Feedback Loop')

# Build the partial order
root = StrictPartialOrder(nodes=[
    site_survey, design_layout, sensor_deploy,
    crop_select, system_install, energy_setup,
    water_cycle, pest_control, regulatory_check,
    staff_training, data_configure, supply_plan,
    harvest_schedule, quality_audit, market_launch,
    feedback_loop
])

# Define the control-flow dependencies
root.order.add_edge(site_survey, design_layout)
root.order.add_edge(design_layout, sensor_deploy)
root.order.add_edge(sensor_deploy, crop_select)
root.order.add_edge(crop_select, system_install)
root.order.add_edge(system_install, energy_setup)
root.order.add_edge(system_install, water_cycle)
root.order.add_edge(system_install, pest_control)
root.order.add_edge(energy_setup, regulatory_check)
root.order.add_edge(energy_setup, data_configure)
root.order.add_edge(water_cycle, data_configure)
root.order.add_edge(pest_control, data_configure)
root.order.add_edge(regulatory_check, staff_training)
root.order.add_edge(regulatory_check, data_configure)
root.order.add_edge(data_configure, supply_plan)
root.order.add_edge(data_configure, harvest_schedule)
root.order.add_edge(data_configure, quality_audit)
root.order.add_edge(data_configure, market_launch)
root.order.add_edge(data_configure, feedback_loop)

# Loop for continuous feedback and optimization
loop_body = StrictPartialOrder(nodes=[
    quality_audit, market_launch
])
loop_body.order.add_edge(quality_audit, market_launch)
feedback_loop_po = StrictPartialOrder(nodes=[feedback_loop])
feedback_loop_po.order.add_edge(feedback_loop, loop_body)

# Merge the feedback loop into the overall partial order
root.order.add_edge(data_configure, feedback_loop_po)
root.order.add_edge(feedback_loop, feedback_loop_po)

print(root)