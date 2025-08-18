from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
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

# Define loop for the hackathon
hackathon_loop = OperatorPOWL(operator=Operator.LOOP, children=[
    progress_monitor,
    live_support,
    feedback_loop,
    submission_check,
    plagiarism_scan,
    jury_evaluation,
    result_compilation
])

# Define exclusive choice for the process flow
exclusive_choice = OperatorPOWL(operator=Operator.XOR, children=[
    participant_signup,
    team_formation,
    workshop_setup,
    workshop_delivery,
    hackathon_loop,
    winner_announcement,
    post_analytics
])

# Create the root model
root = StrictPartialOrder(nodes=[
    concept_ideation,
    sponsor_alignment,
    exclusive_choice
])

# Add edges to the partial order
root.order.add_edge(concept_ideation, sponsor_alignment)
root.order.add_edge(sponsor_alignment, exclusive_choice)

# Print the root model
print(root)