import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
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

# Define the POWL model
root = StrictPartialOrder(
    nodes=[
        intake_check,
        condition_log,
        provenance_review,
        material_test,
        spectrometry_scan,
        stylistic_analysis,
        expert_consult,
        archive_search,
        ledger_verification,
        secondary_review,
        cross_check,
        conservation_prep,
        documentation,
        report_creation,
        database_update
    ],
    order=[
        (intake_check, condition_log),
        (intake_check, provenance_review),
        (condition_log, material_test),
        (condition_log, provenance_review),
        (provenance_review, material_test),
        (provenance_review, expert_consult),
        (material_test, spectrometry_scan),
        (spectrometry_scan, stylistic_analysis),
        (stylistic_analysis, expert_consult),
        (expert_consult, archive_search),
        (archive_search, ledger_verification),
        (ledger_verification, secondary_review),
        (secondary_review, cross_check),
        (cross_check, conservation_prep),
        (conservation_prep, documentation),
        (documentation, report_creation),
        (report_creation, database_update)
    ]
)

# Print the root
print(root)