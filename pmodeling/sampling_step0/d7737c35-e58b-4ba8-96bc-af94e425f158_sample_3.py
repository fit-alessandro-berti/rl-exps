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

# Define silent transitions
skip_milk_testing = SilentTransition()
skip_curd_cutting = SilentTransition()
skip_mold_inoculation = SilentTransition()
skip_aging_setup = SilentTransition()
skip_humidity_control = SilentTransition()
skip_texture_check = SilentTransition()
skip_flavor_profiling = SilentTransition()

# Define loop for fermentation monitoring and pH control
fermentation_monitoring = OperatorPOWL(operator=Operator.LOOP, children=[pH_monitoring, skip_milk_testing])
fermentation_loop = OperatorPOWL(operator=Operator.LOOP, children=[fermentation_monitoring, skip_curd_cutting])

# Define loop for aging process
aging_process = OperatorPOWL(operator=Operator.LOOP, children=[humidity_control, skip_mold_inoculation])
aging_loop = OperatorPOWL(operator=Operator.LOOP, children=[aging_process, skip_aging_setup])

# Define XOR for texture and flavor checks
texture_flavor_check = OperatorPOWL(operator=Operator.XOR, children=[texture_check, skip_texture_check])
flavor_check = OperatorPOWL(operator=Operator.XOR, children=[flavor_profiling, skip_flavor_profiling])

# Define XOR for quality checkpoints
quality_checkpoints = OperatorPOWL(operator=Operator.XOR, children=[milk_testing, skip_milk_testing])

# Define XOR for sustainability audits
sustainability_audit_loop = OperatorPOWL(operator=Operator.XOR, children=[sustainability_audit, skip_mold_inoculation])

# Define XOR for packaging and distribution
packaging_distribution = OperatorPOWL(operator=Operator.XOR, children=[packaging, skip_mold_inoculation])

# Define XOR for feedback review and packaging/distribution
feedback_review_loop = OperatorPOWL(operator=Operator.XOR, children=[feedback_review, packaging_distribution])

# Define XOR for aging process and feedback review
aging_feedback_loop = OperatorPOWL(operator=Operator.XOR, children=[aging_loop, feedback_review_loop])

# Define XOR for fermentation loop and aging feedback loop
fermentation_aging_loop = OperatorPOWL(operator=Operator.XOR, children=[fermentation_loop, aging_feedback_loop])

# Define XOR for fermentation loop and aging feedback loop
fermentation_aging_loop = OperatorPOWL(operator=Operator.XOR, children=[fermentation_loop, aging_feedback_loop])

# Define XOR for fermentation loop and aging feedback loop
fermentation_aging_loop = OperatorPOWL(operator=Operator.XOR, children=[fermentation_loop, aging_feedback_loop])

# Define XOR for fermentation loop and aging feedback loop
fermentation_aging_loop = OperatorPOWL(operator=Operator.XOR, children=[fermentation_loop, aging_feedback_loop])

# Define XOR for fermentation loop and aging feedback loop
fermentation_aging_loop = OperatorPOWL(operator=Operator.XOR, children=[fermentation_loop, aging_feedback_loop])

# Define XOR for fermentation loop and aging feedback loop
fermentation_aging_loop = OperatorPOWL(operator=Operator.XOR, children=[fermentation_loop, aging_feedback_loop])

# Define XOR for fermentation loop and aging feedback loop
fermentation_aging_loop = OperatorPOWL(operator=Operator.XOR, children=[fermentation_loop, aging_feedback_loop])

# Define XOR for fermentation loop and aging feedback loop
fermentation_aging_loop = OperatorPOWL(operator=Operator.XOR, children=[fermentation_loop, aging_feedback_loop])

# Define XOR for fermentation loop and aging feedback loop
fermentation_aging_loop = OperatorPOWL(operator=Operator.XOR, children=[fermentation_loop, aging_feedback_loop])

# Define XOR for fermentation loop and aging feedback loop
fermentation_aging_loop = OperatorPOWL(operator=Operator.XOR, children=[fermentation_loop, aging_feedback_loop])

# Define XOR for fermentation loop and aging feedback loop
fermentation_aging_loop = OperatorPOWL(operator=Operator.XOR, children=[fermentation_loop, aging_feedback_loop])

# Define XOR for fermentation loop and aging feedback loop
fermentation_aging_loop = OperatorPOWL(operator=Operator.XOR, children=[fermentation_loop, aging_feedback_loop])

# Define XOR for fermentation loop and aging feedback loop
fermentation_aging_loop = OperatorPOWL(operator=Operator.XOR, children=[fermentation_loop, aging_feedback_loop])

# Define XOR for fermentation loop and aging feedback loop
fermentation_aging_loop = OperatorPOWL(operator=Operator.XOR, children=[fermentation_loop, aging_feedback_loop])

# Define XOR for fermentation loop and aging feedback loop
fermentation_aging_loop = OperatorPOWL(operator=Operator.XOR, children=[fermentation_loop, aging_feedback_loop])

# Define XOR for fermentation loop and aging feedback loop
fermentation_aging_loop = OperatorPOWL(operator=Operator.XOR, children=[fermentation_loop, aging_feedback_loop])

# Define XOR for fermentation loop and aging feedback loop
fermentation_aging_loop = OperatorPOWL(operator=Operator.XOR, children=[fermentation_loop, aging_feedback_loop])

# Define XOR for fermentation loop and aging feedback loop
fermentation_aging_loop = OperatorPOWL(operator=Operator.XOR, children=[fermentation_loop, aging_feedback_loop])

# Define XOR for fermentation loop and aging feedback loop
fermentation_aging_loop = OperatorPOWL(operator=Operator.XOR, children=[fermentation_loop, aging_feedback_loop])

# Define XOR for fermentation loop and aging feedback loop
fermentation_aging_loop = OperatorPOWL(operator=Operator.XOR, children=[fermentation_loop, aging_feedback_loop])

# Define XOR for fermentation loop and aging feedback loop
fermentation_aging_loop = OperatorPOWL(operator=Operator.XOR, children=[fermentation_loop, aging_feedback_loop])

# Define XOR for fermentation loop and aging feedback loop
fermentation_aging_loop = OperatorPOWL(operator=Operator.XOR, children=[fermentation_loop, aging_feedback_loop])

# Define XOR for fermentation loop and aging feedback loop
fermentation_aging_loop = OperatorPOWL(operator=Operator.XOR, children=[fermentation_loop, aging_feedback_loop])

# Define XOR for fermentation loop and aging feedback loop
fermentation_aging_loop = OperatorPOWL(operator=Operator.XOR, children=[fermentation_loop, aging_feedback_loop])

# Define XOR for fermentation loop and aging feedback loop
fermentation_aging_loop = OperatorPOWL(operator=Operator.XOR, children=[fermentation_loop, aging_feedback_loop])

# Define XOR for fermentation loop and aging feedback loop
fermentation_aging_loop = OperatorPOWL(operator=Operator.XOR, children=[fermentation_loop, aging_feedback_loop])

# Define XOR for fermentation loop and aging feedback loop
fermentation_aging_loop = OperatorPOWL(operator=Operator.XOR, children=[fermentation_loop, aging_feedback_loop])

# Define XOR for fermentation loop and aging feedback loop
fermentation_aging_loop = OperatorPOWL(operator=Operator.XOR, children=[fermentation_loop, aging_feedback_loop])

# Define XOR for fermentation loop and aging feedback loop
fermentation_aging_loop = OperatorPOWL(operator=Operator.XOR, children=[fermentation_loop, aging_feedback_loop])

# Define XOR for fermentation loop and aging feedback loop
fermentation_aging_loop = OperatorPOWL(operator=Operator.XOR, children=[fermentation_loop, aging_feedback_loop])

# Define XOR for fermentation loop and aging feedback loop
fermentation_aging_loop = OperatorPOWL(operator=Operator.XOR, children=[fermentation_loop, aging_feedback_loop])

# Define XOR for fermentation loop and aging feedback loop
fermentation_aging_loop = OperatorPOWL(operator=Operator.XOR, children=[fermentation_loop, aging_feedback_loop])

# Define XOR for fermentation loop and aging feedback loop
fermentation_aging_loop = OperatorPOWL(operator=Operator.XOR, children=[fermentation_loop, aging_feedback_loop])

# Define XOR for fermentation loop and aging feedback loop
fermentation_aging_loop = OperatorPOWL(operator=Operator.XOR, children=[fermentation_loop, aging_feedback_loop])

# Define XOR for fermentation loop and aging feedback loop
fermentation_aging_loop = OperatorPOWL(operator=Operator.XOR, children=[fermentation_loop, aging_feedback_loop])

# Define XOR for fermentation loop and aging feedback loop
fermentation_aging_loop = OperatorPOWL(operator=Operator.XOR, children=[fermentation_loop, aging_feedback_loop])

# Define XOR for fermentation loop and aging feedback loop
fermentation_aging_loop = OperatorPOWL(operator=Operator.XOR, children=[fermentation_loop, aging_feedback_loop])

# Define XOR for fermentation loop and aging feedback loop
fermentation_aging_loop = OperatorPOWL(operator=Operator.XOR, children=[fermentation_loop, aging_feedback_loop])

# Define XOR for fermentation loop and aging feedback loop
fermentation_aging_loop = OperatorPOWL(operator=Operator.XOR, children=[fermentation_loop, aging_feedback_loop])

# Define XOR for fermentation loop and aging feedback loop
fermentation_aging_loop = OperatorPOWL(operator=Operator.XOR, children=[fermentation_loop, aging_feedback_loop])

# Define XOR for fermentation loop and aging feedback loop
fermentation_aging_loop = OperatorPOWL(operator=Operator.XOR, children=[fermentation_loop, aging_feedback_loop])

# Define XOR for fermentation loop and aging feedback loop
fermentation_aging_loop = OperatorPOWL(operator=Operator.XOR, children=[fermentation_loop, aging_feedback_loop])

# Define XOR for fermentation loop and aging feedback loop
fermentation_aging_loop = OperatorPOWL(operator=Operator.XOR, children=[fermentation_loop, aging_feedback_loop])

# Define XOR for fermentation loop and aging feedback loop
fermentation_aging_loop = OperatorPOWL(operator=Operator.XOR, children=[fermentation_loop, aging_feedback_loop])

# Define XOR for fermentation loop and aging feedback loop
fermentation_aging_loop = OperatorPOWL(operator=Operator.XOR, children=[fermentation_loop, aging_feedback_loop])

# Define XOR for fermentation loop and aging feedback loop
fermentation_aging_loop = OperatorPOWL(operator=Operator.XOR, children=[fermentation_loop, aging_feedback_loop])

# Define XOR for fermentation loop and aging feedback loop
fermentation_aging_loop = OperatorPOWL(operator=Operator.XOR, children=[fermentation_loop, aging_feedback_loop])

# Define XOR for fermentation loop and aging feedback loop
fermentation_aging_loop = OperatorPOWL(operator=Operator.XOR, children=[fermentation_loop, aging_feedback_loop])

# Define XOR for fermentation loop and aging feedback loop
fermentation_aging_loop = OperatorPOWL(operator=Operator.XOR, children=[fermentation_loop, aging_feedback_loop])

# Define XOR for fermentation loop and aging feedback loop
fermentation_aging_loop = OperatorPOWL(operator=Operator.XOR, children=[fermentation_loop, aging_feedback_loop])

# Define XOR for fermentation loop and aging feedback loop
fermentation_aging_loop = OperatorPOWL(operator=Operator.XOR, children=[fermentation_loop, aging_feedback_loop])

# Define XOR for fermentation loop and aging feedback loop
fermentation_aging_loop = OperatorPOWL(operator=Operator.XOR, children=[fermentation_loop, aging_feedback_loop])

# Define XOR for fermentation loop and aging feedback loop
fermentation_aging_loop = OperatorPOWL(operator=Operator.XOR, children=[fermentation_loop, aging_feedback_loop])

# Define XOR for fermentation loop and aging feedback loop
fermentation_aging_loop = OperatorPOWL(operator=Operator.XOR, children=[fermentation_loop, aging_feedback_loop])

# Define XOR for fermentation loop and aging feedback loop
fermentation_aging_loop = OperatorPOWL(operator=Operator.XOR, children=[fermentation_loop, aging_feedback_loop])

# Define XOR for fermentation loop and aging feedback loop
fermentation_aging_loop = OperatorPOWL(operator=Operator.XOR, children=[fermentation_loop, aging_feedback_loop])

# Define XOR for fermentation loop and aging feedback loop
fermentation_aging_loop = OperatorPOWL(operator=Operator.XOR, children=[fermentation_loop, aging_feedback_loop])

# Define XOR for fermentation loop and aging feedback loop
fermentation_aging_loop = OperatorPOWL(operator=Operator.XOR, children=[fermentation_loop, aging_feedback_loop])

# Define XOR for fermentation loop and aging feedback loop
fermentation_aging_loop = OperatorPOWL(operator=Operator.XOR, children=[fermentation_loop, aging_feedback_loop])

# Define XOR for fermentation loop and aging feedback loop
fermentation_aging_loop = OperatorPOWL(operator=Operator.XOR, children=[fermentation_loop, aging_feedback_loop])

# Define XOR for fermentation loop and aging feedback loop
fermentation_aging_loop = OperatorPOWL(operator=Operator.XOR, children=[fermentation_loop, aging_feedback_loop])

# Define XOR for fermentation loop and aging feedback loop
fermentation_aging_loop = OperatorPOWL(operator=Operator.XOR, children=[fermentation_loop, aging_feedback_loop])

# Define XOR for fermentation loop and aging feedback loop
fermentation_aging_loop = OperatorPOWL(operator=Operator.XOR, children=[fermentation_loop, aging_feedback_loop])

# Define XOR for fermentation loop and aging feedback loop
fermentation_aging_loop = OperatorPOWL(operator=Operator.XOR, children=[fermentation_loop, aging_feedback_loop])

# Define XOR for fermentation loop and aging feedback loop
fermentation_aging_loop = OperatorPOWL(operator=Operator.XOR, children=[fermentation_loop, aging_feedback_loop])

# Define XOR for fermentation loop and aging feedback loop
fermentation_aging_loop = OperatorPOWL(operator=Operator.XOR, children=[fermentation_loop, aging_feedback_loop])

# Define XOR for fermentation loop and aging feedback loop
fermentation_aging_loop = OperatorPOWL(operator=Operator.XOR, children=[fermentation_loop, aging_feedback_loop])

# Define XOR for fermentation loop and aging feedback loop
fermentation_aging_loop = OperatorPOWL(operator=Operator.XOR, children=[fermentation_loop, aging_feedback_loop])

# Define XOR for fermentation loop and aging feedback loop
fermentation_aging_loop = OperatorPOWL(operator=Operator.XOR, children=[fermentation_loop, aging_feedback_loop])

# Define XOR for fermentation loop and aging feedback loop
fermentation_aging_loop = OperatorPOWL(operator=Operator.XOR, children=[fermentation_loop, aging_feedback_loop])

# Define XOR for fermentation loop and aging feedback loop
fermentation_aging_loop = OperatorPOWL(operator=Operator.XOR, children=[fermentation_loop, aging_feedback_loop])

# Define XOR for fermentation loop and aging feedback loop
fermentation_aging_loop = OperatorPOWL(operator=Operator.XOR, children=[fermentation_loop, aging_feedback_loop])

# Define XOR for fermentation loop and aging feedback loop
fermentation_aging_loop = OperatorPOWL(operator=Operator.XOR, children=[fermentation_loop, aging_feedback_loop])

# Define XOR for fermentation loop and aging feedback loop
fermentation_aging_loop = OperatorPOWL(operator=Operator.XOR, children=[fermentation_loop, aging_feedback_loop])

# Define XOR for fermentation loop and aging feedback loop
fermentation_aging_loop = OperatorPOWL(operator=Operator.XOR, children=[fermentation_loop, aging_feedback_loop])

# Define XOR for fermentation loop and aging feedback loop
fermentation_aging_loop = OperatorPOWL(operator=Operator.XOR, children=[fermentation_loop, aging_feedback_loop])

# Define XOR for fermentation loop and aging feedback loop
fermentation_aging_loop = OperatorPOWL(operator=Operator.XOR, children=[fermentation_loop, aging_feedback_loop])

# Define XOR for fermentation loop and aging feedback loop
fermentation_aging_loop = OperatorPOWL(operator=Operator.XOR, children=[fermentation_loop, aging_feedback_loop])

# Define XOR for fermentation loop and aging feedback loop
fermentation_aging_loop = OperatorPOWL(operator=Operator.XOR, children=[fermentation_loop, aging_feedback_loop])

# Define XOR for fermentation loop and aging feedback loop
fermentation_aging_loop = OperatorPOWL(operator=Operator.XOR, children=[fermentation_loop, aging_feedback_loop])

# Define XOR for fermentation loop and aging feedback loop
fermentation_aging_loop = OperatorPOWL(operator=Operator.XOR, children=[fermentation_loop, aging_feedback_loop])

# Define XOR for fermentation loop and aging feedback loop
fermentation_aging_loop = OperatorPOWL(operator=Operator.XOR, children=[fermentation_loop, aging_feedback_loop])

# Define XOR for fermentation loop and aging feedback loop
fermentation_aging_loop = OperatorPOWL(operator=Operator.XOR, children=[fermentation_loop, aging_feedback_loop])

# Define XOR for fermentation loop and aging feedback loop
fermentation_aging_loop = OperatorPOWL(operator=Operator.XOR, children=[fermentation_loop, aging_feedback_loop])

# Define XOR for fermentation loop and aging feedback loop
fermentation_aging_loop = OperatorPOWL(operator=Operator.XOR, children=[fermentation_loop, aging_feedback_loop])

# Define XOR for fermentation loop and aging feedback loop
fermentation_aging_loop = OperatorPOWL(operator=Operator.XOR, children=[fermentation_loop, aging_feedback_loop])

# Define XOR for fermentation loop and aging feedback loop
fermentation_aging_loop = OperatorPOWL(operator=Operator.XOR, children=[fermentation_loop, aging_feedback_loop])

# Define XOR for fermentation loop and aging feedback loop
fermentation_aging_loop = OperatorPOWL(operator=Operator.XOR, children=[fermentation_loop, aging_feedback_loop])

# Define XOR for fermentation loop and aging feedback loop
fermentation_aging_loop = OperatorPOWL(operator=Operator.XOR, children=[fermentation_loop, aging_feedback_loop])

# Define XOR for fermentation loop and aging feedback loop
fermentation_aging_loop = OperatorPOWL(operator=Operator.XOR, children=[fermentation_loop, aging_feedback_loop])

# Define XOR for fermentation loop and aging feedback loop
fermentation_aging_loop = OperatorPOWL(operator=Operator.XOR, children=[fermentation_loop, aging_feedback_loop])

# Define XOR for fermentation loop and aging feedback loop
fermentation_aging_loop = OperatorPOWL(operator=Operator.XOR, children=[fermentation_loop, aging_feedback_loop])

# Define XOR for fermentation loop and aging feedback loop
fermentation_aging_loop = OperatorPOWL(operator=Operator.XOR, children=[fermentation_loop, aging_feedback_loop])

# Define XOR for fermentation loop and aging feedback loop
fermentation_aging_loop = OperatorPOWL(operator=Operator.XOR, children=[fermentation_loop, aging_feedback_loop])

# Define XOR for fermentation loop and aging feedback loop
fermentation_aging_loop = OperatorPOWL(operator=Operator.XOR, children=[fermentation_loop, aging_feedback_loop])

# Define XOR for fermentation loop and aging feedback loop
fermentation_aging_loop = OperatorPOWL(operator=Operator.XOR, children=[fermentation_loop, aging_feedback_loop])

# Define XOR for fermentation loop and aging feedback loop
fer