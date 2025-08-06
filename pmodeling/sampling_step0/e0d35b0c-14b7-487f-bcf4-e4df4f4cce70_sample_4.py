import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator
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

# Define silent activities (tau labels)
skip1 = SilentTransition()
skip2 = SilentTransition()
skip3 = SilentTransition()
skip4 = SilentTransition()

# Define exclusive choice (X)
exclusive_choice1 = OperatorPOWL(operator=Operator.XOR, children=[regulation_review, skip1])
exclusive_choice2 = OperatorPOWL(operator=Operator.XOR, children=[stakeholder_meet, skip2])
exclusive_choice3 = OperatorPOWL(operator=Operator.XOR, children=[volunteer_train, skip3])
exclusive_choice4 = OperatorPOWL(operator=Operator.XOR, children=[crop_selection, skip4])

# Define loop nodes (*)
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[lighting_setup, irrigation_setup])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[climate_control, growth_monitor])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[data_logging, waste_manage])
loop4 = OperatorPOWL(operator=Operator.LOOP, children=[feedback_collect, skip4])

# Define partial order
root = StrictPartialOrder(nodes=[
    site_survey,
    structural_check,
    resource_sourcing,
    system_install,
    exclusive_choice1,
    exclusive_choice2,
    exclusive_choice3,
    exclusive_choice4,
    loop1,
    loop2,
    loop3,
    loop4
])

# Add dependencies
root.order.add_edge(site_survey, structural_check)
root.order.add_edge(site_survey, resource_sourcing)
root.order.add_edge(site_survey, system_install)
root.order.add_edge(structural_check, exclusive_choice1)
root.order.add_edge(resource_sourcing, exclusive_choice2)
root.order.add_edge(system_install, exclusive_choice3)
root.order.add_edge(exclusive_choice1, exclusive_choice4)
root.order.add_edge(exclusive_choice2, exclusive_choice4)
root.order.add_edge(exclusive_choice3, exclusive_choice4)
root.order.add_edge(exclusive_choice4, loop1)
root.order.add_edge(exclusive_choice4, loop2)
root.order.add_edge(exclusive_choice4, loop3)
root.order.add_edge(exclusive_choice4, loop4)
root.order.add_edge(loop1, loop2)
root.order.add_edge(loop2, loop3)
root.order.add_edge(loop3, loop4)