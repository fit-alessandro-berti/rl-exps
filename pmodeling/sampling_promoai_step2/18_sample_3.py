from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
submit_application = Transition(label='Submit application online')
review_documents = Transition(label='Review application and documents')
notify_missing_documents = Transition(label='Notify applicant of missing documents')
process_fees = Transition(label='Process fees or waivers')
acceptance_letter = Transition(label='Send acceptance letter')
orientation_materials = Transition(label='Send orientation materials')
rejection_letter = Transition(label='Send rejection letter')
confirm_enrollment = Transition(label='Confirm enrollment')
set_up_it_accounts = Transition(label='Set up IT accounts')
assist_with_visa_processing = Transition(label='Assist with visa processing')
meet_with_advisor = Transition(label='Meet with academic advisor')
resolve_schedule_conflicts = Transition(label='Resolve schedule conflicts')
select_courses = Transition(label='Select courses')
post_grades = Transition(label='Post grades')
review_grades_online = Transition(label='Review grades online')
submit_appeal_form = Transition(label='Submit appeal form')
meet_with_appeals_committee = Transition(label='Meet with appeals committee')
await_decision = Transition(label='Await decision')
graduate = Transition(label='Graduate')
cancel_application = Transition(label='Cancel application')
begin_attending_classes = Transition(label='Begin attending classes')
add_drop_courses = Transition(label='Add/drop courses')

# Define silent transitions
skip = SilentTransition()

# Define the process
root = StrictPartialOrder(
    nodes=[
        submit_application,
        review_documents,
        notify_missing_documents,
        process_fees,
        acceptance_letter,
        orientation_materials,
        rejection_letter,
        confirm_enrollment,
        set_up_it_accounts,
        assist_with_visa_processing,
        meet_with_advisor,
        resolve_schedule_conflicts,
        select_courses,
        post_grades,
        review_grades_online,
        submit_appeal_form,
        meet_with_appeals_committee,
        await_decision,
        graduate,
        cancel_application,
        begin_attending_classes,
        add_drop_courses
    ]
)

# Define dependencies
root.order.add_edge(submit_application, review_documents)
root.order.add_edge(review_documents, notify_missing_documents)
root.order.add_edge(notify_missing_documents, process_fees)
root.order.add_edge(process_fees, acceptance_letter)
root.order.add_edge(acceptance_letter, orientation_materials)
root.order.add_edge(orientation_materials, confirm_enrollment)
root.order.add_edge(confirm_enrollment, set_up_it_accounts)
root.order.add_edge(set_up_it_accounts, assist_with_visa_processing)
root.order.add_edge(assist_with_visa_processing, meet_with_advisor)
root.order.add_edge(meet_with_advisor, resolve_schedule_conflicts)
root.order.add_edge(resolve_schedule_conflicts, select_courses)
root.order.add_edge(select_courses, post_grades)
root.order.add_edge(post_grades, review_grades_online)
root.order.add_edge(review_grades_online, submit_appeal_form)
root.order.add_edge(submit_appeal_form, meet_with_appeals_committee)
root.order.add_edge(meet_with_appeals_committee, await_decision)
root.order.add_edge(await_decision, graduate)
root.order.add_edge(graduate, cancel_application)
root.order.add_edge(cancel_application, begin_attending_classes)
root.order.add_edge(begin_attending_classes, add_drop_courses)