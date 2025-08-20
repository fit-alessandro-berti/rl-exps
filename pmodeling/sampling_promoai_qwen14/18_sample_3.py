import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities as transitions
submit_application = Transition(label='Submit application online')
review_application = Transition(label='Review application and documents')
notify_missing_docs = Transition(label='Notify applicant of missing documents')
process_fees = Transition(label='Process fees or waivers')
evaluate_application = Transition(label='Evaluate application by admissions committee')
send_acceptance = Transition(label='Send acceptance letter')
send_rejection = Transition(label='Send rejection letter')
confirm_enrollment = Transition(label='Confirm enrollment')
cancel_application = Transition(label='Cancel application')
provide_missing_docs = Transition(label='Provide missing documents')
assist_visa = Transition(label='Assist with visa processing')
setup_it_accounts = Transition(label='Set up IT accounts')
send_orientation = Transition(label='Send orientation materials')
obtain_id_card = Transition(label='Obtain student ID card')
meet_advisor = Transition(label='Meet with academic advisor')
select_courses = Transition(label='Select courses')
resolve_conflicts = Transition(label='Resolve schedule conflicts')
begin_classes = Transition(label='Begin attending classes')
add_drop_courses = Transition(label='Add/drop courses')
post_grades = Transition(label='Post grades')
review_grades = Transition(label='Review grades online')
file_appeal = Transition(label='File an appeal')
submit_appeal_form = Transition(label='Submit appeal form')
meet_appeals_committee = Transition(label='Meet with appeals committee')
await_decision = Transition(label='Await decision')
graduate = Transition(label='Graduate')
withdraw = Transition(label='Withdraw')

# Define the loop for the semester process
semester_loop = OperatorPOWL(operator=Operator.LOOP, children=[
    OperatorPOWL(operator=Operator.XOR, children=[
        OperatorPOWL(operator=Operator.SEQUENCE, children=[
            add_drop_courses,
            post_grades,
            OperatorPOWL(operator=Operator.XOR, children=[
                OperatorPOWL(operator=Operator.SEQUENCE, children=[
                    review_grades,
                    OperatorPOWL(operator=Operator.XOR, children=[
                        OperatorPOWL(operator=Operator.SEQUENCE, children=[
                            file_appeal,
                            OperatorPOWL(operator=Operator.SEQUENCE, children=[
                                submit_appeal_form,
                                meet_appeals_committee,
                                await_decision
                            ])
                        ]),
                        silent_transition  # If no appeal is filed, the loop continues
                    ])
                ]),
                silent_transition  # If grades are not reviewed, the loop continues
            ])
        ]),
        silent_transition  # If no courses are added/dropped, the loop continues
    ])
])

# Define the main process
root = StrictPartialOrder(nodes=[
    submit_application,
    review_application,
    OperatorPOWL(operator=Operator.XOR, children=[
        OperatorPOWL(operator=Operator.SEQUENCE, children=[
            notify_missing_docs,
            provide_missing_docs
        ]),
        silent_transition
    ]),
    process_fees,
    evaluate_application,
    OperatorPOWL(operator=Operator.XOR, children=[
        OperatorPOWL(operator=Operator.SEQUENCE, children=[
            send_acceptance,
            OperatorPOWL(operator=Operator.XOR, children=[
                OperatorPOWL(operator=Operator.SEQUENCE, children=[
                    confirm_enrollment,
                    OperatorPOWL(operator=Operator.SEQUENCE, children=[
                        setup_it_accounts,
                        OperatorPOWL(operator=Operator.XOR, children=[
                            OperatorPOWL(operator=Operator.SEQUENCE, children=[
                                send_orientation,
                                obtain_id_card,
                                OperatorPOWL(operator=Operator.SEQUENCE, children=[
                                    meet_advisor,
                                    select_courses,
                                    resolve_conflicts,
                                    begin_classes,
                                    semester_loop
                                ])
                            ]),
                            OperatorPOWL(operator=Operator.SEQUENCE, children=[
                                assist_visa,
                                OperatorPOWL(operator=Operator.SEQUENCE, children=[
                                    meet_advisor,
                                    select_courses,
                                    resolve_conflicts,
                                    begin_classes,
                                    semester_loop
                                ])
                            ])
                        ])
                    ])
                ]),
                cancel_application
            ])
        ]),
        send_rejection
    ]),
    OperatorPOWL(operator=Operator.XOR, children=[
        graduate,
        withdraw
    ])
])

# Define the order of the nodes
root.order.add_edge(submit_application, review_application)
root.order.add_edge(review_application, notify_missing_docs)
root.order.add_edge(notify_missing_docs, provide_missing_docs)
root.order.add_edge(provide_missing_docs, process_fees)
root.order.add_edge(process_fees, evaluate_application)
root.order.add_edge(evaluate_application, send_acceptance)
root.order.add_edge(send_acceptance, confirm_enrollment)
root.order.add_edge(confirm_enrollment, setup_it_accounts)
root.order.add_edge(setup_it_accounts, send_orientation)
root.order.add_edge(send_orientation, obtain_id_card)
root.order.add_edge(obtain_id_card, meet_advisor)
root.order.add_edge(meet_advisor, select_courses)
root.order.add_edge(select_courses, resolve_conflicts)
root.order.add_edge(resolve_conflicts, begin_classes)
root.order.add_edge(begin_classes, semester_loop)
root.order.add_edge(semester_loop, graduate)
root.order.add_edge(semester_loop, withdraw)
root.order.add_edge(evaluate_application, send_rejection)
root.order.add_edge(send_rejection, cancel_application)

# Add edges for the loop
root.order.add_edge(add_drop_courses, post_grades)
root.order.add_edge(post_grades, review_grades)
root.order.add_edge(review_grades, file_appeal)
root.order.add_edge(file_appeal, submit_appeal_form)
root.order.add_edge(submit_appeal_form, meet_appeals_committee)
root.order.add_edge(meet_appeals_committee, await_decision)
root.order.add_edge(await_decision, silent_transition)
root.order.add_edge(review_grades, silent_transition)
root.order.add_edge(add_drop_courses, silent_transition)