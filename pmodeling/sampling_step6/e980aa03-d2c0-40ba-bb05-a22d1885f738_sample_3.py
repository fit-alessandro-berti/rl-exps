import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for each activity
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

# Create the partial order
root = StrictPartialOrder(nodes=[client_brief, spec_analysis, material_sourcing, component_vetting, frame_assembly, sensor_install, propulsion_setup, calibration, software_load, flight_test, ai_training, qa_review, mission_pack, client_training, deployment_support])
# Add dependencies if any are specified in the problem statement
# For example, if 'Spec Analysis' must precede 'Material Sourcing', you would add:
# root.order.add_edge(client_brief, spec_analysis)
# root.order.add_edge(spec_analysis, material_sourcing)

# Save the result in the variable 'root'