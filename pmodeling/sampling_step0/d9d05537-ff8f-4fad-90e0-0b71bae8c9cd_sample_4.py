import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator
alert_verify = Transition(label='Alert Verify')
impact_assess = Transition(label='Impact Assess')
team_assemble = Transition(label='Team Assemble')
resource_allocate = Transition(label='Resource Allocate')
stakeholder_notify = Transition(label='Stakeholder Notify')
legal_review = Transition(label='Legal Review')
media_brief = Transition(label='Media Brief')
response_deploy = Transition(label='Response Deploy')
situation_monitor = Transition(label='Situation Monitor')
data_collect = Transition(label='Data Collect')
risk_mitigate = Transition(label='Risk Mitigate')
recovery_plan = Transition(label='Recovery Plan')
external_consult = Transition(label='External Consult')
status_update = Transition(label='Status Update')
post_review = Transition(label='Post Review')
skip = SilentTransition()
# Rapid assessment
rapid_assessment = OperatorPOWL(operator=Operator.LOOP, children=[alert_verify, impact_assess])
# Resource mobilization and communication strategies
resource_mobilization = OperatorPOWL(operator=Operator.XOR, children=[team_assemble, skip])
communication_strategies = OperatorPOWL(operator=Operator.XOR, children=[resource_allocate, stakeholder_notify])
# Legal compliance checks and iterative recovery efforts
legal_compliance_checks = OperatorPOWL(operator=Operator.LOOP, children=[legal_review, media_brief])
iterative_recovery = OperatorPOWL(operator=Operator.XOR, children=[response_deploy, skip])
# Cross-functional teams, external agencies, and continuous monitoring
cross_functional_teams = OperatorPOWL(operator=Operator.LOOP, children=[external_consult, status_update])
external_agencies = OperatorPOWL(operator=Operator.XOR, children=[situation_monitor, skip])
continuous_monitoring = OperatorPOWL(operator=Operator.LOOP, children=[data_collect, risk_mitigate])
# Post-crisis evaluation
post_crisis_evaluation = OperatorPOWL(operator=Operator.LOOP, children=[recovery_plan, post_review])
# Integration
root = StrictPartialOrder(nodes=[rapid_assessment, resource_mobilization, communication_strategies, legal_compliance_checks, iterative_recovery, cross_functional_teams, external_agencies, continuous_monitoring, post_crisis_evaluation])
root.order.add_edge(rapid_assessment, resource_mobilization)
root.order.add_edge(rapid_assessment, communication_strategies)
root.order.add_edge(resource_mobilization, legal_compliance_checks)
root.order.add_edge(resource_mobilization, iterative_recovery)
root.order.add_edge(communication_strategies, cross_functional_teams)
root.order.add_edge(communication_strategies, external_agencies)
root.order.add_edge(legal_compliance_checks, iterative_recovery)
root.order.add_edge(legal_compliance_checks, cross_functional_teams)
root.order.add_edge(legal_compliance_checks, external_agencies)
root.order.add_edge(iterative_recovery, cross_functional_teams)
root.order.add_edge(iterative_recovery, external_agencies)
root.order.add_edge(cross_functional_teams, continuous_monitoring)
root.order.add_edge(external_agencies, continuous_monitoring)
root.order.add_edge(continuous_monitoring, post_crisis_evaluation)