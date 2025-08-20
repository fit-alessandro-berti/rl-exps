import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

Identify_development_needs_or_career_aspirations = Transition(label='Identify development needs or career aspirations')
Create_personal_development_plan = Transition(label='Create personal development plan')
Work_on_skill_enhancement = Transition(label='Work on skill enhancement')
Receive_feedback_and_evaluation_from_supervisors = Transition(label='Receive feedback and evaluation from supervisors')
Consider_employee_for_promotion_or_new_role = Transition(label='Consider employee for promotion or new role')
Conducts_formal_performance_review = Transition(label='Conducts formal performance review')
Approve_promotion = Transition(label='Approve promotion')
Set_new_responsibilities = Transition(label='Set new responsibilities')
Adjust_compensation = Transition(label='Adjust compensation')
Transition_into_new_role = Transition(label='Transition into new role')

# Create a loop for work on skill enhancement, receive feedback, and consider for promotion
loop = OperatorPOWL(operator=Operator.LOOP, children=[Work_on_skill_enhancement, Receive_feedback_and_evaluation_from_supervisors, Consider_employee_for_promotion_or_new_role])

# Create an XOR for approval of promotion and setting new responsibilities
xor = OperatorPOWL(operator=Operator.XOR, children=[Approve_promotion, Set_new_responsibilities])

# Create a strict partial order
root = StrictPartialOrder(nodes=[Identify_development_needs_or_career_aspirations, Create_personal_development_plan, loop, xor, Conducts_formal_performance_review, Adjust_compensation, Transition_into_new_role])

# Add edges to represent the partial order
root.order.add_edge(Identify_development_needs_or_career_aspirations, Create_personal_development_plan)
root.order.add_edge(Create_personal_development_plan, loop)
root.order.add_edge(loop, Conducts_formal_performance_review)
root.order.add_edge(Conducts_formal_performance_review, xor)
root.order.add_edge(xor, Adjust_compensation)
root.order.add_edge(Adjust_compensation, Transition_into_new_role)