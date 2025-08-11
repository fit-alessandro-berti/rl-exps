import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions
add_drop_courses = Transition(label='Add/drop courses')
assist_with_visa_processing = Transition(label='Assist with visa processing')
await_decision = Transition(label='Await decision')
begin_attending_classes = Transition(label='Begin attending classes')
cancel_application = Transition(label='Cancel application')
confirm_enrollment = Transition(label='Confirm enrollment')
evaluate_application = Transition(label='Evaluate application by admissions committee')
graduate = Transition(label='Graduate')
meet_with_advisor = Transition(label='Meet with academic advisor')
meet_with_appeals_committee = Transition(label='Meet with appeals committee')
notify_applicant_of_missing_documents = Transition(label='Notify applicant of missing documents')
obtain_student_id_card = Transition(label='Obtain student ID card')
post_grades = Transition(label='Post grades')
process_fees_or_waivers = Transition(label='Process fees or waivers')
provide_missing_documents = Transition(label='Provide missing documents')
resolve_schedule_conflicts = Transition(label='Resolve schedule conflicts')
review_application_and_documents = Transition(label='Review application and documents')
review_grades_online = Transition(label='Review grades online')
select_courses = Transition(label='Select courses')
send_acceptance_letter = Transition(label='Send acceptance letter')
send_orientation_materials = Transition(label='Send orientation materials')
send_rejection_letter = Transition(label='Send rejection letter')
set_up_it_accounts = Transition(label='Set up IT accounts')
submit_appeal_form = Transition(label='Submit appeal form')
submit_application_online = Transition(label='Submit application online')
withdraw = Transition(label='Withdraw')

# Define silent transitions
skip = SilentTransition()

# Define partial order
root = StrictPartialOrder(nodes=[
    add_drop_courses, assist_with_visa_processing, await_decision, begin_attending_classes,
    cancel_application, confirm_enrollment, evaluate_application, graduate, meet_with_advisor,
    meet_with_appeals_committee, notify_applicant_of_missing_documents, obtain_student_id_card,
    post_grades, process_fees_or_waivers, provide_missing_documents, resolve_schedule_conflicts,
    review_application_and_documents, review_grades_online, select_courses, send_acceptance_letter,
    send_orientation_materials, send_rejection_letter, set_up_it_accounts, submit_appeal_form,
    submit_application_online, withdraw
])

# Define partial order edges
root.order.add_edge(submit_application_online, evaluate_application)
root.order.add_edge(evaluate_application, notify_applicant_of_missing_documents)
root.order.add_edge(notify_applicant_of_missing_documents, provide_missing_documents)
root.order.add_edge(provide_missing_documents, resolve_schedule_conflicts)
root.order.add_edge(resolve_schedule_conflicts, select_courses)
root.order.add_edge(select_courses, begin_attending_classes)
root.order.add_edge(begin_attending_classes, confirm_enrollment)
root.order.add_edge(confirm_enrollment, await_decision)
root.order.add_edge(await_decision, process_fees_or_waivers)
root.order.add_edge(process_fees_or_waivers, assist_with_visa_processing)
root.order.add_edge(assist_with_visa_processing, meet_with_advisor)
root.order.add_edge(meet_with_advisor, meet_with_appeals_committee)
root.order.add_edge(meet_with_appeals_committee, submit_appeal_form)
root.order.add_edge(submit_appeal_form, await_decision)
root.order.add_edge(await_decision, send_acceptance_letter)
root.order.add_edge(send_acceptance_letter, send_orientation_materials)
root.order.add_edge(send_acceptance_letter, set_up_it_accounts)
root.order.add_edge(set_up_it_accounts, graduate)
root.order.add_edge(graduate, withdraw)
root.order.add_edge(withdraw, cancel_application)
root.order.add_edge(cancel_application, send_rejection_letter)