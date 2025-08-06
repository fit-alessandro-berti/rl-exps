import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
concept_ideation = Transition(label='Concept Ideation')
sponsor_alignment = Transition(label='Sponsor Alignment')
participant_sign_up = Transition(label='Participant SignUp')
team_formation = Transition(label='Team Formation')
workshop_setup = Transition(label='Workshop Setup')
workshop_delivery = Transition(label='Workshop Delivery')
progress_monitor = Transition(label='Progress Monitor')
live_support = Transition(label='Live Support')
feedback_loop = Transition(label='Feedback Loop')
submission_check = Transition(label='Submission Check')
plagiarism_scan = Transition(label='Plagiarism Scan')
jury_evaluation = Transition(label='Jury Evaluation')
result_compilation = Transition(label='Result Compilation')
winner_announcement = Transition(label='Winner Announcement')
post_analytics = Transition(label='Post Analytics')

# Define silent transitions
skip = SilentTransition()

# Define loops and choices
workshop_loop = OperatorPOWL(operator=Operator.LOOP, children=[workshop_setup, workshop_delivery, progress_monitor, live_support, feedback_loop])
plagiarism_loop = OperatorPOWL(operator=Operator.LOOP, children=[submission_check, plagiarism_scan])
jury_evaluation_loop = OperatorPOWL(operator=Operator.LOOP, children=[jury_evaluation, result_compilation, post_analytics])
sponsor_loop = OperatorPOWL(operator=Operator.LOOP, children=[sponsor_alignment, team_formation])

# Define partial order
root = StrictPartialOrder(nodes=[sponsor_loop, workshop_loop, plagiarism_loop, jury_evaluation_loop, winner_announcement])
root.order.add_edge(sponsor_loop, workshop_loop)
root.order.add_edge(workshop_loop, plagiarism_loop)
root.order.add_edge(plagiarism_loop, jury_evaluation_loop)
root.order.add_edge(jury_evaluation_loop, winner_announcement)