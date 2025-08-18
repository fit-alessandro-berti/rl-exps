import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
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

# Define the partial order
root = StrictPartialOrder(nodes=[
    Milk_Sourcing,
    Culture_Selection,
    Milk_Testing,
    Curd_Cutting,
    Whey_Draining,
    Mold_Inoculation,
    Forming_Cheese,
    Salting_Stage,
    Aging_Setup,
    Climate_Control,
    Quality_Tasting,
    Packaging_Prep,
    Label_Printing,
    Distribution_Plan,
    Retail_Delivery,
    Event_Coordination,
    Regulatory_Audit
])

# Define the dependencies between nodes
root.order.add_edge(Milk_Sourcing, Culture_Selection)
root.order.add_edge(Culture_Selection, Milk_Testing)
root.order.add_edge(Milk_Testing, Curd_Cutting)
root.order.add_edge(Curd_Cutting, Whey_Draining)
root.order.add_edge(Whey_Draining, Mold_Inoculation)
root.order.add_edge(Mold_Inoculation, Forming_Cheese)
root.order.add_edge(Forming_Cheese, Salting_Stage)
root.order.add_edge(Salting_Stage, Aging_Setup)
root.order.add_edge(Aging_Setup, Climate_Control)
root.order.add_edge(Climate_Control, Quality_Tasting)
root.order.add_edge(Quality_Tasting, Packaging_Prep)
root.order.add_edge(Packaging_Prep, Label_Printing)
root.order.add_edge(Label_Printing, Distribution_Plan)
root.order.add_edge(Distribution_Plan, Retail_Delivery)
root.order.add_edge(Retail_Delivery, Event_Coordination)
root.order.add_edge(Event_Coordination, Regulatory_Audit)

# Print the final POWL model
print(root)