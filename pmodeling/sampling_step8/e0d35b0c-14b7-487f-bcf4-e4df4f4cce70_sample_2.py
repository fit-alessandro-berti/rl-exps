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

# Define the partial order structure
root = StrictPartialOrder(
    nodes=[
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
    ],
    order=[
        (site_survey, structural_check), 
        (structural_check, resource_sourcing), 
        (resource_sourcing, system_install), 
        (system_install, lighting_setup), 
        (system_install, irrigation_setup), 
        (lighting_setup, stakeholder_meet), 
        (irrigation_setup, stakeholder_meet), 
        (stakeholder_meet, volunteer_train), 
        (volunteer_train, regulation_review), 
        (regulation_review, crop_selection), 
        (crop_selection, planting_phase), 
        (planting_phase, climate_control), 
        (climate_control, growth_monitor), 
        (growth_monitor, data_logging), 
        (data_logging, harvest_event), 
        (harvest_event, waste_manage), 
        (waste_manage, feedback_collect)
    ]
)