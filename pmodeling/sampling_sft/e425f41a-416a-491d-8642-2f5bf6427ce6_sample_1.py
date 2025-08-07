import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
ing_sourcing    = Transition(label='Ingredient Sourcing')
bot_extr        = Transition(label='Botanical Extraction')
init_blend      = Transition(label='Initial Blending')
sens_testing    = Transition(label='Sensory Testing')
chem_analysis   = Transition(label='Chemical Analysis')
recipe_refine   = Transition(label='Recipe Refinement')
stability_check = Transition(label='Stability Check')
client_sampling = Transition(label='Client Sampling')
feedback_rev    = Transition(label='Feedback Review')
final_adj       = Transition(label='Final Adjustment')
custom_pack     = Transition(label='Custom Packaging')
label_design    = Transition(label='Label Design')
hand_labeling   = Transition(label='Hand Labeling')
reg_audit       = Transition(label='Regulatory Audit')
batch_doc       = Transition(label='Batch Documentation')
limited_release = Transition(label='Limited Release')
market_launch   = Transition(label='Market Launch')

# Build the refinement loop: Sensory Testing -> Chemical Analysis -> Recipe Refinement
refine_body = StrictPartialOrder(nodes=[sens_testing, chem_analysis, recipe_refine])
refine_body.order.add_edge(sens_testing, chem_analysis)
refine_body.order.add_edge(chem_analysis, recipe_refine)

# Loop: do refine_body, then optionally do stability_check and repeat
refine_loop = OperatorPOWL(operator=Operator.LOOP, children=[refine_body, stability_check])

# Build the main process partial order
root = StrictPartialOrder(nodes=[
    ing_sourcing, bot_extr, init_blend, refine_loop,
    client_sampling, feedback_rev, final_adj,
    custom_pack, label_design, hand_labeling,
    reg_audit, batch_doc, limited_release, market_launch
])

# Define the control-flow dependencies
root.order.add_edge(ing_sourcing, bot_extr)
root.order.add_edge(bot_extr, init_blend)
root.order.add_edge(init_blend, refine_loop)
root.order.add_edge(refine_loop, client_sampling)
root.order.add_edge(client_sampling, feedback_rev)
root.order.add_edge(feedback_rev, final_adj)
root.order.add_edge(final_adj, custom_pack)
root.order.add_edge(custom_pack, label_design)
root.order.add_edge(label_design, hand_labeling)
root.order.add_edge(hand_labeling, reg_audit)
root.order.add_edge(reg_audit, batch_doc)
root.order.add_edge(batch_doc, limited_release)
root.order.add_edge(limited_release, market_launch)