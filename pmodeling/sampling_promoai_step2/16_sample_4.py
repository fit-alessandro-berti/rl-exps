import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
approve_report = Transition(label='Approve report')
archive_report = Transition(label='Archive report')
check_regulatory_updates = Transition(label='Check regulatory updates')
close_audit_process = Transition(label='Close audit process')
compile_audit_report = Transition(label='Compile audit report')
complete_risk_assessment = Transition(label='Complete risk assessment/mitigation')
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
request_clarifications = Transition(label='Request clarifications of discrepancies')
review_report_audit_director = Transition(label='Review report by audit director')
review_submission = Transition(label='Review submission')
send_notification = Transition(label='Send notification')
send_report_revision = Transition(label='Send report for revision')
submit_documents = Transition(label='Submit documents')
update_resubmit_report = Transition(label='Update and resubmit report')

# Define the POWL model structure
root = StrictPartialOrder(nodes=[
    check_regulatory_updates,
    gather_necessary_documents,
    launch_detailed_investigation,
    perform_site_visits,
    prepare_financial_statements,
    receive_clarifications,
    request_clarifications,
    review_submission,
    submit_documents,
    update_resubmit_report,
    evaluate_financial_risks,
    evaluate_operational_risks,
    evaluate_compliance_risks,
    complete_risk_assessment,
    conduct_data_analysis,
    conduct_interviews,
    compile_audit_report,
    review_report_audit_director,
    send_report_revision,
    approve_report,
    distribute_final_report,
    close_audit_process,
    archive_report
])

# Define the dependencies between nodes
root.order.add_edge(check_regulatory_updates, gather_necessary_documents)
root.order.add_edge(gather_necessary_documents, launch_detailed_investigation)
root.order.add_edge(launch_detailed_investigation, perform_site_visits)
root.order.add_edge(perform_site_visits, prepare_financial_statements)
root.order.add_edge(prepare_financial_statements, receive_clarifications)
root.order.add_edge(receive_clarifications, request_clarifications)
root.order.add_edge(request_clarifications, review_submission)
root.order.add_edge(review_submission, submit_documents)
root.order.add_edge(submit_documents, update_resubmit_report)
root.order.add_edge(update_resubmit_report, evaluate_financial_risks)
root.order.add_edge(evaluate_financial_risks, evaluate_operational_risks)
root.order.add_edge(evaluate_operational_risks, evaluate_compliance_risks)
root.order.add_edge(evaluate_compliance_risks, complete_risk_assessment)
root.order.add_edge(complete_risk_assessment, conduct_data_analysis)
root.order.add_edge(conduct_data_analysis, conduct_interviews)
root.order.add_edge(conduct_interviews, compile_audit_report)
root.order.add_edge(compile_audit_report, review_report_audit_director)
root.order.add_edge(review_report_audit_director, send_report_revision)
root.order.add_edge(send_report_revision, approve_report)
root.order.add_edge(approve_report, distribute_final_report)
root.order.add_edge(distribute_final_report, close_audit_process)
root.order.add_edge(close_audit_process, archive_report)

# Print the POWL model
print(root)