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

client_brief_choice = OperatorPOWL(operator=Operator.XOR, children=[spec_analysis, material_sourcing])
material_sourcing_choice = OperatorPOWL(operator=Operator.XOR, children=[component_vetting, SilentTransition()])

component_vetting_loop = OperatorPOWL(operator=Operator.LOOP, children=[frame_assembly, sensor_install])
sensor_install_loop = OperatorPOWL(operator=Operator.LOOP, children=[propulsion_setup, calibration])
propulsion_setup_loop = OperatorPOWL(operator=Operator.LOOP, children=[software_load, flight_test])
software_load_loop = OperatorPOWL(operator=Operator.LOOP, children=[ai_training, qa_review])

qa_review_choice = OperatorPOWL(operator=Operator.XOR, children=[mission_pack, SilentTransition()])
mission_pack_choice = OperatorPOWL(operator=Operator.XOR, children=[client_training, deployment_support])

root = StrictPartialOrder(nodes=[client_brief, client_brief_choice, material_sourcing, material_sourcing_choice, component_vetting_loop, sensor_install_loop, propulsion_setup_loop, software_load_loop, qa_review_choice, mission_pack_choice])
root.order.add_edge(client_brief, client_brief_choice)
root.order.add_edge(client_brief_choice, material_sourcing)
root.order.add_edge(material_sourcing, material_sourcing_choice)
root.order.add_edge(material_sourcing_choice, component_vetting_loop)
root.order.add_edge(component_vetting_loop, sensor_install_loop)
root.order.add_edge(sensor_install_loop, propulsion_setup_loop)
root.order.add_edge(propulsion_setup_loop, software_load_loop)
root.order.add_edge(software_load_loop, qa_review_choice)
root.order.add_edge(qa_review_choice, mission_pack_choice)
root.order.add_edge(mission_pack_choice, client_training)
root.order.add_edge(mission_pack_choice, deployment_support)