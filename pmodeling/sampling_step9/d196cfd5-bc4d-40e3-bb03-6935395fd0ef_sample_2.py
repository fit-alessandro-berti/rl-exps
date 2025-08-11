import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

concept_ideation = Transition(label='Concept Ideation')
sponsor_alignment = Transition(label='Sponsor Alignment')
participant_signup = Transition(label='Participant SignUp')
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

xor_1 = OperatorPOWL(operator=Operator.XOR, children=[team_formation, skip])
xor_2 = OperatorPOWL(operator=Operator.XOR, children=[workshop_delivery, skip])
xor_3 = OperatorPOWL(operator=Operator.XOR, children=[plagiarism_scan, skip])

loop_1 = OperatorPOWL(operator=Operator.LOOP, children=[xor_1, xor_2])
loop_2 = OperatorPOWL(operator=Operator.LOOP, children=[progress_monitor, live_support])
loop_3 = OperatorPOWL(operator=Operator.LOOP, children=[feedback_loop, xor_3])
loop_4 = OperatorPOWL(operator=Operator.LOOP, children=[jury_evaluation, result_compilation])

xor_4 = OperatorPOWL(operator=Operator.XOR, children=[loop_1, loop_2])
xor_5 = OperatorPOWL(operator=Operator.XOR, children=[loop_3, loop_4])
xor_6 = OperatorPOWL(operator=Operator.XOR, children=[loop_1, loop_2])

xor_7 = OperatorPOWL(operator=Operator.XOR, children=[xor_4, xor_5])
xor_8 = OperatorPOWL(operator=Operator.XOR, children=[xor_6, skip])

root = StrictPartialOrder(nodes=[xor_7, xor_8])
root.order.add_edge(xor_7, xor_8)