#group102
#working on homeworks:
#task1
#Clock shows h hours, m minutes and s seconds after midnight.
#Your task is to write a function which returns the time 
#since midnight in milliseconds.
# test.assert_equals(past(0,1,1),61000)
# test.assert_equals(past(1,1,1),3661000)
#test.assert_equals(past(0,0,0),0)
def past(h, m, s):
    return (h*3600 + m*60 + s)*1000