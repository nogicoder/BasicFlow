def students_ranker(s):
    return sorted(s,key=lambda k:(k['subject']['math'],k['subject']['physic'],k['subject']['history']))
