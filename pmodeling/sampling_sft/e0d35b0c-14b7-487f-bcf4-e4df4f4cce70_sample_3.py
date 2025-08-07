import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
site_survey      = Transition(label='Site Survey')
structural_check = Transition(label='Structural Check')
resource_sourcing= Transition(label='Resource Sourcing')
system_install   = Transition(label='System Install')
lighting_setup   = Transition(label='Lighting Setup')
irrigation_setup = Transition(label='Irrigation Setup')
stakeholder_meet = Transition(label='Stakeholder Meet')
volunteer_train  = Transition(label='Volunteer Train')
regulation_review= Transition(label='Regulation Review')
crop_selection   = Transition(label='Crop Selection')
planting_phase   = Transition(label='Planting Phase')
climate_control  = Transition(label='Climate Control')
growth_monitor   = Transition(label='Growth Monitor')
data_logging     = Transition(label='Data Logging')
harvest_event    = Transition(label='Harvest Event')
waste_manage     = Transition(label='Waste Manage')
feedback_collect = Transition(label='Feedback Collect')

# Build the monitoring & optimization loop: Growth Monitor -> Data Logging -> Feedback Collect
monitor_loop_body = StrictPartialOrder(nodes=[growth_monitor, data_logging, feedback_collect])
monitor_loop_body.order.add_edge(growth_monitor, data_logging)
monitor_loop_body.order.add_edge(data_logging, feedback_collect)

# Loop: Climate Control, then optionally do the monitoring loop, then repeat
monitor_loop = OperatorPOWL(operator=Operator.LOOP, children=[climate_control, monitor_loop_body])

# Assemble the full process into a strict partial order
root = StrictPartialOrder(nodes=[
    site_survey,
    structural_check,
    resource_sourcing,
    system_install,
    lighting_setup,
    irrigation_setup,
    stakeholder_meet,
    volunteer_train,
    regulation_review,
    crop_selection,
    planting_phase,
    monitor_loop,
    harvest_event,
    waste_manage
])

# Define the control-flow dependencies
root.order.add_edge(site_survey, structural_check)
root.order.add_edge(structural_check, resource_sourcing)
root.order.add_edge(resource_sourcing, system_install)
root.order.add_edge(system_install, lighting_setup)
root.order.add_edge(system_install, irrigation_setup)
root.order.add_edge(lighting_setup, stakeholder_meet)
root.order.add_edge(irrigation_setup, stakeholder_meet)
root.order.add_edge(stakeholder_meet, volunteer_train)
root.order.add_edge(volunteer_train, regulation_review)
root.order.add_edge(regulation_review, crop_selection)
root.order.add_edge(crop_selection, planting_phase)
root.order.add_edge(planting_phase, monitor_loop)
root.order.add_edge(monitor_loop, harvest_event)
root.order.add_edge(harvest_event, waste_manage)