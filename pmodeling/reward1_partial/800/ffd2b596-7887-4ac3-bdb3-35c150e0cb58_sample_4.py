import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for the process
sourcing = Transition(label='Component Sourcing')
calibrate = Transition(label='Sensor Calibrate')
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

# Define the POWL model
root = StrictPartialOrder(
    nodes=[sourcing, calibrate, motor_assembly, frame_build, software_install,
           algorithm_tune, battery_integrate, signal_test, durability_check,
           flight_simulate, quality_inspect, compliance_review, packaging_prep,
           logistics_plan, client_feedback],
    order={
        sourcing: [calibrate, motor_assembly, frame_build],
        calibrate: [motor_assembly, frame_build],
        motor_assembly: [frame_build],
        frame_build: [software_install, algorithm_tune],
        software_install: [algorithm_tune],
        algorithm_tune: [battery_integrate, signal_test],
        battery_integrate: [signal_test],
        signal_test: [durability_check, quality_inspect],
        durability_check: [quality_inspect],
        quality_inspect: [compliance_review, packaging_prep],
        compliance_review: [packaging_prep],
        packaging_prep: [logistics_plan, client_feedback],
        logistics_plan: [client_feedback],
        client_feedback: []
    }
)