import pm4py
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
batch = Transition(label='Batch Scheduling')
custom_approvals = Transition(label='Custom Approvals')
inventory = Transition(label='Inventory Adjust')
production = Transition(label='Production Sync')
shipping = Transition(label='Shipping Plan')
compliance = Transition(label='Compliance Check')
feedback = Transition(label='Feedback Loop')
target = Transition(label='Market Target')
fulfill = Transition(label='Order Fulfill')
sustainability = Transition(label='Sustainability')
engage = Transition(label='Customer Engage')

# Define silent transitions for looping
skip_audit = SilentTransition()
skip_verify = SilentTransition()
skip_concept = SilentTransition()
skip_prototype = SilentTransition()
skip_review = SilentTransition()
skip_assign = SilentTransition()
skip_batch = SilentTransition()
skip_custom_approvals = SilentTransition()
skip_inventory = SilentTransition()
skip_production = SilentTransition()
skip_shipping = SilentTransition()
skip_compliance = SilentTransition()
skip_feedback = SilentTransition()
skip_target = SilentTransition()
skip_fulfill = SilentTransition()
skip_sustainability = SilentTransition()
skip_engage = SilentTransition()

# Define the POWL model
audit_loop = OperatorPOWL(operator=Operator.LOOP, children=[audit, skip_audit])
verify_loop = OperatorPOWL(operator=Operator.LOOP, children=[verify, skip_verify])
concept_loop = OperatorPOWL(operator=Operator.LOOP, children=[concept, skip_concept])
prototype_loop = OperatorPOWL(operator=Operator.LOOP, children=[prototype, skip_prototype])
review_loop = OperatorPOWL(operator=Operator.LOOP, children=[review, skip_review])
assign_loop = OperatorPOWL(operator=Operator.LOOP, children=[assign, skip_assign])
batch_loop = OperatorPOWL(operator=Operator.LOOP, children=[batch, skip_batch])
custom_approvals_loop = OperatorPOWL(operator=Operator.LOOP, children=[custom_approvals, skip_custom_approvals])
inventory_loop = OperatorPOWL(operator=Operator.LOOP, children=[inventory, skip_inventory])
production_loop = OperatorPOWL(operator=Operator.LOOP, children=[production, skip_production])
shipping_loop = OperatorPOWL(operator=Operator.LOOP, children=[shipping, skip_shipping])
compliance_loop = OperatorPOWL(operator=Operator.LOOP, children=[compliance, skip_compliance])
feedback_loop = OperatorPOWL(operator=Operator.LOOP, children=[feedback, skip_feedback])
target_loop = OperatorPOWL(operator=Operator.LOOP, children=[target, skip_target])
fulfill_loop = OperatorPOWL(operator=Operator.LOOP, children=[fulfill, skip_fulfill])
sustainability_loop = OperatorPOWL(operator=Operator.LOOP, children=[sustainability, skip_sustainability])
engage_loop = OperatorPOWL(operator=Operator.LOOP, children=[engage, skip_engage])

root = StrictPartialOrder(
    nodes=[
        sourcing,
        audit_loop,
        verify_loop,
        concept_loop,
        prototype_loop,
        review_loop,
        assign_loop,
        batch_loop,
        custom_approvals_loop,
        inventory_loop,
        production_loop,
        shipping_loop,
        compliance_loop,
        feedback_loop,
        target_loop,
        fulfill_loop,
        sustainability_loop,
        engage_loop
    ]
)

# Define dependencies between nodes
root.order.add_edge(sourcing, audit_loop)
root.order.add_edge(audit_loop, verify_loop)
root.order.add_edge(verify_loop, concept_loop)
root.order.add_edge(concept_loop, prototype_loop)
root.order.add_edge(prototype_loop, review_loop)
root.order.add_edge(review_loop, assign_loop)
root.order.add_edge(assign_loop, batch_loop)
root.order.add_edge(batch_loop, custom_approvals_loop)
root.order.add_edge(custom_approvals_loop, inventory_loop)
root.order.add_edge(inventory_loop, production_loop)
root.order.add_edge(production_loop, shipping_loop)
root.order.add_edge(shipping_loop, compliance_loop)
root.order.add_edge(compliance_loop, feedback_loop)
root.order.add_edge(feedback_loop, target_loop)
root.order.add_edge(target_loop, fulfill_loop)
root.order.add_edge(fulfill_loop, sustainability_loop)
root.order.add_edge(sustainability_loop, engage_loop)

# Print the root node for verification
print(root)