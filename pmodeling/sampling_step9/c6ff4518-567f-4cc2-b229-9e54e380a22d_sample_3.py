import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
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

# Define silent transitions
skip = SilentTransition()

# Define the POWL model structure
loop_Microclimate_Control = OperatorPOWL(operator=Operator.LOOP, children=[Microclimate_Control])
xor_Niche_Shipping = OperatorPOWL(operator=Operator.XOR, children=[Niche_Shipping, skip])
xor_Texture_Inspect = OperatorPOWL(operator=Operator.XOR, children=[Texture_Inspect, skip])
xor_Batch_Labeling = OperatorPOWL(operator=Operator.XOR, children=[Batch_Labeling, skip])
xor_Blockchain_Log = OperatorPOWL(operator=Operator.XOR, children=[Blockchain_Log, skip])
xor_Eco_Packaging = OperatorPOWL(operator=Operator.XOR, children=[Eco_Packaging, skip])
xor_Quality_Check = OperatorPOWL(operator=Operator.XOR, children=[Quality_Check, skip])
xor_Sensory_Review = OperatorPOWL(operator=Operator.XOR, children=[Sensory_Review, skip])
xor_Flavor_Profiling = OperatorPOWL(operator=Operator.XOR, children=[Flavor_Profiling, skip])
xor_Aging_Setup = OperatorPOWL(operator=Operator.XOR, children=[Aging_Setup, skip])
xor_Rind_Treatment = OperatorPOWL(operator=Operator.XOR, children=[Rind_Treatment, skip])
xor_Salting = OperatorPOWL(operator=Operator.XOR, children=[Salting, skip])
xor_Pressing = OperatorPOWL(operator=Operator.XOR, children=[Pressing, skip])
xor_Curd_Cutting = OperatorPOWL(operator=Operator.XOR, children=[Curd_Cutting, skip])
xor_Whey_Draining = OperatorPOWL(operator=Operator.XOR, children=[Whey_Draining, skip])
xor_Milk_Pasteurization = OperatorPOWL(operator=Operator.XOR, children=[Milk_Pasteurization, skip])
xor_Culture_Preparation = OperatorPOWL(operator=Operator.XOR, children=[Culture_Preparation, skip])
xor_Milk_Sourcing = OperatorPOWL(operator=Operator.XOR, children=[Milk_Sourcing, skip])

# Construct the root node
root = StrictPartialOrder(nodes=[loop_Microclimate_Control, xor_Niche_Shipping, xor_Texture_Inspect, xor_Batch_Labeling, xor_Blockchain_Log, xor_Eco_Packaging, xor_Quality_Check, xor_Sensory_Review, xor_Flavor_Profiling, xor_Aging_Setup, xor_Rind_Treatment, xor_Salting, xor_Pressing, xor_Curd_Cutting, xor_Whey_Draining, xor_Milk_Pasteurization, xor_Culture_Preparation, xor_Milk_Sourcing])

# Define the order of dependencies
root.order.add_edge(loop_Microclimate_Control, xor_Niche_Shipping)
root.order.add_edge(loop_Microclimate_Control, xor_Texture_Inspect)
root.order.add_edge(loop_Microclimate_Control, xor_Batch_Labeling)
root.order.add_edge(loop_Microclimate_Control, xor_Blockchain_Log)
root.order.add_edge(loop_Microclimate_Control, xor_Eco_Packaging)
root.order.add_edge(loop_Microclimate_Control, xor_Quality_Check)
root.order.add_edge(loop_Microclimate_Control, xor_Sensory_Review)
root.order.add_edge(loop_Microclimate_Control, xor_Flavor_Profiling)
root.order.add_edge(loop_Microclimate_Control, xor_Aging_Setup)
root.order.add_edge(loop_Microclimate_Control, xor_Rind_Treatment)
root.order.add_edge(loop_Microclimate_Control, xor_Salting)
root.order.add_edge(loop_Microclimate_Control, xor_Pressing)
root.order.add_edge(loop_Microclimate_Control, xor_Curd_Cutting)
root.order.add_edge(loop_Microclimate_Control, xor_Whey_Draining)
root.order.add_edge(loop_Microclimate_Control, xor_Milk_Pasteurization)
root.order.add_edge(loop_Microclimate_Control, xor_Culture_Preparation)
root.order.add_edge(loop_Microclimate_Control, xor_Milk_Sourcing)

# Print the root node to verify the POWL model
print(root)