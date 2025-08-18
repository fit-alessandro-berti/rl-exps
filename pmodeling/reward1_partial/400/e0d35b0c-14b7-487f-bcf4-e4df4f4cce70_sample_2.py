import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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

site_survey_order = OperatorPOWL(operator=Operator.XOR, children=[structural_check, resource_sourcing])
system_install_order = OperatorPOWL(operator=Operator.XOR, children=[lighting_setup, irrigation_setup])
stakeholder_meet_order = OperatorPOWL(operator=Operator.XOR, children=[volunteer_train, regulation_review])
crop_selection_order = OperatorPOWL(operator=Operator.XOR, children=[planting_phase, climate_control])
growth_monitor_order = OperatorPOWL(operator=Operator.XOR, children=[data_logging, harvest_event])
waste_manage_order = OperatorPOWL(operator=Operator.XOR, children=[feedback_collect, waste_manage])

root = StrictPartialOrder(nodes=[
    site_survey, structural_check, resource_sourcing, system_install, lighting_setup, irrigation_setup,
    stakeholder_meet, volunteer_train, regulation_review, crop_selection, planting_phase, climate_control,
    growth_monitor, data_logging, harvest_event, waste_manage, feedback_collect
])

root.order.add_edge(site_survey, site_survey_order)
root.order.add_edge(structural_check, site_survey_order)
root.order.add_edge(resource_sourcing, site_survey_order)
root.order.add_edge(system_install, system_install_order)
root.order.add_edge(lighting_setup, system_install_order)
root.order.add_edge(irrigation_setup, system_install_order)
root.order.add_edge(stakeholder_meet, stakeholder_meet_order)
root.order.add_edge(volunteer_train, stakeholder_meet_order)
root.order.add_edge(regulation_review, stakeholder_meet_order)
root.order.add_edge(crop_selection, crop_selection_order)
root.order.add_edge(planting_phase, crop_selection_order)
root.order.add_edge(climate_control, crop_selection_order)
root.order.add_edge(growth_monitor, growth_monitor_order)
root.order.add_edge(data_logging, growth_monitor_order)
root.order.add_edge(harvest_event, growth_monitor_order)
root.order.add_edge(waste_manage, waste_manage_order)
root.order.add_edge(feedback_collect, waste_manage_order)