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

# Define the POWL model
root = StrictPartialOrder(nodes=[
    client_brief,
    spec_analysis,
    material_sourcing,
    component_vetting,
    frame_assembly,
    sensor_install,
    propulsion_setup,
    calibration,
    software_load,
    flight_test,
    ai_training,
    qa_review,
    mission_pack,
    client_training,
    deployment_support
])

# Add dependencies if necessary (not specified in the description)
# For example, if Client Brief and Spec Analysis must be done before Material Sourcing:
root.order.add_edge(client_brief, material_sourcing)
root.order.add_edge(spec_analysis, material_sourcing)

# Add more dependencies as needed based on the process description
# Example: Spec Analysis and Component Vetting must be done before Frame Assembly:
root.order.add_edge(spec_analysis, frame_assembly)
root.order.add_edge(component_vetting, frame_assembly)

# Continue adding dependencies for each activity as per the process description
# ...

# The final POWL model is defined in the 'root' variable