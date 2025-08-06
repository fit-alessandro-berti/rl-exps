from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define transitions
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

# Define POWL model
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