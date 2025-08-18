from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define the activities
activities = {
    'Trend Scan': Transition(label='Trend Scan'),
    'Opportunity Map': Transition(label='Opportunity Map'),
    'Expert Gather': Transition(label='Expert Gather'),
    'Idea Sprint': Transition(label='Idea Sprint'),
    'Proto Build': Transition(label='Proto Build'),
    'User Feedback': Transition(label='User Feedback'),
    'Risk Review': Transition(label='Risk Review'),
    'IP Audit': Transition(label='IP Audit'),
    'Pilot Launch': Transition(label='Pilot Launch'),
    'Stakeholder Meet': Transition(label='Stakeholder Meet'),
    'Resource Shift': Transition(label='Resource Shift'),
    'Scale Up': Transition(label='Scale Up'),
    'Impact Assess': Transition(label='Impact Assess'),
    'Knowledge Share': Transition(label='Knowledge Share'),
    'Monitor Trends': Transition(label='Monitor Trends')
}

# Define the operators and their order
operators = [
    OperatorPOWL(operator=Operator.LOOP, children=[activities['Trend Scan'], activities['Opportunity Map']]),
    OperatorPOWL(operator=Operator.XOR, children=[activities['Expert Gather'], activities['Idea Sprint']]),
    OperatorPOWL(operator=Operator.XOR, children=[activities['Proto Build'], activities['User Feedback']]),
    OperatorPOWL(operator=Operator.XOR, children=[activities['Risk Review'], activities['IP Audit']]),
    OperatorPOWL(operator=Operator.XOR, children=[activities['Pilot Launch'], activities['Stakeholder Meet']]),
    OperatorPOWL(operator=Operator.XOR, children=[activities['Resource Shift'], activities['Scale Up']]),
    OperatorPOWL(operator=Operator.XOR, children=[activities['Impact Assess'], activities['Knowledge Share']]),
    OperatorPOWL(operator=Operator.XOR, children=[activities['Monitor Trends'], SilentTransition()])
]

# Create the partial order
root = StrictPartialOrder(nodes=operators, order=[])
root.order.add_edge(operators[0], operators[1])
root.order.add_edge(operators[1], operators[2])
root.order.add_edge(operators[2], operators[3])
root.order.add_edge(operators[3], operators[4])
root.order.add_edge(operators[4], operators[5])
root.order.add_edge(operators[5], operators[6])
root.order.add_edge(operators[6], operators[7])
root.order.add_edge(operators[7], operators[8])
root.order.add_edge(operators[8], operators[9])
root.order.add_edge(operators[9], operators[10])
root.order.add_edge(operators[10], operators[11])
root.order.add_edge(operators[11], operators[12])

print(root)