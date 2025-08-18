from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities as transitions
activities = {
    'Site Survey': Transition(label='Site Survey'),
    'Soil Testing': Transition(label='Soil Testing'),
    'Stakeholder Meet': Transition(label='Stakeholder Meet'),
    'Resource Plan': Transition(label='Resource Plan'),
    'Crop Selection': Transition(label='Crop Selection'),
    'Volunteer Sign-up': Transition(label='Volunteer Sign-up'),
    'Tech Setup': Transition(label='Tech Setup'),
    'Irrigation Check': Transition(label='Irrigation Check'),
    'Data Collection': Transition(label='Data Collection'),
    'Growth Monitoring': Transition(label='Growth Monitoring'),
    'Conflict Mediate': Transition(label='Conflict Mediate'),
    'Workshop Prep': Transition(label='Workshop Prep'),
    'Market Forecast': Transition(label='Market Forecast'),
    'Yield Analysis': Transition(label='Yield Analysis'),
    'Sustainability Audit': Transition(label='Sustainability Audit'),
    'Community Feedback': Transition(label='Community Feedback'),
    'Equipment Maintain': Transition(label='Equipment Maintain'),
    'Waste Manage': Transition(label='Waste Manage')
}

# Define the POWL model
root = StrictPartialOrder(nodes=activities.values())
root.order.add_edge(activities['Site Survey'], activities['Soil Testing'])
root.order.add_edge(activities['Site Survey'], activities['Stakeholder Meet'])
root.order.add_edge(activities['Soil Testing'], activities['Resource Plan'])
root.order.add_edge(activities['Resource Plan'], activities['Crop Selection'])
root.order.add_edge(activities['Crop Selection'], activities['Volunteer Sign-up'])
root.order.add_edge(activities['Volunteer Sign-up'], activities['Tech Setup'])
root.order.add_edge(activities['Tech Setup'], activities['Irrigation Check'])
root.order.add_edge(activities['Irrigation Check'], activities['Data Collection'])
root.order.add_edge(activities['Data Collection'], activities['Growth Monitoring'])
root.order.add_edge(activities['Growth Monitoring'], activities['Conflict Mediate'])
root.order.add_edge(activities['Conflict Mediate'], activities['Workshop Prep'])
root.order.add_edge(activities['Workshop Prep'], activities['Market Forecast'])
root.order.add_edge(activities['Market Forecast'], activities['Yield Analysis'])
root.order.add_edge(activities['Yield Analysis'], activities['Sustainability Audit'])
root.order.add_edge(activities['Sustainability Audit'], activities['Community Feedback'])
root.order.add_edge(activities['Community Feedback'], activities['Equipment Maintain'])
root.order.add_edge(activities['Equipment Maintain'], activities['Waste Manage'])

print(root)