from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for the process
initial_assess = Transition(label='Initial Assess')
disassemble_parts = Transition(label='Disassemble Parts')
ultrasonic_clean = Transition(label='Ultrasonic Clean')
inspect_components = Transition(label='Inspect Components')
fabricate_gears = Transition(label='Fabricate Gears')
dial_restoration = Transition(label='Dial Restoration')
repaint_markers = Transition(label='Repaint Markers')
reassemble_movement = Transition(label='Reassemble Movement')
lubricate_bearings = Transition(label='Lubricate Bearings')
calibrate_timing = Transition(label='Calibrate Timing')
polish_case = Transition(label='Polish Case')
re_case_watch = Transition(label='Re-case Watch')
quality_testing = Transition(label='Quality Testing')
document_process = Transition(label='Document Process')
package_product = Transition(label='Package Product')

# Define the silent transitions
skip_initial_assess = SilentTransition()
skip_disassemble_parts = SilentTransition()
skip_ultrasonic_clean = SilentTransition()
skip_inspect_components = SilentTransition()
skip_fabricate_gears = SilentTransition()
skip_dial_restoration = SilentTransition()
skip_repaint_markers = SilentTransition()
skip_reassemble_movement = SilentTransition()
skip_lubricate_bearings = SilentTransition()
skip_calibrate_timing = SilentTransition()
skip_polish_case = SilentTransition()
skip_re_case_watch = SilentTransition()
skip_quality_testing = SilentTransition()
skip_document_process = SilentTransition()
skip_package_product = SilentTransition()

# Define the POWL model
root = StrictPartialOrder(
    nodes=[
        initial_assess,
        disassemble_parts,
        ultrasonic_clean,
        inspect_components,
        fabricate_gears,
        dial_restoration,
        repaint_markers,
        reassemble_movement,
        lubricate_bearings,
        calibrate_timing,
        polish_case,
        re_case_watch,
        quality_testing,
        document_process,
        package_product
    ],
    order=[
        (initial_assess, disassemble_parts),
        (disassemble_parts, ultrasonic_clean),
        (ultrasonic_clean, inspect_components),
        (inspect_components, fabricate_gears),
        (fabricate_gears, dial_restoration),
        (dial_restoration, repaint_markers),
        (repaint_markers, reassemble_movement),
        (reassemble_movement, lubricate_bearings),
        (lubricate_bearings, calibrate_timing),
        (calibrate_timing, polish_case),
        (polish_case, re_case_watch),
        (re_case_watch, quality_testing),
        (quality_testing, document_process),
        (document_process, package_product)
    ]
)

# Add the silent transitions to the model
root.order.add_edge(skip_initial_assess, initial_assess)
root.order.add_edge(skip_disassemble_parts, disassemble_parts)
root.order.add_edge(skip_ultrasonic_clean, ultrasonic_clean)
root.order.add_edge(skip_inspect_components, inspect_components)
root.order.add_edge(skip_fabricate_gears, fabricate_gears)
root.order.add_edge(skip_dial_restoration, dial_restoration)
root.order.add_edge(skip_repaint_markers, repaint_markers)
root.order.add_edge(skip_reassemble_movement, reassemble_movement)
root.order.add_edge(skip_lubricate_bearings, lubricate_bearings)
root.order.add_edge(skip_calibrate_timing, calibrate_timing)
root.order.add_edge(skip_polish_case, polish_case)
root.order.add_edge(skip_re_case_watch, re_case_watch)
root.order.add_edge(skip_quality_testing, quality_testing)
root.order.add_edge(skip_document_process, document_process)
root.order.add_edge(skip_package_product, package_product)

# Print the final POWL model
print(root)