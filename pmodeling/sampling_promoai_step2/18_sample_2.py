import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
add_drop_courses = Transition(label='Add/drop courses')
assist_with_visa = Transition(label='Assist with visa processing')
await_decision = Transition(label='Await decision')
begin_attending_classes = Transition(label='Begin attending classes')
cancel_application = Transition(label='Cancel application')
confirm_enrollment = Transition(label='Confirm enrollment')
evaluate_application = Transition(label='Evaluate application by admissions committee')
graduate = Transition(label='Graduate')
meet_with_advisor = Transition(label='Meet with academic advisor')
meet_with_appeals = Transition(label='Meet with appeals committee')
notify_missing_docs = Transition(label='Notify applicant of missing documents')
obtain_id_card = Transition(label='Obtain student ID card')
post_grades = Transition(label='Post grades')
process_fees = Transition(label='Process fees or waivers')
provide_missing_docs = Transition(label='Provide missing documents')
resolve_schedule_conflicts = Transition(label='Resolve schedule conflicts')
review_app_docs = Transition(label='Review application and documents')
review_grades_online = Transition(label='Review grades online')
select_courses = Transition(label='Select courses')
send_acceptance_letter = Transition(label='Send acceptance letter')
send_orientation = Transition(label='Send orientation materials')
send_rejection_letter = Transition(label='Send rejection letter')
set_up_it_accounts = Transition(label='Set up IT accounts')
submit_appeal_form = Transition(label='Submit appeal form')
submit_application = Transition(label='Submit application online')
withdraw = Transition(label='Withdraw')

# Define the partial order structure
root = StrictPartialOrder(nodes=[
    add_drop_courses,
    assist_with_visa,
    await_decision,
    begin_attending_classes,
    cancel_application,
    confirm_enrollment,
    evaluate_application,
    graduate,
    meet_with_advisor,
    meet_with_appeals,
    notify_missing_docs,
    obtain_id_card,
    post_grades,
    process_fees,
    provide_missing_docs,
    resolve_schedule_conflicts,
    review_app_docs,
    review_grades_online,
    select_courses,
    send_acceptance_letter,
    send_orientation,
    send_rejection_letter,
    set_up_it_accounts,
    submit_appeal_form,
    submit_application,
    withdraw
])

# Define the dependencies between activities
root.order.add_edge(submit_application, add_drop_courses)
root.order.add_edge(add_drop_courses, meet_with_advisor)
root.order.add_edge(meet_with_advisor, select_courses)
root.order.add_edge(select_courses, resolve_schedule_conflicts)
root.order.add_edge(resolve_schedule_conflicts, begin_attending_classes)
root.order.add_edge(begin_attending_classes, process_fees)
root.order.add_edge(process_fees, provide_missing_docs)
root.order.add_edge(provide_missing_docs, notify_missing_docs)
root.order.add_edge(notify_missing_docs, add_drop_courses)
root.order.add_edge(add_drop_courses, review_app_docs)
root.order.add_edge(review_app_docs, evaluate_application)
root.order.add_edge(evaluate_application, confirm_enrollment)
root.order.add_edge(confirm_enrollment, send_acceptance_letter)
root.order.add_edge(confirm_enrollment, send_orientation)
root.order.add_edge(send_acceptance_letter, meet_with_appeals)
root.order.add_edge(send_orientation, meet_with_advisor)
root.order.add_edge(meet_with_appeals, await_decision)
root.order.add_edge(await_decision, review_grades_online)
root.order.add_edge(review_grades_online, submit_appeal_form)
root.order.add_edge(submit_appeal_form, meet_with_appeals)
root.order.add_edge(meet_with_appeals, await_decision)
root.order.add_edge(await_decision, send_rejection_letter)
root.order.add_edge(send_rejection_letter, cancel_application)
root.order.add_edge(cancel_application, withdraw)
root.order.add_edge(withdraw, graduate)
root.order.add_edge(graduate, send_rejection_letter)