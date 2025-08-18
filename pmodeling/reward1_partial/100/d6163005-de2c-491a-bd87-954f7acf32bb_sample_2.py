import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions
req_analysis = Transition(label='Requirement Analysis')
comp_sourcing = Transition(label='Component Sourcing')
quality_check = Transition(label='Quality Check')
frame_assembly = Transition(label='Frame Assembly')
motor_install = Transition(label='Motor Installation')
sensor_setup = Transition(label='Sensor Setup')
control_unit = Transition(label='Control Unit')
firmware_upload = Transition(label='Firmware Upload')
system_calibration = Transition(label='System Calibration')
flight_testing = Transition(label='Flight Testing')
error_correction = Transition(label='Error Correction')
cosmetic_finish = Transition(label='Cosmetic Finish')
packaging_prep = Transition(label='Packaging Prep')
user_manual = Transition(label='User Manual')
client_training = Transition(label='Client Training')
support_scheduling = Transition(label='Support Scheduling')

# Define the partial order structure
root = StrictPartialOrder(
    nodes=[req_analysis, comp_sourcing, quality_check, frame_assembly, motor_install, sensor_setup,
           control_unit, firmware_upload, system_calibration, flight_testing, error_correction,
           cosmetic_finish, packaging_prep, user_manual, client_training, support_scheduling],
    order={
        (req_analysis, comp_sourcing),
        (comp_sourcing, quality_check),
        (quality_check, frame_assembly),
        (frame_assembly, motor_install),
        (motor_install, sensor_setup),
        (sensor_setup, control_unit),
        (control_unit, firmware_upload),
        (firmware_upload, system_calibration),
        (system_calibration, flight_testing),
        (flight_testing, error_correction),
        (error_correction, cosmetic_finish),
        (cosmetic_finish, packaging_prep),
        (packaging_prep, user_manual),
        (user_manual, client_training),
        (client_training, support_scheduling)
    }
)

print(root)