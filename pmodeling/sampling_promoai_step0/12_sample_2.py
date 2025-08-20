import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
adjust_compensation = Transition(label='Adjust compensation')
approve_promotion = Transition(label='Approve promotion')
conduct_performance_review = Transition(label='Conducts formal performance review')
consider_promotion_new_role = Transition(label='Consider employee for promotion or new role')
create_personal_dev_plan = Transition(label='Create personal development plan')
identify_development_needs = Transition(label='Identify development needs or career aspirations')
receive_feedback_evaluation = Transition(label='Receive feedback and evaluation from supervisors')
set_new_responsibilities = Transition(label='Set new responsibilities')
transition_new_role = Transition(label='Transition into new role')
work_on_skill_enhancement = Transition(label='Work on skill enhancement')

# Define the silent transitions
skip = SilentTransition()

# Define the loop node for skill enhancement
loop = OperatorPOWL(operator=Operator.LOOP, children=[work_on_skill_enhancement])

# Define the exclusive choice node for promotion or new role
xor = OperatorPOWL(operator=Operator.XOR, children=[consider_promotion_new_role, skip])

# Define the root POWL model
root = StrictPartialOrder(nodes=[create_personal_dev_plan, adjust_compensation, approve_promotion, conduct_performance_review, set_new_responsibilities, transition_new_role, loop, xor])
root.order.add_edge(create_personal_dev_plan, identify_development_needs)
root.order.add_edge(identify_development_needs, receive_feedback_evaluation)
root.order.add_edge(receive_feedback_evaluation, set_new_responsibilities)
root.order.add_edge(set_new_responsibilities, conduct_performance_review)
root.order.add_edge(conduct_performance_review, consider_promotion_new_role)
root.order.add_edge(consider_promotion_new_role, approve_promotion)
root.order.add_edge(approve_promotion, adjust_compensation)
root.order.add_edge(adjust_compensation, transition_new_role)
root.order.add_edge(loop, xor)
root.order.add_edge(xor, consider_promotion_new_role)