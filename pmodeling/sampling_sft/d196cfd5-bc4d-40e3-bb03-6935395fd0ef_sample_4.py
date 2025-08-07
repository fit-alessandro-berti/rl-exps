import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
concept = Transition(label='Concept Ideation')
sponsor = Transition(label='Sponsor Alignment')
sign_up = Transition(label='Participant SignUp')
team = Transition(label='Team Formation')
workshop_setup = Transition(label='Workshop Setup')
workshop_delivery = Transition(label='Workshop Delivery')
progress = Transition(label='Progress Monitor')
live = Transition(label='Live Support')
feedback = Transition(label='Feedback Loop')
submission = Transition(label='Submission Check')
plagiarism = Transition(label='Plagiarism Scan')
jury = Transition(label='Jury Evaluation')
result = Transition(label='Result Compilation')
announcement = Transition(label='Winner Announcement')
post = Transition(label='Post Analytics')

# Loop for continuous monitoring and support
monitor_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[progress, live]
)

# Build the partial order
root = StrictPartialOrder(nodes=[
    concept, sponsor, sign_up, team, workshop_setup,
    workshop_delivery, monitor_loop,
    submission, plagiarism, jury,
    result, announcement, post
])

# Define the control-flow dependencies
root.order.add_edge(concept, sponsor)
root.order.add_edge(sponsor, sign_up)
root.order.add_edge(sign_up, team)
root.order.add_edge(team, workshop_setup)
root.order.add_edge(workshop_setup, workshop_delivery)
root.order.add_edge(workshop_delivery, monitor_loop)
root.order.add_edge(monitor_loop, submission)
root.order.add_edge(submission, plagiarism)
root.order.add_edge(plagiarism, jury)
root.order.add_edge(jury, result)
root.order.add_edge(result, announcement)
root.order.add_edge(announcement, post)