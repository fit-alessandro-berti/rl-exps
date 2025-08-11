from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define transitions for each activity
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

# Define silent transitions (empty labels)
skip = SilentTransition()

# Define partial orders for each stage of the process
milk_testing_loop = OperatorPOWL(operator=Operator.LOOP, children=[milk_sourcing, culture_selection])
aging_setup_loop = OperatorPOWL(operator=Operator.LOOP, children=[aging_setup, climate_control, quality_tasting])
distribution_plan_loop = OperatorPOWL(operator=Operator.LOOP, children=[distribution_plan, retail_delivery, event_coordination])
regulatory_audit_loop = OperatorPOWL(operator=Operator.LOOP, children=[regulatory_audit])

# Define exclusive choice for cheese production stages
cheese_production_exclusive = OperatorPOWL(operator=Operator.XOR, children=[milk_testing_loop, aging_setup_loop, distribution_plan_loop, regulatory_audit_loop])

# Define root POWL model
root = StrictPartialOrder(nodes=[cheese_production_exclusive])
root.order.add_edge(cheese_production_exclusive, milk_testing_loop)
root.order.add_edge(cheese_production_exclusive, aging_setup_loop)
root.order.add_edge(cheese_production_exclusive, distribution_plan_loop)
root.order.add_edge(cheese_production_exclusive, regulatory_audit_loop)