import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
identify_development_needs = Transition(label='Identify development needs or career aspirations')
create_personal_development_plan = Transition(label='Create personal development plan')
set_new_responsibilities = Transition(label='Set new responsibilities')
work_on_skill_enhancement = Transition(label='Work on skill enhancement')
receive_feedback_and_evaluation = Transition(label='Receive feedback and evaluation from supervisors')
conducts_performance_review = Transition(label='Conducts formal performance review')
consider_employee_for_promotion = Transition(label='Consider employee for promotion or new role')
approve_promotion = Transition(label='Approve promotion')
adjust_compensation = Transition(label='Adjust compensation')
transition_into_new_role = Transition(label='Transition into new role')

# Define the POWL model
root = StrictPartialOrder(nodes=[
    identify_development_needs,
    create_personal_development_plan,
    set_new_responsibilities,
    work_on_skill_enhancement,
    receive_feedback_and_evaluation,
    conducts_performance_review,
    consider_employee_for_promotion,
    approve_promotion,
    adjust_compensation,
    transition_into_new_role
])

# Define the order of execution
root.order.add_edge(identify_development_needs, create_personal_development_plan)
root.order.add_edge(create_personal_development_plan, set_new_responsibilities)
root.order.add_edge(set_new_responsibilities, work_on_skill_enhancement)
root.order.add_edge(work_on_skill_enhancement, receive_feedback_and_evaluation)
root.order.add_edge(receive_feedback_and_evaluation, conducts_performance_review)
root.order.add_edge(conducts_performance_review, consider_employee_for_promotion)
root.order.add_edge(consider_employee_for_promotion, approve_promotion)
root.order.add_edge(approve_promotion, adjust_compensation)
root.order.add_edge(adjust_compensation, transition_into_new_role)

print(root)