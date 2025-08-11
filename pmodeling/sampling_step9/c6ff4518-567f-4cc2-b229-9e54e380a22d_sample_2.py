import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
Milk_Sourcing = Transition(label='Milk Sourcing')
Culture_Prep = Transition(label='Culture Prep')
Milk_Pasteurize = Transition(label='Milk Pasteurize')
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

# Define silent transitions
skip = SilentTransition()

# Define loops
aging_loop = OperatorPOWL(operator=Operator.LOOP, children=[Aging_Setup, Microclimate_Control])
culture_loop = OperatorPOWL(operator=Operator.LOOP, children=[Culture_Prep, Milk_Sourcing])
milk_loop = OperatorPOWL(operator=Operator.LOOP, children=[Milk_Pasteurize, Coagulation])
curd_loop = OperatorPOWL(operator=Operator.LOOP, children=[Curd_Cutting, Whey_Draining])
molding_loop = OperatorPOWL(operator=Operator.LOOP, children=[Hand_Molding, Pressing])
salting_loop = OperatorPOWL(operator=Operator.LOOP, children=[Salting, Rind_Treatment])
flavor_loop = OperatorPOWL(operator=Operator.LOOP, children=[Flavor_Profiling, Quality_Check])
sensory_loop = OperatorPOWL(operator=Operator.LOOP, children=[Sensory_Review, Texture_Inspect])
packaging_loop = OperatorPOWL(operator=Operator.LOOP, children=[Eco_Packaging, Batch_Labeling])

# Define exclusive choices
milk_exclusive = OperatorPOWL(operator=Operator.XOR, children=[Milk_Pasteurize, culture_loop])
coagulation_exclusive = OperatorPOWL(operator=Operator.XOR, children=[Coagulation, aging_loop])
curd_exclusive = OperatorPOWL(operator=Operator.XOR, children=[Curd_Cutting, flavor_loop])
molding_exclusive = OperatorPOWL(operator=Operator.XOR, children=[Hand_Molding, salting_loop])
aging_exclusive = OperatorPOWL(operator=Operator.XOR, children=[Aging_Setup, packaging_loop])
flavor_exclusive = OperatorPOWL(operator=Operator.XOR, children=[Flavor_Profiling, niche_shipping])
sensory_exclusive = OperatorPOWL(operator=Operator.XOR, children=[Sensory_Review, niche_shipping])
packaging_exclusive = OperatorPOWL(operator=Operator.XOR, children=[Eco_Packaging, niche_shipping])

# Define the root POWL model
root = StrictPartialOrder(nodes=[milk_exclusive, coagulation_exclusive, curd_exclusive, molding_exclusive, aging_exclusive, flavor_exclusive, sensory_exclusive, packaging_exclusive])
root.order.add_edge(milk_exclusive, coagulation_exclusive)
root.order.add_edge(coagulation_exclusive, curd_exclusive)
root.order.add_edge(curd_exclusive, molding_exclusive)
root.order.add_edge(molding_exclusive, aging_exclusive)
root.order.add_edge(aging_exclusive, flavor_exclusive)
root.order.add_edge(flavor_exclusive, sensory_exclusive)
root.order.add_edge(sensory_exclusive, packaging_exclusive)
root.order.add_edge(packaging_exclusive, niche_shipping)