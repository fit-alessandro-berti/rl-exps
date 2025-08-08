import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

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

# Define the loop for participant registration and team formation
participant_registration_loop = OperatorPOWL(operator=Operator.LOOP, children=[participant_sign_up, team_formation])

# Define the XOR for workshop setup and delivery
workshop_setup_xor = OperatorPOWL(operator=Operator.XOR, children=[workshop_setup, SilentTransition()])

# Define the POWL model
root = StrictPartialOrder(nodes=[concept_ideation, sponsor_alignment, participant_registration_loop, workshop_setup_xor, progress_monitor, live_support, feedback_loop, submission_check, plagiarism_scan, jury_evaluation, result_compilation, winner_announcement, post_analytics])
root.order.add_edge(concept_ideation, sponsor_alignment)
root.order.add_edge(sponsor_alignment, participant_registration_loop)
root.order.add_edge(participant_registration_loop, workshop_setup_xor)
root.order.add_edge(workshop_setup_xor, progress_monitor)
root.order.add_edge(progress_monitor, live_support)
root.order.add_edge(live_support, feedback_loop)
root.order.add_edge(feedback_loop, submission_check)
root.order.add_edge(submission_check, plagiarism_scan)
root.order.add_edge(plagiarism_scan, jury_evaluation)
root.order.add_edge(jury_evaluation, result_compilation)
root.order.add_edge(result_compilation, winner_announcement)
root.order.add_edge(winner_announcement, post_analytics)