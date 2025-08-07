import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator
from pm4py.algo.conformance.tokenreplay import algorithm as token_replay

# Define the activities
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

# Define the partial order
root = StrictPartialOrder(nodes=list(activities.values()))

# Define the edges for the partial order
root.order.add_edge(activities['Site Survey'], activities['Soil Testing'])
root.order.add_edge(activities['Site Survey'], activities['Stakeholder Meet'])
root.order.add_edge(activities['Site Survey'], activities['Resource Plan'])
root.order.add_edge(activities['Site Survey'], activities['Crop Selection'])
root.order.add_edge(activities['Soil Testing'], activities['Resource Plan'])
root.order.add_edge(activities['Soil Testing'], activities['Crop Selection'])
root.order.add_edge(activities['Soil Testing'], activities['Volunteer Sign-up'])
root.order.add_edge(activities['Stakeholder Meet'], activities['Resource Plan'])
root.order.add_edge(activities['Stakeholder Meet'], activities['Crop Selection'])
root.order.add_edge(activities['Stakeholder Meet'], activities['Volunteer Sign-up'])
root.order.add_edge(activities['Resource Plan'], activities['Crop Selection'])
root.order.add_edge(activities['Resource Plan'], activities['Volunteer Sign-up'])
root.order.add_edge(activities['Crop Selection'], activities['Volunteer Sign-up'])
root.order.add_edge(activities['Volunteer Sign-up'], activities['Tech Setup'])
root.order.add_edge(activities['Volunteer Sign-up'], activities['Irrigation Check'])
root.order.add_edge(activities['Volunteer Sign-up'], activities['Data Collection'])
root.order.add_edge(activities['Volunteer Sign-up'], activities['Growth Monitoring'])
root.order.add_edge(activities['Tech Setup'], activities['Irrigation Check'])
root.order.add_edge(activities['Tech Setup'], activities['Data Collection'])
root.order.add_edge(activities['Tech Setup'], activities['Growth Monitoring'])
root.order.add_edge(activities['Irrigation Check'], activities['Data Collection'])
root.order.add_edge(activities['Irrigation Check'], activities['Growth Monitoring'])
root.order.add_edge(activities['Data Collection'], activities['Growth Monitoring'])
root.order.add_edge(activities['Growth Monitoring'], activities['Conflict Mediate'])
root.order.add_edge(activities['Growth Monitoring'], activities['Workshop Prep'])
root.order.add_edge(activities['Growth Monitoring'], activities['Market Forecast'])
root.order.add_edge(activities['Growth Monitoring'], activities['Yield Analysis'])
root.order.add_edge(activities['Conflict Mediate'], activities['Workshop Prep'])
root.order.add_edge(activities['Conflict Mediate'], activities['Market Forecast'])
root.order.add_edge(activities['Conflict Mediate'], activities['Yield Analysis'])
root.order.add_edge(activities['Workshop Prep'], activities['Market Forecast'])
root.order.add_edge(activities['Workshop Prep'], activities['Yield Analysis'])
root.order.add_edge(activities['Market Forecast'], activities['Yield Analysis'])
root.order.add_edge(activities['Yield Analysis'], activities['Sustainability Audit'])
root.order.add_edge(activities['Yield Analysis'], activities['Community Feedback'])
root.order.add_edge(activities['Yield Analysis'], activities['Equipment Maintain'])
root.order.add_edge(activities['Yield Analysis'], activities['Waste Manage'])
root.order.add_edge(activities['Sustainability Audit'], activities['Community Feedback'])
root.order.add_edge(activities['Sustainability Audit'], activities['Equipment Maintain'])
root.order.add_edge(activities['Sustainability Audit'], activities['Waste Manage'])
root.order.add_edge(activities['Community Feedback'], activities['Equipment Maintain'])
root.order.add_edge(activities['Community Feedback'], activities['Waste Manage'])
root.order.add_edge(activities['Equipment Maintain'], activities['Waste Manage'])

# Define the exclusive choice
exclusive_choice = OperatorPOWL(operator=Operator.XOR, children=list(activities.values()))

# Define the final loop
loop = OperatorPOWL(operator=Operator.LOOP, children=[exclusive_choice])

# Define the final partial order
root = StrictPartialOrder(nodes=[loop])
root.order.add_edge(loop, exclusive_choice)

# Print the final POWL model
print(root)