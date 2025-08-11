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

# Client Brief and Spec Analysis
client_brief_and_spec_analysis = OperatorPOWL(operator=Operator.XOR, children=[client_brief, spec_analysis])

# Material Sourcing and Component Vetting
material_sourcing_and_component_vetting = OperatorPOWL(operator=Operator.XOR, children=[material_sourcing, component_vetting])

# Frame Assembly and Sensor Install
frame_assembly_and_sensor_install = OperatorPOWL(operator=Operator.XOR, children=[frame_assembly, sensor_install])

# Propulsion Setup and Calibration
propulsion_setup_and_calibration = OperatorPOWL(operator=Operator.XOR, children=[propulsion_setup, calibration])

# Software Load and Flight Test
software_load_and_flight_test = OperatorPOWL(operator=Operator.XOR, children=[software_load, flight_test])

# AI Training and QA Review
ai_training_and_qa_review = OperatorPOWL(operator=Operator.XOR, children=[ai_training, qa_review])

# Mission Pack and Client Training
mission_pack_and_client_training = OperatorPOWL(operator=Operator.XOR, children=[mission_pack, client_training])

# Deployment Support
deployment_support = OperatorPOWL(operator=Operator.XOR, children=[deployment_support, skip])

root = StrictPartialOrder(nodes=[client_brief_and_spec_analysis, material_sourcing_and_component_vetting, frame_assembly_and_sensor_install, propulsion_setup_and_calibration, software_load_and_flight_test, ai_training_and_qa_review, mission_pack_and_client_training, deployment_support])
root.order.add_edge(client_brief_and_spec_analysis, material_sourcing_and_component_vetting)
root.order.add_edge(material_sourcing_and_component_vetting, frame_assembly_and_sensor_install)
root.order.add_edge(frame_assembly_and_sensor_install, propulsion_setup_and_calibration)
root.order.add_edge(propulsion_setup_and_calibration, software_load_and_flight_test)
root.order.add_edge(software_load_and_flight_test, ai_training_and_qa_review)
root.order.add_edge(ai_training_and_qa_review, mission_pack_and_client_training)
root.order.add_edge(mission_pack_and_client_training, deployment_support)