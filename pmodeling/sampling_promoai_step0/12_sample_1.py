import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
adjust_compensation = Transition(label='Adjust compensation')
approve_promotion = Transition(label='Approve promotion')
conduct_formal_review = Transition(label='Conducts formal performance review')
consider_employee = Transition(label='Consider employee for promotion or new role')
create_plan = Transition(label='Create personal development plan')
identify_development = Transition(label='Identify development needs or career aspirations')
receive_feedback = Transition(label='Receive feedback and evaluation from supervisors')
set_responsibilities = Transition(label='Set new responsibilities')
transition_new_role = Transition(label='Transition into new role')
work_on_skill = Transition(label='Work on skill enhancement')

# Define the silent transitions
skip = SilentTransition()

# Define the partial order
loop = OperatorPOWL(operator=Operator.LOOP, children=[work_on_skill, receive_feedback])
xor = OperatorPOWL(operator=Operator.XOR, children=[set_responsibilities, skip])
root = StrictPartialOrder(nodes=[loop, xor])

# Define the order
root.order.add_edge(loop, xor)

# Define the process tree
process_tree = pm4py.objects.process_tree.obj.ProcessTree()
process_tree.children = [create_plan, loop, xor, approve_promotion, conduct_formal_review, consider_employee, transition_new_role]

# Define the process
process = pm4py.objects.process_tree.obj.ProcessTree()
process.children = [process_tree]

# Define the model
model = pm4py.objects.process_tree.obj.ProcessTree()
model.children = [root]

# Print the model
print(model)