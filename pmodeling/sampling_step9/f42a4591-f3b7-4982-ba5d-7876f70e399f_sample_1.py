import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

inspect = Transition(label='Inspect Item')
verify = Transition(label='Verify Provenance')
document = Transition(label='Document Condition')
disassemble = Transition(label='Disassemble Parts')
clean = Transition(label='Clean Components')
analyze = Transition(label='Analyze Damage')
select_materials = Transition(label='Select Materials')
perform_repairs = Transition(label='Perform Repairs')
match_finishes = Transition(label='Match Finishes')
apply_treatments = Transition(label='Apply Treatments')
reassemble = Transition(label='Reassemble Item')
quality_check = Transition(label='Quality Check')
photograph = Transition(label='Photograph Results')
update_archive = Transition(label='Update Archive')
client_review = Transition(label='Client Review')
finalize = Transition(label='Finalize Report')

skip = SilentTransition()

inspect_verify = OperatorPOWL(operator=Operator.XOR, children=[inspect, verify])
inspect_document = OperatorPOWL(operator=Operator.XOR, children=[inspect, document])
inspect_disassemble = OperatorPOWL(operator=Operator.XOR, children=[inspect, disassemble])
inspect_clean = OperatorPOWL(operator=Operator.XOR, children=[inspect, clean])
inspect_analyze = OperatorPOWL(operator=Operator.XOR, children=[inspect, analyze])
inspect_select = OperatorPOWL(operator=Operator.XOR, children=[inspect, select_materials])
inspect_perform = OperatorPOWL(operator=Operator.XOR, children=[inspect, perform_repairs])
inspect_match = OperatorPOWL(operator=Operator.XOR, children=[inspect, match_finishes])
inspect_apply = OperatorPOWL(operator=Operator.XOR, children=[inspect, apply_treatments])
inspect_reassemble = OperatorPOWL(operator=Operator.XOR, children=[inspect, reassemble])
inspect_quality = OperatorPOWL(operator=Operator.XOR, children=[inspect, quality_check])
inspect_photograph = OperatorPOWL(operator=Operator.XOR, children=[inspect, photograph])
inspect_update = OperatorPOWL(operator=Operator.XOR, children=[inspect, update_archive])
inspect_client = OperatorPOWL(operator=Operator.XOR, children=[inspect, client_review])
inspect_finalize = OperatorPOWL(operator=Operator.XOR, children=[inspect, finalize])

verify_document = OperatorPOWL(operator=Operator.XOR, children=[verify, document])
verify_disassemble = OperatorPOWL(operator=Operator.XOR, children=[verify, disassemble])
verify_clean = OperatorPOWL(operator=Operator.XOR, children=[verify, clean])
verify_analyze = OperatorPOWL(operator=Operator.XOR, children=[verify, analyze])
verify_select = OperatorPOWL(operator=Operator.XOR, children=[verify, select_materials])
verify_perform = OperatorPOWL(operator=Operator.XOR, children=[verify, perform_repairs])
verify_match = OperatorPOWL(operator=Operator.XOR, children=[verify, match_finishes])
verify_apply = OperatorPOWL(operator=Operator.XOR, children=[verify, apply_treatments])
verify_reassemble = OperatorPOWL(operator=Operator.XOR, children=[verify, reassemble])
verify_quality = OperatorPOWL(operator=Operator.XOR, children=[verify, quality_check])
verify_photograph = OperatorPOWL(operator=Operator.XOR, children=[verify, photograph])
verify_update = OperatorPOWL(operator=Operator.XOR, children=[verify, update_archive])
verify_client = OperatorPOWL(operator=Operator.XOR, children=[verify, client_review])
verify_finalize = OperatorPOWL(operator=Operator.XOR, children=[verify, finalize])

document_disassemble = OperatorPOWL(operator=Operator.XOR, children=[document, disassemble])
document_clean = OperatorPOWL(operator=Operator.XOR, children=[document, clean])
document_analyze = OperatorPOWL(operator=Operator.XOR, children=[document, analyze])
document_select = OperatorPOWL(operator=Operator.XOR, children=[document, select_materials])
document_perform = OperatorPOWL(operator=Operator.XOR, children=[document, perform_repairs])
document_match = OperatorPOWL(operator=Operator.XOR, children=[document, match_finishes])
document_apply = OperatorPOWL(operator=Operator.XOR, children=[document, apply_treatments])
document_reassemble = OperatorPOWL(operator=Operator.XOR, children=[document, reassemble])
document_quality = OperatorPOWL(operator=Operator.XOR, children=[document, quality_check])
document_photograph = OperatorPOWL(operator=Operator.XOR, children=[document, photograph])
document_update = OperatorPOWL(operator=Operator.XOR, children=[document, update_archive])
document_client = OperatorPOWL(operator=Operator.XOR, children=[document, client_review])
document_finalize = OperatorPOWL(operator=Operator.XOR, children=[document, finalize])

disassemble_clean = OperatorPOWL(operator=Operator.XOR, children=[disassemble, clean])
disassemble_analyze = OperatorPOWL(operator=Operator.XOR, children=[disassemble, analyze])
disassemble_select = OperatorPOWL(operator=Operator.XOR, children=[disassemble, select_materials])
disassemble_perform = OperatorPOWL(operator=Operator.XOR, children=[disassemble, perform_repairs])
disassemble_match = OperatorPOWL(operator=Operator.XOR, children=[disassemble, match_finishes])
disassemble_apply = OperatorPOWL(operator=Operator.XOR, children=[disassemble, apply_treatments])
disassemble_reassemble = OperatorPOWL(operator=Operator.XOR, children=[disassemble, reassemble])
disassemble_quality = OperatorPOWL(operator=Operator.XOR, children=[disassemble, quality_check])
disassemble_photograph = OperatorPOWL(operator=Operator.XOR, children=[disassemble, photograph])
disassemble_update = OperatorPOWL(operator=Operator.XOR, children=[disassemble, update_archive])
disassemble_client = OperatorPOWL(operator=Operator.XOR, children=[disassemble, client_review])
disassemble_finalize = OperatorPOWL(operator=Operator.XOR, children=[disassemble, finalize])

clean_analyze = OperatorPOWL(operator=Operator.XOR, children=[clean, analyze])
clean_select = OperatorPOWL(operator=Operator.XOR, children=[clean, select_materials])
clean_perform = OperatorPOWL(operator=Operator.XOR, children=[clean, perform_repairs])
clean_match = OperatorPOWL(operator=Operator.XOR, children=[clean, match_finishes])
clean_apply = OperatorPOWL(operator=Operator.XOR, children=[clean, apply_treatments])
clean_reassemble = OperatorPOWL(operator=Operator.XOR, children=[clean, reassemble])
clean_quality = OperatorPOWL(operator=Operator.XOR, children=[clean, quality_check])
clean_photograph = OperatorPOWL(operator=Operator.XOR, children=[clean, photograph])
clean_update = OperatorPOWL(operator=Operator.XOR, children=[clean, update_archive])
clean_client = OperatorPOWL(operator=Operator.XOR, children=[clean, client_review])
clean_finalize = OperatorPOWL(operator=Operator.XOR, children=[clean, finalize])

analyze_select = OperatorPOWL(operator=Operator.XOR, children=[analyze, select_materials])
analyze_perform = OperatorPOWL(operator=Operator.XOR, children=[analyze, perform_repairs])
analyze_match = OperatorPOWL(operator=Operator.XOR, children=[analyze, match_finishes])
analyze_apply = OperatorPOWL(operator=Operator.XOR, children=[analyze, apply_treatments])
analyze_reassemble = OperatorPOWL(operator=Operator.XOR, children=[analyze, reassemble])
analyze_quality = OperatorPOWL(operator=Operator.XOR, children=[analyze, quality_check])
analyze_photograph = OperatorPOWL(operator=Operator.XOR, children=[analyze, photograph])
analyze_update = OperatorPOWL(operator=Operator.XOR, children=[analyze, update_archive])
analyze_client = OperatorPOWL(operator=Operator.XOR, children=[analyze, client_review])
analyze_finalize = OperatorPOWL(operator=Operator.XOR, children=[analyze, finalize])

select_perform = OperatorPOWL(operator=Operator.XOR, children=[select_materials, perform_repairs])
select_match = OperatorPOWL(operator=Operator.XOR, children=[select_materials, match_finishes])
select_apply = OperatorPOWL(operator=Operator.XOR, children=[select_materials, apply_treatments])
select_reassemble = OperatorPOWL(operator=Operator.XOR, children=[select_materials, reassemble])
select_quality = OperatorPOWL(operator=Operator.XOR, children=[select_materials, quality_check])
select_photograph = OperatorPOWL(operator=Operator.XOR, children=[select_materials, photograph])
select_update = OperatorPOWL(operator=Operator.XOR, children=[select_materials, update_archive])
select_client = OperatorPOWL(operator=Operator.XOR, children=[select_materials, client_review])
select_finalize = OperatorPOWL(operator=Operator.XOR, children=[select_materials, finalize])

perform_match = OperatorPOWL(operator=Operator.XOR, children=[perform_repairs, match_finishes])
perform_apply = OperatorPOWL(operator=Operator.XOR, children=[perform_repairs, apply_treatments])
perform_reassemble = OperatorPOWL(operator=Operator.XOR, children=[perform_repairs, reassemble])
perform_quality = OperatorPOWL(operator=Operator.XOR, children=[perform_repairs, quality_check])
perform_photograph = OperatorPOWL(operator=Operator.XOR, children=[perform_repairs, photograph])
perform_update = OperatorPOWL(operator=Operator.XOR, children=[perform_repairs, update_archive])
perform_client = OperatorPOWL(operator=Operator.XOR, children=[perform_repairs, client_review])
perform_finalize = OperatorPOWL(operator=Operator.XOR, children=[perform_repairs, finalize])

match_apply = OperatorPOWL(operator=Operator.XOR, children=[match_finishes, apply_treatments])
match_reassemble = OperatorPOWL(operator=Operator.XOR, children=[match_finishes, reassemble])
match_quality = OperatorPOWL(operator=Operator.XOR, children=[match_finishes, quality_check])
match_photograph = OperatorPOWL(operator=Operator.XOR, children=[match_finishes, photograph])
match_update = OperatorPOWL(operator=Operator.XOR, children=[match_finishes, update_archive])
match_client = OperatorPOWL(operator=Operator.XOR, children=[match_finishes, client_review])
match_finalize = OperatorPOWL(operator=Operator.XOR, children=[match_finishes, finalize])

apply_reassemble = OperatorPOWL(operator=Operator.XOR, children=[apply_treatments, reassemble])
apply_quality = OperatorPOWL(operator=Operator.XOR, children=[apply_treatments, quality_check])
apply_photograph = OperatorPOWL(operator=Operator.XOR, children=[apply_treatments, photograph])
apply_update = OperatorPOWL(operator=Operator.XOR, children=[apply_treatments, update_archive])
apply_client = OperatorPOWL(operator=Operator.XOR, children=[apply_treatments, client_review])
apply_finalize = OperatorPOWL(operator=Operator.XOR, children=[apply_treatments, finalize])

reassemble_quality = OperatorPOWL(operator=Operator.XOR, children=[reassemble, quality_check])
reassemble_photograph = OperatorPOWL(operator=Operator.XOR, children=[reassemble, photograph])
reassemble_update = OperatorPOWL(operator=Operator.XOR, children=[reassemble, update_archive])
reassemble_client = OperatorPOWL(operator=Operator.XOR, children=[reassemble, client_review])
reassemble_finalize = OperatorPOWL(operator=Operator.XOR, children=[reassemble, finalize])

quality_photograph = OperatorPOWL(operator=Operator.XOR, children=[quality_check, photograph])
quality_update = OperatorPOWL(operator=Operator.XOR, children=[quality_check, update_archive])
quality_client = OperatorPOWL(operator=Operator.XOR, children=[quality_check, client_review])
quality_finalize = OperatorPOWL(operator=Operator.XOR, children=[quality_check, finalize])

photograph_update = OperatorPOWL(operator=Operator.XOR, children=[photograph, update_archive])
photograph_client = OperatorPOWL(operator=Operator.XOR, children=[photograph, client_review])
photograph_finalize = OperatorPOWL(operator=Operator.XOR, children=[photograph, finalize])

update_client = OperatorPOWL(operator=Operator.XOR, children=[update_archive, client_review])
update_finalize = OperatorPOWL(operator=Operator.XOR, children=[update_archive, finalize])

client_finalize = OperatorPOWL(operator=Operator.XOR, children=[client_review, finalize])

root = StrictPartialOrder(nodes=[
    inspect_verify,
    inspect_document,
    inspect_disassemble,
    inspect_clean,
    inspect_analyze,
    inspect_select,
    inspect_perform,
    inspect_match,
    inspect_apply,
    inspect_reassemble,
    inspect_quality,
    inspect_photograph,
    inspect_update,
    inspect_client,
    inspect_finalize,
    
    verify_document,
    verify_disassemble,
    verify_clean,
    verify_analyze,
    verify_select,
    verify_perform,
    verify_match,
    verify_apply,
    verify_reassemble,
    verify_quality,
    verify_photograph,
    verify_update,
    verify_client,
    verify_finalize,
    
    document_disassemble,
    document_clean,
    document_analyze,
    document_select,
    document_perform,
    document_match,
    document_apply,
    document_reassemble,
    document_quality,
    document_photograph,
    document_update,
    document_client,
    document_finalize,
    
    disassemble_clean,
    disassemble_analyze,
    disassemble_select,
    disassemble_perform,
    disassemble_match,
    disassemble_apply,
    disassemble_reassemble,
    disassemble_quality,
    disassemble_photograph,
    disassemble_update,
    disassemble_client,
    disassemble_finalize,
    
    clean_analyze,
    clean_select,
    clean_perform,
    clean_match,
    clean_apply,
    clean_reassemble,
    clean_quality,
    clean_photograph,
    clean_update,
    clean_client,
    clean_finalize,
    
    analyze_select,
    analyze_perform,
    analyze_match,
    analyze_apply,
    analyze_reassemble,
    analyze_quality,
    analyze_photograph,
    analyze_update,
    analyze_client,
    analyze_finalize,
    
    select_perform,
    select_match,
    select_apply,
    select_reassemble,
    select_quality,
    select_photograph,
    select_update,
    select_client,
    select_finalize,
    
    perform_match,
    perform_apply,
    perform_reassemble,
    perform_quality,
    perform_photograph,
    perform_update,
    perform_client,
    perform_finalize,
    
    match_apply,
    match_reassemble,
    match_quality,
    match_photograph,
    match_update,
    match_client,
    match_finalize,
    
    apply_reassemble,
    apply_quality,
    apply_photograph,
    apply_update,
    apply_client,
    apply_finalize,
    
    reassemble_quality,
    reassemble_photograph,
    reassemble_update,
    reassemble_client,
    reassemble_finalize,
    
    quality_photograph,
    quality_update,
    quality_client,
    quality_finalize,
    
    photograph_update,
    photograph_client,
    photograph_finalize,
    
    update_client,
    update_finalize,
    
    client_finalize
])

root.order.add_edge(inspect, inspect_verify)
root.order.add_edge(inspect, inspect_document)
root.order.add_edge(inspect, inspect_disassemble)
root.order.add_edge(inspect, inspect_clean)
root.order.add_edge(inspect, inspect_analyze)
root.order.add_edge(inspect, inspect_select)
root.order.add_edge(inspect, inspect_perform)
root.order.add_edge(inspect, inspect_match)
root.order.add_edge(inspect, inspect_apply)
root.order.add_edge(inspect, inspect_reassemble)
root.order.add_edge(inspect, inspect_quality)
root.order.add_edge(inspect, inspect_photograph)
root.order.add_edge(inspect, inspect_update)
root.order.add_edge(inspect, inspect_client)
root.order.add_edge(inspect, inspect_finalize)