import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
identify = Transition(label='Identify development needs or career aspirations')
create_plan = Transition(label='Create personal development plan')
work_enhance = Transition(label='Work on skill enhancement')
receive_feedback = Transition(label='Receive feedback and evaluation from supervisors')
set_responsibilities = Transition(label='Set new responsibilities')
approve_promotion = Transition(label='Approve promotion')
conduct_review = Transition(label='Conducts formal performance review')
consider_promotion = Transition(label='Consider employee for promotion or new role')
adjust_compensation = Transition(label='Adjust compensation')
transition_role = Transition(label='Transition into new role')

# Define the partial order
root = StrictPartialOrder(nodes=[identify, create_plan, work_enhance, receive_feedback, set_responsibilities, approve_promotion, conduct_review, consider_promotion, adjust_compensation, transition_role])

# Define the partial order dependencies
root.order.add_edge(identify, create_plan)
root.order.add_edge(create_plan, work_enhance)
root.order.add_edge(work_enhance, receive_feedback)
root.order.add_edge(receive_feedback, set_responsibilities)
root.order.add_edge(set_responsibilities, approve_promotion)
root.order.add_edge(approve_promotion, conduct_review)
root.order.add_edge(conduct_review, consider_promotion)
root.order.add_edge(consider_promotion, adjust_compensation)
root.order.add_edge(adjust_compensation, transition_role)

# Print the root POWL model
print(root)