import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all transitions
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

# Define the harvest loop: Harvest Schedule, Quality Audit, then optionally Feedback Loop
harvest_loop = OperatorPOWL(operator=Operator.LOOP, children=[harvest_schedule, quality_audit])

# Assemble the overall partial order
root = StrictPartialOrder(nodes=[
    site_survey, design_layout, sensor_deploy, crop_select,
    system_install, energy_setup, water_cycle, pest_control,
    regulatory_check, staff_training, data_configure,
    supply_plan, harvest_loop, market_launch, feedback_loop
])

# Define the control-flow dependencies
root.order.add_edge(site_survey,     design_layout)
root.order.add_edge(design_layout,   sensor_deploy)
root.order.add_edge(design_layout,   crop_select)
root.order.add_edge(sensor_deploy,   system_install)
root.order.add_edge(system_install,  energy_setup)
root.order.add_edge(system_install,  water_cycle)
root.order.add_edge(system_install,  pest_control)
root.order.add_edge(energy_setup,    regulatory_check)
root.order.add_edge(energy_setup,    staff_training)
root.order.add_edge(energy_setup,    data_configure)
root.order.add_edge(data_configure,  supply_plan)
root.order.add_edge(supply_plan,     harvest_loop)
root.order.add_edge(harvest_loop,    market_launch)
root.order.add_edge(market_launch,   feedback_loop)