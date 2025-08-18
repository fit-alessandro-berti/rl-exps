import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
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

# Define the process
client_brief_choice = OperatorPOWL(operator=Operator.XOR, children=[client_brief, spec_analysis])
spec_analysis_choice = OperatorPOWL(operator=Operator.XOR, children=[material_sourcing, component_vetting])
component_vetting_choice = OperatorPOWL(operator=Operator.XOR, children=[frame_assembly, sensor_install])
frame_assembly_choice = OperatorPOWL(operator=Operator.XOR, children=[propulsion_setup, calibration])
propulsion_setup_choice = OperatorPOWL(operator=Operator.XOR, children=[software_load, flight_test])
calibration_choice = OperatorPOWL(operator=Operator.XOR, children=[ai_training, qa_review])
ai_training_choice = OperatorPOWL(operator=Operator.XOR, children=[mission_pack, client_training])
mission_pack_choice = OperatorPOWL(operator=Operator.XOR, children=[deployment_support, client_training])

# Define the partial order
root = StrictPartialOrder(nodes=[client_brief_choice, spec_analysis_choice, material_sourcing, component_vetting_choice, frame_assembly_choice, propulsion_setup_choice, calibration_choice, ai_training_choice, mission_pack_choice, deployment_support])
root.order.add_edge(client_brief_choice, spec_analysis_choice)
root.order.add_edge(spec_analysis_choice, material_sourcing)
root.order.add_edge(material_sourcing, component_vetting_choice)
root.order.add_edge(component_vetting_choice, frame_assembly_choice)
root.order.add_edge(frame_assembly_choice, propulsion_setup_choice)
root.order.add_edge(propulsion_setup_choice, calibration_choice)
root.order.add_edge(calibration_choice, ai_training_choice)
root.order.add_edge(ai_training_choice, mission_pack_choice)
root.order.add_edge(mission_pack_choice, deployment_support)

print(root)