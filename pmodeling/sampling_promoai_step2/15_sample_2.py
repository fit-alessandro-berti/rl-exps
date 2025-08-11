import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
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

# Define the partial order
root = StrictPartialOrder(nodes=[
    award_certification, 
    conduct_external_audit, 
    conduct_final_audit, 
    conduct_self_assessment, 
    gather_evidence, 
    identify_gaps_or_issues, 
    issue_official_documents, 
    make_necessary_corrections_or_improvements, 
    prepare_documentation, 
    schedule_compliance_audit
])

# Define the dependencies between activities
root.order.add_edge(schedule_compliance_audit, prepare_documentation)
root.order.add_edge(prepare_documentation, conduct_self_assessment)
root.order.add_edge(conduct_self_assessment, gather_evidence)
root.order.add_edge(gather_evidence, identify_gaps_or_issues)
root.order.add_edge(identify_gaps_or_issues, make_necessary_corrections_or_improvements)
root.order.add_edge(make_necessary_corrections_or_improvements, conduct_external_audit)
root.order.add_edge(conduct_external_audit, conduct_final_audit)
root.order.add_edge(conduct_final_audit, award_certification)
root.order.add_edge(award_certification, issue_official_documents)

print(root)