from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define transitions
source_component_sourcing = Transition(label='Component Sourcing')
source_frame_assembly = Transition(label='Frame Assembly')
source_sensor_mounting = Transition(label='Sensor Mounting')
source_wiring_harness = Transition(label='Wiring Harness')
source_circuit_testing = Transition(label='Circuit Testing')
source_firmware_loading = Transition(label='Firmware Loading')
source_initial_calibration = Transition(label='Initial Calibration')
source_software_integration = Transition(label='Software Integration')
source_flight_testing = Transition(label='Flight Testing')
source_data_logging = Transition(label='Data Logging')
source_performance_tuning = Transition(label='Performance Tuning')
source_packaging_prep = Transition(label='Packaging Prep')
source_custom_labeling = Transition(label='Custom Labeling')
source_documentation_print = Transition(label='Documentation Print')
source_quality_review = Transition(label='Quality Review')
source_client_training = Transition(label='Client Training')
source_remote_monitoring = Transition(label='Remote Monitoring')
source_firmware_update = Transition(label='Firmware Update')

# Define silent transitions
silent_transition = SilentTransition()

# Define operators
exclusive_choice = OperatorPOWL(operator=Operator.XOR, children=[source_initial_calibration, source_firmware_update])
loop = OperatorPOWL(operator=Operator.LOOP, children=[source_component_sourcing, source_frame_assembly, source_sensor_mounting, source_wiring_harness, source_circuit_testing, source_firmware_loading, source_software_integration, source_flight_testing, source_data_logging, source_performance_tuning, source_packaging_prep, source_custom_labeling, source_documentation_print, source_quality_review, source_client_training, source_remote_monitoring, source_firmware_update])
xor = OperatorPOWL(operator=Operator.XOR, children=[silent_transition, exclusive_choice])

# Define root
root = StrictPartialOrder(nodes=[loop, xor])
root.order.add_edge(loop, xor)

# Return the root
return root