from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities) with their labels
milk_sourcing = Transition(label='Milk Sourcing')
culture_selection = Transition(label='Culture Selection')
milk_testing = Transition(label='Milk Testing')
curd_cutting = Transition(label='Curd Cutting')
whey_draining = Transition(label='Whey Draining')
mold_inoculation = Transition(label='Mold Inoculation')
forming_cheese = Transition(label='Forming Cheese')
salting_stage = Transition(label='Salting Stage')
aging_setup = Transition(label='Aging Setup')
climate_control = Transition(label='Climate Control')
quality_tasting = Transition(label='Quality Tasting')
packaging_prep = Transition(label='Packaging Prep')
label_printing = Transition(label='Label Printing')
distribution_plan = Transition(label='Distribution Plan')
retail_delivery = Transition(label='Retail Delivery')
event_coordination = Transition(label='Event Coordination')
regulatory_audit = Transition(label='Regulatory Audit')

# Define the control-flow operators for the POWL model
xor = OperatorPOWL(operator=Operator.XOR, children=[
    culture_selection,
    milk_sourcing
])

choice1 = OperatorPOWL(operator=Operator.XOR, children=[
    milk_testing,
    xor
])

choice2 = OperatorPOWL(operator=Operator.XOR, children=[
    curd_cutting,
    choice1
])

choice3 = OperatorPOWL(operator=Operator.XOR, children=[
    whey_draining,
    choice2
])

choice4 = OperatorPOWL(operator=Operator.XOR, children=[
    mold_inoculation,
    choice3
])

choice5 = OperatorPOWL(operator=Operator.XOR, children=[
    forming_cheese,
    choice4
])

choice6 = OperatorPOWL(operator=Operator.XOR, children=[
    salting_stage,
    choice5
])

choice7 = OperatorPOWL(operator=Operator.XOR, children=[
    aging_setup,
    choice6
])

choice8 = OperatorPOWL(operator=Operator.XOR, children=[
    climate_control,
    choice7
])

choice9 = OperatorPOWL(operator=Operator.XOR, children=[
    quality_tasting,
    choice8
])

choice10 = OperatorPOWL(operator=Operator.XOR, children=[
    packaging_prep,
    choice9
])

choice11 = OperatorPOWL(operator=Operator.XOR, children=[
    label_printing,
    choice10
])

choice12 = OperatorPOWL(operator=Operator.XOR, children=[
    distribution_plan,
    choice11
])

choice13 = OperatorPOWL(operator=Operator.XOR, children=[
    retail_delivery,
    choice12
])

choice14 = OperatorPOWL(operator=Operator.XOR, children=[
    event_coordination,
    choice13
])

choice15 = OperatorPOWL(operator=Operator.XOR, children=[
    regulatory_audit,
    choice14
])

# Create the root of the POWL model
root = StrictPartialOrder(nodes=[
    choice15,
    choice14,
    choice13,
    choice12,
    choice11,
    choice10,
    choice9,
    choice8,
    choice7,
    choice6,
    choice5,
    choice4,
    choice3,
    choice2,
    choice1,
    milk_sourcing
])

# Add the necessary dependencies (edges) to the POWL model
root.order.add_edge(milk_sourcing, choice1)
root.order.add_edge(choice1, choice2)
root.order.add_edge(choice2, choice3)
root.order.add_edge(choice3, choice4)
root.order.add_edge(choice4, choice5)
root.order.add_edge(choice5, choice6)
root.order.add_edge(choice6, choice7)
root.order.add_edge(choice7, choice8)
root.order.add_edge(choice8, choice9)
root.order.add_edge(choice9, choice10)
root.order.add_edge(choice10, choice11)
root.order.add_edge(choice11, choice12)
root.order.add_edge(choice12, choice13)
root.order.add_edge(choice13, choice14)
root.order.add_edge(choice14, choice15)

# Print the root of the POWL model
print(root)