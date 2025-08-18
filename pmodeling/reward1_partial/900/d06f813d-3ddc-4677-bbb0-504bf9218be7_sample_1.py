import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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

skip = SilentTransition()

provenance_check_node = OperatorPOWL(operator=Operator.SEQUENCE, children=[provenance_check, specimen_sampling])
specimen_sampling_node = OperatorPOWL(operator=Operator.SEQUENCE, children=[specimen_sampling, spectroscopy_test, radiocarbon_date, material_analysis])
forensic_review_node = OperatorPOWL(operator=Operator.SEQUENCE, children=[forensic_review, expert_consult, legal_verify, ownership_audit, risk_assess, insurance_quote, condition_report])
documentation_node = OperatorPOWL(operator=Operator.SEQUENCE, children=[documentation, committee_review, final_approval])

root = StrictPartialOrder(nodes=[provenance_check_node, specimen_sampling_node, forensic_review_node, documentation_node])
root.order.add_edge(provenance_check_node, specimen_sampling_node)
root.order.add_edge(specimen_sampling_node, forensic_review_node)
root.order.add_edge(forensic_review_node, documentation_node)