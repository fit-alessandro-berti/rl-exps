import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
award_certification = Transition(label='Award certification')
conduct_external_audit = Transition(label='Conduct external audit')
conduct_final_audit = Transition(label='Conduct final audit')
conduct_self_assessment = Transition(label='Conduct self-assessment')
gather_evidence = Transition(label='Gather evidence')
identify_gaps_or_issues = Transition(label='Identify gaps or issues')
issue_official_documents = Transition(label='Issue official documents')
make_necessary_corrections_or_improvements = Transition(label='Make necessary corrections or improvements')
prepare_documentation = Transition(label='Prepare documentation')
schedule_compliance_audit = Transition(label='Schedule compliance audit')

# Define the silent transitions
skip = SilentTransition()

# Define the loop nodes
loop_1 = OperatorPOWL(operator=Operator.LOOP, children=[conduct_self_assessment, gather_evidence, identify_gaps_or_issues])
loop_2 = OperatorPOWL(operator=Operator.LOOP, children=[make_necessary_corrections_or_improvements, prepare_documentation])

# Define the exclusive choice nodes
xor_1 = OperatorPOWL(operator=Operator.XOR, children=[conduct_external_audit, skip])
xor_2 = OperatorPOWL(operator=Operator.XOR, children=[conduct_final_audit, skip])

# Define the root node
root = StrictPartialOrder(nodes=[loop_1, loop_2, xor_1, xor_2, award_certification])
root.order.add_edge(loop_1, xor_1)
root.order.add_edge(loop_1, xor_2)
root.order.add_edge(loop_2, xor_1)
root.order.add_edge(loop_2, xor_2)
root.order.add_edge(xor_1, award_certification)
root.order.add_edge(xor_2, award_certification)

# Save the final result in the variable 'root'