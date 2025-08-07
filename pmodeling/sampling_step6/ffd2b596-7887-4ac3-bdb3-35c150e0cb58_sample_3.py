import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define each activity as a Transition object
component_sourcing = Transition(label='Component Sourcing')
sensor_calibrate = Transition(label='Sensor Calibrate')
motor_assembly = Transition(label='Motor Assembly')
frame_build = Transition(label='Frame Build')
software_install = Transition(label='Software Install')
algorithm_tune = Transition(label='Algorithm Tune')
battery_integrate = Transition(label='Battery Integrate')
signal_test = Transition(label='Signal Test')
durability_check = Transition(label='Durability Check')
flight_simulate = Transition(label='Flight Simulate')
quality_inspect = Transition(label='Quality Inspect')
compliance_review = Transition(label='Compliance Review')
packaging_prep = Transition(label='Packaging Prep')
logistics_plan = Transition(label='Logistics Plan')
client_feedback = Transition(label='Client Feedback')

# Define the root of the POWL model
root = StrictPartialOrder(nodes=[
    component_sourcing,
    sensor_calibrate,
    motor_assembly,
    frame_build,
    software_install,
    algorithm_tune,
    battery_integrate,
    signal_test,
    durability_check,
    flight_simulate,
    quality_inspect,
    compliance_review,
    packaging_prep,
    logistics_plan,
    client_feedback
])