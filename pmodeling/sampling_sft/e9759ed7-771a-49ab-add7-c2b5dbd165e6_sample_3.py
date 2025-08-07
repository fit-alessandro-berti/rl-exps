import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
t_source = Transition(label='Ingredient Sourcing')
t_sample = Transition(label='Sample Testing')
t_oil = Transition(label='Oil Extraction')
t_blend = Transition(label='Blend Formulation')
t_quality = Transition(label='Quality Control')
t_aging = Transition(label='Aging Process')
t_allergen = Transition(label='Allergen Check')
t_market = Transition(label='Market Research')
t_design = Transition(label='Bottle Design')
t_label = Transition(label='Label Approval')
t_pack = Transition(label='Packaging Setup')
t_mix = Transition(label='Batch Mixing')
t_profiling = Transition(label='Scent Profiling')
t_feedback = Transition(label='Client Feedback')
t_release = Transition(label='Release Scheduling')
t_reg = Transition(label='Regulatory Review')
t_training = Transition(label='Sales Training')

# Build the partial‐order workflow
root = StrictPartialOrder(nodes=[
    t_source, t_sample, t_oil, t_blend, t_quality, t_aging,
    t_allergen, t_market, t_design, t_label, t_pack, t_mix,
    t_profiling, t_feedback, t_release, t_reg, t_training
])

# Define the control‐flow dependencies
root.order.add_edge(t_source, t_sample)
root.order.add_edge(t_source, t_oil)
root.order.add_edge(t_sample, t_blend)
root.order.add_edge(t_oil, t_blend)
root.order.add_edge(t_blend, t_quality)
root.order.add_edge(t_quality, t_aging)
root.order.add_edge(t_aging, t_allergen)
root.order.add_edge(t_allergen, t_market)
root.order.add_edge(t_market, t_design)
root.order.add_edge(t_design, t_label)
root.order.add_edge(t_label, t_pack)
root.order.add_edge(t_pack, t_mix)
root.order.add_edge(t_mix, t_profiling)
root.order.add_edge(t_profiling, t_feedback)
root.order.add_edge(t_feedback, t_release)
root.order.add_edge(t_release, t_reg)
root.order.add_edge(t_reg, t_training)

# Finalize the model
root.order.add_edge(t_allergen, t_release)
root.order.add_edge(t_market, t_design)
root.order.add_edge(t_design, t_label)
root.order.add_edge(t_label, t_pack)
root.order.add_edge(t_pack, t_mix)
root.order.add_edge(t_mix, t_profiling)
root.order.add_edge(t_profiling, t_feedback)
root.order.add_edge(t_feedback, t_release)
root.order.add_edge(t_release, t_reg)
root.order.add_edge(t_reg, t_training)