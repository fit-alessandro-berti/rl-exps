from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition

# Define the transitions
approve_report = Transition(label='Approve report')
archive_report = Transition(label='Archive report')
check_regulatory_updates = Transition(label='Check regulatory updates')
close_audit_process = Transition(label='Close audit process')
compile_audit_report = Transition(label='Compile audit report')
complete_risk_assessment_mitigation = Transition(label='Complete risk assessment/mitigation')
conduct_data_analysis = Transition(label='Conduct data analysis')
conduct_interviews = Transition(label='Conduct interviews')
distribute_final_report = Transition(label='Distribute final report')
evaluate_compliance_risks = Transition(label='Evaluate compliance risks')
evaluate_financial_risks = Transition(label='Evaluate financial risks')
evaluate_operational_risks = Transition(label='Evaluate operational risks')
gather_necessary_documents = Transition(label='Gather necessary documents')
launch_detailed_investigation = Transition(label='Launch detailed investigation')
perform_site_visits = Transition(label='Perform site visits')
prepare_financial_statements = Transition(label='Prepare financial statements')
receive_clarifications = Transition(label='Receive clarifications')
request_clarifications_of_discrepancies = Transition(label='Request clarifications of discrepancies')
review_report_by_audit_director = Transition(label='Review report by audit director')
review_submission = Transition(label='Review submission')
send_notification = Transition(label='Send notification')
send_report_for_revision = Transition(label='Send report for revision')
submit_documents = Transition(label='Submit documents')
update_and_resubmit_report = Transition(label='Update and resubmit report')

# Define the partial order
root = StrictPartialOrder(nodes=[
    approve_report,
    archive_report,
    check_regulatory_updates,
    close_audit_process,
    compile_audit_report,
    complete_risk_assessment_mitigation,
    conduct_data_analysis,
    conduct_interviews,
    distribute_final_report,
    evaluate_compliance_risks,
    evaluate_financial_risks,
    evaluate_operational_risks,
    gather_necessary_documents,
    launch_detailed_investigation,
    perform_site_visits,
    prepare_financial_statements,
    receive_clarifications,
    request_clarifications_of_discrepancies,
    review_report_by_audit_director,
    review_submission,
    send_notification,
    send_report_for_revision,
    submit_documents,
    update_and_resubmit_report
])

# Define the dependencies
root.order.add_edge(send_notification, gather_necessary_documents)
root.order.add_edge(gather_necessary_documents, prepare_financial_statements)
root.order.add_edge(prepare_financial_statements, check_regulatory_updates)
root.order.add_edge(check_regulatory_updates, request_clarifications_of_discrepancies)
root.order.add_edge(request_clarifications_of_discrepancies, receive_clarifications)
root.order.add_edge(receive_clarifications, launch_detailed_investigation)
root.order.add_edge(launch_detailed_investigation, perform_site_visits)
root.order.add_edge(perform_site_visits, complete_risk_assessment_mitigation)
root.order.add_edge(complete_risk_assessment_mitigation, conduct_data_analysis)
root.order.add_edge(conduct_data_analysis, conduct_interviews)
root.order.add_edge(conduct_interviews, review_submission)
root.order.add_edge(review_submission, submit_documents)
root.order.add_edge(submit_documents, review_report_by_audit_director)
root.order.add_edge(review_report_by_audit_director, send_report_for_revision)
root.order.add_edge(send_report_for_revision, update_and_resubmit_report)
root.order.add_edge(update_and_resubmit_report, review_report_by_audit_director)
root.order.add_edge(review_report_by_audit_director, distribute_final_report)
root.order.add_edge(distribute_final_report, archive_report)
root.order.add_edge(archive_report, close_audit_process)

print(root)