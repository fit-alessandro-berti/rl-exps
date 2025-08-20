import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
identify_needs = Transition(label='Identify development needs or career aspirations')
create_plan = Transition(label='Create personal development plan')
work_on_skills = Transition(label='Work on skill enhancement')
feedback_evaluation = Transition(label='Receive feedback and evaluation from supervisors')
consider_promotion = Transition(label='Consider employee for promotion or new role')
formal_review = Transition(label='Conducts formal performance review')
approve_promotion = Transition(label='Approve promotion')
adjust_compensation = Transition(label='Adjust compensation')
set_new_responsibilities = Transition(label='Set new responsibilities')
transition_new_role = Transition(label='Transition into new role')

# Define edges
edges = [
    (identify_needs, create_plan),
    (create_plan, work_on_skills),
    (work_on_skills, feedback_evaluation),
    (feedback_evaluation, consider_promotion),
    (consider_promotion, formal_review),
    (formal_review, approve_promotion),
    (approve_promotion, adjust_compensation),
    (adjust_compensation, set_new_responsibilities),
    (set_new_responsibilities, transition_new_role)
]

# Create StrictPartialOrder
root = StrictPartialOrder(nodes=[identify_needs, create_plan, work_on_skills, feedback_evaluation, consider_promotion, formal_review, approve_promotion, adjust_compensation, set_new_responsibilities, transition_new_role])

# Add edges to order
for edge in edges:
    root.order.add_edge(*edge)