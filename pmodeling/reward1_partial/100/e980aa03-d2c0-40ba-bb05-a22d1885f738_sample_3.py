import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
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

# Define operators and partial orders
xor = OperatorPOWL(operator=Operator.XOR, children=[qa_review, client_training])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[mission_pack, deployment_support])

loop = OperatorPOWL(operator=Operator.LOOP, children=[frame_assembly, material_sourcing, component_vetting, sensor_install, propulsion_setup, calibration, software_load, flight_test, ai_training])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[qa_review, client_training, mission_pack, deployment_support])

root = StrictPartialOrder(nodes=[client_brief, spec_analysis, loop, xor, loop2, xor2])
root.order.add_edge(client_brief, spec_analysis)
root.order.add_edge(spec_analysis, loop)
root.order.add_edge(loop, xor)
root.order.add_edge(xor, loop2)
root.order.add_edge(loop2, xor2)
root.order.add_edge(xor2, deployment_support)

# Print the final result
print(root)