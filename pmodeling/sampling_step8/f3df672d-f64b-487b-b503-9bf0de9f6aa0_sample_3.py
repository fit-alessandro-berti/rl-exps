import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions
data_collection = Transition(label='Data Collection')
provenance_check = Transition(label='Provenance Check')
material_scan = Transition(label='Material Scan')
historical_review = Transition(label='Historical Review')
expert_panel = Transition(label='Expert Panel')
blockchain_verify = Transition(label='Blockchain Verify')
oral_history = Transition(label='Oral History')
condition_report = Transition(label='Condition Report')
legal_review = Transition(label='Legal Review')
certification = Transition(label='Certification')
archival_update = Transition(label='Archival Update')
insurance_setup = Transition(label='Insurance Setup')
exhibition_prep = Transition(label='Exhibition Prep')
iot_monitoring = Transition(label='IoT Monitoring')
re_validation = Transition(label='Re-validation')

# Define silent transitions
skip = SilentTransition()

# Define partial order model
root = StrictPartialOrder(nodes=[
    data_collection,
    provenance_check,
    material_scan,
    historical_review,
    expert_panel,
    blockchain_verify,
    oral_history,
    condition_report,
    legal_review,
    certification,
    archival_update,
    insurance_setup,
    exhibition_prep,
    iot_monitoring,
    re_validation
])

# Define dependencies
root.order.add_edge(data_collection, provenance_check)
root.order.add_edge(provenance_check, material_scan)
root.order.add_edge(material_scan, historical_review)
root.order.add_edge(historical_review, expert_panel)
root.order.add_edge(expert_panel, blockchain_verify)
root.order.add_edge(blockchain_verify, oral_history)
root.order.add_edge(oral_history, condition_report)
root.order.add_edge(condition_report, legal_review)
root.order.add_edge(legal_review, certification)
root.order.add_edge(certification, archival_update)
root.order.add_edge(archival_update, insurance_setup)
root.order.add_edge(insurance_setup, exhibition_prep)
root.order.add_edge(exhibition_prep, iot_monitoring)
root.order.add_edge(iot_monitoring, re_validation)

# Add loop for IoT monitoring
loop = OperatorPOWL(operator=Operator.LOOP, children=[iot_monitoring, re_validation])
root.order.add_edge(loop, re_validation)

# Add concurrent activities for legal review
concurrent_legal_review = OperatorPOWL(operator=Operator.CONC, children=[legal_review, archival_update])
root.order.add_edge(legal_review, concurrent_legal_review)
root.order.add_edge(archival_update, concurrent_legal_review)

# Add concurrent activities for insurance setup
concurrent_insurance_setup = OperatorPOWL(operator=Operator.CONC, children=[insurance_setup, exhibition_prep])
root.order.add_edge(insurance_setup, concurrent_insurance_setup)
root.order.add_edge(exhibition_prep, concurrent_insurance_setup)

# Add concurrent activities for IoT monitoring
concurrent_iot_monitoring = OperatorPOWL(operator=Operator.CONC, children=[iot_monitoring, re_validation])
root.order.add_edge(iot_monitoring, concurrent_iot_monitoring)
root.order.add_edge(re_validation, concurrent_iot_monitoring)

# Add concurrent activities for exhibition prep
concurrent_exhibition_prep = OperatorPOWL(operator=Operator.CONC, children=[exhibition_prep, re_validation])
root.order.add_edge(exhibition_prep, concurrent_exhibition_prep)
root.order.add_edge(re_validation, concurrent_exhibition_prep)

# Add concurrent activities for archival update
concurrent_archival_update = OperatorPOWL(operator=Operator.CONC, children=[archival_update, re_validation])
root.order.add_edge(archival_update, concurrent_archival_update)
root.order.add_edge(re_validation, concurrent_archival_update)

# Add concurrent activities for insurance setup
concurrent_insurance_setup = OperatorPOWL(operator=Operator.CONC, children=[insurance_setup, exhibition_prep])
root.order.add_edge(insurance_setup, concurrent_insurance_setup)
root.order.add_edge(exhibition_prep, concurrent_insurance_setup)

# Add concurrent activities for IoT monitoring
concurrent_iot_monitoring = OperatorPOWL(operator=Operator.CONC, children=[iot_monitoring, re_validation])
root.order.add_edge(iot_monitoring, concurrent_iot_monitoring)
root.order.add_edge(re_validation, concurrent_iot_monitoring)

# Add concurrent activities for exhibition prep
concurrent_exhibition_prep = OperatorPOWL(operator=Operator.CONC, children=[exhibition_prep, re_validation])
root.order.add_edge(exhibition_prep, concurrent_exhibition_prep)
root.order.add_edge(re_validation, concurrent_exhibition_prep)

# Add concurrent activities for archival update
concurrent_archival_update = OperatorPOWL(operator=Operator.CONC, children=[archival_update, re_validation])
root.order.add_edge(archival_update, concurrent_archival_update)
root.order.add_edge(re_validation, concurrent_archival_update)

# Add concurrent activities for insurance setup
concurrent_insurance_setup = OperatorPOWL(operator=Operator.CONC, children=[insurance_setup, exhibition_prep])
root.order.add_edge(insurance_setup, concurrent_insurance_setup)
root.order.add_edge(exhibition_prep, concurrent_insurance_setup)

# Add concurrent activities for IoT monitoring
concurrent_iot_monitoring = OperatorPOWL(operator=Operator.CONC, children=[iot_monitoring, re_validation])
root.order.add_edge(iot_monitoring, concurrent_iot_monitoring)
root.order.add_edge(re_validation, concurrent_iot_monitoring)

# Add concurrent activities for exhibition prep
concurrent_exhibition_prep = OperatorPOWL(operator=Operator.CONC, children=[exhibition_prep, re_validation])
root.order.add_edge(exhibition_prep, concurrent_exhibition_prep)
root.order.add_edge(re_validation, concurrent_exhibition_prep)

# Add concurrent activities for archival update
concurrent_archival_update = OperatorPOWL(operator=Operator.CONC, children=[archival_update, re_validation])
root.order.add_edge(archival_update, concurrent_archival_update)
root.order.add_edge(re_validation, concurrent_archival_update)

# Add concurrent activities for insurance setup
concurrent_insurance_setup = OperatorPOWL(operator=Operator.CONC, children=[insurance_setup, exhibition_prep])
root.order.add_edge(insurance_setup, concurrent_insurance_setup)
root.order.add_edge(exhibition_prep, concurrent_insurance_setup)

# Add concurrent activities for IoT monitoring
concurrent_iot_monitoring = OperatorPOWL(operator=Operator.CONC, children=[iot_monitoring, re_validation])
root.order.add_edge(iot_monitoring, concurrent_iot_monitoring)
root.order.add_edge(re_validation, concurrent_iot_monitoring)

# Add concurrent activities for exhibition prep
concurrent_exhibition_prep = OperatorPOWL(operator=Operator.CONC, children=[exhibition_prep, re_validation])
root.order.add_edge(exhibition_prep, concurrent_exhibition_prep)
root.order.add_edge(re_validation, concurrent_exhibition_prep)

# Add concurrent activities for archival update
concurrent_archival_update = OperatorPOWL(operator=Operator.CONC, children=[archival_update, re_validation])
root.order.add_edge(archival_update, concurrent_archival_update)
root.order.add_edge(re_validation, concurrent_archival_update)

# Add concurrent activities for insurance setup
concurrent_insurance_setup = OperatorPOWL(operator=Operator.CONC, children=[insurance_setup, exhibition_prep])
root.order.add_edge(insurance_setup, concurrent_insurance_setup)
root.order.add_edge(exhibition_prep, concurrent_insurance_setup)

# Add concurrent activities for IoT monitoring
concurrent_iot_monitoring = OperatorPOWL(operator=Operator.CONC, children=[iot_monitoring, re_validation])
root.order.add_edge(iot_monitoring, concurrent_iot_monitoring)
root.order.add_edge(re_validation, concurrent_iot_monitoring)

# Add concurrent activities for exhibition prep
concurrent_exhibition_prep = OperatorPOWL(operator=Operator.CONC, children=[exhibition_prep, re_validation])
root.order.add_edge(exhibition_prep, concurrent_exhibition_prep)
root.order.add_edge(re_validation, concurrent_exhibition_prep)

# Add concurrent activities for archival update
concurrent_archival_update = OperatorPOWL(operator=Operator.CONC, children=[archival_update, re_validation])
root.order.add_edge(archival_update, concurrent_archival_update)
root.order.add_edge(re_validation, concurrent_archival_update)

# Add concurrent activities for insurance setup
concurrent_insurance_setup = OperatorPOWL(operator=Operator.CONC, children=[insurance_setup, exhibition_prep])
root.order.add_edge(insurance_setup, concurrent_insurance_setup)
root.order.add_edge(exhibition_prep, concurrent_insurance_setup)

# Add concurrent activities for IoT monitoring
concurrent_iot_monitoring = OperatorPOWL(operator=Operator.CONC, children=[iot_monitoring, re_validation])
root.order.add_edge(iot_monitoring, concurrent_iot_monitoring)
root.order.add_edge(re_validation, concurrent_iot_monitoring)

# Add concurrent activities for exhibition prep
concurrent_exhibition_prep = OperatorPOWL(operator=Operator.CONC, children=[exhibition_prep, re_validation])
root.order.add_edge(exhibition_prep, concurrent_exhibition_prep)
root.order.add_edge(re_validation, concurrent_exhibition_prep)

# Add concurrent activities for archival update
concurrent_archival_update = OperatorPOWL(operator=Operator.CONC, children=[archival_update, re_validation])
root.order.add_edge(archival_update, concurrent_archival_update)
root.order.add_edge(re_validation, concurrent_archival_update)

# Add concurrent activities for insurance setup
concurrent_insurance_setup = OperatorPOWL(operator=Operator.CONC, children=[insurance_setup, exhibition_prep])
root.order.add_edge(insurance_setup, concurrent_insurance_setup)
root.order.add_edge(exhibition_prep, concurrent_insurance_setup)

# Add concurrent activities for IoT monitoring
concurrent_iot_monitoring = OperatorPOWL(operator=Operator.CONC, children=[iot_monitoring, re_validation])
root.order.add_edge(iot_monitoring, concurrent_iot_monitoring)
root.order.add_edge(re_validation, concurrent_iot_monitoring)

# Add concurrent activities for exhibition prep
concurrent_exhibition_prep = OperatorPOWL(operator=Operator.CONC, children=[exhibition_prep, re_validation])
root.order.add_edge(exhibition_prep, concurrent_exhibition_prep)
root.order.add_edge(re_validation, concurrent_exhibition_prep)

# Add concurrent activities for archival update
concurrent_archival_update = OperatorPOWL(operator=Operator.CONC, children=[archival_update, re_validation])
root.order.add_edge(archival_update, concurrent_archival_update)
root.order.add_edge(re_validation, concurrent_archival_update)

# Add concurrent activities for insurance setup
concurrent_insurance_setup = OperatorPOWL(operator=Operator.CONC, children=[insurance_setup, exhibition_prep])
root.order.add_edge(insurance_setup, concurrent_insurance_setup)
root.order.add_edge(exhibition_prep, concurrent_insurance_setup)

# Add concurrent activities for IoT monitoring
concurrent_iot_monitoring = OperatorPOWL(operator=Operator.CONC, children=[iot_monitoring, re_validation])
root.order.add_edge(iot_monitoring, concurrent_iot_monitoring)
root.order.add_edge(re_validation, concurrent_iot_monitoring)

# Add concurrent activities for exhibition prep
concurrent_exhibition_prep = OperatorPOWL(operator=Operator.CONC, children=[exhibition_prep, re_validation])
root.order.add_edge(exhibition_prep, concurrent_exhibition_prep)
root.order.add_edge(re_validation, concurrent_exhibition_prep)

# Add concurrent activities for archival update
concurrent_archival_update = OperatorPOWL(operator=Operator.CONC, children=[archival_update, re_validation])
root.order.add_edge(archival_update, concurrent_archival_update)
root.order.add_edge(re_validation, concurrent_archival_update)

# Add concurrent activities for insurance setup
concurrent_insurance_setup = OperatorPOWL(operator=Operator.CONC, children=[insurance_setup, exhibition_prep])
root.order.add_edge(insurance_setup, concurrent_insurance_setup)
root.order.add_edge(exhibition_prep, concurrent_insurance_setup)

# Add concurrent activities for IoT monitoring
concurrent_iot_monitoring = OperatorPOWL(operator=Operator.CONC, children=[iot_monitoring, re_validation])
root.order.add_edge(iot_monitoring, concurrent_iot_monitoring)
root.order.add_edge(re_validation, concurrent_iot_monitoring)

# Add concurrent activities for exhibition prep
concurrent_exhibition_prep = OperatorPOWL(operator=Operator.CONC, children=[exhibition_prep, re_validation])
root.order.add_edge(exhibition_prep, concurrent_exhibition_prep)
root.order.add_edge(re_validation, concurrent_exhibition_prep)

# Add concurrent activities for archival update
concurrent_archival_update = OperatorPOWL(operator=Operator.CONC, children=[archival_update, re_validation])
root.order.add_edge(archival_update, concurrent_archival_update)
root.order.add_edge(re_validation, concurrent_archival_update)

# Add concurrent activities for insurance setup
concurrent_insurance_setup = OperatorPOWL(operator=Operator.CONC, children=[insurance_setup, exhibition_prep])
root.order.add_edge(insurance_setup, concurrent_insurance_setup)
root.order.add_edge(exhibition_prep, concurrent_insurance_setup)

# Add concurrent activities for IoT monitoring
concurrent_iot_monitoring = OperatorPOWL(operator=Operator.CONC, children=[iot_monitoring, re_validation])
root.order.add_edge(iot_monitoring, concurrent_iot_monitoring)
root.order.add_edge(re_validation, concurrent_iot_monitoring)

# Add concurrent activities for exhibition prep
concurrent_exhibition_prep = OperatorPOWL(operator=Operator.CONC, children=[exhibition_prep, re_validation])
root.order.add_edge(exhibition_prep, concurrent_exhibition_prep)
root.order.add_edge(re_validation, concurrent_exhibition_prep)

# Add concurrent activities for archival update
concurrent_archival_update = OperatorPOWL(operator=Operator.CONC, children=[archival_update, re_validation])
root.order.add_edge(archival_update, concurrent_archival_update)
root.order.add_edge(re_validation, concurrent_archival_update)

# Add concurrent activities for insurance setup
concurrent_insurance_setup = OperatorPOWL(operator=Operator.CONC, children=[insurance_setup, exhibition_prep])
root.order.add_edge(insurance_setup, concurrent_insurance_setup)
root.order.add_edge(exhibition_prep, concurrent_insurance_setup)

# Add concurrent activities for IoT monitoring
concurrent_iot_monitoring = OperatorPOWL(operator=Operator.CONC, children=[iot_monitoring, re_validation])
root.order.add_edge(iot_monitoring, concurrent_iot_monitoring)
root.order.add_edge(re_validation, concurrent_iot_monitoring)

# Add concurrent activities for exhibition prep
concurrent_exhibition_prep = OperatorPOWL(operator=Operator.CONC, children=[exhibition_prep, re_validation])
root.order.add_edge(exhibition_prep, concurrent_exhibition_prep)
root.order.add_edge(re_validation, concurrent_exhibition_prep)

# Add concurrent activities for archival update
concurrent_archival_update = OperatorPOWL(operator=Operator.CONC, children=[archival_update, re_validation])
root.order.add_edge(archival_update, concurrent_archival_update)
root.order.add_edge(re_validation, concurrent_archival_update)

# Add concurrent activities for insurance setup
concurrent_insurance_setup = OperatorPOWL(operator=Operator.CONC, children=[insurance_setup, exhibition_prep])
root.order.add_edge(insurance_setup, concurrent_insurance_setup)
root.order.add_edge(exhibition_prep, concurrent_insurance_setup)

# Add concurrent activities for IoT monitoring
concurrent_iot_monitoring = OperatorPOWL(operator=Operator.CONC, children=[iot_monitoring, re_validation])
root.order.add_edge(iot_monitoring, concurrent_iot_monitoring)
root.order.add_edge(re_validation, concurrent_iot_monitoring)

# Add concurrent activities for exhibition prep
concurrent_exhibition_prep = OperatorPOWL(operator=Operator.CONC, children=[exhibition_prep, re_validation])
root.order.add_edge(exhibition_prep, concurrent_exhibition_prep)
root.order.add_edge(re_validation, concurrent_exhibition_prep)

# Add concurrent activities for archival update
concurrent_archival_update = OperatorPOWL(operator=Operator.CONC, children=[archival_update, re_validation])
root.order.add_edge(archival_update, concurrent_archival_update)
root.order.add_edge(re_validation, concurrent_archival_update)

# Add concurrent activities for insurance setup
concurrent_insurance_setup = OperatorPOWL(operator=Operator.CONC, children=[insurance_setup, exhibition_prep])
root.order.add_edge(insurance_setup, concurrent_insurance_setup)
root.order.add_edge(exhibition_prep, concurrent_insurance_setup)

# Add concurrent activities for IoT monitoring
concurrent_iot_monitoring = OperatorPOWL(operator=Operator.CONC, children=[iot_monitoring, re_validation])
root.order.add_edge(iot_monitoring, concurrent_iot_monitoring)
root.order.add_edge(re_validation, concurrent_iot_monitoring)

# Add concurrent activities for exhibition prep
concurrent_exhibition_prep = OperatorPOWL(operator=Operator.CONC, children=[exhibition_prep, re_validation])
root.order.add_edge(exhibition_prep, concurrent_exhibition_prep)
root.order.add_edge(re_validation, concurrent_exhibition_prep)

# Add concurrent activities for archival update
concurrent_archival_update = OperatorPOWL(operator=Operator.CONC, children=[archival_update, re_validation])
root.order.add_edge(archival_update, concurrent_archival_update)
root.order.add_edge(re_validation, concurrent_archival_update)

# Add concurrent activities for insurance setup
concurrent_insurance_setup = OperatorPOWL(operator=Operator.CONC, children=[insurance_setup, exhibition_prep])
root.order.add_edge(insurance_setup, concurrent_insurance_setup)
root.order.add_edge(exhibition_prep, concurrent_insurance_setup)

# Add concurrent activities for IoT monitoring
concurrent_iot_monitoring = OperatorPOWL(operator=Operator.CONC, children=[iot_monitoring, re_validation])
root.order.add_edge(iot_monitoring, concurrent_iot_monitoring)
root.order.add_edge(re_validation, concurrent_iot_monitoring)

# Add concurrent activities for exhibition prep
concurrent_exhibition_prep = OperatorPOWL(operator=Operator.CONC, children=[exhibition_prep, re_validation])
root.order.add_edge(exhibition_prep, concurrent_exhibition_prep)
root.order.add_edge(re_validation, concurrent_exhibition_prep)

# Add concurrent activities for archival update
concurrent_archival_update = OperatorPOWL(operator=Operator.CONC, children=[archival_update, re_validation])
root.order.add_edge(archival_update, concurrent_archival_update)
root.order.add_edge(re_validation, concurrent_archival_update)

# Add concurrent activities for insurance setup
concurrent_insurance_setup = OperatorPOWL(operator=Operator.CONC, children=[insurance_setup, exhibition_prep])
root.order.add_edge(insurance_setup, concurrent_insurance_setup)
root.order.add_edge(exhibition_prep, concurrent_insurance_setup)

# Add concurrent activities for IoT monitoring
concurrent_iot_monitoring = OperatorPOWL(operator=Operator.CONC, children=[iot_monitoring, re_validation])
root.order.add_edge(iot_monitoring, concurrent_iot_monitoring)
root.order.add_edge(re_validation, concurrent_iot_monitoring)

# Add concurrent activities for exhibition prep
concurrent_exhibition_prep = OperatorPOWL(operator=Operator.CONC, children=[exhibition_prep, re_validation])
root.order.add_edge(exhibition_prep, concurrent_exhibition_prep)
root.order.add_edge(re_validation, concurrent_exhibition_prep)

# Add concurrent activities for archival update
concurrent_archival_update = OperatorPOWL(operator=Operator.CONC, children=[archival_update, re_validation])
root.order.add_edge(archival_update, concurrent_archival_update)
root.order.add_edge(re_validation, concurrent_archival_update)

# Add concurrent activities for insurance setup
concurrent_insurance_setup = OperatorPOWL(operator=Operator.CONC, children=[insurance_setup, exhibition_prep])
root.order.add_edge(insurance_setup, concurrent_insurance_setup)
root.order.add_edge(exhibition_prep, concurrent_insurance_setup)

# Add concurrent activities for IoT monitoring
concurrent_iot_monitor