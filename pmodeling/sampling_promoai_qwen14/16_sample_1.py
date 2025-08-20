import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities as transitions
send_notification = Transition(label='Send notification')
prepare_financial_statements = Transition(label='Prepare financial statements')
gather_necessary_documents = Transition(label='Gather necessary documents')
check_regulatory_updates = Transition(label='Check regulatory updates')
submit_documents = Transition(label='Submit documents')
review_submission = Transition(label='Review submission')
request_clarifications = Transition(label='Request clarifications of discrepancies')
receive_clarifications = Transition(label='Receive clarifications')
complete_risk_assessment = OperatorPOWL(operator=Operator.XOR, children=[
    Transition(label='Evaluate financial risks'),
    Transition(label='Evaluate operational risks'),
    Transition(label='Evaluate compliance risks')
])
launch_detailed_investigation = OperatorPOWL(operator=Operator.XOR, children=[
    Transition(label='Conduct data analysis'),
    Transition(label='Conduct interviews'),
    OperatorPOWL(operator=Operator.XOR, children=[
        Transition(label='Perform site visits'),
        SilentTransition()  # Optional activity, represented by a silent transition
    ])
])
compile_audit_report = Transition(label='Compile audit report')
review_report_by_audit_director = Transition(label='Review report by audit director')
approve_report = Transition(label='Approve report')
send_report_for_revision = Transition(label='Send report for revision')
update_and_resubmit_report = Transition(label='Update and resubmit report')
distribute_final_report = Transition(label='Distribute final report')
archive_report = Transition(label='Archive report')
close_audit_process = Transition(label='Close audit process')

# Define loops and choices
regional_office_loop = OperatorPOWL(operator=Operator.LOOP, children=[
    prepare_financial_statements,
    gather_necessary_documents,
    submit_documents
])
compliance_team_loop = OperatorPOWL(operator=Operator.LOOP, children=[
    check_regulatory_updates
])
clarifications_loop = OperatorPOWL(operator=Operator.LOOP, children=[
    request_clarifications,
    receive_clarifications
])
report_revision_loop = OperatorPOWL(operator=Operator.LOOP, children=[
    review_report_by_audit_director,
    OperatorPOWL(operator=Operator.XOR, children=[
        approve_report,
        send_report_for_revision
    ]),
    update_and_resubmit_report
])

# Define the root partial order
root = StrictPartialOrder(nodes=[
    send_notification,
    regional_office_loop,
    compliance_team_loop,
    review_submission,
    clarifications_loop,
    complete_risk_assessment,
    launch_detailed_investigation,
    compile_audit_report,
    report_revision_loop,
    distribute_final_report,
    archive_report,
    close_audit_process
])

# Define dependencies between activities
root.order.add_edge(send_notification, regional_office_loop)
root.order.add_edge(send_notification, compliance_team_loop)
root.order.add_edge(regional_office_loop, review_submission)
root.order.add_edge(compliance_team_loop, review_submission)
root.order.add_edge(review_submission, clarifications_loop)
root.order.add_edge(clarifications_loop, complete_risk_assessment)
root.order.add_edge(complete_risk_assessment, launch_detailed_investigation)
root.order.add_edge(launch_detailed_investigation, compile_audit_report)
root.order.add_edge(compile_audit_report, report_revision_loop)
root.order.add_edge(report_revision_loop, distribute_final_report)
root.order.add_edge(distribute_final_report, archive_report)
root.order.add_edge(archive_report, close_audit_process)