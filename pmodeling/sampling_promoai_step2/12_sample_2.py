import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
adjust_compensation = Transition(label='Adjust compensation')
approve_promotion = Transition(label='Approve promotion')
conducts_formal_performance_review = Transition(label='Conducts formal performance review')
consider_employee_for_promotion_or_new_role = Transition(label='Consider employee for promotion or new role')
create_personal_development_plan = Transition(label='Create personal development plan')
identify_development_needs_or_career_aspirations = Transition(label='Identify development needs or career aspirations')
receive_feedback_and_evaluation_from_supervisors = Transition(label='Receive feedback and evaluation from supervisors')
set_new_responsibilities = Transition(label='Set new responsibilities')
transition_into_new_role = Transition(label='Transition into new role')
work_on_skill_enhancement = Transition(label='Work on skill enhancement')

# Define the process
root = StrictPartialOrder(nodes=[
    adjust_compensation,
    approve_promotion,
    conducts_formal_performance_review,
    consider_employee_for_promotion_or_new_role,
    create_personal_development_plan,
    identify_development_needs_or_career_aspirations,
    receive_feedback_and_evaluation_from_supervisors,
    set_new_responsibilities,
    transition_into_new_role,
    work_on_skill_enhancement
])

root.order.add_edge(identify_development_needs_or_career_aspirations, create_personal_development_plan)
root.order.add_edge(create_personal_development_plan, receive_feedback_and_evaluation_from_supervisors)
root.order.add_edge(receive_feedback_and_evaluation_from_supervisors, work_on_skill_enhancement)
root.order.add_edge(work_on_skill_enhancement, conductsa_formal_performance_review)
root.order.add_edge(conductsa_formal_performance_review, consider_employee_for_promotion_or_new_role)
root.order.add_edge(consider_employee_for_promotion_or_new_role, approve_promotion)
root.order.add_edge(approve_promotion, adjust_compensation)
root.order.add_edge(adjust_compensation, transition_into_new_role)

print(root)