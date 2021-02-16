import argparse


def fallback(inp, transitions, stack, state_expressions, expression_tokens, final_states):
	r = 0
	l = 0
	length = len(inp)
	# print(length)

	tokens=[]

	failed_token=[]

	counter = 1

	lits_stack = []


	while(True):
		while(r <= l < length):
			lit = inp[l]
			for t in transitions:
				found = False
				if (t[1] == lit) and (t[0] == stack[-1][0]):
					target_lit=t[2]
					for se in state_expressions:
						if se[0] == target_lit:
							# print(t[0])
							# print(final_states)
							if se[0] not in final_states:
								new_se = (se[0], '"DEFAULT"')
								# print('ksksks')
								# print(new_se)
								stack.append(new_se)
								lits_stack.append(lit)
								found = True
								break
							else:	
								stack.append(se)
								lits_stack.append(lit)
								found = True
								break
				if found == True:
					break			
			l+=1
		
		# print(stack)
		last_element = stack.pop()
		if counter == 1:
			# print(r)
			# print(l)
			# print(last_element)
			counter-=1
		l-=1
		if(last_element[1] != '"DEFAULT"'):
			for et in expression_tokens:
				if et[0] == last_element[1]:
					token_string = ''
					for literal in lits_stack:
						token_string+=literal
					tokens.append((et, token_string))
					return tokens
		else:
			while((len(stack)!=0) and (last_element[1] == '"DEFAULT"')):
				last_element = stack.pop()
				lits_stack.pop()
				l-=1
			if len(stack) == 0:
				for et in expression_tokens:
					if et[0] == last_element[1]:
						failed_token.append((et, inp))
						return failed_token
			else:
				for et in expression_tokens:
					if et[0] == last_element[1]:
						token_string = ''
						for literal in lits_stack:
							token_string+=literal
						tokens.append((et, token_string))
						stack = []
						lits_stack = []
						for se in state_expressions:
							if se[0] == initial_state:
								stack.append(se)
						l+=1
						r = l
						# print(r)
						# print(l)







if __name__ == '__main__':
    parser = argparse.ArgumentParser(add_help=True, description='Sample Commandline')

    parser.add_argument('--dfa-file', action="store", help="path of file to take as input to construct DFA", nargs="?", metavar="dfa_file")
    parser.add_argument('--input-file', action="store", help="path of file to take as input to test strings in on DFA", nargs="?", metavar="input_file")
    
    args = parser.parse_args()

    print(args.dfa_file)
    print(args.input_file)

    with open(args.dfa_file) as f:
    	states = f.readline().replace('\n', '').split(', ')
    	alphabet = f.readline().replace('\n', '').split(', ')
    	initial_state = f.readline().replace('\n', '')
    	final_states = f.readline().replace('\n', '').split(', ')


    	trans = f.readline().replace('\n', '').replace('(', '').split('), ')    
    	last_transition = trans[-1].replace(')', '')

    	trans[-1] = last_transition
    	transitions = []

    	for transition in trans:
    		# print(transition)

    		trans_list = transition.split(', ')
    		trans_tuple = tuple(trans_list)
    		transitions.append(trans_tuple)


    	state_expression = f.readline().replace('\n', '').replace('(', '').split('), ')   
    	last_state_expression = state_expression[-1].replace(')', '')

    	state_expression[-1] = last_state_expression
    	state_expressions = []

    	# print(state_expression) 

    	for se in state_expression:
    		# print(transition)

    		se_list = se.split(', ')
    		se_tuple = tuple(se_list)
    		state_expressions.append(se_tuple)	

    	expression_token = f.readline().replace('\n', '').replace('(', '').split('), ')    
    	last_expression_token = expression_token[-1].replace(')', '')

    	expression_token[-1] = last_expression_token
    	expression_tokens = []

    	for et in expression_token:
    		# print(transition)

    		et_list = et.split(', ')
    		et_tuple = tuple(et_list)
    		expression_tokens.append(et_tuple)	

    	# print(final_states)

    	with open(args.input_file) as file:
    		inp = file.readline()
    		stack = []

    		dead_se = ''


    		for se in state_expressions:
    			if se[0] == initial_state:
    				stack.append(se)
    			if se[0] == 'DEAD':
    				dead_se = se	

    		# print(stack)	

    		result = fallback(inp, transitions, stack, state_expressions, expression_tokens, final_states)
    		# print(result)

    		with open('task_3_1_result.txt', 'w') as f:
    			for res in result:
    				f.write(res[1]+', '+res[0][1])
    				f.write('\n')


    		
    		



							




						






    						





    				


