from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
activities = {
    'Site Survey': Transition(label='Site Survey'),
    'Structural Check': Transition(label='Structural Check'),
    'Resource Sourcing': Transition(label='Resource Sourcing'),
    'System Install': Transition(label='System Install'),
    'Lighting Setup': Transition(label='Lighting Setup'),
    'Irrigation Setup': Transition(label='Irrigation Setup'),
    'Stakeholder Meet': Transition(label='Stakeholder Meet'),
    'Volunteer Train': Transition(label='Volunteer Train'),
    'Regulation Review': Transition(label='Regulation Review'),
    'Crop Selection': Transition(label='Crop Selection'),
    'Planting Phase': Transition(label='Planting Phase'),
    'Climate Control': Transition(label='Climate Control'),
    'Growth Monitor': Transition(label='Growth Monitor'),
    'Data Logging': Transition(label='Data Logging'),
    'Harvest Event': Transition(label='Harvest Event'),
    'Waste Manage': Transition(label='Waste Manage'),
    'Feedback Collect': Transition(label='Feedback Collect')
}

# Define the POWL model
root = StrictPartialOrder()

# Define the dependencies
dependencies = {
    'Site Survey': ['Structural Check', 'Resource Sourcing'],
    'Structural Check': ['System Install'],
    'Resource Sourcing': ['System Install'],
    'System Install': ['Lighting Setup', 'Irrigation Setup'],
    'Lighting Setup': ['Stakeholder Meet'],
    'Irrigation Setup': ['Stakeholder Meet'],
    'Stakeholder Meet': ['Volunteer Train'],
    'Volunteer Train': ['Regulation Review'],
    'Regulation Review': ['Crop Selection'],
    'Crop Selection': ['Planting Phase'],
    'Planting Phase': ['Climate Control', 'Growth Monitor'],
    'Climate Control': ['Growth Monitor'],
    'Growth Monitor': ['Data Logging'],
    'Data Logging': ['Harvest Event'],
    'Harvest Event': ['Waste Manage', 'Feedback Collect']
}

# Add activities to the POWL model
for activity in activities.values():
    root.add_activity(activity)

# Add dependencies to the POWL model
for activity, dependencies in dependencies.items():
    for dependency in dependencies:
        root.add_dependency(activities[activity], activities[dependency])

# Print the POWL model
print(root)