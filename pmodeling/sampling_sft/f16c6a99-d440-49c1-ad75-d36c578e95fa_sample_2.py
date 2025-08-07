import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
site_survey       = Transition(label='Site Survey')
design_layout     = Transition(label='Design Layout')
sensor_deploy     = Transition(label='Sensor Deploy')
crop_select       = Transition(label='Crop Select')
system_install    = Transition(label='System Install')
energy_setup      = Transition(label='Energy Setup')
water_cycle       = Transition(label='Water Cycle')
pest_control      = Transition(label='Pest Control')
regulatory_check  = Transition(label='Regulatory Check')
staff_training    = Transition(label='Staff Training')
data_configure    = Transition(label='Data Configure')
supply_plan       = Transition(label='Supply Plan')
harvest_schedule  = Transition(label='Harvest Schedule')
quality_audit     = Transition(label='Quality Audit')
market_launch     = Transition(label='Market Launch')
feedback_loop     = Transition(label='Feedback Loop')

# Loop for continuous feedback and adjustment
feedback_loop_body = StrictPartialOrder(nodes=[data_configure, supply_plan, harvest_schedule, quality_audit, market_launch])
feedback_loop_body.order.add_edge(data_configure, supply_plan)
feedback_loop_body.order.add_edge(supply_plan, harvest_schedule)
feedback_loop_body.order.add_edge(harvest_schedule, quality_audit)
feedback_loop_body.order.add_edge(quality_audit, market_launch)
feedback_loop_body.order.add_edge(market_launch, data_configure)

# Main partial order of the process
root = StrictPartialOrder(nodes=[
    site_survey,
    design_layout,
    sensor_deploy,
    crop_select,
    system_install,
    energy_setup,
    water_cycle,
    pest_control,
    regulatory_check,
    staff_training,
    data_configure,
    supply_plan,
    harvest_schedule,
    quality_audit,
    market_launch,
    feedback_loop
])

# Define the control-flow dependencies
root.order.add_edge(site_survey, design_layout)
root.order.add_edge(design_layout, sensor_deploy)
root.order.add_edge(sensor_deploy, crop_select)
root.order.add_edge(crop_select, system_install)
root.order.add_edge(system_install, energy_setup)
root.order.add_edge(energy_setup, water_cycle)
root.order.add_edge(water_cycle, pest_control)
root.order.add_edge(pest_control, regulatory_check)
root.order.add_edge(regulatory_check, staff_training)
root.order.add_edge(staff_training, data_configure)

# After initial setup, enter the feedback loop
root.order.add_edge(data_configure, feedback_loop)
for src, tgt in feedback_loop_body.order.edges:
    root.order.add_edge(feedback_loop, src)
    root.order.add_edge(tgt, feedback_loop)

# Final steps after the feedback loop completes
root.order.add_edge(feedback_loop, supply_plan)
root.order.add_edge(supply_plan, harvest_schedule)
root.order.add_edge(harvest_schedule, quality_audit)
root.order.add_edge(quality_audit, market_launch)
root.order.add_edge(market_launch, feedback_loop)