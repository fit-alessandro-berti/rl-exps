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

# Define the control flow operators
xor = OperatorPOWL(operator=Operator.XOR, children=[stakeholder_meet, volunteer_train])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[regulation_review, crop_selection])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[planting_phase, climate_control])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[growth_monitor, data_logging])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[harvest_event, waste_manage])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[feedback_collect])

# Define the partial order
root = StrictPartialOrder(nodes=[site_survey, structural_check, resource_sourcing, system_install, lighting_setup, irrigation_setup, xor, xor2, xor3, xor4, xor5, xor6])
root.order.add_edge(site_survey, structural_check)
root.order.add_edge(structural_check, resource_sourcing)
root.order.add_edge(resource_sourcing, system_install)
root.order.add_edge(system_install, lighting_setup)
root.order.add_edge(lighting_setup, irrigation_setup)
root.order.add_edge(irrigation_setup, xor)
root.order.add_edge(xor, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, xor5)
root.order.add_edge(xor5, xor6)
root.order.add_edge(xor6, feedback_collect)