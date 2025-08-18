import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for each activity
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

# Define loop for aging setup
aging_loop = OperatorPOWL(operator=Operator.LOOP, children=[Aging_Setup, Microclimate_Control, Flavor_Profiling, Quality_Check, Sensory_Review, Texture_Inspect])

# Define XOR for quality check
quality_check_xor = OperatorPOWL(operator=Operator.XOR, children=[skip, Batch_Labeling, Eco_Packaging, Niche_Shipping])

# Define the root model
root = StrictPartialOrder(nodes=[Milk_Sourcing, Culture_Prep, Milk_Pasteurize, Coagulation, Curd_Cutting, Whey_Draining, Hand_Molding, Pressing, Salting, Rind_Treatment, aging_loop, quality_check_xor])
root.order.add_edge(aging_loop, quality_check_xor)