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

concept_ideation_and_sponsor_alignment = OperatorPOWL(operator=Operator.XOR, children=[concept_ideation, sponsor_alignment])
participant_sign_up_and_team_formation = OperatorPOWL(operator=Operator.XOR, children=[participant_sign_up, team_formation])
workshop_setup_and_delivery = OperatorPOWL(operator=Operator.XOR, children=[workshop_setup, workshop_delivery])
progress_monitor_and_live_support = OperatorPOWL(operator=Operator.XOR, children=[progress_monitor, live_support])
feedback_loop_and_submission_check = OperatorPOWL(operator=Operator.XOR, children=[feedback_loop, submission_check])
plagiarism_scan_and_jury_evaluation = OperatorPOWL(operator=Operator.XOR, children=[plagiarism_scan, jury_evaluation])
result_compilation_and_winner_announcement = OperatorPOWL(operator=Operator.XOR, children=[result_compilation, winner_announcement])
post_analytics_and_skip = OperatorPOWL(operator=Operator.XOR, children=[post_analytics, skip])

root = StrictPartialOrder(nodes=[
    concept_ideation_and_sponsor_alignment,
    participant_sign_up_and_team_formation,
    workshop_setup_and_delivery,
    progress_monitor_and_live_support,
    feedback_loop_and_submission_check,
    plagiarism_scan_and_jury_evaluation,
    result_compilation_and_winner_announcement,
    post_analytics_and_skip
])

root.order.add_edge(concept_ideation_and_sponsor_alignment, participant_sign_up_and_team_formation)
root.order.add_edge(participant_sign_up_and_team_formation, workshop_setup_and_delivery)
root.order.add_edge(workshop_setup_and_delivery, progress_monitor_and_live_support)
root.order.add_edge(progress_monitor_and_live_support, feedback_loop_and_submission_check)
root.order.add_edge(feedback_loop_and_submission_check, plagiarism_scan_and_jury_evaluation)
root.order.add_edge(plagiarism_scan_and_jury_evaluation, result_compilation_and_winner_announcement)
root.order.add_edge(result_compilation_and_winner_announcement, post_analytics_and_skip)