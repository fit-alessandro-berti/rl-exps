import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
activity1 = Transition(label='Material Sourcing')
activity2 = Transition(label='Supplier Vetting')
activity3 = Transition(label='Design Review')
activity4 = Transition(label='Prototype Build')
activity5 = Transition(label='Quality Audit')
activity6 = Transition(label='Batch Scheduling')
activity7 = Transition(label='Handcrafting')
activity8 = Transition(label='Packaging Design')
activity9 = Transition(label='Custom Labeling')
activity10 = Transition(label='Sustainability Check')
activity11 = Transition(label='Inventory Sync')
activity12 = Transition(label='Market Analysis')
activity13 = Transition(label='Order Aggregation')
activity14 = Transition(label='Distribution Plan')
activity15 = Transition(label='Customer Feedback')

# Define partial order structure
root = StrictPartialOrder(nodes=[
    activity1, activity2, activity3, activity4, activity5, activity6, activity7, activity8, activity9, activity10,
    activity11, activity12, activity13, activity14, activity15
])

# Define dependencies between activities
root.order.add_edge(activity1, activity2)
root.order.add_edge(activity2, activity3)
root.order.add_edge(activity3, activity4)
root.order.add_edge(activity4, activity5)
root.order.add_edge(activity5, activity6)
root.order.add_edge(activity6, activity7)
root.order.add_edge(activity7, activity8)
root.order.add_edge(activity8, activity9)
root.order.add_edge(activity9, activity10)
root.order.add_edge(activity10, activity11)
root.order.add_edge(activity11, activity12)
root.order.add_edge(activity12, activity13)
root.order.add_edge(activity13, activity14)
root.order.add_edge(activity14, activity15)

# Print the root
print(root)