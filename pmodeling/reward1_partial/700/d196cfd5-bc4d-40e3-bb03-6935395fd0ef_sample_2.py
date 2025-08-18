import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL nodes (activities)
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

# Define the operators for choice and loop structures
xor = OperatorPOWL(operator=Operator.XOR, children=[workshop_setup, workshop_delivery])
loop = OperatorPOWL(operator=Operator.LOOP, children=[progress_monitor, live_support, feedback_loop, submission_check, plagiarism_scan, jury_evaluation, result_compilation, winner_announcement, post_analytics])

# Define the partial order and add the nodes and dependencies
root = StrictPartialOrder(nodes=[concept_ideation, sponsor_alignment, participant_sign_up, team_formation, xor, loop])
root.order.add_edge(concept_ideation, sponsor_alignment)
root.order.add_edge(sponsor_alignment, participant_sign_up)
root.order.add_edge(participant_sign_up, team_formation)
root.order.add_edge(team_formation, xor)
root.order.add_edge(xor, loop)