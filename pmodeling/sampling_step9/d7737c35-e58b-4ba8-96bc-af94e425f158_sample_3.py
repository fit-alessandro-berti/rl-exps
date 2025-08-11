import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model for the artisan cheese production process
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

skip = SilentTransition()

# Define the process steps
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[Milk_Testing, pH_Monitoring, Curd_Cutting, Mold_Inoculation, Aging_Setup, Humidity_Control])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[Texture_Check, Flavor_Profiling, Batch_Labeling])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[Packaging, Distribution, Feedback_Review])
loop4 = OperatorPOWL(operator=Operator.LOOP, children=[Sustainability_Audit])

# Define the exclusive choice between Supplier_Audit and Culture_Prep
xor = OperatorPOWL(operator=Operator.XOR, children=[Supplier_Audit, Culture_Prep])

# Define the root node of the POWL model
root = StrictPartialOrder(nodes=[xor, loop1, loop2, loop3, loop4])
root.order.add_edge(xor, loop1)
root.order.add_edge(xor, loop2)
root.order.add_edge(xor, loop3)
root.order.add_edge(xor, loop4)