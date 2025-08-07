import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
t1 = Transition(label='Ingredient Sourcing')
t2 = Transition(label='Quality Testing')
t3 = Transition(label='Scent Blending')
t4 = Transition(label='Micro Batch')
t5 = Transition(label='Sensory Panel')
t6 = Transition(label='Formula Adjust')
t7 = Transition(label='Safety Review')
t8 = Transition(label='Sustainability Check')
t9 = Transition(label='Packaging Design')
t10 = Transition(label='Prototype Creation')
t11 = Transition(label='Client Feedback')
t12 = Transition(label='Label Approval')
t13 = Transition(label='Final Production')
t14 = Transition(label='Marketing Plan')
t15 = Transition(label='Distribution Prep')
t16 = Transition(label='Sales Launch')

# Build the loop for sensory panel and formula adjustment
loop = OperatorPOWL(operator=Operator.LOOP, children=[t5, t6])

# Build the partial order
root = StrictPartialOrder(nodes=[
    t1, t2, t3, t4, loop,
    t7, t8, t9, t10,
    t11, t12, t13, t14,
    t15, t16
])

# Define the control-flow dependencies
root.order.add_edge(t1, t2)
root.order.add_edge(t2, t3)
root.order.add_edge(t3, t4)
root.order.add_edge(t4, loop)
root.order.add_edge(loop, t7)
root.order.add_edge(t7, t8)
root.order.add_edge(t8, t9)
root.order.add_edge(t9, t10)
root.order.add_edge(t10, t11)
root.order.add_edge(t11, t12)
root.order.add_edge(t12, t13)
root.order.add_edge(t13, t14)
root.order.add_edge(t14, t15)
root.order.add_edge(t15, t16)

print(root)