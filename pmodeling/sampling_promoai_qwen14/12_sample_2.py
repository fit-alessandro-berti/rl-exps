import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
Identify = Transition(label='Identify development needs or career aspirations')
CreatePlan = Transition(label='Create personal development plan')
WorkEnhance = Transition(label='Work on skill enhancement')
Feedback = Transition(label='Receive feedback and evaluation from supervisors')
Consider = Transition(label='Consider employee for promotion or new role')
Review = Transition(label='Conducts formal performance review')
Approve = Transition(label='Approve promotion')
AdjustCompensation = Transition(label='Adjust compensation')
SetResponsibilities = Transition(label='Set new responsibilities')
TransitionRole = Transition(label='Transition into new role')

# Define the loop for the continuous feedback and evaluation
Loop = OperatorPOWL(operator=Operator.LOOP, children=[WorkEnhance, Feedback])

# Define the sequence of activities leading to the promotion
Sequence = StrictPartialOrder(nodes=[CreatePlan, Loop, Consider, Review, Approve, AdjustCompensation, SetResponsibilities, TransitionRole])

# Define the XOR choice for the promotion process
XOR = OperatorPOWL(operator=Operator.XOR, children=[Sequence])

# Define the root POWL model
root = StrictPartialOrder(nodes=[Identify, XOR])
root.order.add_edge(Identify, XOR)