import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
provenance_check = Transition(label='Provenance Check')
specimen_sampling = Transition(label='Specimen Sampling')
spectroscopy_test = Transition(label='Spectroscopy Test')
radiocarbon_date = Transition(label='Radiocarbon Date')
material_analysis = Transition(label='Material Analysis')
forensic_review = Transition(label='Forensic Review')
expert_consult = Transition(label='Expert Consult')
legal_verify = Transition(label='Legal Verify')
ownership_audit = Transition(label='Ownership Audit')
risk_assess = Transition(label='Risk Assess')
insurance_quote = Transition(label='Insurance Quote')
condition_report = Transition(label='Condition Report')
documentation = Transition(label='Documentation')
committee_review = Transition(label='Committee Review')
final_approval = Transition(label='Final Approval')

# Define silent transitions
skip = SilentTransition()

# Define exclusive choice for expert consult and forensic review
expert_or_forensic = OperatorPOWL(operator=Operator.XOR, children=[expert_consult, forensic_review])

# Define loop for risk assessment and insurance quote
risk_insurance_loop = OperatorPOWL(operator=Operator.LOOP, children=[risk_assess, insurance_quote])

# Define partial order for the process
root = StrictPartialOrder(nodes=[
    provenance_check,
    specimen_sampling,
    spectroscopy_test,
    radiocarbon_date,
    material_analysis,
    expert_or_forensic,
    ownership_audit,
    risk_insurance_loop,
    condition_report,
    documentation,
    committee_review,
    final_approval
])

# Define the order of execution
root.order.add_edge(provenance_check, specimen_sampling)
root.order.add_edge(provenance_check, spectroscopy_test)
root.order.add_edge(provenance_check, radiocarbon_date)
root.order.add_edge(provenance_check, material_analysis)
root.order.add_edge(specimen_sampling, expert_or_forensic)
root.order.add_edge(specimen_sampling, ownership_audit)
root.order.add_edge(expert_or_forensic, risk_insurance_loop)
root.order.add_edge(expert_or_forensic, condition_report)
root.order.add_edge(ownership_audit, risk_insurance_loop)
root.order.add_edge(ownership_audit, condition_report)
root.order.add_edge(risk_insurance_loop, condition_report)
root.order.add_edge(condition_report, documentation)
root.order.add_edge(condition_report, committee_review)
root.order.add_edge(committee_review, final_approval)