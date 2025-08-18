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

# Create the POWL model
root = StrictPartialOrder(nodes=[
    inspect_item,
    verify_provenance,
    document_condition,
    disassemble_parts,
    clean_components,
    analyze_damage,
    select_materials,
    perform_repairs,
    match_finishes,
    apply_treatments,
    reassemble_item,
    quality_check,
    photograph_results,
    update_archive,
    client_review,
    finalize_report
])

# Define the partial order
root.order.add_edge(inspect_item, verify_provenance)
root.order.add_edge(verify_provenance, document_condition)
root.order.add_edge(document_condition, disassemble_parts)
root.order.add_edge(disassemble_parts, clean_components)
root.order.add_edge(clean_components, analyze_damage)
root.order.add_edge(analyze_damage, select_materials)
root.order.add_edge(select_materials, perform_repairs)
root.order.add_edge(perform_repairs, match_finishes)
root.order.add_edge(match_finishes, apply_treatments)
root.order.add_edge(apply_treatments, reassemble_item)
root.order.add_edge(reassemble_item, quality_check)
root.order.add_edge(quality_check, photograph_results)
root.order.add_edge(photograph_results, update_archive)
root.order.add_edge(update_archive, client_review)
root.order.add_edge(client_review, finalize_report)

print(root)