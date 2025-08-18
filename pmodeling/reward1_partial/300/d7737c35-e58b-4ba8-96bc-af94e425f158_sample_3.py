from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
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

# Define loops and exclusive choices
# Milk Sourcing Loop
milk_sourcing_loop = OperatorPOWL(operator=Operator.LOOP, children=[milk_sourcing])

# Supplier Audit Loop
supplier_audit_loop = OperatorPOWL(operator=Operator.LOOP, children=[supplier_audit])

# Culture Prep Loop
culture_prep_loop = OperatorPOWL(operator=Operator.LOOP, children=[culture_prep])

# Milk Testing Loop
milk_testing_loop = OperatorPOWL(operator=Operator.LOOP, children=[milk_testing])

# Fermentation Start Loop
fermentation_start_loop = OperatorPOWL(operator=Operator.LOOP, children=[fermentation_start])

# pH Monitoring Loop
pH_monitoring_loop = OperatorPOWL(operator=Operator.LOOP, children=[pH_monitoring])

# Curd Cutting Loop
curd_cutting_loop = OperatorPOWL(operator=Operator.LOOP, children=[curd_cutting])

# Mold Inoculation Loop
mold_inoculation_loop = OperatorPOWL(operator=Operator.LOOP, children=[mold_inoculation])

# Aging Setup Loop
aging_setup_loop = OperatorPOWL(operator=Operator.LOOP, children=[aging_setup])

# Humidity Control Loop
humidity_control_loop = OperatorPOWL(operator=Operator.LOOP, children=[humidity_control])

# Texture Check Loop
texture_check_loop = OperatorPOWL(operator=Operator.LOOP, children=[texture_check])

# Flavor Profiling Loop
flavor_profiling_loop = OperatorPOWL(operator=Operator.LOOP, children=[flavor_profiling])

# Batch Labeling Loop
batch_labeling_loop = OperatorPOWL(operator=Operator.LOOP, children=[batch_labeling])

# Packaging Loop
packaging_loop = OperatorPOWL(operator=Operator.LOOP, children=[packaging])

# Distribution Loop
distribution_loop = OperatorPOWL(operator=Operator.LOOP, children=[distribution])

# Feedback Review Loop
feedback_review_loop = OperatorPOWL(operator=Operator.LOOP, children=[feedback_review])

# Sustainability Audit Loop
sustainability_audit_loop = OperatorPOWL(operator=Operator.LOOP, children=[sustainability_audit])

# Define exclusive choices
# Milk Sourcing - Supplier Audit
milk_sourcing_supplier_audit = OperatorPOWL(operator=Operator.XOR, children=[milk_sourcing, supplier_audit])

# Culture Prep - Milk Testing
culture_prep_milk_testing = OperatorPOWL(operator=Operator.XOR, children=[culture_prep, milk_testing])

# Fermentation Start - pH Monitoring
fermentation_start_pH_monitoring = OperatorPOWL(operator=Operator.XOR, children=[fermentation_start, pH_monitoring])

# Curd Cutting - Mold Inoculation
curd_cutting_mold_inoculation = OperatorPOWL(operator=Operator.XOR, children=[curd_cutting, mold_inoculation])

# Aging Setup - Humidity Control
aging_setup_humidity_control = OperatorPOWL(operator=Operator.XOR, children=[aging_setup, humidity_control])

# Texture Check - Flavor Profiling
texture_check_flavor_profiling = OperatorPOWL(operator=Operator.XOR, children=[texture_check, flavor_profiling])

# Batch Labeling - Packaging
batch_labeling_packaging = OperatorPOWL(operator=Operator.XOR, children=[batch_labeling, packaging])

# Distribution - Feedback Review
distribution_feedback_review = OperatorPOWL(operator=Operator.XOR, children=[distribution, feedback_review])

# Feedback Review - Sustainability Audit
feedback_review_sustainability_audit = OperatorPOWL(operator=Operator.XOR, children=[feedback_review, sustainability_audit])

# Define the root POWL model
root = StrictPartialOrder(nodes=[
    milk_sourcing_loop,
    supplier_audit_loop,
    culture_prep_loop,
    milk_testing_loop,
    fermentation_start_loop,
    pH_monitoring_loop,
    curd_cutting_loop,
    mold_inoculation_loop,
    aging_setup_loop,
    humidity_control_loop,
    texture_check_loop,
    flavor_profiling_loop,
    batch_labeling_loop,
    packaging_loop,
    distribution_loop,
    feedback_review_loop,
    sustainability_audit_loop,
    milk_sourcing_supplier_audit,
    culture_prep_milk_testing,
    fermentation_start_pH_monitoring,
    curd_cutting_mold_inoculation,
    aging_setup_humidity_control,
    texture_check_flavor_profiling,
    batch_labeling_packaging,
    distribution_feedback_review,
    feedback_review_sustainability_audit
])

# Add dependencies between nodes
root.order.add_edge(milk_sourcing_loop, supplier_audit_loop)
root.order.add_edge(supplier_audit_loop, culture_prep_loop)
root.order.add_edge(culture_prep_loop, milk_testing_loop)
root.order.add_edge(milk_testing_loop, fermentation_start_loop)
root.order.add_edge(fermentation_start_loop, pH_monitoring_loop)
root.order.add_edge(pH_monitoring_loop, curd_cutting_loop)
root.order.add_edge(curd_cutting_loop, mold_inoculation_loop)
root.order.add_edge(mold_inoculation_loop, aging_setup_loop)
root.order.add_edge(aging_setup_loop, humidity_control_loop)
root.order.add_edge(humidity_control_loop, texture_check_loop)
root.order.add_edge(texture_check_loop, flavor_profiling_loop)
root.order.add_edge(flavor_profiling_loop, batch_labeling_loop)
root.order.add_edge(batch_labeling_loop, packaging_loop)
root.order.add_edge(packaging_loop, distribution_loop)
root.order.add_edge(distribution_loop, feedback_review_loop)
root.order.add_edge(feedback_review_loop, sustainability_audit_loop)
root.order.add_edge(milk_sourcing_loop, milk_sourcing_supplier_audit)
root.order.add_edge(culture_prep_loop, culture_prep_milk_testing)
root.order.add_edge(fermentation_start_loop, fermentation_start_pH_monitoring)
root.order.add_edge(curd_cutting_loop, curd_cutting_mold_inoculation)
root.order.add_edge(aging_setup_loop, aging_setup_humidity_control)
root.order.add_edge(texture_check_loop, texture_check_flavor_profiling)
root.order.add_edge(batch_labeling_loop, batch_labeling_packaging)
root.order.add_edge(distribution_loop, distribution_feedback_review)
root.order.add_edge(feedback_review_loop, feedback_review_sustainability_audit)

print(root)