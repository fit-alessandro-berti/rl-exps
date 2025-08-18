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

# Define silent transitions for concurrent activities
skip = SilentTransition()

# Define the POWL model
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[workshop_setup, workshop_delivery])
xor1 = OperatorPOWL(operator=Operator.XOR, children=[plagiarism_scan, skip])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[feedback_loop, skip])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[progress_monitor, skip])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[live_support, skip])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[jury_evaluation, skip])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[result_compilation, skip])
xor7 = OperatorPOWL(operator=Operator.XOR, children=[winner_announcement, skip])
xor8 = OperatorPOWL(operator=Operator.XOR, children=[post_analytics, skip])

root = StrictPartialOrder(nodes=[concept_ideation, sponsor_alignment, participant_sign_up, team_formation, loop1, xor1, xor2, xor3, xor4, xor5, xor6, xor7, xor8])
root.order.add_edge(concept_ideation, sponsor_alignment)
root.order.add_edge(sponsor_alignment, participant_sign_up)
root.order.add_edge(participant_sign_up, team_formation)
root.order.add_edge(team_formation, loop1)
root.order.add_edge(loop1, xor1)
root.order.add_edge(xor1, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, xor5)
root.order.add_edge(xor5, xor6)
root.order.add_edge(xor6, xor7)
root.order.add_edge(xor7, xor8)