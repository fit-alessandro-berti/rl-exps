import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions
submit_application = Transition(label='Submit application online')
review_documents = Transition(label='Review application and documents')
notify_missing_documents = Transition(label='Notify applicant of missing documents')
process_fees = Transition(label='Process fees or waivers')
evaluate_committee = Transition(label='Evaluate application by admissions committee')
acceptance_letter = Transition(label='Send acceptance letter')
orientation_materials = Transition(label='Send orientation materials')
rejection_letter = Transition(label='Send rejection letter')
confirm_enrollment = Transition(label='Confirm enrollment')
cancel_application = Transition(label='Cancel application')
academic_advisor = Transition(label='Meet with academic advisor')
select_courses = Transition(label='Select courses')
resolve_conflicts = Transition(label='Resolve schedule conflicts')
add_drop_courses = Transition(label='Add/drop courses')
graduate = Transition(label='Graduate')
withdraw = Transition(label='Withdraw')
student_id_card = Transition(label='Obtain student ID card')
post_grades = Transition(label='Post grades')
resolve_grades = Transition(label='Review grades online')
submit_form = Transition(label='Submit appeal form')
meet_committee = Transition(label='Meet with appeals committee')
await_decision = Transition(label='Await decision')
set_up_accounts = Transition(label='Set up IT accounts')

# Define silent transitions
skip = SilentTransition()

# Define POWL model
root = StrictPartialOrder(nodes=[
    submit_application,
    review_documents,
    notify_missing_documents,
    process_fees,
    evaluate_committee,
    acceptance_letter,
    orientation_materials,
    rejection_letter,
    confirm_enrollment,
    cancel_application,
    academic_advisor,
    select_courses,
    resolve_conflicts,
    add_drop_courses,
    graduate,
    withdraw,
    student_id_card,
    post_grades,
    resolve_grades,
    submit_form,
    meet_committee,
    await_decision,
    set_up_accounts
])

# Define partial order dependencies
root.order.add_edge(submit_application, review_documents)
root.order.add_edge(review_documents, notify_missing_documents)
root.order.add_edge(notify_missing_documents, process_fees)
root.order.add_edge(process_fees, evaluate_committee)
root.order.add_edge(evaluate_committee, acceptance_letter)
root.order.add_edge(acceptance_letter, orientation_materials)
root.order.add_edge(acceptance_letter, rejection_letter)
root.order.add_edge(rejection_letter, confirm_enrollment)
root.order.add_edge(confirm_enrollment, cancel_application)
root.order.add_edge(cancel_application, academic_advisor)
root.order.add_edge(academic_advisor, select_courses)
root.order.add_edge(select_courses, resolve_conflicts)
root.order.add_edge(resolve_conflicts, add_drop_courses)
root.order.add_edge(add_drop_courses, graduate)
root.order.add_edge(add_drop_courses, withdraw)
root.order.add_edge(withdraw, student_id_card)
root.order.add_edge(student_id_card, post_grades)
root.order.add_edge(post_grades, resolve_grades)
root.order.add_edge(resolve_grades, submit_form)
root.order.add_edge(submit_form, meet_committee)
root.order.add_edge(meet_committee, await_decision)
root.order.add_edge(await_decision, set_up_accounts)