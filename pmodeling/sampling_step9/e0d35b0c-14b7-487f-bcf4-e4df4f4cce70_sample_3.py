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

skip = SilentTransition()

loop_1 = OperatorPOWL(operator=Operator.LOOP, children=[system_install, lighting_setup, irrigation_setup])
loop_2 = OperatorPOWL(operator=Operator.LOOP, children=[stakeholder_meet, volunteer_train, regulation_review])
loop_3 = OperatorPOWL(operator=Operator.LOOP, children=[crop_selection, planting_phase, climate_control])
loop_4 = OperatorPOWL(operator=Operator.LOOP, children=[growth_monitor, data_logging, waste_manage])
loop_5 = OperatorPOWL(operator=Operator.LOOP, children=[harvest_event, feedback_collect])

xor_1 = OperatorPOWL(operator=Operator.XOR, children=[site_survey, structural_check])
xor_2 = OperatorPOWL(operator=Operator.XOR, children=[resource_sourcing, loop_1])
xor_3 = OperatorPOWL(operator=Operator.XOR, children=[loop_2, loop_3])
xor_4 = OperatorPOWL(operator=Operator.XOR, children=[loop_4, loop_5])

root = StrictPartialOrder(nodes=[xor_1, xor_2, xor_3, xor_4])
root.order.add_edge(xor_1, xor_2)
root.order.add_edge(xor_1, xor_3)
root.order.add_edge(xor_1, xor_4)
root.order.add_edge(xor_2, xor_3)
root.order.add_edge(xor_2, xor_4)
root.order.add_edge(xor_3, xor_4)

print(root)