import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions
schedule_audit = Transition(label='Schedule compliance audit')
prepare_docs = Transition(label='Prepare documentation')
gather_evidence = Transition(label='Gather evidence')
self_assessment = Transition(label='Conduct self-assessment')
external_audit = Transition(label='Conduct external audit')
identify_issues = Transition(label='Identify gaps or issues')
correct_improve = Transition(label='Make necessary corrections or improvements')
final_audit = Transition(label='Conduct final audit')
award_cert = Transition(label='Award certification')
issue_docs = Transition(label='Issue official documents')

# Define the partial order
root = StrictPartialOrder(nodes=[schedule_audit, prepare_docs, gather_evidence, self_assessment, external_audit, identify_issues, correct_improve, final_audit, award_cert, issue_docs])

# Define the order of the nodes
root.order.add_edge(schedule_audit, prepare_docs)
root.order.add_edge(prepare_docs, gather_evidence)
root.order.add_edge(gather_evidence, self_assessment)
root.order.add_edge(self_assessment, external_audit)
root.order.add_edge(external_audit, identify_issues)
root.order.add_edge(identify_issues, correct_improve)
root.order.add_edge(correct_improve, final_audit)
root.order.add_edge(final_audit, award_cert)
root.order.add_edge(award_cert, issue_docs)

# Return the root
root