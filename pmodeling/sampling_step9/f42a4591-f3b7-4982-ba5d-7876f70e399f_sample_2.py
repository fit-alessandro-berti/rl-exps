import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
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

# Define the silent transitions
skip = SilentTransition()

# Define the partial order for each step
inspect_verify = OperatorPOWL(operator=Operator.XOR, children=[inspect_item, verify_provenance])
document_clean = OperatorPOWL(operator=Operator.XOR, children=[document_condition, clean_components])
analyze_select = OperatorPOWL(operator=Operator.XOR, children=[analyze_damage, select_materials])
repair_match = OperatorPOWL(operator=Operator.XOR, children=[perform_repairs, match_finishes])
treat_apply = OperatorPOWL(operator=Operator.XOR, children=[apply_treatments, reassemble_item])
check_final = OperatorPOWL(operator=Operator.XOR, children=[quality_check, photograph_results])
update_client = OperatorPOWL(operator=Operator.XOR, children=[update_archive, client_review])
finalize_report = OperatorPOWL(operator=Operator.XOR, children=[finalize_report])

# Define the loop for quality control
quality_loop = OperatorPOWL(operator=Operator.LOOP, children=[quality_check, photograph_results])

# Define the partial order for the entire process
root = StrictPartialOrder(nodes=[inspect_verify, document_clean, analyze_select, repair_match, treat_apply, quality_loop, update_client, finalize_report])
root.order.add_edge(inspect_verify, document_clean)
root.order.add_edge(document_clean, analyze_select)
root.order.add_edge(analyze_select, repair_match)
root.order.add_edge(repair_match, treat_apply)
root.order.add_edge(treat_apply, quality_loop)
root.order.add_edge(quality_loop, update_client)
root.order.add_edge(update_client, finalize_report)

# Print the root node
print(root)