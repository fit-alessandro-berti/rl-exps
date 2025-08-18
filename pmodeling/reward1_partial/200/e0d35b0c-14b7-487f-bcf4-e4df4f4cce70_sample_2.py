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

# Define the parallel activities
stakeholder_activities = OperatorPOWL(operator=Operator.XOR, children=[stakeholder_meet, volunteer_train])
regulation_activities = OperatorPOWL(operator=Operator.XOR, children=[regulation_review, crop_selection])

# Define the loop for the crop growth phase
crop_growth_loop = OperatorPOWL(operator=Operator.LOOP, children=[climate_control, growth_monitor, data_logging])

# Define the partial order
root = StrictPartialOrder(nodes=[site_survey, structural_check, resource_sourcing, system_install, lighting_setup, irrigation_setup, stakeholder_activities, regulation_activities, planting_phase, crop_growth_loop, harvest_event, waste_manage, feedback_collect])
root.order.add_edge(site_survey, structural_check)
root.order.add_edge(site_survey, resource_sourcing)
root.order.add_edge(structural_check, system_install)
root.order.add_edge(system_install, lighting_setup)
root.order.add_edge(system_install, irrigation_setup)
root.order.add_edge(resource_sourcing, stakeholder_activities)
root.order.add_edge(resource_sourcing, regulation_activities)
root.order.add_edge(stakeholder_activities, planting_phase)
root.order.add_edge(regulation_activities, planting_phase)
root.order.add_edge(planting_phase, crop_growth_loop)
root.order.add_edge(crop_growth_loop, harvest_event)
root.order.add_edge(harvest_event, waste_manage)
root.order.add_edge(waste_manage, feedback_collect)