import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
inspect = Transition(label='Inspect Item')
verify = Transition(label='Verify Provenance')
document = Transition(label='Document Condition')
disassemble = Transition(label='Disassemble Parts')
clean = Transition(label='Clean Components')
analyze = Transition(label='Analyze Damage')
select = Transition(label='Select Materials')
repair = Transition(label='Perform Repairs')
match_finishes = Transition(label='Match Finishes')
apply_treatments = Transition(label='Apply Treatments')
reassemble = Transition(label='Reassemble Item')
quality = Transition(label='Quality Check')
photograph = Transition(label='Photograph Results')
update_archive = Transition(label='Update Archive')
client_review = Transition(label='Client Review')
finalize = Transition(label='Finalize Report')

# Loop for iterative analysis and repair
loop_analysis_repair = OperatorPOWL(
    operator=Operator.LOOP,
    children=[analyze, repair]
)

# Build the partial order
root = StrictPartialOrder(nodes=[
    inspect,
    verify,
    document,
    disassemble,
    clean,
    loop_analysis_repair,
    select,
    match_finishes,
    apply_treatments,
    reassemble,
    quality,
    photograph,
    update_archive,
    client_review,
    finalize
])

# Define the control-flow order
root.order.add_edge(inspect, verify)
root.order.add_edge(verify, document)
root.order.add_edge(document, disassemble)
root.order.add_edge(disassemble, clean)
root.order.add_edge(clean, loop_analysis_repair)
root.order.add_edge(loop_analysis_repair, select)
root.order.add_edge(select, match_finishes)
root.order.add_edge(select, apply_treatments)
root.order.add_edge(match_finishes, reassemble)
root.order.add_edge(apply_treatments, reassemble)
root.order.add_edge(reassemble, quality)
root.order.add_edge(quality, photograph)
root.order.add_edge(photograph, update_archive)
root.order.add_edge(update_archive, client_review)
root.order.add_edge(client_review, finalize)