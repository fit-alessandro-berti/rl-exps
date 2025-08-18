import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model for the process
receive_artifact = Transition(label='Receive Artifact')
condition_log = Transition(label='Condition Log')
radiocarbon_test = Transition(label='Radiocarbon Test')
spectroscopy_scan = Transition(label='Spectroscopy Scan')
expert_consult = Transition(label='Expert Consult')
provenance_check = Transition(label='Provenance Check')
archive_search = Transition(label='Archive Search')
risk_assess = Transition(label='Risk Assess')
three_d_scan = Transition(label='3D Scan')
legal_review = Transition(label='Legal Review')
insurance_setup = Transition(label='Insurance Setup')
certificate_draft = Transition(label='Certificate Draft')
certificate_approve = Transition(label='Certificate Approve')
climate_pack = Transition(label='Climate Pack')
conservation_plan = Transition(label='Conservation Plan')
monitoring_schedule = Transition(label='Monitoring Schedule')

# Define the partial order structure
root = StrictPartialOrder(
    nodes=[
        receive_artifact,
        condition_log,
        radiocarbon_test,
        spectroscopy_scan,
        expert_consult,
        provenance_check,
        archive_search,
        risk_assess,
        three_d_scan,
        legal_review,
        insurance_setup,
        certificate_draft,
        certificate_approve,
        climate_pack,
        conservation_plan,
        monitoring_schedule
    ],
    order=[
        (receive_artifact, condition_log),
        (condition_log, radiocarbon_test),
        (condition_log, spectroscopy_scan),
        (radiocarbon_test, expert_consult),
        (spectroscopy_scan, expert_consult),
        (expert_consult, provenance_check),
        (provenance_check, archive_search),
        (provenance_check, risk_assess),
        (archive_search, three_d_scan),
        (risk_assess, three_d_scan),
        (three_d_scan, legal_review),
        (legal_review, insurance_setup),
        (insurance_setup, certificate_draft),
        (certificate_draft, certificate_approve),
        (certificate_approve, climate_pack),
        (climate_pack, conservation_plan),
        (conservation_plan, monitoring_schedule)
    ]
)

# Output the root POWL model
print(root)