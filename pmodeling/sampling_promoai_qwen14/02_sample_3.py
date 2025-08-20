import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities as transitions
begin_onboarding_process = Transition(label='Begin onboarding process')
choose_candidate = Transition(label='Choose candidate')
collect_resumes = Transition(label='Collect resumes')
complete_orientation = Transition(label='Complete orientation')
complete_paperwork = Transition(label='Complete paperwork')
complete_training = Transition(label='Complete training')
conduct_virtual_interview = Transition(label='Conduct a virtual interview')
conduct_in_person_interview = Transition(label='Conduct an in-person interview')
conduct_initial_phone_interviews = Transition(label='Conduct initial phone interviews')
create_job_description = Transition(label='Create job description')
extend_offer = Transition(label='Extend offer')
identify_need_for_new_hire = Transition(label='Identify need for new hire')
invite_candidates_for_interviews = Transition(label='Invite candidates for interviews')
negotiate_salary = Transition(label='Negotiate salary')
post_job_description = Transition(label='Post job description')
screen_resumes = Transition(label='Screen resumes')

# Define the loops and choices
screen_resumes_loop = OperatorPOWL(operator=Operator.LOOP, children=[screen_resumes, conduct_initial_phone_interviews])
conduct_interview_choice = OperatorPOWL(operator=Operator.XOR, children=[conduct_virtual_interview, conduct_in_person_interview])
negotiate_salary_choice = OperatorPOWL(operator=Operator.XOR, children=[negotiate_salary, SilentTransition()])

# Define the partial orders
post_job_description_order = StrictPartialOrder(nodes=[post_job_description, collect_resumes])
collect_resumes_order = StrictPartialOrder(nodes=[collect_resumes, screen_resumes_loop])
screen_resumes_loop_order = StrictPartialOrder(nodes=[screen_resumes_loop, invite_candidates_for_interviews])
invite_candidates_for_interviews_order = StrictPartialOrder(nodes=[invite_candidates_for_interviews, conduct_interview_choice])
conduct_interview_choice_order = StrictPartialOrder(nodes=[conduct_interview_choice, choose_candidate])
choose_candidate_order = StrictPartialOrder(nodes=[choose_candidate, extend_offer])
extend_offer_order = StrictPartialOrder(nodes=[extend_offer, negotiate_salary_choice])
negotiate_salary_choice_order = StrictPartialOrder(nodes=[negotiate_salary_choice, begin_onboarding_process])
begin_onboarding_process_order = StrictPartialOrder(nodes=[begin_onboarding_process, complete_paperwork, complete_orientation, complete_training])

# Define the root
root = StrictPartialOrder(nodes=[identify_need_for_new_hire, post_job_description_order, collect_resumes_order, screen_resumes_loop_order, invite_candidates_for_interviews_order, conduct_interview_choice_order, choose_candidate_order, extend_offer_order, negotiate_salary_choice_order, begin_onboarding_process_order])

# Define the dependencies
root.order.add_edge(identify_need_for_new_hire, post_job_description_order)
root.order.add_edge(post_job_description_order, collect_resumes_order)
root.order.add_edge(collect_resumes_order, screen_resumes_loop_order)
root.order.add_edge(screen_resumes_loop_order, invite_candidates_for_interviews_order)
root.order.add_edge(invite_candidates_for_interviews_order, conduct_interview_choice_order)
root.order.add_edge(conduct_interview_choice_order, choose_candidate_order)
root.order.add_edge(choose_candidate_order, extend_offer_order)
root.order.add_edge(extend_offer_order, negotiate_salary_choice_order)
root.order.add_edge(negotiate_salary_choice_order, begin_onboarding_process_order)
root.order.add_edge(begin_onboarding_process_order, complete_paperwork)
root.order.add_edge(begin_onboarding_process_order, complete_orientation)
root.order.add_edge(begin_onboarding_process_order, complete_training)