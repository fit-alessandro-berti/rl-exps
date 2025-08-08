import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities with their respective labels
activities = {
    'Site Survey': Transition(label='Site Survey'),
    'Structural Audit': Transition(label='Structural Audit'),
    'Climate Design': Transition(label='Climate Design'),
    'Lighting Setup': Transition(label='Lighting Setup'),
    'Irrigation Plan': Transition(label='Irrigation Plan'),
    'Nutrient Mix': Transition(label='Nutrient Mix'),
    'Sensor Install': Transition(label='Sensor Install'),
    'AI Calibration': Transition(label='AI Calibration'),
    'Pest Scan': Transition(label='Pest Scan'),
    'Energy Audit': Transition(label='Energy Audit'),
    'Renewable Sync': Transition(label='Renewable Sync'),
    'Data Modeling': Transition(label='Data Modeling'),
    'Staff Briefing': Transition(label='Staff Briefing'),
    'Compliance Check': Transition(label='Compliance Check'),
    'Community Meet': Transition(label='Community Meet'),
    'Yield Review': Transition(label='Yield Review'),
    'Feedback Loop': Transition(label='Feedback Loop')
}

# Define the partial order graph
root = StrictPartialOrder(nodes=list(activities.values()))

# Define the dependencies between activities
root.order.add_edge(activities['Site Survey'], activities['Structural Audit'])
root.order.add_edge(activities['Structural Audit'], activities['Climate Design'])
root.order.add_edge(activities['Climate Design'], activities['Lighting Setup'])
root.order.add_edge(activities['Lighting Setup'], activities['Irrigation Plan'])
root.order.add_edge(activities['Irrigation Plan'], activities['Nutrient Mix'])
root.order.add_edge(activities['Nutrient Mix'], activities['Sensor Install'])
root.order.add_edge(activities['Sensor Install'], activities['AI Calibration'])
root.order.add_edge(activities['AI Calibration'], activities['Pest Scan'])
root.order.add_edge(activities['Pest Scan'], activities['Energy Audit'])
root.order.add_edge(activities['Energy Audit'], activities['Renewable Sync'])
root.order.add_edge(activities['Renewable Sync'], activities['Data Modeling'])
root.order.add_edge(activities['Data Modeling'], activities['Staff Briefing'])
root.order.add_edge(activities['Staff Briefing'], activities['Compliance Check'])
root.order.add_edge(activities['Compliance Check'], activities['Community Meet'])
root.order.add_edge(activities['Community Meet'], activities['Yield Review'])
root.order.add_edge(activities['Yield Review'], activities['Feedback Loop'])

# Print the final POWL model
print(root)