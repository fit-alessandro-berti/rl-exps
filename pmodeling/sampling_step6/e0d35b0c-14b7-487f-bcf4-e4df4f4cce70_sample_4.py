import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for each activity
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

# Define the partial order
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
    climate_control,
    growth_monitor,
    data_logging,
    harvest_event,
    waste_manage,
    feedback_collect
])

# Define the dependencies between activities
root.order.add_edge(site_survey, structural_check)
root.order.add_edge(site_survey, resource_sourcing)
root.order.add_edge(site_survey, system_install)
root.order.add_edge(site_survey, lighting_setup)
root.order.add_edge(site_survey, irrigation_setup)
root.order.add_edge(site_survey, stakeholder_meet)
root.order.add_edge(site_survey, volunteer_train)
root.order.add_edge(site_survey, regulation_review)
root.order.add_edge(site_survey, crop_selection)
root.order.add_edge(site_survey, planting_phase)
root.order.add_edge(site_survey, climate_control)
root.order.add_edge(site_survey, growth_monitor)
root.order.add_edge(site_survey, data_logging)
root.order.add_edge(site_survey, harvest_event)
root.order.add_edge(site_survey, waste_manage)
root.order.add_edge(site_survey, feedback_collect)