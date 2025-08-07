import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
inspect = Transition(label='Inspect Item')
verify = Transition(label='Verify Provenance')
document = Transition(label='Document Condition')
disassemble = Transition(label='Disassemble Parts')
clean = Transition(label='Clean Components')
analyze = Transition(label='Analyze Damage')
select = Transition(label='Select Materials')
repair = Transition(label='Perform Repairs')
finish = Transition(label='Match Finishes')
treatment = Transition(label='Apply Treatments')
reassemble = Transition(label='Reassemble Item')
quality = Transition(label='Quality Check')
photograph = Transition(label='Photograph Results')
update_archive = Transition(label='Update Archive')
client_review = Transition(label='Client Review')
finalize = Transition(label='Finalize Report')

# Loop for continuous analysis and repair until satisfied
loop = OperatorPOWL(
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
    loop,
    select,
    finish,
    treatment,
    reassemble,
    quality,
    photograph,
    update_archive,
    client_review,
    finalize
])

# Define the control-flow dependencies
root.order.add_edge(inspect, verify)
root.order.add_edge(verify, document)
root.order.add_edge(document, disassemble)
root.order.add_edge(disassemble, clean)
root.order.add_edge(clean, loop)
root.order.add_edge(loop, select)
root.order.add_edge(select, finish)
root.order.add_edge(finish, treatment)
root.order.add_edge(treatment, reassemble)
root.order.add_edge(reassemble, quality)
root.order.add_edge(quality, photograph)
root.order.add_edge(photograph, update_archive)
root.order.add_edge(update_archive, client_review)
root.order.add_edge(client_review, finalize)