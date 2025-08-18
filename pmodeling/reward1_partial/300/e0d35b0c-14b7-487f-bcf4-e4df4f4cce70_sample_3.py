import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
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

# Define parallel activities
stakeholder_meet_train = OperatorPOWL(operator=Operator.XOR, children=[stakeholder_meet, volunteer_train])
regulation_review_train = OperatorPOWL(operator=Operator.XOR, children=[regulation_review, volunteer_train])
crop_selection_train = OperatorPOWL(operator=Operator.XOR, children=[crop_selection, volunteer_train])
planting_phase_train = OperatorPOWL(operator=Operator.XOR, children=[planting_phase, volunteer_train])
climate_control_train = OperatorPOWL(operator=Operator.XOR, children=[climate_control, volunteer_train])
growth_monitor_train = OperatorPOWL(operator=Operator.XOR, children=[growth_monitor, volunteer_train])
data_logging_train = OperatorPOWL(operator=Operator.XOR, children=[data_logging, volunteer_train])
harvest_event_train = OperatorPOWL(operator=Operator.XOR, children=[harvest_event, volunteer_train])
waste_manage_train = OperatorPOWL(operator=Operator.XOR, children=[waste_manage, volunteer_train])
feedback_collect_train = OperatorPOWL(operator=Operator.XOR, children=[feedback_collect, volunteer_train])

# Define loop for monitoring and logging
monitoring_loop = OperatorPOWL(operator=Operator.LOOP, children=[growth_monitor, data_logging])

# Define root model
root = StrictPartialOrder(nodes=[
    site_survey, structural_check, resource_sourcing, system_install, lighting_setup, irrigation_setup,
    stakeholder_meet_train, regulation_review_train, crop_selection_train, planting_phase_train,
    climate_control_train, growth_monitor_train, data_logging_train, harvest_event_train, waste_manage_train,
    feedback_collect_train, monitoring_loop
])

# Add dependencies
root.order.add_edge(site_survey, structural_check)
root.order.add_edge(structural_check, resource_sourcing)
root.order.add_edge(resource_sourcing, system_install)
root.order.add_edge(system_install, lighting_setup)
root.order.add_edge(system_install, irrigation_setup)
root.order.add_edge(lighting_setup, stakeholder_meet_train)
root.order.add_edge(lighting_setup, regulation_review_train)
root.order.add_edge(irrigation_setup, crop_selection_train)
root.order.add_edge(irrigation_setup, planting_phase_train)
root.order.add_edge(crop_selection_train, climate_control_train)
root.order.add_edge(planting_phase_train, growth_monitor_train)
root.order.add_edge(climate_control_train, data_logging_train)
root.order.add_edge(data_logging_train, harvest_event_train)
root.order.add_edge(harvest_event_train, waste_manage_train)
root.order.add_edge(waste_manage_train, feedback_collect_train)
root.order.add_edge(feedback_collect_train, monitoring_loop)

print(root)