import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
initial_inquiry       = Transition(label='Initial Inquiry')
document_review       = Transition(label='Document Review')
historical_research   = Transition(label='Historical Research')
material_sampling     = Transition(label='Material Sampling')
forensic_testing      = Transition(label='Forensic Testing')
ownership_audit       = Transition(label='Ownership Audit')
legal_verification    = Transition(label='Legal Verification')
ethical_screening     = Transition(label='Ethical Screening')
expert_consultation   = Transition(label='Expert Consultation')
cultural_assessment   = Transition(label='Cultural Assessment')
condition_survey      = Transition(label='Condition Survey')
provenance_mapping    = Transition(label='Provenance Mapping')
risk_analysis         = Transition(label='Risk Analysis')
report_compilation    = Transition(label='Report Compilation')
acquisition_approval  = Transition(label='Acquisition Approval')
repatriation_review   = Transition(label='Repatriation Review')
archival_storage      = Transition(label='Archival Storage')

# Silent transition for loop exit
skip = SilentTransition()

# Define the loop for optional repatriation review
repatriation_loop = OperatorPOWL(operator=Operator.LOOP, children=[repatriation_review, skip])

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    initial_inquiry,
    document_review,
    historical_research,
    material_sampling,
    forensic_testing,
    ownership_audit,
    legal_verification,
    ethical_screening,
    expert_consultation,
    cultural_assessment,
    condition_survey,
    provenance_mapping,
    risk_analysis,
    report_compilation,
    acquisition_approval,
    repatriation_loop,
    archival_storage
])

# Sequential dependencies
root.order.add_edge(initial_inquiry, document_review)

# After document review, multiple concurrent tasks
root.order.add_edge(document_review, historical_research)
root.order.add_edge(document_review, material_sampling)

# Sampling and research feed into forensic testing
root.order.add_edge(historical_research, forensic_testing)
root.order.add_edge(material_sampling, forensic_testing)

# Forensic testing feeds into ownership and legal verification
root.order.add_edge(forensic_testing, ownership_audit)
root.order.add_edge(forensic_testing, legal_verification)

# Ownership and legal verification feed into ethical screening
root.order.add_edge(ownership_audit, ethical_screening)
root.order.add_edge(legal_verification, ethical_screening)

# Ethical screening feeds into expert consultation
root.order.add_edge(ethical_screening, expert_consultation)

# Expert consultation feeds into cultural and condition assessment
root.order.add_edge(expert_consultation, cultural_assessment)
root.order.add_edge(expert_consultation, condition_survey)

# Both assessment tasks feed into provenance mapping
root.order.add_edge(cultural_assessment, provenance_mapping)
root.order.add_edge(condition_survey, provenance_mapping)

# Provenance mapping feeds into risk analysis
root.order.add_edge(provenance_mapping, risk_analysis)

# Risk analysis feeds into report compilation
root.order.add_edge(risk_analysis, report_compilation)

# Report compilation feeds into acquisition approval
root.order.add_edge(report_compilation, acquisition_approval)

# Acquisition approval then either proceeds to repatriation or archival storage
root.order.add_edge(acquisition_approval, repatriation_loop)
root.order.add_edge(acquisition_approval, archival_storage)