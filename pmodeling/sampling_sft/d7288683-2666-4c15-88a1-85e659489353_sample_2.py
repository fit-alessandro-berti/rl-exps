import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
comp_sourcing = Transition(label='Component Sourcing')
frame_assembly = Transition(label='Frame Assembly')
motor_install = Transition(label='Motor Installation')
sensor_mount = Transition(label='Sensor Mounting')
wiring_setup = Transition(label='Wiring Setup')
firmware_upload = Transition(label='Firmware Upload')
ai_module = Transition(label='AI Module')
calibration = Transition(label='Calibration Phase')
stress_test = Transition(label='Stress Testing')
flight_sim = Transition(label='Flight Simulation')
pattern_adj = Transition(label='Pattern Adjustment')
quality_inspect = Transition(label='Quality Inspect')
compliance_check = Transition(label='Compliance Check')
packaging_final = Transition(label='Packaging Final')
delivery_setup = Transition(label='Delivery Setup')

# Loop for iterative flight pattern adjustment
# A = Flight Simulation -> Pattern Adjustment
# B = skip (no additional adjustment after one iteration)
adjust_loop = OperatorPOWL(operator=Operator.LOOP, children=[flight_sim, pattern_adj])

# Build the partial order
root = StrictPartialOrder(nodes=[
    comp_sourcing,
    frame_assembly,
    motor_install,
    sensor_mount,
    wiring_setup,
    firmware_upload,
    ai_module,
    calibration,
    stress_test,
    adjust_loop,
    quality_inspect,
    compliance_check,
    packaging_final,
    delivery_setup
])

# Define the control-flow dependencies
root.order.add_edge(comp_sourcing, frame_assembly)
root.order.add_edge(frame_assembly, motor_install)
root.order.add_edge(frame_assembly, sensor_mount)
root.order.add_edge(frame_assembly, wiring_setup)
root.order.add_edge(motor_install, firmware_upload)
root.order.add_edge(sensor_mount, firmware_upload)
root.order.add_edge(wiring_setup, firmware_upload)
root.order.add_edge(firmware_upload, ai_module)
root.order.add_edge(ai_module, calibration)
root.order.add_edge(calibration, stress_test)
root.order.add_edge(stress_test, adjust_loop)
root.order.add_edge(adjust_loop, quality_inspect)
root.order.add_edge(quality_inspect, compliance_check)
root.order.add_edge(compliance_check, packaging_final)
root.order.add_edge(packaging_final, delivery_setup)