from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

milk_sourcing = Transition(label='Milk Sourcing')
farm_selection = Transition(label='Farm Selection')
quality_testing = Transition(label='Quality Testing')
milk_pasturize = Transition(label='Milk Pasteurize')
starter_culture = Transition(label='Starter Culture')
coagulation = Transition(label='Coagulation')
curd_cutting = Transition(label='Curd Cutting')
whey_draining = Transition(label='Whey Draining')
mold_inoculate = Transition(label='Mold Inoculate')
aging_control = Transition(label='Aging Control')
flavor_tasting = Transition(label='Flavor Tasting')
packaging_design = Transition(label='Packaging Design')
label_approval = Transition(label='Label Approval')
inventory_audit = Transition(label='Inventory Audit')
order_fulfill = Transition(label='Order Fulfill')
retail_shipping = Transition(label='Retail Shipping')

# Define the partial order and the dependencies between activities
root = StrictPartialOrder(
    nodes=[
        milk_sourcing, 
        farm_selection, 
        quality_testing, 
        milk_pasturize, 
        starter_culture, 
        coagulation, 
        curd_cutting, 
        whey_draining, 
        mold_inoculate, 
        aging_control, 
        flavor_tasting, 
        packaging_design, 
        label_approval, 
        inventory_audit, 
        order_fulfill, 
        retail_shipping
    ]
)

# Define the dependencies between activities
root.order.add_edge(milk_sourcing, farm_selection)
root.order.add_edge(farm_selection, quality_testing)
root.order.add_edge(quality_testing, milk_pasturize)
root.order.add_edge(milk_pasturize, starter_culture)
root.order.add_edge(starter_culture, coagulation)
root.order.add_edge(coagulation, curd_cutting)
root.order.add_edge(curd_cutting, whey_draining)
root.order.add_edge(whey_draining, mold_inoculate)
root.order.add_edge(mold_inoculate, aging_control)
root.order.add_edge(aging_control, flavor_tasting)
root.order.add_edge(flavor_tasting, packaging_design)
root.order.add_edge(packaging_design, label_approval)
root.order.add_edge(label_approval, inventory_audit)
root.order.add_edge(inventory_audit, order_fulfill)
root.order.add_edge(order_fulfill, retail_shipping)

# Define the loop for inventory audit and order fulfill
inventory_audit_loop = OperatorPOWL(operator=Operator.LOOP, children=[inventory_audit, order_fulfill])
root.order.add_edge(inventory_audit, inventory_audit_loop)
root.order.add_edge(inventory_audit_loop, inventory_audit)
root.order.add_edge(order_fulfill, inventory_audit_loop)
root.order.add_edge(inventory_audit_loop, order_fulfill)

# Define the exclusive choice for retail shipping and inventory audit
exclusive_choice = OperatorPOWL(operator=Operator.XOR, children=[retail_shipping, inventory_audit_loop])
root.order.add_edge(retail_shipping, exclusive_choice)
root.order.add_edge(exclusive_choice, retail_shipping)
root.order.add_edge(inventory_audit_loop, exclusive_choice)

# Define the exclusive choice for aging control and flavor tasting
aging_control_tasting_choice = OperatorPOWL(operator=Operator.XOR, children=[aging_control, flavor_tasting])
root.order.add_edge(aging_control, aging_control_tasting_choice)
root.order.add_edge(aging_control_tasting_choice, aging_control)
root.order.add_edge(flavor_tasting, aging_control_tasting_choice)
root.order.add_edge(aging_control_tasting_choice, flavor_tasting)

# Define the exclusive choice for mold inoculate and aging control
mold_inoculate_aging_control_choice = OperatorPOWL(operator=Operator.XOR, children=[mold_inoculate, aging_control])
root.order.add_edge(mold_inoculate, mold_inoculate_aging_control_choice)
root.order.add_edge(mold_inoculate_aging_control_choice, mold_inoculate)
root.order.add_edge(aging_control, mold_inoculate_aging_control_choice)
root.order.add_edge(mold_inoculate_aging_control_choice, aging_control)

# Define the exclusive choice for curd cutting and whey draining
curd_cutting_whey_draining_choice = OperatorPOWL(operator=Operator.XOR, children=[curd_cutting, whey_draining])
root.order.add_edge(curd_cutting, curd_cutting_whey_draining_choice)
root.order.add_edge(curd_cutting_whey_draining_choice, curd_cutting)
root.order.add_edge(whey_draining, curd_cutting_whey_draining_choice)
root.order.add_edge(curd_cutting_whey_draining_choice, whey_draining)

# Define the exclusive choice for coagulation and starter culture
coagulation_starter_culture_choice = OperatorPOWL(operator=Operator.XOR, children=[coagulation, starter_culture])
root.order.add_edge(coagulation, coagulation_starter_culture_choice)
root.order.add_edge(coagulation_starter_culture_choice, coagulation)
root.order.add_edge(starter_culture, coagulation_starter_culture_choice)
root.order.add_edge(coagulation_starter_culture_choice, starter_culture)

# Define the exclusive choice for milk pasturize and milk sourcing
milk_pasturize_milk_sourcing_choice = OperatorPOWL(operator=Operator.XOR, children=[milk_pasturize, milk_sourcing])
root.order.add_edge(milk_pasturize, milk_pasturize_milk_sourcing_choice)
root.order.add_edge(milk_pasturize_milk_sourcing_choice, milk_pasturize)
root.order.add_edge(milk_sourcing, milk_pasturize_milk_sourcing_choice)
root.order.add_edge(milk_pasturize_milk_sourcing_choice, milk_sourcing)

# Define the exclusive choice for farm selection and milk sourcing
farm_selection_milk_sourcing_choice = OperatorPOWL(operator=Operator.XOR, children=[farm_selection, milk_sourcing])
root.order.add_edge(farm_selection, farm_selection_milk_sourcing_choice)
root.order.add_edge(farm_selection_milk_sourcing_choice, farm_selection)
root.order.add_edge(milk_sourcing, farm_selection_milk_sourcing_choice)
root.order.add_edge(farm_selection_milk_sourcing_choice, milk_sourcing)

# Define the exclusive choice for quality testing and milk sourcing
quality_testing_milk_sourcing_choice = OperatorPOWL(operator=Operator.XOR, children=[quality_testing, milk_sourcing])
root.order.add_edge(quality_testing, quality_testing_milk_sourcing_choice)
root.order.add_edge(quality_testing_milk_sourcing_choice, quality_testing)
root.order.add_edge(milk_sourcing, quality_testing_milk_sourcing_choice)
root.order.add_edge(quality_testing_milk_sourcing_choice, milk_sourcing)

# Define the exclusive choice for milk sourcing and farm selection
milk_sourcing_farm_selection_choice = OperatorPOWL(operator=Operator.XOR, children=[milk_sourcing, farm_selection])
root.order.add_edge(milk_sourcing, milk_sourcing_farm_selection_choice)
root.order.add_edge(milk_sourcing_farm_selection_choice, milk_sourcing)
root.order.add_edge(farm_selection, milk_sourcing_farm_selection_choice)
root.order.add_edge(milk_sourcing_farm_selection_choice, farm_selection)

# Define the exclusive choice for milk sourcing and quality testing
milk_sourcing_quality_testing_choice = OperatorPOWL(operator=Operator.XOR, children=[milk_sourcing, quality_testing])
root.order.add_edge(milk_sourcing, milk_sourcing_quality_testing_choice)
root.order.add_edge(milk_sourcing_quality_testing_choice, milk_sourcing)
root.order.add_edge(quality_testing, milk_sourcing_quality_testing_choice)
root.order.add_edge(milk_sourcing_quality_testing_choice, quality_testing)

# Define the exclusive choice for milk sourcing and milk pasturize
milk_sourcing_milk_pasturize_choice = OperatorPOWL(operator=Operator.XOR, children=[milk_sourcing, milk_pasturize])
root.order.add_edge(milk_sourcing, milk_sourcing_milk_pasturize_choice)
root.order.add_edge(milk_sourcing_milk_pasturize_choice, milk_sourcing)
root.order.add_edge(milk_pasturize, milk_sourcing_milk_pasturize_choice)
root.order.add_edge(milk_sourcing_milk_pasturize_choice, milk_pasturize)

# Define the exclusive choice for milk sourcing and farm selection
milk_sourcing_farm_selection_choice = OperatorPOWL(operator=Operator.XOR, children=[milk_sourcing, farm_selection])
root.order.add_edge(milk_sourcing, milk_sourcing_farm_selection_choice)
root.order.add_edge(milk_sourcing_farm_selection_choice, milk_sourcing)
root.order.add_edge(farm_selection, milk_sourcing_farm_selection_choice)
root.order.add_edge(milk_sourcing_farm_selection_choice, farm_selection)

# Define the exclusive choice for milk sourcing and quality testing
milk_sourcing_quality_testing_choice = OperatorPOWL(operator=Operator.XOR, children=[milk_sourcing, quality_testing])
root.order.add_edge(milk_sourcing, milk_sourcing_quality_testing_choice)
root.order.add_edge(milk_sourcing_quality_testing_choice, milk_sourcing)
root.order.add_edge(quality_testing, milk_sourcing_quality_testing_choice)
root.order.add_edge(milk_sourcing_quality_testing_choice, quality_testing)

# Define the exclusive choice for milk sourcing and milk pasturize
milk_sourcing_milk_pasturize_choice = OperatorPOWL(operator=Operator.XOR, children=[milk_sourcing, milk_pasturize])
root.order.add_edge(milk_sourcing, milk_sourcing_milk_pasturize_choice)
root.order.add_edge(milk_sourcing_milk_pasturize_choice, milk_sourcing)
root.order.add_edge(milk_pasturize, milk_sourcing_milk_pasturize_choice)
root.order.add_edge(milk_sourcing_milk_pasturize_choice, milk_pasturize)

# Define the exclusive choice for milk sourcing and farm selection
milk_sourcing_farm_selection_choice = OperatorPOWL(operator=Operator.XOR, children=[milk_sourcing, farm_selection])
root.order.add_edge(milk_sourcing, milk_sourcing_farm_selection_choice)
root.order.add_edge(milk_sourcing_farm_selection_choice, milk_sourcing)
root.order.add_edge(farm_selection, milk_sourcing_farm_selection_choice)
root.order.add_edge(milk_sourcing_farm_selection_choice, farm_selection)

# Define the exclusive choice for milk sourcing and quality testing
milk_sourcing_quality_testing_choice = OperatorPOWL(operator=Operator.XOR, children=[milk_sourcing, quality_testing])
root.order.add_edge(milk_sourcing, milk_sourcing_quality_testing_choice)
root.order.add_edge(milk_sourcing_quality_testing_choice, milk_sourcing)
root.order.add_edge(quality_testing, milk_sourcing_quality_testing_choice)
root.order.add_edge(milk_sourcing_quality_testing_choice, quality_testing)

# Define the exclusive choice for milk sourcing and milk pasturize
milk_sourcing_milk_pasturize_choice = OperatorPOWL(operator=Operator.XOR, children=[milk_sourcing, milk_pasturize])
root.order.add_edge(milk_sourcing, milk_sourcing_milk_pasturize_choice)
root.order.add_edge(milk_sourcing_milk_pasturize_choice, milk_sourcing)
root.order.add_edge(milk_pasturize, milk_sourcing_milk_pasturize_choice)
root.order.add_edge(milk_sourcing_milk_pasturize_choice, milk_pasturize)

# Define the exclusive choice for milk sourcing and farm selection
milk_sourcing_farm_selection_choice = OperatorPOWL(operator=Operator.XOR, children=[milk_sourcing, farm_selection])
root.order.add_edge(milk_sourcing, milk_sourcing_farm_selection_choice)
root.order.add_edge(milk_sourcing_farm_selection_choice, milk_sourcing)
root.order.add_edge(farm_selection, milk_sourcing_farm_selection_choice)
root.order.add_edge(milk_sourcing_farm_selection_choice, farm_selection)

# Define the exclusive choice for milk sourcing and quality testing
milk_sourcing_quality_testing_choice = OperatorPOWL(operator=Operator.XOR, children=[milk_sourcing, quality_testing])
root.order.add_edge(milk_sourcing, milk_sourcing_quality_testing_choice)
root.order.add_edge(milk_sourcing_quality_testing_choice, milk_sourcing)
root.order.add_edge(quality_testing, milk_sourcing_quality_testing_choice)
root.order.add_edge(milk_sourcing_quality_testing_choice, quality_testing)

# Define the exclusive choice for milk sourcing and milk pasturize
milk_sourcing_milk_pasturize_choice = OperatorPOWL(operator=Operator.XOR, children=[milk_sourcing, milk_pasturize])
root.order.add_edge(milk_sourcing, milk_sourcing_milk_pasturize_choice)
root.order.add_edge(milk_sourcing_milk_pasturize_choice, milk_sourcing)
root.order.add_edge(milk_pasturize, milk_sourcing_milk_pasturize_choice)
root.order.add_edge(milk_sourcing_milk_pasturize_choice, milk_pasturize)

# Define the exclusive choice for milk sourcing and farm selection
milk_sourcing_farm_selection_choice = OperatorPOWL(operator=Operator.XOR, children=[milk_sourcing, farm_selection])
root.order.add_edge(milk_sourcing, milk_sourcing_farm_selection_choice)
root.order.add_edge(milk_sourcing_farm_selection_choice, milk_sourcing)
root.order.add_edge(farm_selection, milk_sourcing_farm_selection_choice)
root.order.add_edge(milk_sourcing_farm_selection_choice, farm_selection)

# Define the exclusive choice for milk sourcing and quality testing
milk_sourcing_quality_testing_choice = OperatorPOWL(operator=Operator.XOR, children=[milk_sourcing, quality_testing])
root.order.add_edge(milk_sourcing, milk_sourcing_quality_testing_choice)
root.order.add_edge(milk_sourcing_quality_testing_choice, milk_sourcing)
root.order.add_edge(quality_testing, milk_sourcing_quality_testing_choice)
root.order.add_edge(milk_sourcing_quality_testing_choice, quality_testing)

# Define the exclusive choice for milk sourcing and milk pasturize
milk_sourcing_milk_pasturize_choice = OperatorPOWL(operator=Operator.XOR, children=[milk_sourcing, milk_pasturize])
root.order.add_edge(milk_sourcing, milk_sourcing_milk_pasturize_choice)
root.order.add_edge(milk_sourcing_milk_pasturize_choice, milk_sourcing)
root.order.add_edge(milk_pasturize, milk_sourcing_milk_pasturize_choice)
root.order.add_edge(milk_sourcing_milk_pasturize_choice, milk_pasturize)

# Define the exclusive choice for milk sourcing and farm selection
milk_sourcing_farm_selection_choice = OperatorPOWL(operator=Operator.XOR, children=[milk_sourcing, farm_selection])
root.order.add_edge(milk_sourcing, milk_sourcing_farm_selection_choice)
root.order.add_edge(milk_sourcing_farm_selection_choice, milk_sourcing)
root.order.add_edge(farm_selection, milk_sourcing_farm_selection_choice)
root.order.add_edge(milk_sourcing_farm_selection_choice, farm_selection)

# Define the exclusive choice for milk sourcing and quality testing
milk_sourcing_quality_testing_choice = OperatorPOWL(operator=Operator.XOR, children=[milk_sourcing, quality_testing])
root.order.add_edge(milk_sourcing, milk_sourcing_quality_testing_choice)
root.order.add_edge(milk_sourcing_quality_testing_choice, milk_sourcing)
root.order.add_edge(quality_testing, milk_sourcing_quality_testing_choice)
root.order.add_edge(milk_sourcing_quality_testing_choice, quality_testing)

# Define the exclusive choice for milk sourcing and milk pasturize
milk_sourcing_milk_pasturize_choice = OperatorPOWL(operator=Operator.XOR, children=[milk_sourcing, milk_pasturize])
root.order.add_edge(milk_sourcing, milk_sourcing_milk_pasturize_choice)
root.order.add_edge(milk_sourcing_milk_pasturize_choice, milk_sourcing)
root.order.add_edge(milk_pasturize, milk_sourcing_milk_pasturize_choice)
root.order.add_edge(milk_sourcing_milk_pasturize_choice, milk_pasturize)

# Define the exclusive choice for milk sourcing and farm selection
milk_sourcing_farm_selection_choice = OperatorPOWL(operator=Operator.XOR, children=[milk_sourcing, farm_selection])
root.order.add_edge(milk_sourcing, milk_sourcing_farm_selection_choice)
root.order.add_edge(milk_sourcing_farm_selection_choice, milk_sourcing)
root.order.add_edge(farm_selection, milk_sourcing_farm_selection_choice)
root.order.add_edge(milk_sourcing_farm_selection_choice, farm_selection)

# Define the exclusive choice for milk sourcing and quality testing
milk_sourcing_quality_testing_choice = OperatorPOWL(operator=Operator.XOR, children=[milk_sourcing, quality_testing])
root.order.add_edge(milk_sourcing, milk_sourcing_quality_testing_choice)
root.order.add_edge(milk_sourcing_quality_testing_choice, milk_sourcing)
root.order.add_edge(quality_testing, milk_sourcing_quality_testing_choice)
root.order.add_edge(milk_sourcing_quality_testing_choice, quality_testing)

# Define the exclusive choice for milk sourcing and milk pasturize
milk_sourcing_milk_pasturize_choice = OperatorPOWL(operator=Operator.XOR, children=[milk_sourcing, milk_pasturize])
root.order.add_edge(milk_sourcing, milk_sourcing_milk_pasturize_choice)
root.order.add_edge(milk_sourcing_milk_pasturize_choice, milk_sourcing)
root.order.add_edge(milk_pasturize, milk_sourcing_milk_pasturize_choice)
root.order.add_edge(milk_sourcing_milk_pasturize_choice, milk_pasturize)

# Define the exclusive choice for milk sourcing and farm selection
milk_sourcing_farm_selection_choice = OperatorPOWL(operator=Operator.XOR, children=[milk_sourcing, farm_selection])
root.order.add_edge(milk_sourcing, milk_sourcing_farm_selection_choice)
root.order.add_edge(milk_sourcing_farm_selection_choice, milk_sourcing)
root.order.add_edge(farm_selection, milk_sourcing_farm_selection_choice)
root.order.add_edge(milk_sourcing_farm_selection_choice, farm_selection)

# Define the exclusive choice for milk sourcing and quality testing
milk_sourcing_quality_testing_choice = OperatorPOWL(operator=Operator.XOR, children=[milk_sourcing, quality_testing])
root.order.add_edge(milk_sourcing, milk_sourcing_quality_testing_choice)
root.order.add_edge(milk_sourcing_quality_testing_choice, milk_sourcing)
root.order.add_edge(quality_testing, milk_sourcing_quality_testing_choice)
root.order.add_edge(milk_sourcing_quality_testing_choice, quality_testing)

# Define the exclusive choice for milk sourcing and milk pasturize
milk_sourcing_milk_pasturize_choice = OperatorPOWL(operator=Operator.XOR, children=[milk_sourcing, milk_pasturize])
root.order.add_edge(milk_sourcing, milk_sourcing_milk_pasturize_choice)
root.order.add_edge(milk_sourcing_milk_pasturize_choice, milk_sourcing)
root.order.add_edge(milk_pasturize, milk_sourcing_milk_pasturize_choice)
root.order.add_edge(milk_sourcing_milk_pasturize_choice, milk_pasturize)

#