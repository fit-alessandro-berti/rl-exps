import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
Milk_Sourcing = Transition(label='Milk Sourcing')
Supplier_Audit = Transition(label='Supplier Audit')
Culture_Prep = Transition(label='Culture Prep')
Milk_Testing = Transition(label='Milk Testing')
Fermentation_Start = Transition(label='Fermentation Start')
pH_Monitoring = Transition(label='pH Monitoring')
Curd_Cutting = Transition(label='Curd Cutting')
Mold_Inoculation = Transition(label='Mold Inoculation')
Aging_Setup = Transition(label='Aging Setup')
Humidity_Control = Transition(label='Humidity Control')
Texture_Check = Transition(label='Texture Check')
Flavor_Profiling = Transition(label='Flavor Profiling')
Batch_Labeling = Transition(label='Batch Labeling')
Packaging = Transition(label='Packaging')
Distribution = Transition(label='Distribution')
Feedback_Review = Transition(label='Feedback Review')
Sustainability_Audit = Transition(label='Sustainability Audit')

# Define the partial order
root = StrictPartialOrder(nodes=[
    Milk_Sourcing, Supplier_Audit, Culture_Prep, Milk_Testing, Fermentation_Start, pH_Monitoring,
    Curd_Cutting, Mold_Inoculation, Aging_Setup, Humidity_Control, Texture_Check, Flavor_Profiling,
    Batch_Labeling, Packaging, Distribution, Feedback_Review, Sustainability_Audit
])

# Define the order
root.order.add_edge(Milk_Sourcing, Supplier_Audit)
root.order.add_edge(Supplier_Audit, Culture_Prep)
root.order.add_edge(Culture_Prep, Milk_Testing)
root.order.add_edge(Milk_Testing, Fermentation_Start)
root.order.add_edge(Fermentation_Start, pH_Monitoring)
root.order.add_edge(pH_Monitoring, Curd_Cutting)
root.order.add_edge(Curd_Cutting, Mold_Inoculation)
root.order.add_edge(Mold_Inoculation, Aging_Setup)
root.order.add_edge(Aging_Setup, Humidity_Control)
root.order.add_edge(Humidity_Control, Texture_Check)
root.order.add_edge(Texture_Check, Flavor_Profiling)
root.order.add_edge(Flavor_Profiling, Batch_Labeling)
root.order.add_edge(Batch_Labeling, Packaging)
root.order.add_edge(Packaging, Distribution)
root.order.add_edge(Distribution, Feedback_Review)
root.order.add_edge(Feedback_Review, Sustainability_Audit)

# Print the root
print(root)