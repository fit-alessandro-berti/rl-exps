import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions
identify_need = Transition(label='Identify need for new hire')
create_description = Transition(label='Create job description')
post_description = Transition(label='Post job description')
collect_resumes = Transition(label='Collect resumes')
screen_resumes = Transition(label='Screen resumes')
initial_phone_interviews = Transition(label='Conduct initial phone interviews')
invite_candidates = Transition(label='Invite candidates for interviews')
virtual_interview = Transition(label='Conduct a virtual interview')
in_person_interview = Transition(label='Conduct an in-person interview')
choose_candidate = Transition(label='Choose candidate')
extend_offer = Transition(label='Extend offer')
negotiate_salary = Transition(label='Negotiate salary')
begin_onboarding = Transition(label='Begin onboarding process')
complete_paperwork = Transition(label='Complete paperwork')
complete_orientation = Transition(label='Complete orientation')
complete_training = Transition(label='Complete training')

# Define choices and loops
interview_choice = OperatorPOWL(operator=Operator.XOR, children=[virtual_interview, in_person_interview])
negotiate_salary_loop = OperatorPOWL(operator=Operator.LOOP, children=[negotiate_salary, extend_offer])
onboarding_process = OperatorPOWL(operator=Operator.LOOP, children=[complete_paperwork, complete_orientation, complete_training])

# Define the root
root = StrictPartialOrder(nodes=[identify_need, create_description, post_description, collect_resumes, screen_resumes, initial_phone_interviews, invite_candidates, interview_choice, choose_candidate, extend_offer, negotiate_salary_loop, begin_onboarding, onboarding_process])

# Define the order
root.order.add_edge(identify_need, create_description)
root.order.add_edge(create_description, post_description)
root.order.add_edge(post_description, collect_resumes)
root.order.add_edge(collect_resumes, screen_resumes)
root.order.add_edge(screen_resumes, initial_phone_interviews)
root.order.add_edge(initial_phone_interviews, invite_candidates)
root.order.add_edge(invite_candidates, interview_choice)
root.order.add_edge(interview_choice, choose_candidate)
root.order.add_edge(choose_candidate, extend_offer)
root.order.add_edge(extend_offer, negotiate_salary_loop)
root.order.add_edge(negotiate_salary_loop, begin_onboarding)
root.order.add_edge(begin_onboarding, onboarding_process)