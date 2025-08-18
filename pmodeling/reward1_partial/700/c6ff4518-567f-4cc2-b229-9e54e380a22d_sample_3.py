import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
milk_sourcing = Transition(label='Milk Sourcing')
culture_prep = Transition(label='Culture Prep')
milk_pasturize = Transition(label='Milk Pasteurize')
coagulation = Transition(label='Coagulation')
curd_cutting = Transition(label='Curd Cutting')
whey_draining = Transition(label='Whey Draining')
hand_molding = Transition(label='Hand Molding')
pressing = Transition(label='Pressing')
salting = Transition(label='Salting')
rind_treatment = Transition(label='Rind Treatment')
aging_setup = Transition(label='Aging Setup')
microclimate_control = Transition(label='Microclimate Control')
flavor_profiling = Transition(label='Flavor Profiling')
quality_check = Transition(label='Quality Check')
sensory_review = Transition(label='Sensory Review')
texture_inspect = Transition(label='Texture Inspect')
eco_packaging = Transition(label='Eco Packaging')
batch_labeling = Transition(label='Batch Labeling')
blockchain_log = Transition(label='Blockchain Log')
niche_shipping = Transition(label='Niche Shipping')

# Define control flow
milk_sourcing_order = OperatorPOWL(operator=Operator.ORDER, children=[milk_sourcing, culture_prep, milk_pasturize, coagulation, curd_cutting, whey_draining, hand_molding, pressing, salting, rind_treatment, aging_setup, microclimate_control])
rind_treatment_order = OperatorPOWL(operator=Operator.ORDER, children=[rind_treatment, flavor_profiling, quality_check])
quality_check_order = OperatorPOWL(operator=Operator.ORDER, children=[quality_check, sensory_review, texture_inspect])
eco_packaging_order = OperatorPOWL(operator=Operator.ORDER, children=[eco_packaging, batch_labeling, blockchain_log])
blockchain_log_order = OperatorPOWL(operator=Operator.ORDER, children=[blockchain_log, niche_shipping])

# Define partial order
root = StrictPartialOrder(nodes=[milk_sourcing_order, rind_treatment_order, quality_check_order, eco_packaging_order, blockchain_log_order])
root.order.add_edge(milk_sourcing_order, rind_treatment_order)
root.order.add_edge(rind_treatment_order, quality_check_order)
root.order.add_edge(quality_check_order, eco_packaging_order)
root.order.add_edge(eco_packaging_order, blockchain_log_order)
root.order.add_edge(blockchain_log_order, niche_shipping)