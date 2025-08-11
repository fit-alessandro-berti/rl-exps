import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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

skip = SilentTransition()

loop_1 = OperatorPOWL(operator=Operator.LOOP, children=[material_sourcing, component_vetting])
loop_2 = OperatorPOWL(operator=Operator.LOOP, children=[sensor_install, propulsion_setup, calibration, software_load])
loop_3 = OperatorPOWL(operator=Operator.LOOP, children=[flight_test, ai_training])
loop_4 = OperatorPOWL(operator=Operator.LOOP, children=[qa_review, mission_pack])
loop_5 = OperatorPOWL(operator=Operator.LOOP, children=[client_training, deployment_support])

xor_1 = OperatorPOWL(operator=Operator.XOR, children=[frame_assembly, skip])
xor_2 = OperatorPOWL(operator=Operator.XOR, children=[loop_1, loop_2])
xor_3 = OperatorPOWL(operator=Operator.XOR, children=[loop_3, loop_4])
xor_4 = OperatorPOWL(operator=Operator.XOR, children=[loop_5, skip])

root = StrictPartialOrder(nodes=[xor_1, xor_2, xor_3, xor_4])
root.order.add_edge(xor_1, xor_2)
root.order.add_edge(xor_1, xor_3)
root.order.add_edge(xor_1, xor_4)
root.order.add_edge(xor_2, xor_3)
root.order.add_edge(xor_2, xor_4)
root.order.add_edge(xor_3, xor_4)