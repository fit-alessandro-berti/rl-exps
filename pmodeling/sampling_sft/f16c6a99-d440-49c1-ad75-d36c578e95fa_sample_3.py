import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
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

# Build the partial‐order model
root = StrictPartialOrder(nodes=[
    site_survey, design_layout, sensor_deploy, crop_select,
    system_install, energy_setup, water_cycle, pest_control,
    regulatory_check, staff_training, data_configure,
    supply_plan, harvest_schedule, quality_audit,
    market_launch, feedback_loop
])

# Site Survey -> Design Layout
root.order.add_edge(site_survey, design_layout)

# Design Layout -> Sensor Deploy
root.order.add_edge(design_layout, sensor_deploy)

# Sensor Deploy -> Crop Select
root.order.add_edge(sensor_deploy, crop_select)

# Crop Select -> System Install
root.order.add_edge(crop_select, system_install)

# System Install -> Energy Setup
root.order.add_edge(system_install, energy_setup)

# Energy Setup -> Water Cycle
root.order.add_edge(energy_setup, water_cycle)

# Water Cycle -> Pest Control
root.order.add_edge(water_cycle, pest_control)

# Pest Control -> Regulatory Check
root.order.add_edge(pest_control, regulatory_check)

# Regulatory Check -> Staff Training
root.order.add_edge(regulatory_check, staff_training)

# Staff Training -> Data Configure
root.order.add_edge(staff_training, data_configure)

# Data Configure -> Supply Plan
root.order.add_edge(data_configure, supply_plan)

# Supply Plan -> Harvest Schedule
root.order.add_edge(supply_plan, harvest_schedule)

# Harvest Schedule -> Quality Audit
root.order.add_edge(harvest_schedule, quality_audit)

# Quality Audit -> Market Launch
root.order.add_edge(quality_audit, market_launch)

# Market Launch -> Feedback Loop
root.order.add_edge(market_launch, feedback_loop)