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

# Define the process
inspect_verify = OperatorPOWL(operator=Operator.XOR, children=[inspect_item, verify_provenance])
document_condition_clean = OperatorPOWL(operator=Operator.XOR, children=[document_condition, clean_components])
analyze_damage_select = OperatorPOWL(operator=Operator.XOR, children=[analyze_damage, select_materials])
perform_repairs_match = OperatorPOWL(operator=Operator.XOR, children=[perform_repairs, match_finishes])
apply_treatments_quality = OperatorPOWL(operator=Operator.XOR, children=[apply_treatments, quality_check])
reassemble_item_photograph = OperatorPOWL(operator=Operator.XOR, children=[reassemble_item, photograph_results])
update_archive_client = OperatorPOWL(operator=Operator.XOR, children=[update_archive, client_review])
finalize_report = Transition(label='Finalize Report')

# Define the partial order
root = StrictPartialOrder(nodes=[inspect_verify, document_condition_clean, analyze_damage_select, perform_repairs_match, apply_treatments_quality, reassemble_item_photograph, update_archive_client, finalize_report])
root.order.add_edge(inspect_verify, document_condition_clean)
root.order.add_edge(document_condition_clean, analyze_damage_select)
root.order.add_edge(analyze_damage_select, perform_repairs_match)
root.order.add_edge(perform_repairs_match, apply_treatments_quality)
root.order.add_edge(apply_treatments_quality, reassemble_item_photograph)
root.order.add_edge(reassemble_item_photograph, update_archive_client)
root.order.add_edge(update_archive_client, finalize_report)

print(root)