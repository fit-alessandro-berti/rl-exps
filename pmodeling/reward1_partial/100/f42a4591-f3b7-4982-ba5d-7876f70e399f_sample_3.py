from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define the transitions
inspect = Transition(label='Inspect Item')
verify = Transition(label='Verify Provenance')
document = Transition(label='Document Condition')
disassemble = Transition(label='Disassemble Parts')
clean = Transition(label='Clean Components')
analyze = Transition(label='Analyze Damage')
select_materials = Transition(label='Select Materials')
perform_repair = Transition(label='Perform Repairs')
match_finishes = Transition(label='Match Finishes')
apply_treatments = Transition(label='Apply Treatments')
reassemble = Transition(label='Reassemble Item')
quality_check = Transition(label='Quality Check')
photograph = Transition(label='Photograph Results')
update_archive = Transition(label='Update Archive')
client_review = Transition(label='Client Review')
finalize_report = Transition(label='Finalize Report')

# Define the loop and XOR transitions
loop = OperatorPOWL(operator=Operator.LOOP, children=[inspect, verify, document, disassemble, clean, analyze, select_materials, perform_repair, match_finishes, apply_treatments, reassemble, quality_check, photograph, update_archive, client_review, finalize_report])

xor = OperatorPOWL(operator=Operator.XOR, children=[finalize_report])

# Create the root node
root = StrictPartialOrder(nodes=[loop, xor])

# Add edges to the root node
root.order.add_edge(loop, xor)

print(root)