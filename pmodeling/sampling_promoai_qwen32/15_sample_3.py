import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
schedule_audit = Transition(label='Schedule compliance audit')
prepare_docs = Transition(label='Prepare documentation')
gather_evidence = Transition(label='Gather evidence')
self_assessment = Transition(label='Conduct self-assessment')
external_audit = Transition(label='Conduct external audit')
identify_gaps = Transition(label='Identify gaps or issues')
corrections = Transition(label='Make necessary corrections or improvements')
final_audit = Transition(label='Conduct final audit')
certification = Transition(label='Award certification')
issue_docs = Transition(label='Issue official documents')

# Define the process tree
root = StrictPartialOrder(nodes=[schedule_audit, prepare_docs, gather_evidence, self_assessment, external_audit, identify_gaps, corrections, final_audit, certification, issue_docs])

# Define the order
root.order.add_edge(schedule_audit, prepare_docs)
root.order.add_edge(prepare_docs, gather_evidence)
root.order.add_edge(gather_evidence, self_assessment)
root.order.add_edge(self_assessment, external_audit)
root.order.add_edge(external_audit, identify_gaps)
root.order.add_edge(identify_gaps, corrections)
root.order.add_edge(corrections, final_audit)
root.order.add_edge(final_audit, certification)
root.order.add_edge(certification, issue_docs)