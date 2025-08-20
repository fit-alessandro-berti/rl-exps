import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
schedule_audit = Transition(label='Schedule compliance audit')
prepare_doc = Transition(label='Prepare documentation')
gather_evidence = Transition(label='Gather evidence')
self_assessment = Transition(label='Conduct self-assessment')
external_audit = Transition(label='Conduct external audit')
identify_gaps = Transition(label='Identify gaps or issues')
make_corrections = Transition(label='Make necessary corrections or improvements')
final_audit = Transition(label='Conduct final audit')
award_cert = Transition(label='Award certification')
issue_docs = Transition(label='Issue official documents')

# Create a sequence for the main flow
main_sequence = [schedule_audit, prepare_doc, gather_evidence, self_assessment, external_audit, identify_gaps, make_corrections, final_audit, award_cert, issue_docs]

# Create the root node as a strict partial order
root = StrictPartialOrder(nodes=main_sequence)

# Add edges to represent the sequence
for i in range(len(main_sequence) - 1):
    root.order.add_edge(main_sequence[i], main_sequence[i+1])

# Return the root node
root