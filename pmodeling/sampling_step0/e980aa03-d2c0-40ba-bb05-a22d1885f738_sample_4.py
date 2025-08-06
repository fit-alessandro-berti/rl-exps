import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
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

# Define operators
# Exclusive choice (XOR)
xor = OperatorPOWL(operator=Operator.XOR, children=[client_brief, spec_analysis])

# Partial order
partial_order = StrictPartialOrder(nodes=[
    material_sourcing, component_vetting, frame_assembly,
    sensor_install, propulsion_setup, calibration,
    software_load, flight_test, ai_training, qa_review,
    mission_pack, client_training, deployment_support
])

# Define dependencies
partial_order.order.add_edge(material_sourcing, component_vetting)
partial_order.order.add_edge(component_vetting, frame_assembly)
partial_order.order.add_edge(frame_assembly, sensor_install)
partial_order.order.add_edge(frame_assembly, propulsion_setup)
partial_order.order.add_edge(sensor_install, calibration)
partial_order.order.add_edge(propulsion_setup, calibration)
partial_order.order.add_edge(calibration, software_load)
partial_order.order.add_edge(software_load, flight_test)
partial_order.order.add_edge(flight_test, ai_training)
partial_order.order.add_edge(ai_training, qa_review)
partial_order.order.add_edge(qa_review, mission_pack)
partial_order.order.add_edge(mission_pack, client_training)
partial_order.order.add_edge(client_training, deployment_support)

# Define root
root = partial_order