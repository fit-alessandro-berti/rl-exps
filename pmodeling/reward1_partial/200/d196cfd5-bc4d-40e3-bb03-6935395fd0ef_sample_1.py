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

concept_ideation_choice = OperatorPOWL(operator=Operator.XOR, children=[sponsor_alignment, concept_ideation])
participant_sign_up_choice = OperatorPOWL(operator=Operator.XOR, children=[team_formation, participant_sign_up])
workshop_setup_choice = OperatorPOWL(operator=Operator.XOR, children=[workshop_delivery, workshop_setup])
progress_monitor_choice = OperatorPOWL(operator=Operator.XOR, children=[feedback_loop, progress_monitor])
submission_check_choice = OperatorPOWL(operator=Operator.XOR, children=[plagiarism_scan, submission_check])
jury_evaluation_choice = OperatorPOWL(operator=Operator.XOR, children=[result_compilation, jury_evaluation])
winner_announcement_choice = OperatorPOWL(operator=Operator.XOR, children=[post_analytics, winner_announcement])

root = StrictPartialOrder(nodes=[
    concept_ideation_choice,
    participant_sign_up_choice,
    workshop_setup_choice,
    progress_monitor_choice,
    submission_check_choice,
    jury_evaluation_choice,
    winner_announcement_choice
])
root.order.add_edge(concept_ideation_choice, participant_sign_up_choice)
root.order.add_edge(participant_sign_up_choice, workshop_setup_choice)
root.order.add_edge(workshop_setup_choice, progress_monitor_choice)
root.order.add_edge(progress_monitor_choice, submission_check_choice)
root.order.add_edge(submission_check_choice, jury_evaluation_choice)
root.order.add_edge(jury_evaluation_choice, winner_announcement_choice)
root.order.add_edge(winner_announcement_choice, post_analytics)