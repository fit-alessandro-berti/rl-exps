from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define activities
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
stakeholder_meet_volunteer_train = OperatorPOWL(operator=Operator.XOR, children=[stakeholder_meet, volunteer_train])
regulation_review_crop_selection = OperatorPOWL(operator=Operator.XOR, children=[regulation_review, crop_selection])
planting_phase_climate_control = OperatorPOWL(operator=Operator.XOR, children=[planting_phase, climate_control])
growth_monitor_data_logging = OperatorPOWL(operator=Operator.XOR, children=[growth_monitor, data_logging])
waste_manage_feedback_collect = OperatorPOWL(operator=Operator.XOR, children=[waste_manage, feedback_collect])

# Define the POWL model
root = StrictPartialOrder(nodes=[
    site_survey, structural_check, resource_sourcing, system_install, lighting_setup, irrigation_setup,
    stakeholder_meet_volunteer_train, regulation_review_crop_selection, planting_phase_climate_control,
    growth_monitor_data_logging, harvest_event, waste_manage_feedback_collect])

# Add dependencies
root.order.add_edge(site_survey, structural_check)
root.order.add_edge(site_survey, resource_sourcing)
root.order.add_edge(structural_check, system_install)
root.order.add_edge(resource_sourcing, system_install)
root.order.add_edge(system_install, lighting_setup)
root.order.add_edge(system_install, irrigation_setup)
root.order.add_edge(lighting_setup, stakeholder_meet_volunteer_train)
root.order.add_edge(irrigation_setup, stakeholder_meet_volunteer_train)
root.order.add_edge(stakeholder_meet_volunteer_train, regulation_review_crop_selection)
root.order.add_edge(regulation_review_crop_selection, planting_phase_climate_control)
root.order.add_edge(planting_phase_climate_control, growth_monitor_data_logging)
root.order.add_edge(growth_monitor_data_logging, waste_manage_feedback_collect)
root.order.add_edge(waste_manage_feedback_collect, harvest_event)