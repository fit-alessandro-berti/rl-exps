import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
site_survey    = Transition(label='Site Survey')
structural_check = Transition(label='Structural Check')
resource_sourcing = Transition(label='Resource Sourcing')
system_install = Transition(label='System Install')
lighting_setup = Transition(label='Lighting Setup')
irrigation_setup = Transition(label='Irrigation Setup')
stakeholder_meet = Transition(label='Stakeholder Meet')
volunteer_train = Transition(label='Volunteer Train')
regulation_review = Transition(label='Regulation Review')
crop_selection = Transition(label='Crop Selection')
planting_phase = Transition(label='Planting Phase')
climate_control = Transition(label='Climate Control')
growth_monitor = Transition(label='Growth Monitor')
data_logging = Transition(label='Data Logging')
harvest_event = Transition(label='Harvest Event')
waste_manage = Transition(label='Waste Manage')
feedback_collect = Transition(label='Feedback Collect')

# Build the root partial order
root = StrictPartialOrder(nodes=[
    site_survey, structural_check, resource_sourcing,
    system_install, lighting_setup, irrigation_setup,
    stakeholder_meet, volunteer_train, regulation_review,
    crop_selection, planting_phase,
    climate_control, growth_monitor, data_logging,
    harvest_event, waste_manage, feedback_collect
])

# Structural check must precede resource sourcing
root.order.add_edge(site_survey, resource_sourcing)
root.order.add_edge(structural_check, resource_sourcing)

# Resource sourcing must precede installation
root.order.add_edge(resource_sourcing, system_install)

# Installation must precede lighting and irrigation setup
root.order.add_edge(system_install, lighting_setup)
root.order.add_edge(system_install, irrigation_setup)

# Lighting and irrigation setup must precede climate control
root.order.add_edge(lighting_setup, climate_control)
root.order.add_edge(irrigation_setup, climate_control)

# Climate control must precede planting phase
root.order.add_edge(climate_control, planting_phase)

# Planting phase must precede growth monitoring
root.order.add_edge(planting_phase, growth_monitor)

# Growth monitoring must precede data logging
root.order.add_edge(growth_monitor, data_logging)

# Data logging must precede harvest event
root.order.add_edge(data_logging, harvest_event)

# Harvest event must precede waste management
root.order.add_edge(harvest_event, waste_manage)

# Waste management must precede feedback collection
root.order.add_edge(waste_manage, feedback_collect)

# Stakeholder and volunteer meetings can happen in parallel before regulation review
root.order.add_edge(stakeholder_meet, regulation_review)
root.order.add_edge(volunteer_train, regulation_review)