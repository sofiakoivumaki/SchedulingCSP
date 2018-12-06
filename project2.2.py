from aima3 import csp

class Problem(csp.CSP):

    def __init__(self, fh):
        # set variables, domains, graph, and constraint_function accordingly
        self.file = fh
        lines = []
        # Values for variables and domains
        T = []; R = []; S = []; W = []; A = []
        ip = []

        # Student and course dictionary; Key=Course and Value=list of students participating
        student_dict = {}
        for i in range(0, len(A)):
            student_dict.setdefault(A[i][1], []).append(A[i][0])


        for line in self.file:
            lines.append(line)

        for i in lines:
            ip = i.split("␣")
            if ip[0] == 'T': #if T
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
                        t_tuple[0] = 5
                    T.append(tuple(t_tuple))

            elif(ip[0] == 'R'):	#if R
                # Remove first R
                for i in ip[1:]:
                    R.append((i))

            elif(ip[0] == 'S'):	#if S
                #  Remove first S
                for i in ip[1:]:
                    S.append((i))

            elif(ip[0] == 'W'): #if W
                # Change values to tuples of three ","
                for i in ip[1:]:
                    w_tuple = i.split(',')
                    w_tuple[2] = int(w_tuple[2]) #changing from strign to int so that it is easier to compare
                    W.append(tuple(w_tuple))

            elif(ip[0] == 'A'):	#if A
                # change values to tuples of two
                for i in ip[1:]:
                    a_tuple = tuple(i.split(','))
                    A.append((a_tuple))


        # Set variables
        vars = W

        # Set the domain list which is all the possible combinations of T x R [{day, time, place}, Doimains = [{day, time, place}, {day, time, place}, ...]
        domain_list = []
        for i in range(0, len(T)):
            for j in range(0, len(R)):
                domain_list.append(T[i]+R[j])

        # Set the domain for each variable
        domains = {}
        for i in range (0,len(W)):
            domains[W[i]] = domain_list

        # Set neighbors
        neighbors = {}

        for i in range(0,len(vars)):
            neighbors[vars[i]] = vars

        # Sketch the constraints

        def const1(A,a,B,b):		#Class cant happen at the same time same day same place ({A,B} = variables, {a,b} = domains)
            if (a[0] == b[0]):						      #if same day
                if (a[0] == b[0] and a[1] == b[1]):	    #if same time and same room
                    return False
                else:
                    return True
            else:
                return True


        def const2(A,a,B,b):		#Class cant have two (or more) theoretical or practical lessons within one day

            if(A[0] == B[0]):				#if same subject
                if(A[1] == B[1]):			#if same type of class
                    if(a[0] == b[0]):	 	#if same day
                        return False
                    else:
                        return True
                else:
                    return True
            else:
                return True

        def const3(A,a,B,b):		#Two classes cant have the same student type at the same time
            if(a[0] == b[0]):				                #if same day
                if(a[1] == b[1]): 		                    #if same time
                    for i in student_dict[B[0]]:            # Go through the students in this course
                        for j in student_dict[A[0]]:        # Go through the students in this course
                           if(i == j):		                #if same student types overlaps in these courses
                                return False
                        
                else:
                    return True
            else:
                return True

        def const4(A,a,B,b):		#Class type (TH or PR) can appear only certain amounts a week in increasing order
            if(A[0] == B[0]):	      				         #if same subject
                if(A[1] == B[1]):               	       #if same class type
                    if(A[2] < B[2] and a[0] < b[0]):        #if class number is increasing and if days are also increasing
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False


        super().__init__(vars, domains, neighbors, constraints_function)

def dump_solution(self, fh):
    pass

def solve(input_file):
    p = Problem(input_file)
    ans = csp.backtracking_search(self,p)    # Place here your code that calls function csp.backtracking_search(self, ...
    print(ans)

def main():
    input_file = open("input.txt")
    solve(input_file)

if __name__ == "__main__":
    main()

# Place here your code that calls function csp.backtracking_search(self, ...)
    p.dump_solution(output_file)


    #		variables   	A list of variables; each is atomic (e.g. int or string).

    #       domains     	A dict of {var:[possible_value, ...]} entries.

    #       neighbors   	A dict of {var:[var,...]} that for each variable lists
    #                   	the other variables that participate in constraints.

    #       constraints 	A function f(A, a, B, b) that returns true if neighbors

     #						A, B satisfy the constraint when they have values A=a, B=b

