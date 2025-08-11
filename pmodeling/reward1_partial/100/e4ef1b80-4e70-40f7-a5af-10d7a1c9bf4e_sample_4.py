from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define the transitions (activities) with their names
activities = {
    'Opportunity Scan': Transition(label='Opportunity Scan'),
    'Idea Workshop': Transition(label='Idea Workshop'),
    'Concept Merge': Transition(label='Concept Merge'),
    'Resource Align': Transition(label='Resource Align'),
    'Prototype Build': Transition(label='Prototype Build'),
    'Feasibility Test': Transition(label='Feasibility Test'),
    'Pilot Launch': Transition(label='Pilot Launch'),
    'Feedback Gather': Transition(label='Feedback Gather'),
    'Design Adapt': Transition(label='Design Adapt'),
    'Compliance Check': Transition(label='Compliance Check'),
    'Scaling Plan': Transition(label='Scaling Plan'),
    'IP Management': Transition(label='IP Management'),
    'Market Sync': Transition(label='Market Sync'),
    'Partner Review': Transition(label='Partner Review'),
    'Exit Strategy': Transition(label='Exit Strategy')
}

# Define the control-flow operators
xor = OperatorPOWL(operator=Operator.XOR, children=[activities['Exit Strategy']])
loop = OperatorPOWL(operator=Operator.LOOP, children=[activities['Opportunity Scan'], activities['Idea Workshop'], activities['Concept Merge'], activities['Resource Align'], activities['Prototype Build'], activities['Feasibility Test'], activities['Pilot Launch'], activities['Feedback Gather'], activities['Design Adapt'], activities['Compliance Check'], activities['Scaling Plan'], activities['IP Management'], activities['Market Sync'], activities['Partner Review']])

# Create the root Partial Order
root = StrictPartialOrder(nodes=[loop, xor])
root.order.add_edge(loop, xor)

# Print the root POWL model
print(root)