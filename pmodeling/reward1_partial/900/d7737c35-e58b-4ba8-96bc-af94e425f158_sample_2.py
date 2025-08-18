from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define the activities
milk_sourcing = Transition(label='Milk Sourcing')
supplier_audit = Transition(label='Supplier Audit')
culture_prep = Transition(label='Culture Prep')
milk_testing = Transition(label='Milk Testing')
fermentation_start = Transition(label='Fermentation Start')
pH_monitoring = Transition(label='pH Monitoring')
curd_cutting = Transition(label='Curd Cutting')
mold_inoculation = Transition(label='Mold Inoculation')
aging_setup = Transition(label='Aging Setup')
humidity_control = Transition(label='Humidity Control')
texture_check = Transition(label='Texture Check')
flavor_profiling = Transition(label='Flavor Profiling')
batch_labeling = Transition(label='Batch Labeling')
packaging = Transition(label='Packaging')
distribution = Transition(label='Distribution')
feedback_review = Transition(label='Feedback Review')
sustainability_audit = Transition(label='Sustainability Audit')

# Define the loop nodes
aging_loop = OperatorPOWL(operator=Operator.LOOP, children=[texture_check, flavor_profiling, batch_labeling])
aging_loop2 = OperatorPOWL(operator=Operator.LOOP, children=[packaging, distribution, feedback_review])
sustainability_audit_loop = OperatorPOWL(operator=Operator.LOOP, children=[sustainability_audit])

# Define the partial order
root = StrictPartialOrder(nodes=[milk_sourcing, supplier_audit, culture_prep, milk_testing, fermentation_start, pH_monitoring, curd_cutting, mold_inoculation, aging_setup, humidity_control, aging_loop, aging_loop2, sustainability_audit_loop])
root.order.add_edge(milk_sourcing, supplier_audit)
root.order.add_edge(supplier_audit, culture_prep)
root.order.add_edge(culture_prep, milk_testing)
root.order.add_edge(milk_testing, fermentation_start)
root.order.add_edge(fermentation_start, pH_monitoring)
root.order.add_edge(pH_monitoring, curd_cutting)
root.order.add_edge(curd_cutting, mold_inoculation)
root.order.add_edge(mold_inoculation, aging_setup)
root.order.add_edge(aging_setup, humidity_control)
root.order.add_edge(humidity_control, aging_loop)
root.order.add_edge(aging_loop, aging_loop2)
root.order.add_edge(aging_loop2, sustainability_audit_loop)
root.order.add_edge(sustainability_audit_loop, sustainability_audit)

print(root)