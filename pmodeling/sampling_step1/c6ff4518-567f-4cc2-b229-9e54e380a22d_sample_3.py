import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities)
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

# Define the partial order model
root = StrictPartialOrder(nodes=[
    Milk_Sourcing, Culture_Prep, Milk_Pasteurize, Coagulation, Curd_Cutting, Whey_Draining, Hand_Molding, Pressing, Salting, Rind_Treatment, Aging_Setup, Microclimate_Control, Flavor_Profiling, Quality_Check, Sensory_Review, Texture_Inspect, Eco_Packaging, Batch_Labeling, Blockchain_Log, Niche_Shipping
])

# Define the order edges (dependencies)
root.order.add_edge(Milk_Sourcing, Culture_Prep)
root.order.add_edge(Culture_Prep, Milk_Pasteurize)
root.order.add_edge(Milk_Pasteurize, Coagulation)
root.order.add_edge(Coagulation, Curd_Cutting)
root.order.add_edge(Curd_Cutting, Whey_Draining)
root.order.add_edge(Whey_Draining, Hand_Molding)
root.order.add_edge(Hand_Molding, Pressing)
root.order.add_edge(Pressing, Salting)
root.order.add_edge(Salting, Rind_Treatment)
root.order.add_edge(Rind_Treatment, Aging_Setup)
root.order.add_edge(Aging_Setup, Microclimate_Control)
root.order.add_edge(Microclimate_Control, Flavor_Profiling)
root.order.add_edge(Flavor_Profiling, Quality_Check)
root.order.add_edge(Quality_Check, Sensory_Review)
root.order.add_edge(Sensory_Review, Texture_Inspect)
root.order.add_edge(Texture_Inspect, Eco_Packaging)
root.order.add_edge(Eco_Packaging, Batch_Labeling)
root.order.add_edge(Batch_Labeling, Blockchain_Log)
root.order.add_edge(Blockchain_Log, Niche_Shipping)

# Print the final root
print(root)