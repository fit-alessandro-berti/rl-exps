from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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

# Define the process model
root = StrictPartialOrder(
    nodes=[
        milk_sourcing,
        supplier_audit,
        culture_prep,
        milk_testing,
        fermentation_start,
        pH_monitoring,
        curd_cutting,
        mold_inoculation,
        aging_setup,
        humidity_control,
        texture_check,
        flavor_profiling,
        batch_labeling,
        packaging,
        distribution,
        feedback_review,
        sustainability_audit
    ],
    order={
        milk_sourcing: [supplier_audit],
        supplier_audit: [culture_prep, milk_testing],
        culture_prep: [fermentation_start, pH_monitoring],
        milk_testing: [fermentation_start, pH_monitoring],
        fermentation_start: [pH_monitoring, curd_cutting, mold_inoculation],
        pH_monitoring: [curd_cutting, mold_inoculation],
        curd_cutting: [mold_inoculation, aging_setup],
        mold_inoculation: [aging_setup],
        aging_setup: [humidity_control, texture_check, flavor_profiling],
        humidity_control: [texture_check, flavor_profiling],
        texture_check: [batch_labeling],
        flavor_profiling: [batch_labeling],
        batch_labeling: [packaging, distribution],
        packaging: [distribution],
        distribution: [feedback_review],
        feedback_review: [sustainability_audit]
    }
)

print(root)