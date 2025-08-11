import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
identify_development_needs = Transition(label='Identify development needs or career aspirations')
create_plan = Transition(label='Create personal development plan')
work_on_skill_enhancement = Transition(label='Work on skill enhancement')
receive_feedback_evaluation = Transition(label='Receive feedback and evaluation from supervisors')
set_responsibilities = Transition(label='Set new responsibilities')
consider_promotion = Transition(label='Consider employee for promotion or new role')
conduct_performance_review = Transition(label='Conducts formal performance review')
approve_promotion = Transition(label='Approve promotion')
adjust_compensation = Transition(label='Adjust compensation')
transition_new_role = Transition(label='Transition into new role')

# Define the partial order
root = StrictPartialOrder(nodes=[identify_development_needs, create_plan, work_on_skill_enhancement, receive_feedback_evaluation, set_responsibilities, consider_promotion, conduct_performance_review, approve_promotion, adjust_compensation, transition_new_role])

# Define the dependencies
root.order.add_edge(identify_development_needs, create_plan)
root.order.add_edge(create_plan, work_on_skill_enhancement)
root.order.add_edge(work_on_skill_enhancement, receive_feedback_evaluation)
root.order.add_edge(receive_feedback_evaluation, set_responsibilities)
root.order.add_edge(set_responsibilities, consider_promotion)
root.order.add_edge(consider_promotion, conduct_performance_review)
root.order.add_edge(conduct_performance_review, approve_promotion)
root.order.add_edge(approve_promotion, adjust_compensation)
root.order.add_edge(adjust_compensation, transition_new_role)

# Print the result
print(root)