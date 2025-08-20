import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
Schedule_compliance_audit = Transition(label='Schedule compliance audit')
Prepare_documentation = Transition(label='Prepare documentation')
Gather_evidence = Transition(label='Gather evidence')
Conduct_self_assessment = Transition(label='Conduct self-assessment')
Conduct_external_audit = Transition(label='Conduct external audit')
Identify_gaps_or_issues = Transition(label='Identify gaps or issues')
Make_necessary_corrections_or_improvements = Transition(label='Make necessary corrections or improvements')
Conduct_final_audit = Transition(label='Conduct final audit')
Award_certification = Transition(label='Award certification')
Issue_official_documents = Transition(label='Issue official documents')

# Define the POWL model for the process
root = StrictPartialOrder(nodes=[
    Schedule_compliance_audit,
    Prepare_documentation,
    Gather_evidence,
    Conduct_self_assessment,
    Conduct_external_audit,
    Identify_gaps_or_issues,
    Make_necessary_corrections_or_improvements,
    Conduct_final_audit,
    Award_certification,
    Issue_official_documents
])

# Define the order of the transitions
root.order.add_edge(Schedule_compliance_audit, Prepare_documentation)
root.order.add_edge(Prepare_documentation, Gather_evidence)
root.order.add_edge(Gather_evidence, Conduct_self_assessment)
root.order.add_edge(Conduct_self_assessment, Conduct_external_audit)
root.order.add_edge(Conduct_external_audit, Identify_gaps_or_issues)
root.order.add_edge(Identify_gaps_or_issues, Make_necessary_corrections_or_improvements)
root.order.add_edge(Make_necessary_corrections_or_improvements, Conduct_final_audit)
root.order.add_edge(Conduct_final_audit, Award_certification)
root.order.add_edge(Award_certification, Issue_official_documents)