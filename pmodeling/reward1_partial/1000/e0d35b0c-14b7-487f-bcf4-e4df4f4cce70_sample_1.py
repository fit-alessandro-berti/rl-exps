import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
site_survey = Transition(label='Site Survey')
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

# Define the control-flow operators
# Exclusive choice for resource sourcing and system install
resource_sourcing_install = OperatorPOWL(operator=Operator.XOR, children=[resource_sourcing, system_install])

# Loop for climate control, growth monitor, and data logging
climate_control_loop = OperatorPOWL(operator=Operator.LOOP, children=[climate_control, growth_monitor, data_logging])

# Parallel activities for stakeholder meet, volunteer train, and regulation review
stakeholder_volunteer_review = OperatorPOWL(operator=Operator.PARALLEL, children=[stakeholder_meet, volunteer_train, regulation_review])

# Loop for crop selection, planting phase, climate control, growth monitor, and data logging
crop_selection_planting_loop = OperatorPOWL(operator=Operator.LOOP, children=[crop_selection, planting_phase, climate_control_loop])

# Root model with all activities
root = StrictPartialOrder(nodes=[site_survey, structural_check, resource_sourcing_install, stakeholder_volunteer_review, crop_selection_planting_loop, harvest_event, waste_manage, feedback_collect])
root.order.add_edge(site_survey, structural_check)
root.order.add_edge(structural_check, resource_sourcing_install)
root.order.add_edge(resource_sourcing_install, stakeholder_volunteer_review)
root.order.add_edge(stakeholder_volunteer_review, crop_selection_planting_loop)
root.order.add_edge(crop_selection_planting_loop, harvest_event)
root.order.add_edge(harvest_event, waste_manage)
root.order.add_edge(waste_manage, feedback_collect)