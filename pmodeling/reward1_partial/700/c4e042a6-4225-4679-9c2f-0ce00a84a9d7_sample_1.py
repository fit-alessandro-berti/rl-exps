from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
sourcing = Transition(label='Material Sourcing')
audit = Transition(label='Supplier Audit')
verify = Transition(label='Credential Verify')
concept = Transition(label='Design Concept')
prototype = Transition(label='Prototype Build')
review = Transition(label='Quality Review')
assign = Transition(label='Artisan Assign')
schedule = Transition(label='Batch Scheduling')
approvals = Transition(label='Custom Approvals')
inventory = Transition(label='Inventory Adjust')
sync = Transition(label='Production Sync')
shipping = Transition(label='Shipping Plan')
compliance = Transition(label='Compliance Check')
feedback = Transition(label='Feedback Loop')
market = Transition(label='Market Target')
fulfill = Transition(label='Order Fulfill')
sustainability = Transition(label='Sustainability')
engage = Transition(label='Customer Engage')

# Define partial order structure
root = StrictPartialOrder(nodes=[sourcing, audit, verify, concept, prototype, review, assign, schedule, approvals, inventory, sync, shipping, compliance, feedback, market, fulfill, sustainability, engage])

# Define dependencies
root.order.add_edge(sourcing, audit)
root.order.add_edge(audit, verify)
root.order.add_edge(verify, concept)
root.order.add_edge(concept, prototype)
root.order.add_edge(prototype, review)
root.order.add_edge(review, assign)
root.order.add_edge(assign, schedule)
root.order.add_edge(schedule, approvals)
root.order.add_edge(approvals, inventory)
root.order.add_edge(inventory, sync)
root.order.add_edge(sync, shipping)
root.order.add_edge(shipping, compliance)
root.order.add_edge(compliance, feedback)
root.order.add_edge(feedback, market)
root.order.add_edge(market, fulfill)
root.order.add_edge(fulfill, sustainability)
root.order.add_edge(sustainability, engage)

print(root)