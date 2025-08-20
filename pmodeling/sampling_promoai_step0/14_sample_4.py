from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define activities
outline = Transition(label='Outline objectives')
draft = Transition(label='Draft plan')
align = Transition(label='Conduct strategic alignment meeting')
review = Transition(label='Review budget feasibility')
approve = Transition(label='Approve final budget')
adjust = Transition(label='Adjust Plan')
implement = Transition(label='Implement plan')
distribute = Transition(label='Distribute budget')
document = Transition(label='Documented and approve adjustment')
feedback = Transition(label='Provide feedback')

# Define transitions
silent = SilentTransition()
loop = OperatorPOWL(operator=Operator.LOOP, children=[draft, align])
xor = OperatorPOWL(operator=Operator.XOR, children=[adjust, silent])
root = StrictPartialOrder(nodes=[loop, xor, review, approve, distribute, implement, document, feedback])

# Define dependencies
root.order.add_edge(loop, xor)
root.order.add_edge(xor, review)
root.order.add_edge(review, approve)
root.order.add_edge(approve, distribute)
root.order.add_edge(distribute, implement)
root.order.add_edge(implement, document)
root.order.add_edge(document, feedback)

# Print the root model
print(root)