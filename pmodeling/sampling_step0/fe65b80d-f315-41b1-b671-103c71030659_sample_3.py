import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator
from pm4py.objects.petri_net.obj import PetriNet, Marking
from pm4py.objects.petri_net.utils import petri_utils

# Define the POWL model
ingredient_sourcing = Transition(label='Ingredient Sourcing')
quality_testing = Transition(label='Quality Testing')
scent_blending = Transition(label='Scent Blending')
micro_batch = Transition(label='Micro Batch')
sensory_panel = Transition(label='Sensory Panel')
formula_adjust = Transition(label='Formula Adjust')
safety_review = Transition(label='Safety Review')
sustainability_check = Transition(label='Sustainability Check')
packaging_design = Transition(label='Packaging Design')
prototype_creation = Transition(label='Prototype Creation')
client_feedback = Transition(label='Client Feedback')
label_approval = Transition(label='Label Approval')
final_production = Transition(label='Final Production')
marketing_plan = Transition(label='Marketing Plan')
distribution_prep = Transition(label='Distribution Prep')
sales_launch = Transition(label='Sales Launch')

skip = SilentTransition()

loop_ingredient_sourcing = OperatorPOWL(operator=Operator.LOOP, children=[ingredient_sourcing, quality_testing, scent_blending])
loop_micro_batch = OperatorPOWL(operator=Operator.LOOP, children=[micro_batch, sensory_panel, formula_adjust, safety_review, sustainability_check])
loop_packaging_design = OperatorPOWL(operator=Operator.LOOP, children=[packaging_design, prototype_creation])
loop_client_feedback = OperatorPOWL(operator=Operator.LOOP, children=[client_feedback, label_approval])
loop_final_production = OperatorPOWL(operator=Operator.LOOP, children=[final_production, marketing_plan, distribution_prep, sales_launch])

xor_marketing_plan = OperatorPOWL(operator=Operator.XOR, children=[marketing_plan, distribution_prep])
xor_sales_launch = OperatorPOWL(operator=Operator.XOR, children=[sales_launch, client_feedback])

root = StrictPartialOrder(nodes=[loop_ingredient_sourcing, loop_micro_batch, loop_packaging_design, loop_client_feedback, loop_final_production, xor_marketing_plan, xor_sales_launch])
root.order.add_edge(loop_ingredient_sourcing, loop_micro_batch)
root.order.add_edge(loop_micro_batch, loop_packaging_design)
root.order.add_edge(loop_packaging_design, loop_client_feedback)
root.order.add_edge(loop_client_feedback, loop_final_production)
root.order.add_edge(loop_final_production, xor_marketing_plan)
root.order.add_edge(loop_final_production, xor_sales_launch)
root.order.add_edge(xor_marketing_plan, xor_sales_launch)

# Convert to Petri Net
net, im, fm = pm4py.convert_to_petri_net(root)
print(net)
print(im)
print(fm)

# Simulate the Petri Net
initial_marking = im
final_marking = fm
trace = petri_utils.simulate_petri_net(net, initial_marking, final_marking)
print(trace)