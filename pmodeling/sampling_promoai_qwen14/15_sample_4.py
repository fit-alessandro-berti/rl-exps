import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
schedule_audit = Transition(label='Schedule compliance audit')
prepare_docs = Transition(label='Prepare documentation')
gather_evidence = Transition(label='Gather evidence')
self_assessment = Transition(label='Conduct self-assessment')
external_audit = Transition(label='Conduct external audit')
identify_gaps = Transition(label='Identify gaps or issues')
make_corrections = Transition(label='Make necessary corrections or improvements')
final_audit = Transition(label='Conduct final audit')
award_certification = Transition(label='Award certification')
issue_docs = Transition(label='Issue official documents')

# Define loops and choices
loop_audit = OperatorPOWL(operator=Operator.LOOP, children=[identify_gaps, make_corrections])
choice_audit = OperatorPOWL(operator=Operator.XOR, children=[external_audit, loop_audit])

# Define the root POWL model
root = StrictPartialOrder(nodes=[schedule_audit, prepare_docs, gather_evidence, self_assessment, choice_audit, final_audit, award_certification, issue_docs])
root.order.add_edge(schedule_audit, prepare_docs)
root.order.add_edge(prepare_docs, gather_evidence)
root.order.add_edge(gather_evidence, self_assessment)
root.order.add_edge(self_assessment, choice_audit)
root.order.add_edge(choice_audit, final_audit)
root.order.add_edge(final_audit, award_certification)
root.order.add_edge(award_certification, issue_docs)

print(root)