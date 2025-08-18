import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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

skip = SilentTransition()

loop_initial_assess = OperatorPOWL(operator=Operator.LOOP, children=[initial_assess, disassemble_parts, ultrasonic_clean])
loop_inspect_components = OperatorPOWL(operator=Operator.LOOP, children=[inspect_components, fabricate_gears])
loop_dial_restoration = OperatorPOWL(operator=Operator.LOOP, children=[dial_restoration, repaint_markers])
loop_reassemble_movement = OperatorPOWL(operator=Operator.LOOP, children=[reassemble_movement, lubricate_bearings, calibrate_timing])
loop_polish_case = OperatorPOWL(operator=Operator.LOOP, children=[polish_case, re_case_watch])
loop_quality_testing = OperatorPOWL(operator=Operator.LOOP, children=[quality_testing, document_process])
loop_package_product = OperatorPOWL(operator=Operator.LOOP, children=[package_product])

root = StrictPartialOrder(nodes=[
    loop_initial_assess,
    loop_inspect_components,
    loop_dial_restoration,
    loop_reassemble_movement,
    loop_polish_case,
    loop_quality_testing,
    loop_package_product
])

root.order.add_edge(loop_initial_assess, loop_inspect_components)
root.order.add_edge(loop_inspect_components, loop_dial_restoration)
root.order.add_edge(loop_dial_restoration, loop_reassemble_movement)
root.order.add_edge(loop_reassemble_movement, loop_polish_case)
root.order.add_edge(loop_polish_case, loop_quality_testing)
root.order.add_edge(loop_quality_testing, loop_package_product)