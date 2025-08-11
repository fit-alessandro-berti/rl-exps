import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities)
Milk_Sourcing = Transition(label='Milk Sourcing')
Culture_Preparation = Transition(label='Culture Prep')
Milk_Pasteurization = Transition(label='Milk Pasteurize')
Coagulation = Transition(label='Coagulation')
Curd_Cutting = Transition(label='Curd Cutting')
Whey_Draining = Transition(label='Whey Draining')
Hand_Molding = Transition(label='Hand Molding')
Pressing = Transition(label='Pressing')
Salting = Transition(label='Salting')
Rind_Treatment = Transition(label='Rind Treatment')
Aging_Setup = Transition(label='Aging Setup')
Microclimate_Control = Transition(label='Microclimate Control')
Flavor_Profiling = Transition(label='Flavor Profiling')
Quality_Check = Transition(label='Quality Check')
Sensory_Review = Transition(label='Sensory Review')
Texture_Inspect = Transition(label='Texture Inspect')
Eco_Packaging = Transition(label='Eco Packaging')
Batch_Labeling = Transition(label='Batch Labeling')
Blockchain_Log = Transition(label='Blockchain Log')
Niche_Shipping = Transition(label='Niche Shipping')

# Define the silent transitions
skip = SilentTransition()

# Define the loops and choices
culture_loop = OperatorPOWL(operator=Operator.LOOP, children=[Culture_Preparation, skip])
coagulation_loop = OperatorPOWL(operator=Operator.LOOP, children=[Coagulation, skip])
molding_loop = OperatorPOWL(operator=Operator.LOOP, children=[Hand_Molding, skip])
aging_loop = OperatorPOWL(operator=Operator.LOOP, children=[Aging_Setup, skip])
microclimate_loop = OperatorPOWL(operator=Operator.LOOP, children=[Microclimate_Control, skip])
flavor_loop = OperatorPOWL(operator=Operator.LOOP, children=[Flavor_Profiling, skip])
quality_loop = OperatorPOWL(operator=Operator.LOOP, children=[Quality_Check, skip])
sensory_loop = OperatorPOWL(operator=Operator.LOOP, children=[Sensory_Review, skip])
texture_loop = OperatorPOWL(operator=Operator.LOOP, children=[Texture_Inspect, skip])
packaging_loop = OperatorPOWL(operator=Operator.LOOP, children=[Eco_Packaging, skip])
batch_loop = OperatorPOWL(operator=Operator.LOOP, children=[Batch_Labeling, skip])
log_loop = OperatorPOWL(operator=Operator.LOOP, children=[Blockchain_Log, skip])
shipping_loop = OperatorPOWL(operator=Operator.LOOP, children=[Niche_Shipping, skip])

# Define the partial order
root = StrictPartialOrder(nodes=[
    Milk_Sourcing,
    culture_loop,
    coagulation_loop,
    molding_loop,
    aging_loop,
    microclimate_loop,
    flavor_loop,
    quality_loop,
    sensory_loop,
    texture_loop,
    packaging_loop,
    batch_loop,
    log_loop,
    shipping_loop
])

# Define the order dependencies
root.order.add_edge(Milk_Sourcing, culture_loop)
root.order.add_edge(culture_loop, coagulation_loop)
root.order.add_edge(coagulation_loop, molding_loop)
root.order.add_edge(molding_loop, aging_loop)
root.order.add_edge(aging_loop, microclimate_loop)
root.order.add_edge(microclimate_loop, flavor_loop)
root.order.add_edge(flavor_loop, quality_loop)
root.order.add_edge(quality_loop, sensory_loop)
root.order.add_edge(sensory_loop, texture_loop)
root.order.add_edge(texture_loop, packaging_loop)
root.order.add_edge(packaging_loop, batch_loop)
root.order.add_edge(batch_loop, log_loop)
root.order.add_edge(log_loop, shipping_loop)

print(root)