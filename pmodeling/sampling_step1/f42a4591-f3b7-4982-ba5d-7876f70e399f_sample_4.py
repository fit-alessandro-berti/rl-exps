import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
inspect_item = Transition(label='Inspect Item')
verify_provenance = Transition(label='Verify Provenance')
document_condition = Transition(label='Document Condition')
disassemble_parts = Transition(label='Disassemble Parts')
clean_components = Transition(label='Clean Components')
analyze_damage = Transition(label='Analyze Damage')
select_materials = Transition(label='Select Materials')
perform_repairs = Transition(label='Perform Repairs')
match_finishes = Transition(label='Match Finishes')
apply_treatments = Transition(label='Apply Treatments')
reassemble_item = Transition(label='Reassemble Item')
quality_check = Transition(label='Quality Check')
photograph_results = Transition(label='Photograph Results')
update_archive = Transition(label='Update Archive')
client_review = Transition(label='Client Review')
finalize_report = Transition(label='Finalize Report')

# Define silent transitions
skip = SilentTransition()

# Define loops and choices
inspect_verify = OperatorPOWL(operator=Operator.XOR, children=[inspect_item, verify_provenance])
disassemble_clean = OperatorPOWL(operator=Operator.LOOP, children=[disassemble_parts, clean_components])
analyze_select = OperatorPOWL(operator=Operator.XOR, children=[analyze_damage, select_materials])
repair_finish = OperatorPOWL(operator=Operator.LOOP, children=[perform_repairs, match_finishes])
treat_quality = OperatorPOWL(operator=Operator.XOR, children=[apply_treatments, quality_check])
reassemble_update = OperatorPOWL(operator=Operator.XOR, children=[reassemble_item, update_archive])
photograph_review = OperatorPOWL(operator=Operator.XOR, children=[photograph_results, client_review])
finalize_report = OperatorPOWL(operator=Operator.XOR, children=[finalize_report, skip])

# Define the root partial order
root = StrictPartialOrder(nodes=[inspect_verify, disassemble_clean, analyze_select, repair_finish, treat_quality, reassemble_update, photograph_review, finalize_report])
root.order.add_edge(inspect_verify, disassemble_clean)
root.order.add_edge(disassemble_clean, analyze_select)
root.order.add_edge(analyze_select, repair_finish)
root.order.add_edge(repair_finish, treat_quality)
root.order.add_edge(treat_quality, reassemble_update)
root.order.add_edge(reassemble_update, photograph_review)
root.order.add_edge(photograph_review, finalize_report)