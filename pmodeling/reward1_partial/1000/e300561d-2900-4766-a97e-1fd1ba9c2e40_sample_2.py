import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
intake_check = Transition(label='Intake Check')
condition_log = Transition(label='Condition Log')
provenance_review = Transition(label='Provenance Review')
material_test = Transition(label='Material Test')
spectrometry_scan = Transition(label='Spectrometry Scan')
stylistic_analysis = Transition(label='Stylistic Analysis')
expert_consult = Transition(label='Expert Consult')
archive_search = Transition(label='Archive Search')
ledger_verification = Transition(label='Ledger Verification')
secondary_review = Transition(label='Secondary Review')
cross_check = Transition(label='Cross-Check')
conservation_prep = Transition(label='Conservation Prep')
documentation = Transition(label='Documentation')
report_creation = Transition(label='Report Creation')
database_update = Transition(label='Database Update')

skip = SilentTransition()

# Construct the POWL model
intake_to_condition = OperatorPOWL(operator=Operator.LOOP, children=[intake_check, condition_log])
provenance_to_material = OperatorPOWL(operator=Operator.LOOP, children=[provenance_review, material_test])
material_to_spectrometry = OperatorPOWL(operator=Operator.LOOP, children=[material_test, spectrometry_scan])
stylistic_to_expert = OperatorPOWL(operator=Operator.LOOP, children=[stylistic_analysis, expert_consult])
archive_to_ledger = OperatorPOWL(operator=Operator.LOOP, children=[archive_search, ledger_verification])
secondary_to_cross = OperatorPOWL(operator=Operator.LOOP, children=[secondary_review, cross_check])
conservation_to_documentation = OperatorPOWL(operator=Operator.LOOP, children=[conservation_prep, documentation])
report_to_database = OperatorPOWL(operator=Operator.LOOP, children=[report_creation, database_update])

root = StrictPartialOrder(nodes=[intake_to_condition, provenance_to_material, material_to_spectrometry, stylistic_to_expert, archive_to_ledger, secondary_to_cross, conservation_to_documentation, report_to_database])
root.order.add_edge(intake_to_condition, provenance_to_material)
root.order.add_edge(provenance_to_material, material_to_spectrometry)
root.order.add_edge(material_to_spectrometry, stylistic_to_expert)
root.order.add_edge(stylistic_to_expert, archive_to_ledger)
root.order.add_edge(archive_to_ledger, secondary_to_cross)
root.order.add_edge(secondary_to_cross, conservation_to_documentation)
root.order.add_edge(conservation_to_documentation, report_to_database)