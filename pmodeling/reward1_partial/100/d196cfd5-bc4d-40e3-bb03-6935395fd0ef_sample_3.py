from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions
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

# Define silent transitions
skip = SilentTransition()

# Define loop nodes
team_formation_loop = OperatorPOWL(operator=Operator.LOOP, children=[team_formation, skip])
workshop_setup_loop = OperatorPOWL(operator=Operator.LOOP, children=[workshop_setup, skip])
submission_check_loop = OperatorPOWL(operator=Operator.LOOP, children=[submission_check, skip])
plagiarism_scan_loop = OperatorPOWL(operator=Operator.LOOP, children=[plagiarism_scan, skip])
jury_evaluation_loop = OperatorPOWL(operator=Operator.LOOP, children=[jury_evaluation, skip])
result_compilation_loop = OperatorPOWL(operator=Operator.LOOP, children=[result_compilation, skip])

# Define exclusive choice nodes
workshop_delivery_choice = OperatorPOWL(operator=Operator.XOR, children=[workshop_delivery, skip])

# Define root POWL model
root = StrictPartialOrder(
    nodes=[
        concept_ideation,
        sponsor_alignment,
        participant_signup,
        team_formation_loop,
        workshop_setup_loop,
        workshop_delivery_choice,
        progress_monitor,
        live_support,
        feedback_loop,
        submission_check_loop,
        plagiarism_scan_loop,
        jury_evaluation_loop,
        result_compilation_loop,
        winner_announcement,
        post_analytics
    ],
    order={
        team_formation: team_formation_loop,
        workshop_setup: workshop_setup_loop,
        submission_check: submission_check_loop,
        plagiarism_scan: plagiarism_scan_loop,
        jury_evaluation: jury_evaluation_loop,
        result_compilation: result_compilation_loop
    }
)

# Add edges
root.order.add_edge(concept_ideation, sponsor_alignment)
root.order.add_edge(sponsor_alignment, participant_signup)
root.order.add_edge(participant_signup, team_formation_loop)
root.order.add_edge(team_formation, team_formation_loop)
root.order.add_edge(workshop_setup, workshop_setup_loop)
root.order.add_edge(workshop_delivery, workshop_delivery_choice)
root.order.add_edge(progress_monitor, workshop_delivery_choice)
root.order.add_edge(live_support, workshop_delivery_choice)
root.order.add_edge(feedback_loop, workshop_delivery_choice)
root.order.add_edge(submission_check, submission_check_loop)
root.order.add_edge(plagiarism_scan, plagiarism_scan_loop)
root.order.add_edge(jury_evaluation, jury_evaluation_loop)
root.order.add_edge(result_compilation, result_compilation_loop)
root.order.add_edge(winner_announcement, post_analytics)
root.order.add_edge(post_analytics, winner_announcement)

print(root)