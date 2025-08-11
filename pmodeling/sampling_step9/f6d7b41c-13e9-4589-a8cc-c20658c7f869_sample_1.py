import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

ClientConsult = Transition(label='Client Consult')
NeedsAssess = Transition(label='Needs Assess')
ArtSelection = Transition(label='Art Selection')
InventoryCheck = Transition(label='Inventory Check')
LegalDraft = Transition(label='Legal Draft')
ContractSign = Transition(label='Contract Sign')
InsuranceSetup = Transition(label='Insurance Setup')
TransportPlan = Transition(label='Transport Plan')
SecureTransit = Transition(label='Secure Transit')
ArtInstall = Transition(label='Art Install')
ConditionCheck = Transition(label='Condition Check')
AppraisalLog = Transition(label='Appraisal Log')
LeaseRenew = Transition(label='Lease Renew')
PaymentProcess = Transition(label='Payment Process')
DeinstallArt = Transition(label='Deinstall Art')
ReturnInspect = Transition(label='Return Inspect')
PurchaseOption = Transition(label='Purchase Option')

skip = SilentTransition()

# Client Consultation and Needs Assessment
client_consult_and_assess = OperatorPOWL(operator=Operator.XOR, children=[ClientConsult, NeedsAssess])
# Art Selection and Inventory Check
art_selection_and_inventory = OperatorPOWL(operator=Operator.XOR, children=[ArtSelection, InventoryCheck])
# Legal Draft and Contract Sign
legal_draft_and_contract_sign = OperatorPOWL(operator=Operator.XOR, children=[LegalDraft, ContractSign])
# Insurance Setup
insurance_setup = Transition(label='Insurance Setup')
# Transport Plan and Secure Transit
transport_plan_and_secure_transit = OperatorPOWL(operator=Operator.XOR, children=[TransportPlan, SecureTransit])
# Art Install and Condition Check
art_install_and_condition_check = OperatorPOWL(operator=Operator.XOR, children=[ArtInstall, ConditionCheck])
# Appraisal Log and Lease Renew
appraisal_log_and_lease_renew = OperatorPOWL(operator=Operator.XOR, children=[AppraisalLog, LeaseRenew])
# Payment Process and Deinstall Art
payment_process_and_deinstall_art = OperatorPOWL(operator=Operator.XOR, children=[PaymentProcess, DeinstallArt])
# Return Inspect and Purchase Option
return_inspect_and_purchase_option = OperatorPOWL(operator=Operator.XOR, children=[ReturnInspect, PurchaseOption])

# Loops
art_selection_loop = OperatorPOWL(operator=Operator.LOOP, children=[ArtSelection, InventoryCheck])
legal_draft_loop = OperatorPOWL(operator=Operator.LOOP, children=[LegalDraft, ContractSign])
insurance_setup_loop = OperatorPOWL(operator=Operator.LOOP, children=[InsuranceSetup])
transport_plan_loop = OperatorPOWL(operator=Operator.LOOP, children=[TransportPlan, SecureTransit])
art_install_loop = OperatorPOWL(operator=Operator.LOOP, children=[ArtInstall, ConditionCheck])
appraisal_log_loop = OperatorPOWL(operator=Operator.LOOP, children=[AppraisalLog, LeaseRenew])
payment_process_loop = OperatorPOWL(operator=Operator.LOOP, children=[PaymentProcess, DeinstallArt])
return_inspect_loop = OperatorPOWL(operator=Operator.LOOP, children=[ReturnInspect, PurchaseOption])

# Construct the POWL model
root = StrictPartialOrder(nodes=[client_consult_and_assess, art_selection_and_inventory, legal_draft_and_contract_sign, insurance_setup, transport_plan_and_secure_transit, art_install_and_condition_check, appraisal_log_and_lease_renew, payment_process_and_deinstall_art, return_inspect_and_purchase_option, art_selection_loop, legal_draft_loop, insurance_setup_loop, transport_plan_loop, art_install_loop, appraisal_log_loop, payment_process_loop, return_inspect_loop])
root.order.add_edge(client_consult_and_assess, art_selection_and_inventory)
root.order.add_edge(client_consult_and_assess, legal_draft_and_contract_sign)
root.order.add_edge(art_selection_and_inventory, art_selection_loop)
root.order.add_edge(legal_draft_and_contract_sign, legal_draft_loop)
root.order.add_edge(insurance_setup, insurance_setup_loop)
root.order.add_edge(transport_plan_and_secure_transit, transport_plan_loop)
root.order.add_edge(art_install_and_condition_check, art_install_loop)
root.order.add_edge(appraisal_log_and_lease_renew, appraisal_log_loop)
root.order.add_edge(payment_process_and_deinstall_art, payment_process_loop)
root.order.add_edge(return_inspect_and_purchase_option, return_inspect_loop)