from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions
component_check = Transition(label='Component Check')
spec_review = Transition(label='Spec Review')
parts_sorting = Transition(label='Parts Sorting')
mechanical_fit = Transition(label='Mechanical Fit')
firmware_load = Transition(label='Firmware Load')
calibration_run = Transition(label='Calibration Run')
stress_test = Transition(label='Stress Test')
software_patch = Transition(label='Software Patch')
algorithm_tune = Transition(label='Algorithm Tune')
comms_setup = Transition(label='Comms Setup')
validation_pass = Transition(label='Validation Pass')
data_link = Transition(label='Data Link')
onsite_deploy = Transition(label='Onsite Deploy')
live_monitor = Transition(label='Live Monitor')
update_push = Transition(label='Update Push')
recovery_plan = Transition(label='Recovery Plan')
maintenance_log = Transition(label='Maintenance Log')

# Define nodes and their relationships
root = StrictPartialOrder(
    nodes=[
        component_check,
        spec_review,
        parts_sorting,
        mechanical_fit,
        firmware_load,
        calibration_run,
        stress_test,
        software_patch,
        algorithm_tune,
        comms_setup,
        validation_pass,
        data_link,
        onsite_deploy,
        live_monitor,
        update_push,
        recovery_plan,
        maintenance_log
    ],
    order=[
        (component_check, spec_review),
        (spec_review, parts_sorting),
        (parts_sorting, mechanical_fit),
        (mechanical_fit, firmware_load),
        (firmware_load, calibration_run),
        (calibration_run, stress_test),
        (stress_test, software_patch),
        (software_patch, algorithm_tune),
        (algorithm_tune, comms_setup),
        (comms_setup, validation_pass),
        (validation_pass, data_link),
        (data_link, onsite_deploy),
        (onsite_deploy, live_monitor),
        (live_monitor, update_push),
        (update_push, recovery_plan),
        (recovery_plan, maintenance_log)
    ]
)

print(root)