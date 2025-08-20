import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
schedule_compliance_audit = Transition(label='Schedule compliance audit')
prepare_documentation = Transition(label='Prepare documentation')
gather_evidence = Transition(label='Gather evidence')
conduct_self_assessment = Transition(label='Conduct self-assessment')
conduct_external_audit = Transition(label='Conduct external audit')
identify_gaps_or_issues = Transition(label='Identify gaps or issues')
make_necessary_corrections_or_improvements = Transition(label='Make necessary corrections or improvements')
conduct_final_audit = Transition(label='Conduct final audit')
award_certification = Transition(label='Award certification')
issue_official_documents = Transition(label='Issue official documents')

# Define POWL model
root = StrictPartialOrder(nodes=[
    schedule_compliance_audit,
    prepare_documentation,
    gather_evidence,
    conduct_self_assessment,
    conduct_external_audit,
    identify_gaps_or_issues,
    make_necessary_corrections_or_improvements,
    conduct_final_audit,
    award_certification,
    issue_official_documents
])

# Add order
root.order.add_edge(schedule_compliance_audit, prepare_documentation)
root.order.add_edge(prepare_documentation, gather_evidence)
root.order.add_edge(gather_evidence, conduct_self_assessment)
root.order.add_edge(conduct_self_assessment, conduct_external_audit)
root.order.add_edge(conduct_external_audit, identify_gaps_or_issues)
root.order.add_edge(identify_gaps_or_issues, make_necessary_corrections_or_improvements)
root.order.add_edge(make_necessary_corrections_or_improvements, conduct_final_audit)
root.order.add_edge(conduct_final_audit, award_certification)
root.order.add_edge(award_certification, issue_official_documents)