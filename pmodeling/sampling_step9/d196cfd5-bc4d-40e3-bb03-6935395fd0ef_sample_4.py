import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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

skip = SilentTransition()

loop_concept = OperatorPOWL(operator=Operator.LOOP, children=[concept_ideation, sponsor_alignment])
loop_participant = OperatorPOWL(operator=Operator.LOOP, children=[participant_sign_up, team_formation])
loop_workshop = OperatorPOWL(operator=Operator.LOOP, children=[workshop_setup, workshop_delivery])
loop_progress = OperatorPOWL(operator=Operator.LOOP, children=[progress_monitor, live_support, feedback_loop])
loop_submission = OperatorPOWL(operator=Operator.LOOP, children=[submission_check, plagiarism_scan, jury_evaluation, result_compilation])
loop_winner = OperatorPOWL(operator=Operator.LOOP, children=[winner_announcement, post_analytics])

xor_concept = OperatorPOWL(operator=Operator.XOR, children=[loop_concept, skip])
xor_participant = OperatorPOWL(operator=Operator.XOR, children=[loop_participant, skip])
xor_workshop = OperatorPOWL(operator=Operator.XOR, children=[loop_workshop, skip])
xor_progress = OperatorPOWL(operator=Operator.XOR, children=[loop_progress, skip])
xor_submission = OperatorPOWL(operator=Operator.XOR, children=[loop_submission, skip])
xor_winner = OperatorPOWL(operator=Operator.XOR, children=[loop_winner, skip])

root = StrictPartialOrder(nodes=[xor_concept, xor_participant, xor_workshop, xor_progress, xor_submission, xor_winner])
root.order.add_edge(xor_concept, xor_participant)
root.order.add_edge(xor_participant, xor_workshop)
root.order.add_edge(xor_workshop, xor_progress)
root.order.add_edge(xor_progress, xor_submission)
root.order.add_edge(xor_submission, xor_winner)

print(root)