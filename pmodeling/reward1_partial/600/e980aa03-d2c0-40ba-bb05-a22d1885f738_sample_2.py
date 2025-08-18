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
root = StrictPartialOrder(
    nodes=[
        client_brief, spec_analysis, material_sourcing, component_vetting, frame_assembly, sensor_install, 
        propulsion_setup, calibration, software_load, flight_test, ai_training, qa_review, mission_pack, 
        client_training, deployment_support
    ],
    order=[
        # Define the dependencies between activities
        (client_brief, spec_analysis),
        (spec_analysis, material_sourcing),
        (material_sourcing, component_vetting),
        (component_vetting, frame_assembly),
        (frame_assembly, sensor_install),
        (sensor_install, propulsion_setup),
        (propulsion_setup, calibration),
        (calibration, software_load),
        (software_load, flight_test),
        (flight_test, ai_training),
        (ai_training, qa_review),
        (qa_review, mission_pack),
        (mission_pack, client_training),
        (client_training, deployment_support)
    ]
)