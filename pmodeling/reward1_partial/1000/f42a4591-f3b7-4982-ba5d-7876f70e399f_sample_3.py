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

# Define the partial order
root = StrictPartialOrder(
    nodes=[
        inspect_item, verify_provenance, document_condition, disassemble_parts, clean_components, analyze_damage,
        select_materials, perform_repairs, match_finishes, apply_treatments, reassemble_item, quality_check,
        photograph_results, update_archive, client_review, finalize_report
    ],
    order=[
        (inspect_item, verify_provenance), (verify_provenance, document_condition),
        (document_condition, disassemble_parts), (disassemble_parts, clean_components),
        (clean_components, analyze_damage), (analyze_damage, select_materials),
        (select_materials, perform_repairs), (perform_repairs, match_finishes),
        (match_finishes, apply_treatments), (apply_treatments, reassemble_item),
        (reassemble_item, quality_check), (quality_check, photograph_results),
        (photograph_results, update_archive), (update_archive, client_review),
        (client_review, finalize_report)
    ]
)

print(root)