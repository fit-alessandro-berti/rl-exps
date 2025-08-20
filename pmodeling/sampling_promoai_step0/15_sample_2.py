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

# Define the silent transition
skip = SilentTransition()

# Define the loop for the self-assessment process
loop = OperatorPOWL(operator=Operator.LOOP, children=[conduct_self_assessment, gather_evidence, identify_gaps_or_issues, make_necessary_corrections_or_improvements])

# Define the XOR for the external and final audits
xor = OperatorPOWL(operator=Operator.XOR, children=[conduct_external_audit, conduct_final_audit])

# Define the root of the POWL model
root = StrictPartialOrder(nodes=[schedule_compliance_audit, loop, xor])
root.order.add_edge(schedule_compliance_audit, loop)
root.order.add_edge(schedule_compliance_audit, xor)

# Add the remaining edges
root.order.add_edge(loop, conduct_self_assessment)
root.order.add_edge(loop, gather_evidence)
root.order.add_edge(loop, identify_gaps_or_issues)
root.order.add_edge(loop, make_necessary_corrections_or_improvements)
root.order.add_edge(xor, conduct_external_audit)
root.order.add_edge(xor, conduct_final_audit)
root.order.add_edge(conduct_final_audit, issue_official_documents)
root.order.add_edge(conduct_external_audit, issue_official_documents)

# Print the POWL model
print(root)