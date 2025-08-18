import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define the transitions (activities)
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

# Create the partial order for the assembly process
assembly_part = StrictPartialOrder(nodes=[
    spec_review,
    component_pick,
    frame_build,
    motor_mount,
    sensor_fit,
    wiring_setup,
    software_load,
    calibration_test,
    stress_check,
    firmware_flash
])
assembly_part.order.add_edge(spec_review, component_pick)
assembly_part.order.add_edge(component_pick, frame_build)
assembly_part.order.add_edge(frame_build, motor_mount)
assembly_part.order.add_edge(motor_mount, sensor_fit)
assembly_part.order.add_edge(sensor_fit, wiring_setup)
assembly_part.order.add_edge(wiring_setup, software_load)
assembly_part.order.add_edge(software_load, calibration_test)
assembly_part.order.add_edge(calibration_test, stress_check)
assembly_part.order.add_edge(stress_check, firmware_flash)

# Create the partial order for the quality assurance and firmware update process
qa_part = StrictPartialOrder(nodes=[
    calibration_test,
    stress_check,
    firmware_flash
])
qa_part.order.add_edge(calibration_test, stress_check)
qa_part.order.add_edge(stress_check, firmware_flash)

# Create the partial order for the final packaging and shipping process
package_part = StrictPartialOrder(nodes=[
    package_prep,
    doc_compile,
    ship_arrange,
    remote_setup
])
package_part.order.add_edge(package_prep, doc_compile)
package_part.order.add_edge(doc_compile, ship_arrange)
package_part.order.add_edge(ship_arrange, remote_setup)

# Combine all parts into the root
root = StrictPartialOrder(nodes=[
    assembly_part,
    qa_part,
    package_part
])
root.order.add_edge(assembly_part, qa_part)
root.order.add_edge(assembly_part, package_part)

print(root)