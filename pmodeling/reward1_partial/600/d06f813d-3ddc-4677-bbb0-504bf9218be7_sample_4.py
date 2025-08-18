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

provenance_loop = OperatorPOWL(operator=Operator.LOOP, children=[provenance_check, specimen_sampling, spectroscopy_test, radiocarbon_date, material_analysis, forensic_review, expert_consult, legal_verify, ownership_audit])
legal_loop = OperatorPOWL(operator=Operator.LOOP, children=[risk_assess, insurance_quote, condition_report, documentation, committee_review])
root = StrictPartialOrder(nodes=[provenance_loop, legal_loop, final_approval])
root.order.add_edge(provenance_loop, legal_loop)
root.order.add_edge(legal_loop, final_approval)