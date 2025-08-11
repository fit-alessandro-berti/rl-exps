import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions
client_brief = Transition(label='Client Brief')
spec_analysis = Transition(label='Spec Analysis')
material_sourcing = Transition(label='Material Sourcing')
component_vetting = Transition(label='Component Vetting')
frame_assembly = Transition(label='Frame Assembly')
sensor_install = Transition(label='Sensor Install')
propulsion_setup = Transition(label='Propulsion Setup')
calibration = Transition(label='Calibration')
software_load = Transition(label='Software Load')
flight_test = Transition(label='Flight Test')
ai_training = Transition(label='AI Training')
qa_review = Transition(label='QA Review')
mission_pack = Transition(label='Mission Pack')
client_training = Transition(label='Client Training')
deployment_support = Transition(label='Deployment Support')

# Define the silent transitions
skip = SilentTransition()

# Define the loops
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[component_vetting, material_sourcing])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[sensor_install, propulsion_setup])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[calibration, software_load])
loop4 = OperatorPOWL(operator=Operator.LOOP, children=[flight_test, skip])

# Define the choices
choice1 = OperatorPOWL(operator=Operator.XOR, children=[ai_training, qa_review])
choice2 = OperatorPOWL(operator=Operator.XOR, children=[mission_pack, skip])

# Define the partial order
root = StrictPartialOrder(nodes=[loop1, loop2, loop3, loop4, choice1, choice2])
root.order.add_edge(loop1, choice1)
root.order.add_edge(loop2, choice1)
root.order.add_edge(loop3, choice2)
root.order.add_edge(loop4, choice2)