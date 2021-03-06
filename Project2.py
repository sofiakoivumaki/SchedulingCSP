import csp

class Problem(csp.CSP):

    def __init__(self, fh):
        # Place here your code to load problem from opened file object fh and
        # set variables, domains, graph, and constraint_function accordingly
        self.file = fh
        lines = []
        # Values for variables and domains
        T = []; R = []; S = []; W = []; A = []
        ip = []


        for line in file:
        	lines.append(line)

        for i in lines:
        	ip = i.split()
        	if ip[0] = 'T': #if T
        		# Change values to tuples of two "," and remove first letter
        		for i in ip[1:]:	#skip the first letter
        			t_tuple = i.split(',')
        			if(t_tuple[0] == 'Mon'):	# Changing from String to int so that it is easier to compare
						t_tuple[0] = 1
					elif(t_tuple[0] == 'Tue'):
						t_tuple[0] = 2
					elif(t_tuple[0] == 'Wed'):
						t_tuple[0] = 3
					elif(t_tuple[0] == 'Thu'):
						t_tuple[0] = 4
					elif(t_tuple[0] == 'Fri'):
						w_tuple[0] = 5
        			T.append(t_tuple)

        	elif(ip[0] = 'R'):	#if R
        		# Remove first R
        		for i in ip[1:]:
        			R.append(i)

        	elif(ip[0] = 'S'):	#if S
        		# Remove first S
        		for i in ip[1:]:
        			S.append(i)

        	elif(ip[0] = 'W'): #if W
        		# Change values to tuples of three ","
        		for i in ip[1:]:
        			w_tuple = i.split(',')
        			w_tuple[2] = int(w_tuple[2]) #changing from strign to int so that it is easier to compare
        			W.append(w_tuple)

        	elif(ip[0] = 'A'):	#if A 
        		# change values to tuples of two
        		for i in ip[1:]:
        			a_tuple = i.split(',')
        			A.append(a_tuple)

        # Set variables

        var = {};
        for i in len(W):
        	 var['C%s' % i] = []		# creates variable list of [C1, C2, C3, C4, C5.... C(amount of classes)]

       	# Set neighbors
       	###

        # Set domains (time[d,t], room[], weekly_classes[c,k,i], associations[s,c], )
        #Remember to put dict!!!
        domain = []
        domain.append(T)
        domain.append(R)
        domain.append(W)
        domain.append(A)
			
        # Sketch the constraints

        def const1(A,a,B,b):		#Class cant happen at the same time same day same place ({A,B} = variables, {a,b} = domains)
        	if (a[0][0] == b[0][0]):						#if same day
        		if (a[0][1] == b[0][1] && a[1] == b[1]):	#if same time and same room
        			return False
        		else:
        			return True
        	else:
        		return True

        
        def const2(A,a,B,b):		#Class cant have two (or more) theoretical or practical lessons within one day
	       
        	if(a[0][0] == b[0][0]):				#if same day
        		if(a[2][0] == b[2][0])			#if same subject
	        		if(a[2][1] == b[2][1]):	 	#if same class type
	        			return False
	        		else:
	        			return True
	        	else:
	        		return True
	        else:
	        	return True

	    def const3(A,a,B,b):		#Two classes cant have the same student type at the same time 
			if(a[0][0] == b[0][0]):				#if same day
				if(a[0][1] == b[0][1]): 		#if same time
					if(a[3][1] == b[3][1]):		#if same student type
						return False
					else:
						return True
				else:
					return True		
			else:
				return True

		def const4(A,a,B,b):		#Subject has to be the same everywhere in the class ###!!! Can A and B be the same var???
			if(A == B):  								#if both are same var
				if(a[2][0] == a[3][1]):					#if A (and B) is using only one kind of subject
					return True
				else:
					return False
			else: 
				return False 

		def const5(A,a,B,b):		#Class type (TH or PR) can appear only certain amounts a week in increasing order
			if(a[2][0] == b[2][0]):									#if same subject
				if(a[2][1] == b[2][1]):								#if same class type
					if(a[2][2] < b[2][2] && a[0][0] < b[0][0]):		#if class number is increasing and if days are also increasing
						return True:
					else:
						return False:
				else:
					return False:
			else:
				return False:


        super().__init__(variables, domains, graph, constraints_function)
        
    def dump_solution(self, fh):
        # Place here your code to write solution to opened file object fh
        
def solve(input_file, output_file):
    p = Problem(input_file)



    # Place here your code that calls function csp.backtracking_search(self, ...)
    p.dump_solution(output_file)


#		variables   	A list of variables; each is atomic (e.g. int or string).

#       domains     	A dict of {var:[possible_value, ...]} entries.

#       neighbors   	A dict of {var:[var,...]} that for each variable lists
#                   	the other variables that participate in constraints.

#       constraints 	A function f(A, a, B, b) that returns true if neighbors
#						A, B satisfy the constraint when they have values A=a, B=b