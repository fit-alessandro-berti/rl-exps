import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
component_sourcing = Transition(label='Component Sourcing')
frame_assembly = Transition(label='Frame Assembly')
motor_installation = Transition(label='Motor Installation')
sensor_mounting = Transition(label='Sensor Mounting')
wiring_setup = Transition(label='Wiring Setup')
firmware_upload = Transition(label='Firmware Upload')
ai_module = Transition(label='AI Module')
calibration_phase = Transition(label='Calibration Phase')
stress_testing = Transition(label='Stress Testing')
flight_simulation = Transition(label='Flight Simulation')
pattern_adjustment = Transition(label='Pattern Adjustment')
quality_inspect = Transition(label='Quality Inspect')
compliance_check = Transition(label='Compliance Check')
packaging_final = Transition(label='Packaging Final')
delivery_setup = Transition(label='Delivery Setup')

# Define partial order nodes
component_sourcing_to_frame_assembly = OperatorPOWL(operator=Operator.XOR, children=[component_sourcing, frame_assembly])
frame_assembly_to_motor_installation = OperatorPOWL(operator=Operator.XOR, children=[frame_assembly, motor_installation])
motor_installation_to_sensor_mounting = OperatorPOWL(operator=Operator.XOR, children=[motor_installation, sensor_mounting])
sensor_mounting_to_wiring_setup = OperatorPOWL(operator=Operator.XOR, children=[sensor_mounting, wiring_setup])
wiring_setup_to_firmware_upload = OperatorPOWL(operator=Operator.XOR, children=[wiring_setup, firmware_upload])
firmware_upload_to_ai_module = OperatorPOWL(operator=Operator.XOR, children=[firmware_upload, ai_module])
ai_module_to_calibration_phase = OperatorPOWL(operator=Operator.XOR, children=[ai_module, calibration_phase])
calibration_phase_to_stress_testing = OperatorPOWL(operator=Operator.XOR, children=[calibration_phase, stress_testing])
stress_testing_to_flight_simulation = OperatorPOWL(operator=Operator.XOR, children=[stress_testing, flight_simulation])
flight_simulation_to_pattern_adjustment = OperatorPOWL(operator=Operator.XOR, children=[flight_simulation, pattern_adjustment])
pattern_adjustment_to_quality_inspect = OperatorPOWL(operator=Operator.XOR, children=[pattern_adjustment, quality_inspect])
quality_inspect_to_compliance_check = OperatorPOWL(operator=Operator.XOR, children=[quality_inspect, compliance_check])
compliance_check_to_packaging_final = OperatorPOWL(operator=Operator.XOR, children=[compliance_check, packaging_final])
packaging_final_to_delivery_setup = OperatorPOWL(operator=Operator.XOR, children=[packaging_final, delivery_setup])

# Define the partial order
root = StrictPartialOrder(nodes=[
    component_sourcing_to_frame_assembly,
    frame_assembly_to_motor_installation,
    motor_installation_to_sensor_mounting,
    sensor_mounting_to_wiring_setup,
    wiring_setup_to_firmware_upload,
    firmware_upload_to_ai_module,
    ai_module_to_calibration_phase,
    calibration_phase_to_stress_testing,
    stress_testing_to_flight_simulation,
    flight_simulation_to_pattern_adjustment,
    pattern_adjustment_to_quality_inspect,
    quality_inspect_to_compliance_check,
    compliance_check_to_packaging_final,
    packaging_final_to_delivery_setup
])

# Define the edges in the partial order
root.order.add_edge(component_sourcing_to_frame_assembly, frame_assembly_to_motor_installation)
root.order.add_edge(frame_assembly_to_motor_installation, motor_installation_to_sensor_mounting)
root.order.add_edge(motor_installation_to_sensor_mounting, sensor_mounting_to_wiring_setup)
root.order.add_edge(sensor_mounting_to_wiring_setup, wiring_setup_to_firmware_upload)
root.order.add_edge(wiring_setup_to_firmware_upload, firmware_upload_to_ai_module)
root.order.add_edge(firmware_upload_to_ai_module, ai_module_to_calibration_phase)
root.order.add_edge(ai_module_to_calibration_phase, calibration_phase_to_stress_testing)
root.order.add_edge(calibration_phase_to_stress_testing, stress_testing_to_flight_simulation)
root.order.add_edge(stress_testing_to_flight_simulation, flight_simulation_to_pattern_adjustment)
root.order.add_edge(flight_simulation_to_pattern_adjustment, pattern_adjustment_to_quality_inspect)
root.order.add_edge(pattern_adjustment_to_quality_inspect, quality_inspect_to_compliance_check)
root.order.add_edge(quality_inspect_to_compliance_check, compliance_check_to_packaging_final)
root.order.add_edge(compliance_check_to_packaging_final, packaging_final_to_delivery_setup)