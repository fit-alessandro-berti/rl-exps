import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
submit_application = Transition(label='Submit application online')
review_application = Transition(label='Review application and documents')
notify_missing_documents = Transition(label='Notify applicant of missing documents')
provide_missing_documents = Transition(label='Provide missing documents')
evaluate_application = Transition(label='Evaluate application by admissions committee')
process_fees = Transition(label='Process fees or waivers')
acceptance_letter = Transition(label='Send acceptance letter')
rejection_letter = Transition(label='Send rejection letter')
confirm_enrollment = Transition(label='Confirm enrollment')
cancel_application = Transition(label='Cancel application')
send_orientation_materials = Transition(label='Send orientation materials')
set_up_it_accounts = Transition(label='Set up IT accounts')
assist_with_visa_processing = Transition(label='Assist with visa processing')
obtain_student_id_card = Transition(label='Obtain student ID card')
meet_with_academic_advisor = Transition(label='Meet with academic advisor')
select_courses = Transition(label='Select courses')
resolve_schedule_conflicts = Transition(label='Resolve schedule conflicts')
begin_attending_classes = Transition(label='Begin attending classes')
add_drop_courses = Transition(label='Add/drop courses')
post_grades = Transition(label='Post grades')
review_grades_online = Transition(label='Review grades online')
submit_appeal_form = Transition(label='Submit appeal form')
meet_with_appeals_committee = Transition(label='Meet with appeals committee')
await_decision = Transition(label='Await decision')
graduate = Transition(label='Graduate')
withdraw = Transition(label='Withdraw')

# Define the POWL model
root = StrictPartialOrder(nodes=[
    submit_application,
    review_application,
    notify_missing_documents,
    provide_missing_documents,
    evaluate_application,
    process_fees,
    acceptance_letter,
    rejection_letter,
    confirm_enrollment,
    cancel_application,
    send_orientation_materials,
    set_up_it_accounts,
    assist_with_visa_processing,
    obtain_student_id_card,
    meet_with_academic_advisor,
    select_courses,
    resolve_schedule_conflicts,
    begin_attending_classes,
    add_drop_courses,
    post_grades,
    review_grades_online,
    submit_appeal_form,
    meet_with_appeals_committee,
    await_decision,
    graduate,
    withdraw
])

# Define the order of activities
root.order.add_edge(submit_application, review_application)
root.order.add_edge(review_application, notify_missing_documents)
root.order.add_edge(notify_missing_documents, provide_missing_documents)
root.order.add_edge(provide_missing_documents, review_application)
root.order.add_edge(review_application, evaluate_application)
root.order.add_edge(evaluate_application, process_fees)
root.order.add_edge(process_fees, acceptance_letter)
root.order.add_edge(process_fees, rejection_letter)
root.order.add_edge(acceptance_letter, confirm_enrollment)
root.order.add_edge(confirm_enrollment, cancel_application)
root.order.add_edge(acceptance_letter, send_orientation_materials)
root.order.add_edge(acceptance_letter, set_up_it_accounts)
root.order.add_edge(set_up_it_accounts, assist_with_visa_processing)
root.order.add_edge(set_up_it_accounts, obtain_student_id_card)
root.order.add_edge(assist_with_visa_processing, obtain_student_id_card)
root.order.add_edge(obtain_student_id_card, meet_with_academic_advisor)
root.order.add_edge(obtain_student_id_card, select_courses)
root.order.add_edge(obtain_student_id_card, resolve_schedule_conflicts)
root.order.add_edge(meet_with_academic_advisor, select_courses)
root.order.add_edge(select_courses, resolve_schedule_conflicts)
root.order.add_edge(resolve_schedule_conflicts, begin_attending_classes)
root.order.add_edge(begin_attending_classes, add_drop_courses)
root.order.add_edge(begin_attending_classes, post_grades)
root.order.add_edge(add_drop_courses, post_grades)
root.order.add_edge(post_grades, review_grades_online)
root.order.add_edge(review_grades_online, submit_appeal_form)
root.order.add_edge(submit_appeal_form, meet_with_appeals_committee)
root.order.add_edge(meet_with_appeals_committee, await_decision)
root.order.add_edge(await_decision, graduate)
root.order.add_edge(await_decision, withdraw)