import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
artifact_intake = Transition(label='Artifact Intake')
catalog_entry = Transition(label='Catalog Entry')
visual_inspect = Transition(label='Visual Inspect')
material_test = Transition(label='Material Test')
spectroscopy = Transition(label='Spectroscopy')
historical_check = Transition(label='Historical Check')
provenance_trace = Transition(label='Provenance Trace')
style_compare = Transition(label='Style Compare')
three_d_scanning = Transition(label='3D Scanning')
condition_assess = Transition(label='Condition Assess')
preservation_plan = Transition(label='Preservation Plan')
legal_review = Transition(label='Legal Review')
report_draft = Transition(label='Report Draft')
report_finalize = Transition(label='Report Finalize')
archive_data = Transition(label='Archive Data')
sale_prep = Transition(label='Sale Prep')

# Define the process as a StrictPartialOrder
root = StrictPartialOrder(nodes=[
    artifact_intake,
    catalog_entry,
    visual_inspect,
    material_test,
    spectroscopy,
    historical_check,
    provenance_trace,
    style_compare,
    three_d_scanning,
    condition_assess,
    preservation_plan,
    legal_review,
    report_draft,
    report_finalize,
    archive_data,
    sale_prep
])

# Define the dependencies between transitions (if any, as per the process description)
# Since there are no dependencies mentioned in the process description, we do not add any edges to the 'root' object.

# The 'root' variable now contains the POWL model for the process.