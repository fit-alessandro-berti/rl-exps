import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
activities = ['Site Survey', 'Structural Check', 'Resource Sourcing', 'System Install', 'Lighting Setup', 'Irrigation Setup', 'Stakeholder Meet', 'Volunteer Train', 'Regulation Review', 'Crop Selection', 'Planting Phase', 'Climate Control', 'Growth Monitor', 'Data Logging', 'Harvest Event', 'Waste Manage', 'Feedback Collect']

# Create the transitions for each activity
transitions = {activity: Transition(label=activity) for activity in activities}

# Define the process steps
site_survey = transitions['Site Survey']
structural_check = transitions['Structural Check']
resource_sourcing = transitions['Resource Sourcing']
system_install = transitions['System Install']
lighting_setup = transitions['Lighting Setup']
irrigation_setup = transitions['Irrigation Setup']
stakeholder_meet = transitions['Stakeholder Meet']
volunteer_train = transitions['Volunteer Train']
regulation_review = transitions['Regulation Review']
crop_selection = transitions['Crop Selection']
planting_phase = transitions['Planting Phase']
climate_control = transitions['Climate Control']
growth_monitor = transitions['Growth Monitor']
data_logging = transitions['Data Logging']
harvest_event = transitions['Harvest Event']
waste_manage = transitions['Waste Manage']
feedback_collect = transitions['Feedback Collect']

# Define the process flow
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

# Add dependencies between activities
root.order.add_edge(site_survey, structural_check)
root.order.add_edge(site_survey, resource_sourcing)
root.order.add_edge(structural_check, system_install)
root.order.add_edge(resource_sourcing, system_install)
root.order.add_edge(system_install, lighting_setup)
root.order.add_edge(system_install, irrigation_setup)
root.order.add_edge(system_install, stakeholder_meet)
root.order.add_edge(system_install, volunteer_train)
root.order.add_edge(system_install, regulation_review)
root.order.add_edge(lighting_setup, planting_phase)
root.order.add_edge(irrigation_setup, planting_phase)
root.order.add_edge(stakeholder_meet, crop_selection)
root.order.add_edge(volunteer_train, crop_selection)
root.order.add_edge(regulation_review, crop_selection)
root.order.add_edge(crop_selection, planting_phase)
root.order.add_edge(climate_control, growth_monitor)
root.order.add_edge(growth_monitor, data_logging)
root.order.add_edge(data_logging, harvest_event)
root.order.add_edge(harvest_event, waste_manage)
root.order.add_edge(harvest_event, feedback_collect)

# Return the root of the POWL model
return root