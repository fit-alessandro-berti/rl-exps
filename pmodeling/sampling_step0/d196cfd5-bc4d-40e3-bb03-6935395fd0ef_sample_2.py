import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
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

# Define the transitions
xor1 = OperatorPOWL(operator=Operator.XOR, children=[sponsor_alignment, concept_ideation])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[participant_sign_up, xor1])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[team_formation, xor2])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[workshop_setup, xor3])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[workshop_delivery, xor4])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[progress_monitor, xor5])
xor7 = OperatorPOWL(operator=Operator.XOR, children=[live_support, xor6])
xor8 = OperatorPOWL(operator=Operator.XOR, children=[feedback_loop, xor7])
xor9 = OperatorPOWL(operator=Operator.XOR, children=[submission_check, xor8])
xor10 = OperatorPOWL(operator=Operator.XOR, children=[plagiarism_scan, xor9])
xor11 = OperatorPOWL(operator=Operator.XOR, children=[jury_evaluation, xor10])
xor12 = OperatorPOWL(operator=Operator.XOR, children=[result_compilation, xor11])
xor13 = OperatorPOWL(operator=Operator.XOR, children=[winner_announcement, xor12])
xor14 = OperatorPOWL(operator=Operator.XOR, children=[post_analytics, xor13])

# Define the POWL model
root = StrictPartialOrder(nodes=[xor14, xor13, xor12, xor11, xor10, xor9, xor8, xor7, xor6, xor5, xor4, xor3, xor2, xor1, concept_ideation, sponsor_alignment, participant_sign_up, team_formation, workshop_setup, workshop_delivery, progress_monitor, live_support, feedback_loop, submission_check, plagiarism_scan, jury_evaluation, result_compilation, winner_announcement, post_analytics])