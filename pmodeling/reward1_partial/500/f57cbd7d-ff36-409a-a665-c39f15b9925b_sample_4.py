from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define the activities
activities = {
    'Trend Scan': Transition(label='Trend Scan'),
    'Idea Sprint': Transition(label='Idea Sprint'),
    'Feasibility Check': Transition(label='Feasibility Check'),
    'Risk Review': Transition(label='Risk Review'),
    'Tech Prototype': Transition(label='Tech Prototype'),
    'Market Simulate': Transition(label='Market Simulate'),
    'Stakeholder Align': Transition(label='Stakeholder Align'),
    'Budget Adjust': Transition(label='Budget Adjust'),
    'Talent Source': Transition(label='Talent Source'),
    'Pilot Launch': Transition(label='Pilot Launch'),
    'Data Refine': Transition(label='Data Refine'),
    'Scale Analysis': Transition(label='Scale Analysis'),
    'Integration Plan': Transition(label='Integration Plan'),
    'Change Manage': Transition(label='Change Manage'),
    'Knowledge Transfer': Transition(label='Knowledge Transfer')
}

# Define the partial order
root = StrictPartialOrder(nodes=list(activities.values()))

# Add dependencies
root.order.add_edge(activities['Trend Scan'], activities['Idea Sprint'])
root.order.add_edge(activities['Idea Sprint'], activities['Feasibility Check'])
root.order.add_edge(activities['Feasibility Check'], activities['Risk Review'])
root.order.add_edge(activities['Risk Review'], activities['Tech Prototype'])
root.order.add_edge(activities['Tech Prototype'], activities['Market Simulate'])
root.order.add_edge(activities['Market Simulate'], activities['Stakeholder Align'])
root.order.add_edge(activities['Stakeholder Align'], activities['Budget Adjust'])
root.order.add_edge(activities['Budget Adjust'], activities['Talent Source'])
root.order.add_edge(activities['Talent Source'], activities['Pilot Launch'])
root.order.add_edge(activities['Pilot Launch'], activities['Data Refine'])
root.order.add_edge(activities['Data Refine'], activities['Scale Analysis'])
root.order.add_edge(activities['Scale Analysis'], activities['Integration Plan'])
root.order.add_edge(activities['Integration Plan'], activities['Change Manage'])
root.order.add_edge(activities['Change Manage'], activities['Knowledge Transfer'])

print(root)