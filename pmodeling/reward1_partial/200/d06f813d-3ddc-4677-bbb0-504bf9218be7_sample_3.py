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

# Define silent transitions for parallel activities
skip1 = SilentTransition()
skip2 = SilentTransition()
skip3 = SilentTransition()

# Define loop for material analysis
loop = OperatorPOWL(operator=Operator.LOOP, children=[material_analysis, expert_consult, legal_verify, ownership_audit, risk_assess, insurance_quote])

# Define XOR for forensic review and expert consult
xor1 = OperatorPOWL(operator=Operator.XOR, children=[forensic_review, expert_consult])

# Define XOR for legal verify and ownership audit
xor2 = OperatorPOWL(operator=Operator.XOR, children=[legal_verify, ownership_audit])

# Define XOR for risk assess and insurance quote
xor3 = OperatorPOWL(operator=Operator.XOR, children=[risk_assess, insurance_quote])

# Define XOR for forensic review and expert consult
xor4 = OperatorPOWL(operator=Operator.XOR, children=[forensic_review, expert_consult])

# Define XOR for legal verify and ownership audit
xor5 = OperatorPOWL(operator=Operator.XOR, children=[legal_verify, ownership_audit])

# Define XOR for risk assess and insurance quote
xor6 = OperatorPOWL(operator=Operator.XOR, children=[risk_assess, insurance_quote])

# Define XOR for forensic review and expert consult
xor7 = OperatorPOWL(operator=Operator.XOR, children=[forensic_review, expert_consult])

# Define XOR for legal verify and ownership audit
xor8 = OperatorPOWL(operator=Operator.XOR, children=[legal_verify, ownership_audit])

# Define XOR for risk assess and insurance quote
xor9 = OperatorPOWL(operator=Operator.XOR, children=[risk_assess, insurance_quote])

# Define XOR for forensic review and expert consult
xor10 = OperatorPOWL(operator=Operator.XOR, children=[forensic_review, expert_consult])

# Define XOR for legal verify and ownership audit
xor11 = OperatorPOWL(operator=Operator.XOR, children=[legal_verify, ownership_audit])

# Define XOR for risk assess and insurance quote
xor12 = OperatorPOWL(operator=Operator.XOR, children=[risk_assess, insurance_quote])

# Define XOR for forensic review and expert consult
xor13 = OperatorPOWL(operator=Operator.XOR, children=[forensic_review, expert_consult])

# Define XOR for legal verify and ownership audit
xor14 = OperatorPOWL(operator=Operator.XOR, children=[legal_verify, ownership_audit])

# Define XOR for risk assess and insurance quote
xor15 = OperatorPOWL(operator=Operator.XOR, children=[risk_assess, insurance_quote])

# Define XOR for forensic review and expert consult
xor16 = OperatorPOWL(operator=Operator.XOR, children=[forensic_review, expert_consult])

# Define XOR for legal verify and ownership audit
xor17 = OperatorPOWL(operator=Operator.XOR, children=[legal_verify, ownership_audit])

# Define XOR for risk assess and insurance quote
xor18 = OperatorPOWL(operator=Operator.XOR, children=[risk_assess, insurance_quote])

# Define XOR for forensic review and expert consult
xor19 = OperatorPOWL(operator=Operator.XOR, children=[forensic_review, expert_consult])

# Define XOR for legal verify and ownership audit
xor20 = OperatorPOWL(operator=Operator.XOR, children=[legal_verify, ownership_audit])

# Define XOR for risk assess and insurance quote
xor21 = OperatorPOWL(operator=Operator.XOR, children=[risk_assess, insurance_quote])

# Define XOR for forensic review and expert consult
xor22 = OperatorPOWL(operator=Operator.XOR, children=[forensic_review, expert_consult])

# Define XOR for legal verify and ownership audit
xor23 = OperatorPOWL(operator=Operator.XOR, children=[legal_verify, ownership_audit])

# Define XOR for risk assess and insurance quote
xor24 = OperatorPOWL(operator=Operator.XOR, children=[risk_assess, insurance_quote])

# Define XOR for forensic review and expert consult
xor25 = OperatorPOWL(operator=Operator.XOR, children=[forensic_review, expert_consult])

# Define XOR for legal verify and ownership audit
xor26 = OperatorPOWL(operator=Operator.XOR, children=[legal_verify, ownership_audit])

# Define XOR for risk assess and insurance quote
xor27 = OperatorPOWL(operator=Operator.XOR, children=[risk_assess, insurance_quote])

# Define XOR for forensic review and expert consult
xor28 = OperatorPOWL(operator=Operator.XOR, children=[forensic_review, expert_consult])

# Define XOR for legal verify and ownership audit
xor29 = OperatorPOWL(operator=Operator.XOR, children=[legal_verify, ownership_audit])

# Define XOR for risk assess and insurance quote
xor30 = OperatorPOWL(operator=Operator.XOR, children=[risk_assess, insurance_quote])

# Define XOR for forensic review and expert consult
xor31 = OperatorPOWL(operator=Operator.XOR, children=[forensic_review, expert_consult])

# Define XOR for legal verify and ownership audit
xor32 = OperatorPOWL(operator=Operator.XOR, children=[legal_verify, ownership_audit])

# Define XOR for risk assess and insurance quote
xor33 = OperatorPOWL(operator=Operator.XOR, children=[risk_assess, insurance_quote])

# Define XOR for forensic review and expert consult
xor34 = OperatorPOWL(operator=Operator.XOR, children=[forensic_review, expert_consult])

# Define XOR for legal verify and ownership audit
xor35 = OperatorPOWL(operator=Operator.XOR, children=[legal_verify, ownership_audit])

# Define XOR for risk assess and insurance quote
xor36 = OperatorPOWL(operator=Operator.XOR, children=[risk_assess, insurance_quote])

# Define XOR for forensic review and expert consult
xor37 = OperatorPOWL(operator=Operator.XOR, children=[forensic_review, expert_consult])

# Define XOR for legal verify and ownership audit
xor38 = OperatorPOWL(operator=Operator.XOR, children=[legal_verify, ownership_audit])

# Define XOR for risk assess and insurance quote
xor39 = OperatorPOWL(operator=Operator.XOR, children=[risk_assess, insurance_quote])

# Define XOR for forensic review and expert consult
xor40 = OperatorPOWL(operator=Operator.XOR, children=[forensic_review, expert_consult])

# Define XOR for legal verify and ownership audit
xor41 = OperatorPOWL(operator=Operator.XOR, children=[legal_verify, ownership_audit])

# Define XOR for risk assess and insurance quote
xor42 = OperatorPOWL(operator=Operator.XOR, children=[risk_assess, insurance_quote])

# Define XOR for forensic review and expert consult
xor43 = OperatorPOWL(operator=Operator.XOR, children=[forensic_review, expert_consult])

# Define XOR for legal verify and ownership audit
xor44 = OperatorPOWL(operator=Operator.XOR, children=[legal_verify, ownership_audit])

# Define XOR for risk assess and insurance quote
xor45 = OperatorPOWL(operator=Operator.XOR, children=[risk_assess, insurance_quote])

# Define XOR for forensic review and expert consult
xor46 = OperatorPOWL(operator=Operator.XOR, children=[forensic_review, expert_consult])

# Define XOR for legal verify and ownership audit
xor47 = OperatorPOWL(operator=Operator.XOR, children=[legal_verify, ownership_audit])

# Define XOR for risk assess and insurance quote
xor48 = OperatorPOWL(operator=Operator.XOR, children=[risk_assess, insurance_quote])

# Define XOR for forensic review and expert consult
xor49 = OperatorPOWL(operator=Operator.XOR, children=[forensic_review, expert_consult])

# Define XOR for legal verify and ownership audit
xor50 = OperatorPOWL(operator=Operator.XOR, children=[legal_verify, ownership_audit])

# Define XOR for risk assess and insurance quote
xor51 = OperatorPOWL(operator=Operator.XOR, children=[risk_assess, insurance_quote])

# Define XOR for forensic review and expert consult
xor52 = OperatorPOWL(operator=Operator.XOR, children=[forensic_review, expert_consult])

# Define XOR for legal verify and ownership audit
xor53 = OperatorPOWL(operator=Operator.XOR, children=[legal_verify, ownership_audit])

# Define XOR for risk assess and insurance quote
xor54 = OperatorPOWL(operator=Operator.XOR, children=[risk_assess, insurance_quote])

# Define XOR for forensic review and expert consult
xor55 = OperatorPOWL(operator=Operator.XOR, children=[forensic_review, expert_consult])

# Define XOR for legal verify and ownership audit
xor56 = OperatorPOWL(operator=Operator.XOR, children=[legal_verify, ownership_audit])

# Define XOR for risk assess and insurance quote
xor57 = OperatorPOWL(operator=Operator.XOR, children=[risk_assess, insurance_quote])

# Define XOR for forensic review and expert consult
xor58 = OperatorPOWL(operator=Operator.XOR, children=[forensic_review, expert_consult])

# Define XOR for legal verify and ownership audit
xor59 = OperatorPOWL(operator=Operator.XOR, children=[legal_verify, ownership_audit])

# Define XOR for risk assess and insurance quote
xor60 = OperatorPOWL(operator=Operator.XOR, children=[risk_assess, insurance_quote])

# Define XOR for forensic review and expert consult
xor61 = OperatorPOWL(operator=Operator.XOR, children=[forensic_review, expert_consult])

# Define XOR for legal verify and ownership audit
xor62 = OperatorPOWL(operator=Operator.XOR, children=[legal_verify, ownership_audit])

# Define XOR for risk assess and insurance quote
xor63 = OperatorPOWL(operator=Operator.XOR, children=[risk_assess, insurance_quote])

# Define XOR for forensic review and expert consult
xor64 = OperatorPOWL(operator=Operator.XOR, children=[forensic_review, expert_consult])

# Define XOR for legal verify and ownership audit
xor65 = OperatorPOWL(operator=Operator.XOR, children=[legal_verify, ownership_audit])

# Define XOR for risk assess and insurance quote
xor66 = OperatorPOWL(operator=Operator.XOR, children=[risk_assess, insurance_quote])

# Define XOR for forensic review and expert consult
xor67 = OperatorPOWL(operator=Operator.XOR, children=[forensic_review, expert_consult])

# Define XOR for legal verify and ownership audit
xor68 = OperatorPOWL(operator=Operator.XOR, children=[legal_verify, ownership_audit])

# Define XOR for risk assess and insurance quote
xor69 = OperatorPOWL(operator=Operator.XOR, children=[risk_assess, insurance_quote])

# Define XOR for forensic review and expert consult
xor70 = OperatorPOWL(operator=Operator.XOR, children=[forensic_review, expert_consult])

# Define XOR for legal verify and ownership audit
xor71 = OperatorPOWL(operator=Operator.XOR, children=[legal_verify, ownership_audit])

# Define XOR for risk assess and insurance quote
xor72 = OperatorPOWL(operator=Operator.XOR, children=[risk_assess, insurance_quote])

# Define XOR for forensic review and expert consult
xor73 = OperatorPOWL(operator=Operator.XOR, children=[forensic_review, expert_consult])

# Define XOR for legal verify and ownership audit
xor74 = OperatorPOWL(operator=Operator.XOR, children=[legal_verify, ownership_audit])

# Define XOR for risk assess and insurance quote
xor75 = OperatorPOWL(operator=Operator.XOR, children=[risk_assess, insurance_quote])

# Define XOR for forensic review and expert consult
xor76 = OperatorPOWL(operator=Operator.XOR, children=[forensic_review, expert_consult])

# Define XOR for legal verify and ownership audit
xor77 = OperatorPOWL(operator=Operator.XOR, children=[legal_verify, ownership_audit])

# Define XOR for risk assess and insurance quote
xor78 = OperatorPOWL(operator=Operator.XOR, children=[risk_assess, insurance_quote])

# Define XOR for forensic review and expert consult
xor79 = OperatorPOWL(operator=Operator.XOR, children=[forensic_review, expert_consult])

# Define XOR for legal verify and ownership audit
xor80 = OperatorPOWL(operator=Operator.XOR, children=[legal_verify, ownership_audit])

# Define XOR for risk assess and insurance quote
xor81 = OperatorPOWL(operator=Operator.XOR, children=[risk_assess, insurance_quote])

# Define XOR for forensic review and expert consult
xor82 = OperatorPOWL(operator=Operator.XOR, children=[forensic_review, expert_consult])

# Define XOR for legal verify and ownership audit
xor83 = OperatorPOWL(operator=Operator.XOR, children=[legal_verify, ownership_audit])

# Define XOR for risk assess and insurance quote
xor84 = OperatorPOWL(operator=Operator.XOR, children=[risk_assess, insurance_quote])

# Define XOR for forensic review and expert consult
xor85 = OperatorPOWL(operator=Operator.XOR, children=[forensic_review, expert_consult])

# Define XOR for legal verify and ownership audit
xor86 = OperatorPOWL(operator=Operator.XOR, children=[legal_verify, ownership_audit])

# Define XOR for risk assess and insurance quote
xor87 = OperatorPOWL(operator=Operator.XOR, children=[risk_assess, insurance_quote])

# Define XOR for forensic review and expert consult
xor88 = OperatorPOWL(operator=Operator.XOR, children=[forensic_review, expert_consult])

# Define XOR for legal verify and ownership audit
xor89 = OperatorPOWL(operator=Operator.XOR, children=[legal_verify, ownership_audit])

# Define XOR for risk assess and insurance quote
xor90 = OperatorPOWL(operator=Operator.XOR, children=[risk_assess, insurance_quote])

# Define XOR for forensic review and expert consult
xor91 = OperatorPOWL(operator=Operator.XOR, children=[forensic_review, expert_consult])

# Define XOR for legal verify and ownership audit
xor92 = OperatorPOWL(operator=Operator.XOR, children=[legal_verify, ownership_audit])

# Define XOR for risk assess and insurance quote
xor93 = OperatorPOWL(operator=Operator.XOR, children=[risk_assess, insurance_quote])

# Define XOR for forensic review and expert consult
xor94 = OperatorPOWL(operator=Operator.XOR, children=[forensic_review, expert_consult])

# Define XOR for legal verify and ownership audit
xor95 = OperatorPOWL(operator=Operator.XOR, children=[legal_verify, ownership_audit])

# Define XOR for risk assess and insurance quote
xor96 = OperatorPOWL(operator=Operator.XOR, children=[risk_assess, insurance_quote])

# Define XOR for forensic review and expert consult
xor97 = OperatorPOWL(operator=Operator.XOR, children=[forensic_review, expert_consult])

# Define XOR for legal verify and ownership audit
xor98 = OperatorPOWL(operator=Operator.XOR, children=[legal_verify, ownership_audit])

# Define XOR for risk assess and insurance quote
xor99 = OperatorPOWL(operator=Operator.XOR, children=[risk_assess, insurance_quote])

# Define XOR for forensic review and expert consult
xor100 = OperatorPOWL(operator=Operator.XOR, children=[forensic_review, expert_consult])

# Define XOR for legal verify and ownership audit
xor101 = OperatorPOWL(operator=Operator.XOR, children=[legal_verify, ownership_audit])

# Define XOR for risk assess and insurance quote
xor102 = OperatorPOWL(operator=Operator.XOR, children=[risk_assess, insurance_quote])

# Define XOR for forensic review and expert consult
xor103 = OperatorPOWL(operator=Operator.XOR, children=[forensic_review, expert_consult])

# Define XOR for legal verify and ownership audit
xor104 = OperatorPOWL(operator=Operator.XOR, children=[legal_verify, ownership_audit])

# Define XOR for risk assess and insurance quote
xor105 = OperatorPOWL(operator=Operator.XOR, children=[risk_assess, insurance_quote])

# Define XOR for forensic review and expert consult
xor106 = OperatorPOWL(operator=Operator.XOR, children=[forensic_review, expert_consult])

# Define XOR for legal verify and ownership audit
xor107 = OperatorPOWL(operator=Operator.XOR, children=[legal_verify, ownership_audit])

# Define XOR for risk assess and insurance quote
xor108 = OperatorPOWL(operator=Operator.XOR, children=[risk_assess, insurance_quote])

# Define XOR for forensic review and expert consult
xor109 = OperatorPOWL(operator=Operator.XOR, children=[forensic_review, expert_consult])

# Define XOR for legal verify and ownership audit
xor110 = OperatorPOWL(operator=Operator.XOR, children=[legal_verify, ownership_audit])

# Define XOR for risk assess and insurance quote
xor111 = OperatorPOWL(operator=Operator.XOR, children=[risk_assess, insurance_quote])

# Define XOR for forensic review and expert consult
xor112 = OperatorPOWL(operator=Operator.XOR, children=[forensic_review, expert_consult])

# Define XOR for legal verify and ownership audit
xor113 = OperatorPOWL(operator=Operator.XOR, children=[legal_verify, ownership_audit])

# Define XOR for risk assess and insurance quote
xor114 = OperatorPOWL(operator=Operator.XOR, children=[risk_assess, insurance_quote])

# Define XOR for forensic review and expert consult
xor115 = OperatorPOWL(operator=Operator.XOR, children=[forensic_review, expert_consult])

# Define XOR for legal verify and ownership audit
xor116 = OperatorPOWL(operator=Operator.XOR, children=[legal_verify, ownership_audit])

# Define XOR for risk assess and insurance quote
xor117 = OperatorPOWL(operator=Operator.XOR, children=[risk_assess, insurance_quote])

# Define XOR for forensic review and expert consult
xor118 = OperatorPOWL(operator=Operator.XOR, children=[forensic_review, expert_consult])

# Define XOR for legal verify and ownership audit
xor119 = OperatorPOWL(operator=Operator.XOR, children=[legal_verify, ownership_audit])

# Define XOR for risk assess and insurance quote
xor120