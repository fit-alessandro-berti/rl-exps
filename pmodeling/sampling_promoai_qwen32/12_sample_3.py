import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities)
Identify = Transition(label='Identify development needs or career aspirations')
Create = Transition(label='Create personal development plan')
Work = Transition(label='Work on skill enhancement')
Feedback = Transition(label='Receive feedback and evaluation from supervisors')
Consider = Transition(label='Consider employee for promotion or new role')
Review = Transition(label='Conducts formal performance review')
Approve = Transition(label='Approve promotion')
Set = Transition(label='Set new responsibilities')
Adjust = Transition(label='Adjust compensation')
Transition = Transition(label='Transition into new role')

# Define the POWL model
root = StrictPartialOrder(nodes=[Identify, Create, Work, Feedback, Consider, Review, Approve, Set, Adjust, Transition])
root.order.add_edge(Identify, Create)
root.order.add_edge(Create, Work)
root.order.add_edge(Work, Feedback)
root.order.add_edge(Feedback, Consider)
root.order.add_edge(Consider, Review)
root.order.add_edge(Review, Approve)
root.order.add_edge(Approve, Set)
root.order.add_edge(Set, Adjust)
root.order.add_edge(Adjust, Transition)