import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
schedule_audit = Transition(label='Schedule compliance audit')
prepare_docs = Transition(label='Prepare documentation')
gather_evidence = Transition(label='Gather evidence')
self_assessment = Transition(label='Conduct self-assessment')
external_audit = Transition(label='Conduct external audit')
identify_gaps = Transition(label='Identify gaps or issues')
correct_improve = Transition(label='Make necessary corrections or improvements')
final_audit = Transition(label='Conduct final audit')
award_certification = Transition(label='Award certification')
issue_docs = Transition(label='Issue official documents')

# Define a silent transition for skipping steps
skip = SilentTransition()

# Define loops for self-assessment and correction/improvement steps
self_assessment_loop = OperatorPOWL(operator=Operator.LOOP, children=[self_assessment, external_audit])
correct_improve_loop = OperatorPOWL(operator=Operator.LOOP, children=[correct_improve, final_audit])

# Define choices for final audit and issuing documents
final_audit_choice = OperatorPOWL(operator=Operator.XOR, children=[final_audit, award_certification])
issue_docs_choice = OperatorPOWL(operator=Operator.XOR, children=[issue_docs, skip])

# Define the root process with the sequence of activities
root = StrictPartialOrder(nodes=[schedule_audit, prepare_docs, gather_evidence, self_assessment_loop, correct_improve_loop, final_audit_choice, issue_docs_choice])

# Add order dependencies between transitions
root.order.add_edge(schedule_audit, prepare_docs)
root.order.add_edge(prepare_docs, gather_evidence)
root.order.add_edge(gather_evidence, self_assessment_loop)
root.order.add_edge(self_assessment_loop, correct_improve_loop)
root.order.add_edge(correct_improve_loop, final_audit_choice)
root.order.add_edge(final_audit_choice, issue_docs_choice)