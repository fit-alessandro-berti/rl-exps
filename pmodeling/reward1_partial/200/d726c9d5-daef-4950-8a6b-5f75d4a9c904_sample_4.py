from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define activities
activities = ['Site Survey', 'Structure Check', 'Soil Sample', 'Water Test', 'Crop Selection', 'Material Order', 'Planter Setup', 'Irrigation Install', 'Sensor Deploy', 'Solar Setup', 'Data Integration', 'Community Meet', 'Training Session', 'Yield Monitor', 'Adjust Plan']

# Define transitions
transitions = [Transition(label=activity) for activity in activities]

# Define the POWL model
root = StrictPartialOrder(nodes=transitions)

# Define the dependencies between activities
dependencies = {
    'Site Survey': ['Structure Check', 'Soil Sample', 'Water Test'],
    'Structure Check': ['Crop Selection'],
    'Soil Sample': ['Crop Selection'],
    'Water Test': ['Crop Selection'],
    'Crop Selection': ['Material Order'],
    'Material Order': ['Planter Setup'],
    'Planter Setup': ['Irrigation Install'],
    'Irrigation Install': ['Sensor Deploy'],
    'Sensor Deploy': ['Solar Setup'],
    'Solar Setup': ['Data Integration'],
    'Data Integration': ['Community Meet'],
    'Community Meet': ['Training Session'],
    'Training Session': ['Yield Monitor'],
    'Yield Monitor': ['Adjust Plan']
}

# Add dependencies to the POWL model
for source, targets in dependencies.items():
    for target in targets:
        root.order.add_edge(transitions[activities.index(source)], transitions[activities.index(target)])

root