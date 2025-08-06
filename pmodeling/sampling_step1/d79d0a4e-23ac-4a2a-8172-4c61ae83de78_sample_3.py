from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define the activities
spec_review = Transition(label='Spec Review')
component_pick = Transition(label='Component Pick')
frame_build = Transition(label='Frame Build')
motor_mount = Transition(label='Motor Mount')
sensor_fit = Transition(label='Sensor Fit')
wiring_setup = Transition(label='Wiring Setup')
software_load = Transition(label='Software Load')
calibration_test = Transition(label='Calibration Test')
stress_check = Transition(label='Stress Check')
firmware_flash = Transition(label='Firmware Flash')
feedback_loop = Transition(label='Feedback Loop')
package_prep = Transition(label='Package Prep')
doc_compile = Transition(label='Doc Compile')
ship_arrange = Transition(label='Ship Arrange')
remote_setup = Transition(label='Remote Setup')

# Define the workflow
root = StrictPartialOrder(nodes=[
    spec_review,
    component_pick,
    frame_build,
    motor_mount,
    sensor_fit,
    wiring_setup,
    software_load,
    calibration_test,
    stress_check,
    firmware_flash,
    feedback_loop,
    package_prep,
    doc_compile,
    ship_arrange,
    remote_setup
])

# Add dependencies between activities
root.order.add_edge(spec_review, component_pick)
root.order.add_edge(component_pick, frame_build)
root.order.add_edge(frame_build, motor_mount)
root.order.add_edge(motor_mount, sensor_fit)
root.order.add_edge(sensor_fit, wiring_setup)
root.order.add_edge(wiring_setup, software_load)
root.order.add_edge(software_load, calibration_test)
root.order.add_edge(calibration_test, stress_check)
root.order.add_edge(stress_check, firmware_flash)
root.order.add_edge(firmware_flash, feedback_loop)
root.order.add_edge(feedback_loop, package_prep)
root.order.add_edge(package_prep, doc_compile)
root.order.add_edge(doc_compile, ship_arrange)
root.order.add_edge(ship_arrange, remote_setup)

# Print the workflow
print(root)