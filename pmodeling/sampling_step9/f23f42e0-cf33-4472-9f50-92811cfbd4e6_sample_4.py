import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
Milk_Sourcing = Transition(label='Milk Sourcing')
Culture_Selection = Transition(label='Culture Selection')
Milk_Testing = Transition(label='Milk Testing')
Curd_Cutting = Transition(label='Curd Cutting')
Whey_Draining = Transition(label='Whey Draining')
Mold_Inoculation = Transition(label='Mold Inoculation')
Forming_Cheese = Transition(label='Forming Cheese')
Salting_Stage = Transition(label='Salting Stage')
Aging_Setup = Transition(label='Aging Setup')
Climate_Control = Transition(label='Climate Control')
Quality_Tasting = Transition(label='Quality Tasting')
Packaging_Prep = Transition(label='Packaging Prep')
Label_Printing = Transition(label='Label Printing')
Distribution_Plan = Transition(label='Distribution Plan')
Retail_Delivery = Transition(label='Retail Delivery')
Event_Coordination = Transition(label='Event Coordination')
Regulatory_Audit = Transition(label='Regulatory Audit')

# Define silent transitions
skip = SilentTransition()

# Define loop nodes for specific activities
aging_loop = OperatorPOWL(operator=Operator.LOOP, children=[Aging_Setup, Climate_Control])
tasting_loop = OperatorPOWL(operator=Operator.LOOP, children=[Quality_Tasting])
packing_loop = OperatorPOWL(operator=Operator.LOOP, children=[Packaging_Prep, Label_Printing])
distribution_loop = OperatorPOWL(operator=Operator.LOOP, children=[Distribution_Plan, Retail_Delivery])
event_loop = OperatorPOWL(operator=Operator.LOOP, children=[Event_Coordination])

# Define XOR nodes for parallel activities
sourcing_xor = OperatorPOWL(operator=Operator.XOR, children=[Milk_Sourcing, skip])
culture_xor = OperatorPOWL(operator=Operator.XOR, children=[Culture_Selection, skip])
testing_xor = OperatorPOWL(operator=Operator.XOR, children=[Milk_Testing, skip])
cutting_xor = OperatorPOWL(operator=Operator.XOR, children=[Curd_Cutting, skip])
draining_xor = OperatorPOWL(operator=Operator.XOR, children=[Whey_Draining, skip])
inoculation_xor = OperatorPOWL(operator=Operator.XOR, children=[Mold_Inoculation, skip])
forming_xor = OperatorPOWL(operator=Operator.XOR, children=[Forming_Cheese, skip])
salting_xor = OperatorPOWL(operator=Operator.XOR, children=[Salting_Stage, skip])

# Define the root POWL model
root = StrictPartialOrder(nodes=[aging_loop, tasting_loop, packing_loop, distribution_loop, event_loop, sourcing_xor, culture_xor, testing_xor, cutting_xor, draining_xor, inoculation_xor, forming_xor, salting_xor])
root.order.add_edge(aging_loop, tasting_loop)
root.order.add_edge(aging_loop, packing_loop)
root.order.add_edge(aging_loop, distribution_loop)
root.order.add_edge(aging_loop, event_loop)
root.order.add_edge(sourcing_xor, aging_loop)
root.order.add_edge(culture_xor, aging_loop)
root.order.add_edge(testing_xor, aging_loop)
root.order.add_edge(cutting_xor, aging_loop)
root.order.add_edge(draining_xor, aging_loop)
root.order.add_edge(inoculation_xor, aging_loop)
root.order.add_edge(forming_xor, aging_loop)
root.order.add_edge(salting_xor, aging_loop)