import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
intake     = Transition(label='Inquiry Intake')
call       = Transition(label='Consultation Call')
concept    = Transition(label='Concept Draft')
feedback   = Transition(label='Feedback Loop')
setup      = Transition(label='Contract Setup')
match      = Transition(label='Artist Match')
sourcing   = Transition(label='Material Sourcing')
ethics     = Transition(label='Ethics Review')
progress   = Transition(label='Progress Check')
approve    = Transition(label='Milestone Approve')
audit      = Transition(label='Quality Audit')
transfer   = Transition(label='Copyright Transfer')
packaging  = Transition(label='Packaging Plan')
shipping   = Transition(label='Shipping Arrange')
delivery   = Transition(label='Post Delivery')
survey     = Transition(label='Client Survey')

# Build the iterative feedback cycle: Feedback Loop = Concept Draft -> Feedback Loop
feedback_loop = StrictPartialOrder(nodes=[concept, feedback])
feedback_loop.order.add_edge(concept, feedback)

# Build the main workflow as a strict partial order
main_workflow = StrictPartialOrder(nodes=[
    intake, call, feedback_loop, setup, match, sourcing, ethics,
    progress, approve, audit, transfer, packaging, shipping, delivery, survey
])

# Define the control-flow edges
main_workflow.order.add_edge(intake, call)
main_workflow.order.add_edge(call, feedback_loop)
main_workflow.order.add_edge(feedback_loop, setup)
main_workflow.order.add_edge(setup, match)
main_workflow.order.add_edge(match, sourcing)
main_workflow.order.add_edge(sourcing, ethics)
main_workflow.order.add_edge(ethics, progress)
main_workflow.order.add_edge(progress, approve)
main_workflow.order.add_edge(approve, audit)
main_workflow.order.add_edge(audit, transfer)
main_workflow.order.add_edge(transfer, packaging)
main_workflow.order.add_edge(packaging, shipping)
main_workflow.order.add_edge(shipping, delivery)
main_workflow.order.add_edge(delivery, survey)

# Set the root of the partial order
root = main_workflow