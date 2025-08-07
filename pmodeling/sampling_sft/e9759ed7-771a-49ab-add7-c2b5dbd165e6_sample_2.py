import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
t_ing = Transition(label='Ingredient Sourcing')
t_samp = Transition(label='Sample Testing')
t_ext = Transition(label='Oil Extraction')
t_blend = Transition(label='Blend Formulation')
t_qc = Transition(label='Quality Control')
t_aging = Transition(label='Aging Process')
t_allergen = Transition(label='Allergen Check')
t_mr = Transition(label='Market Research')
t_bd = Transition(label='Bottle Design')
t_la = Transition(label='Label Approval')
t_ps = Transition(label='Scent Profiling')
t_release = Transition(label='Release Scheduling')
t_reg = Transition(label='Regulatory Review')
t_train = Transition(label='Sales Training')
t_batch = Transition(label='Batch Mixing')
t_feedback = Transition(label='Client Feedback')
skip = SilentTransition()

# Define the optional feedback loop: if Client Feedback is not skipped, run Client Feedback -> QC -> Batch Mixing
feedback_loop = OperatorPOWL(operator=Operator.LOOP, children=[t_feedback, t_qc])
feedback_loop.order.add_edge(t_feedback, t_qc)
feedback_loop.order.add_edge(t_qc, t_batch)

# Build the root partial order
root = StrictPartialOrder(nodes=[
    t_ing, t_samp, t_ext, t_blend, t_qc, t_aging, t_allergen,
    t_mr, t_bd, t_la, t_ps, t_release, t_reg, t_train, t_batch,
    feedback_loop
])

# Sequence: Ingredient Sourcing -> Sample Testing -> Oil Extraction -> Blend Formulation -> Quality Control
root.order.add_edge(t_ing, t_samp)
root.order.add_edge(t_samp, t_ext)
root.order.add_edge(t_ext, t_blend)
root.order.add_edge(t_blend, t_qc)

# Parallel: Quality Control -> Aging Process -> Allergen Check
root.order.add_edge(t_qc, t_aging)
root.order.add_edge(t_qc, t_allergen)

# Market Research -> Bottle Design -> Label Approval -> Scent Profiling -> Client Feedback (optional)
root.order.add_edge(t_mr, t_bd)
root.order.add_edge(t_bd, t_la)
root.order.add_edge(t_la, t_ps)
root.order.add_edge(t_ps, feedback_loop)

# Optional feedback loop: after optional Client Feedback, Batch Mixing
root.order.add_edge(feedback_loop, t_batch)

# Batch Mixing -> Release Scheduling -> Regulatory Review -> Sales Training
root.order.add_edge(t_batch, t_release)
root.order.add_edge(t_release, t_reg)
root.order.add_edge(t_reg, t_train)

# Final optional feedback: Client Feedback (if not skipped) can be run after Sales Training
root.order.add_edge(t_feedback, t_train)