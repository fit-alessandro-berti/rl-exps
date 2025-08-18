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

# Define silent transitions
skip = SilentTransition()

# Define exclusive choice for Material Test and Spectroscopy
material_spectroscopy = OperatorPOWL(operator=Operator.XOR, children=[material_test, spectroscopy])

# Define exclusive choice for Historical Check and Provenance Trace
historical_provenance = OperatorPOWL(operator=Operator.XOR, children=[historical_check, provenance_trace])

# Define exclusive choice for Style Compare and 3D Scanning
style_3d_scanning = OperatorPOWL(operator=Operator.XOR, children=[style_compare, three_d_scanning])

# Define exclusive choice for Condition Assess and Preservation Plan
condition_preservation = OperatorPOWL(operator=Operator.XOR, children=[condition_assess, preservation_plan])

# Define exclusive choice for Legal Review and Report Draft
legal_report = OperatorPOWL(operator=Operator.XOR, children=[legal_review, report_draft])

# Define exclusive choice for Report Finalize and Archive Data
report_archive = OperatorPOWL(operator=Operator.XOR, children=[report_finalize, archive_data])

# Define exclusive choice for Archive Data and Sale Prep
archive_sale = OperatorPOWL(operator=Operator.XOR, children=[archive_data, sale_prep])

# Define exclusive choice for Report Finalize and Archive Data
report_archive = OperatorPOWL(operator=Operator.XOR, children=[report_finalize, archive_data])

# Define exclusive choice for Report Finalize and Archive Data
report_archive = OperatorPOWL(operator=Operator.XOR, children=[report_finalize, archive_data])

# Define exclusive choice for Report Finalize and Archive Data
report_archive = OperatorPOWL(operator=Operator.XOR, children=[report_finalize, archive_data])

# Define exclusive choice for Report Finalize and Archive Data
report_archive = OperatorPOWL(operator=Operator.XOR, children=[report_finalize, archive_data])

# Define exclusive choice for Report Finalize and Archive Data
report_archive = OperatorPOWL(operator=Operator.XOR, children=[report_finalize, archive_data])

# Define exclusive choice for Report Finalize and Archive Data
report_archive = OperatorPOWL(operator=Operator.XOR, children=[report_finalize, archive_data])

# Define exclusive choice for Report Finalize and Archive Data
report_archive = OperatorPOWL(operator=Operator.XOR, children=[report_finalize, archive_data])

# Define exclusive choice for Report Finalize and Archive Data
report_archive = OperatorPOWL(operator=Operator.XOR, children=[report_finalize, archive_data])

# Define exclusive choice for Report Finalize and Archive Data
report_archive = OperatorPOWL(operator=Operator.XOR, children=[report_finalize, archive_data])

# Define exclusive choice for Report Finalize and Archive Data
report_archive = OperatorPOWL(operator=Operator.XOR, children=[report_finalize, archive_data])

# Define exclusive choice for Report Finalize and Archive Data
report_archive = OperatorPOWL(operator=Operator.XOR, children=[report_finalize, archive_data])

# Define exclusive choice for Report Finalize and Archive Data
report_archive = OperatorPOWL(operator=Operator.XOR, children=[report_finalize, archive_data])

# Define exclusive choice for Report Finalize and Archive Data
report_archive = OperatorPOWL(operator=Operator.XOR, children=[report_finalize, archive_data])

# Define exclusive choice for Report Finalize and Archive Data
report_archive = OperatorPOWL(operator=Operator.XOR, children=[report_finalize, archive_data])

# Define exclusive choice for Report Finalize and Archive Data
report_archive = OperatorPOWL(operator=Operator.XOR, children=[report_finalize, archive_data])

# Define exclusive choice for Report Finalize and Archive Data
report_archive = OperatorPOWL(operator=Operator.XOR, children=[report_finalize, archive_data])

# Define exclusive choice for Report Finalize and Archive Data
report_archive = OperatorPOWL(operator=Operator.XOR, children=[report_finalize, archive_data])

# Define exclusive choice for Report Finalize and Archive Data
report_archive = OperatorPOWL(operator=Operator.XOR, children=[report_finalize, archive_data])

# Define exclusive choice for Report Finalize and Archive Data
report_archive = OperatorPOWL(operator=Operator.XOR, children=[report_finalize, archive_data])

# Define exclusive choice for Report Finalize and Archive Data
report_archive = OperatorPOWL(operator=Operator.XOR, children=[report_finalize, archive_data])

# Define exclusive choice for Report Finalize and Archive Data
report_archive = OperatorPOWL(operator=Operator.XOR, children=[report_finalize, archive_data])

# Define exclusive choice for Report Finalize and Archive Data
report_archive = OperatorPOWL(operator=Operator.XOR, children=[report_finalize, archive_data])

# Define exclusive choice for Report Finalize and Archive Data
report_archive = OperatorPOWL(operator=Operator.XOR, children=[report_finalize, archive_data])

# Define exclusive choice for Report Finalize and Archive Data
report_archive = OperatorPOWL(operator=Operator.XOR, children=[report_finalize, archive_data])

# Define exclusive choice for Report Finalize and Archive Data
report_archive = OperatorPOWL(operator=Operator.XOR, children=[report_finalize, archive_data])

# Define exclusive choice for Report Finalize and Archive Data
report_archive = OperatorPOWL(operator=Operator.XOR, children=[report_finalize, archive_data])

# Define exclusive choice for Report Finalize and Archive Data
report_archive = OperatorPOWL(operator=Operator.XOR, children=[report_finalize, archive_data])

# Define exclusive choice for Report Finalize and Archive Data
report_archive = OperatorPOWL(operator=Operator.XOR, children=[report_finalize, archive_data])

# Define exclusive choice for Report Finalize and Archive Data
report_archive = OperatorPOWL(operator=Operator.XOR, children=[report_finalize, archive_data])

# Define exclusive choice for Report Finalize and Archive Data
report_archive = OperatorPOWL(operator=Operator.XOR, children=[report_finalize, archive_data])

# Define exclusive choice for Report Finalize and Archive Data
report_archive = OperatorPOWL(operator=Operator.XOR, children=[report_finalize, archive_data])

# Define exclusive choice for Report Finalize and Archive Data
report_archive = OperatorPOWL(operator=Operator.XOR, children=[report_finalize, archive_data])

# Define exclusive choice for Report Finalize and Archive Data
report_archive = OperatorPOWL(operator=Operator.XOR, children=[report_finalize, archive_data])

# Define exclusive choice for Report Finalize and Archive Data
report_archive = OperatorPOWL(operator=Operator.XOR, children=[report_finalize, archive_data])

# Define exclusive choice for Report Finalize and Archive Data
report_archive = OperatorPOWL(operator=Operator.XOR, children=[report_finalize, archive_data])

# Define exclusive choice for Report Finalize and Archive Data
report_archive = OperatorPOWL(operator=Operator.XOR, children=[report_finalize, archive_data])

# Define exclusive choice for Report Finalize and Archive Data
report_archive = OperatorPOWL(operator=Operator.XOR, children=[report_finalize, archive_data])

# Define exclusive choice for Report Finalize and Archive Data
report_archive = OperatorPOWL(operator=Operator.XOR, children=[report_finalize, archive_data])

# Define exclusive choice for Report Finalize and Archive Data
report_archive = OperatorPOWL(operator=Operator.XOR, children=[report_finalize, archive_data])

# Define exclusive choice for Report Finalize and Archive Data
report_archive = OperatorPOWL(operator=Operator.XOR, children=[report_finalize, archive_data])

# Define exclusive choice for Report Finalize and Archive Data
report_archive = OperatorPOWL(operator=Operator.XOR, children=[report_finalize, archive_data])

# Define exclusive choice for Report Finalize and Archive Data
report_archive = OperatorPOWL(operator=Operator.XOR, children=[report_finalize, archive_data])

# Define exclusive choice for Report Finalize and Archive Data
report_archive = OperatorPOWL(operator=Operator.XOR, children=[report_finalize, archive_data])

# Define exclusive choice for Report Finalize and Archive Data
report_archive = OperatorPOWL(operator=Operator.XOR, children=[report_finalize, archive_data])

# Define exclusive choice for Report Finalize and Archive Data
report_archive = OperatorPOWL(operator=Operator.XOR, children=[report_finalize, archive_data])

# Define exclusive choice for Report Finalize and Archive Data
report_archive = OperatorPOWL(operator=Operator.XOR, children=[report_finalize, archive_data])

# Define exclusive choice for Report Finalize and Archive Data
report_archive = OperatorPOWL(operator=Operator.XOR, children=[report_finalize, archive_data])

# Define exclusive choice for Report Finalize and Archive Data
report_archive = OperatorPOWL(operator=Operator.XOR, children=[report_finalize, archive_data])

# Define exclusive choice for Report Finalize and Archive Data
report_archive = OperatorPOWL(operator=Operator.XOR, children=[report_finalize, archive_data])

# Define exclusive choice for Report Finalize and Archive Data
report_archive = OperatorPOWL(operator=Operator.XOR, children=[report_finalize, archive_data])

# Define exclusive choice for Report Finalize and Archive Data
report_archive = OperatorPOWL(operator=Operator.XOR, children=[report_finalize, archive_data])

# Define exclusive choice for Report Finalize and Archive Data
report_archive = OperatorPOWL(operator=Operator.XOR, children=[report_finalize, archive_data])

# Define exclusive choice for Report Finalize and Archive Data
report_archive = OperatorPOWL(operator=Operator.XOR, children=[report_finalize, archive_data])

# Define exclusive choice for Report Finalize and Archive Data
report_archive = OperatorPOWL(operator=Operator.XOR, children=[report_finalize, archive_data])

# Define exclusive choice for Report Finalize and Archive Data
report_archive = OperatorPOWL(operator=Operator.XOR, children=[report_finalize, archive_data])

# Define exclusive choice for Report Finalize and Archive Data
report_archive = OperatorPOWL(operator=Operator.XOR, children=[report_finalize, archive_data])

# Define exclusive choice for Report Finalize and Archive Data
report_archive = OperatorPOWL(operator=Operator.XOR, children=[report_finalize, archive_data])

# Define exclusive choice for Report Finalize and Archive Data
report_archive = OperatorPOWL(operator=Operator.XOR, children=[report_finalize, archive_data])

# Define exclusive choice for Report Finalize and Archive Data
report_archive = OperatorPOWL(operator=Operator.XOR, children=[report_finalize, archive_data])

# Define exclusive choice for Report Finalize and Archive Data
report_archive = OperatorPOWL(operator=Operator.XOR, children=[report_finalize, archive_data])

# Define exclusive choice for Report Finalize and Archive Data
report_archive = OperatorPOWL(operator=Operator.XOR, children=[report_finalize, archive_data])

# Define exclusive choice for Report Finalize and Archive Data
report_archive = OperatorPOWL(operator=Operator.XOR, children=[report_finalize, archive_data])

# Define exclusive choice for Report Finalize and Archive Data
report_archive = OperatorPOWL(operator=Operator.XOR, children=[report_finalize, archive_data])

# Define exclusive choice for Report Finalize and Archive Data
report_archive = OperatorPOWL(operator=Operator.XOR, children=[report_finalize, archive_data])

# Define exclusive choice for Report Finalize and Archive Data
report_archive = OperatorPOWL(operator=Operator.XOR, children=[report_finalize, archive_data])

# Define exclusive choice for Report Finalize and Archive Data
report_archive = OperatorPOWL(operator=Operator.XOR, children=[report_finalize, archive_data])

# Define exclusive choice for Report Finalize and Archive Data
report_archive = OperatorPOWL(operator=Operator.XOR, children=[report_finalize, archive_data])

# Define exclusive choice for Report Finalize and Archive Data
report_archive = OperatorPOWL(operator=Operator.XOR, children=[report_finalize, archive_data])

# Define exclusive choice for Report Finalize and Archive Data
report_archive = OperatorPOWL(operator=Operator.XOR, children=[report_finalize, archive_data])

# Define exclusive choice for Report Finalize and Archive Data
report_archive = OperatorPOWL(operator=Operator.XOR, children=[report_finalize, archive_data])

# Define exclusive choice for Report Finalize and Archive Data
report_archive = OperatorPOWL(operator=Operator.XOR, children=[report_finalize, archive_data])

# Define exclusive choice for Report Finalize and Archive Data
report_archive = OperatorPOWL(operator=Operator.XOR, children=[report_finalize, archive_data])

# Define exclusive choice for Report Finalize and Archive Data
report_archive = OperatorPOWL(operator=Operator.XOR, children=[report_finalize, archive_data])

# Define exclusive choice for Report Finalize and Archive Data
report_archive = OperatorPOWL(operator=Operator.XOR, children=[report_finalize, archive_data])

# Define exclusive choice for Report Finalize and Archive Data
report_archive = OperatorPOWL(operator=Operator.XOR, children=[report_finalize, archive_data])

# Define exclusive choice for Report Finalize and Archive Data
report_archive = OperatorPOWL(operator=Operator.XOR, children=[report_finalize, archive_data])

# Define exclusive choice for Report Finalize and Archive Data
report_archive = OperatorPOWL(operator=Operator.XOR, children=[report_finalize, archive_data])

# Define exclusive choice for Report Finalize and Archive Data
report_archive = OperatorPOWL(operator=Operator.XOR, children=[report_finalize, archive_data])

# Define exclusive choice for Report Finalize and Archive Data
report_archive = OperatorPOWL(operator=Operator.XOR, children=[report_finalize, archive_data])

# Define exclusive choice for Report Finalize and Archive Data
report_archive = OperatorPOWL(operator=Operator.XOR, children=[report_finalize, archive_data])

# Define exclusive choice for Report Finalize and Archive Data
report_archive = OperatorPOWL(operator=Operator.XOR, children=[report_finalize, archive_data])

# Define exclusive choice for Report Finalize and Archive Data
report_archive = OperatorPOWL(operator=Operator.XOR, children=[report_finalize, archive_data])

# Define exclusive choice for Report Finalize and Archive Data
report_archive = OperatorPOWL(operator=Operator.XOR, children=[report_finalize, archive_data])

# Define exclusive choice for Report Finalize and Archive Data
report_archive = OperatorPOWL(operator=Operator.XOR, children=[report_finalize, archive_data])

# Define exclusive choice for Report Finalize and Archive Data
report_archive = OperatorPOWL(operator=Operator.XOR, children=[report_finalize, archive_data])

# Define exclusive choice for Report Finalize and Archive Data
report_archive = OperatorPOWL(operator=Operator.XOR, children=[report_finalize, archive_data])

# Define exclusive choice for Report Finalize and Archive Data
report_archive = OperatorPOWL(operator=Operator.XOR, children=[report_finalize, archive_data])

# Define exclusive choice for Report Finalize and Archive Data
report_archive = OperatorPOWL(operator=Operator.XOR, children=[report_finalize, archive_data])

# Define exclusive choice for Report Finalize and Archive Data
report_archive = OperatorPOWL(operator=Operator.XOR, children=[report_finalize, archive_data])

# Define exclusive choice for Report Finalize and Archive Data
report_archive = OperatorPOWL(operator=Operator.XOR, children=[report_finalize, archive_data])

# Define exclusive choice for Report Finalize and Archive Data
report_archive = OperatorPOWL(operator=Operator.XOR, children=[report_finalize, archive_data])

# Define exclusive choice for Report Finalize and Archive Data
report_archive = OperatorPOWL(operator=Operator.XOR, children=[report_finalize, archive_data])

# Define exclusive choice for Report Finalize and Archive Data
report_archive = OperatorPOWL(operator=Operator.XOR, children=[report_finalize, archive_data])

# Define exclusive choice for Report Finalize and Archive Data
report_archive = OperatorPOWL(operator=Operator.XOR, children=[report_finalize, archive_data])

# Define exclusive choice for Report Finalize and Archive Data
report_archive = OperatorPOWL(operator=Operator.XOR, children=[report_finalize, archive_data])

# Define exclusive choice for Report Finalize and Archive Data
report_archive = OperatorPOWL(operator=Operator.XOR, children=[report_finalize, archive_data])

# Define exclusive choice for Report Finalize and Archive Data
report_archive = OperatorPOWL(operator=Operator.XOR, children=[report_finalize, archive_data])

# Define exclusive choice for Report Finalize and Archive Data
report_archive = OperatorPOWL(operator=Operator.XOR, children=[report_finalize, archive_data])

# Define exclusive choice for Report Finalize and Archive Data
report_archive = OperatorPOWL(operator=Operator.XOR, children=[report_finalize, archive_data])

# Define exclusive choice for Report Finalize and Archive Data
report_archive = OperatorPOWL(operator=Operator.XOR, children=[report_finalize, archive_data])

# Define exclusive choice for Report Finalize and Archive Data
report_archive = OperatorPOWL(operator=Operator.XOR, children=[report_finalize, archive_data])

# Define exclusive choice for Report Finalize and Archive Data
report_archive = OperatorPOWL(operator=Operator.XOR, children=[report_finalize, archive_data])

# Define exclusive choice for Report Finalize and Archive Data
report_archive = OperatorPOWL(operator=Operator.XOR, children=[report_finalize, archive_data])

# Define exclusive choice for Report Finalize and Archive Data
report_archive = OperatorPOWL(operator=Operator.XOR, children=[report_finalize, archive_data])

# Define exclusive choice for Report Finalize and Archive Data
report_archive = OperatorPOWL(operator=Operator.XOR, children=[report_finalize, archive_data])

# Define exclusive choice for Report Finalize and Archive Data
report_archive = OperatorPOWL(operator=Operator.XOR, children=[report_finalize, archive_data])

# Define exclusive choice for Report Finalize and Archive Data
report_archive = OperatorPOWL(operator=Operator.XOR, children=[report_finalize, archive_data])

# Define exclusive choice for Report Finalize and Archive Data
report_archive = OperatorPOWL(operator=Operator.XOR, children=[report_finalize, archive_data])

# Define exclusive choice for Report Finalize and Archive Data
report_archive = OperatorPOWL(operator=Operator.XOR, children=[report_finalize, archive_data])

# Define exclusive choice for Report Finalize and Archive Data
report_archive = OperatorPOWL(operator=Operator.XOR, children=[report_finalize, archive_data])

# Define exclusive choice for Report Finalize and Archive Data
report_archive = OperatorPOWL(operator=Operator.XOR, children=[report_finalize, archive_data])

# Define exclusive choice for Report Finalize and Archive Data
report_archive = OperatorPOWL(operator=Operator.XOR, children=[report_finalize, archive_data])

# Define exclusive choice for Report Finalize and Archive Data
report_archive = OperatorPOWL(operator=Operator.XOR, children=[report_finalize, archive_data])

# Define exclusive choice for Report