import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
adjust_compensation = Transition(label='Adjust compensation')
approve_promotion = Transition(label='Approve promotion')
conduct_formal_review = Transition(label='Conducts formal performance review')
consider_promotion_new_role = Transition(label='Consider employee for promotion or new role')
create_personal_dev_plan = Transition(label='Create personal development plan')
identify_dev_needs_career_aspirations = Transition(label='Identify development needs or career aspirations')
receive_feedback_evaluation = Transition(label='Receive feedback and evaluation from supervisors')
set_new_responsibilities = Transition(label='Set new responsibilities')
transition_new_role = Transition(label='Transition into new role')
work_skill_enhancement = Transition(label='Work on skill enhancement')

# Define the process model
root = StrictPartialOrder(nodes=[
    identify_dev_needs_career_aspirations,
    create_personal_dev_plan,
    receive_feedback_evaluation,
    work_skill_enhancement,
    conduct_formal_review,
    consider_promotion_new_role,
    set_new_responsibilities,
    approve_promotion,
    transition_new_role
])

# Define the dependencies
root.order.add_edge(identify_dev_needs_career_aspirations, create_personal_dev_plan)
root.order.add_edge(create_personal_dev_plan, receive_feedback_evaluation)
root.order.add_edge(receive_feedback_evaluation, work_skill_enhancement)
root.order.add_edge(work_skill_enhancement, conduct_formal_review)
root.order.add_edge(conduct_formal_review, consider_promotion_new_role)
root.order.add_edge(consider_promotion_new_role, set_new_responsibilities)
root.order.add_edge(set_new_responsibilities, approve_promotion)
root.order.add_edge(approve_promotion, transition_new_role)

# Print the model
print(root)