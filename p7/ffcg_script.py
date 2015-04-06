
"""
Keishla D. Ortiz Lopez
CSCE 625 - Artificial Intelligence

P7 - Propositional Satisfiability Solver (DPLL)

Script to generate the file of clauses for the Farmer-Fox-Chicken-Grain problem

usage: python ffcg_script.py
output to file named: ffcg.txt
"""

def generateFile():
    timestamp = list(xrange(8))
    objects = ["Fa","Fx","Ch","Gr"]

    data = open("ffcg.txt","w")
    data.write("# Clauses to solve the Farmer-Fox-Chicken-Grain problem\n")
    data.write("# init\n")
    for obj in objects:
        data.write("T0_"+obj+"L\n")

    data.write("\n# goal\n")
    for obj in objects:
        data.write("T7_"+obj+"R\n")

    data.write("\n# the location of objects are time-dependent\n")
    #Ti_objL v Ti_objR
    #-Ti_objL v -Ti_objR
    for obj in objects:
        for t in timestamp:
            data.write("T"+str(t)+"_"+obj+"L T"+str(t)+"_"+obj+"R\n")
            data.write("-T"+str(t)+"_"+obj+"L -T"+str(t)+"_"+obj+"R\n")

    data.write("\n #eating constraints\n")
    #ex: Ti_ChL -> -Ti_GrL v -Ti_FaR
    #    Ti_ChL -> -Ti_FxL v -Ti_FaR
    for t in timestamp:
        data.write("-T"+str(t)+"_ChL"+" -T"+str(t)+"_GrL -T"+str(t)+"_FaR\n")
        data.write("-T"+str(t)+"_ChR"+" -T"+str(t)+"_GrR -T"+str(t)+"_FaL\n")
        data.write("-T"+str(t)+"_ChL"+" -T"+str(t)+"_FxL -T"+str(t)+"_FaR\n")
        data.write("-T"+str(t)+"_ChR"+" -T"+str(t)+"_FxR -T"+str(t)+"_FaL\n")

    data.write("\n# only one action should be executed at each step\n")
    #one action should be executed at each step
    #ex: Ti_mv_obj1_LR -> -Ti_mv_obj1_RL ^ -Ti_mv_obj2_LR ^ -Ti_mv_obj2_RL ^ ... ^ -Ti_mv_objn_LR ^ -Ti_mv_objn_RL
    for obj in objects: 
        for t in xrange(len(timestamp)-1): #0 to 6
            lit1_1 = "-T"+str(t)+"_mv_"+obj+"_LR"
            lit1_2 = "-T"+str(t)+"_mv_"+obj+"_RL"
            for obj2 in objects:
                if obj2 == obj:
                    data.write(lit1_1+" "+lit1_2+"\n")
                    continue
                data.write(lit1_1+" -T"+str(t)+"_mv_"+obj2+"_LR\n")
                data.write(lit1_1+" -T"+str(t)+"_mv_"+obj2+"_RL\n")
                data.write(lit1_2+" -T"+str(t)+"_mv_"+obj2+"_LR\n")
                data.write(lit1_2+" -T"+str(t)+"_mv_"+obj2+"_RL\n")
    data.write("\n")
    #ex: Ti_mv_obj1_LR v Ti_mv_obj1_RL v ... v Ti_mv_objn_LR v Ti_mv_objn_RL 
    for t in xrange(len(timestamp)-1):
        for i in xrange(len(objects)):
            data.write("T"+str(t)+"_mv_"+objects[i]+"_LR ")
            data.write("T"+str(t)+"_mv_"+objects[i]+"_RL ")

        data.write("\n")

    data.write("\n # Preconditions and effects of each action \n")

    # Ti_mv_obj_RL <-> Ti_objR ^ Ti_FaR ^ T(i+1)_objL ^ T(i+1)_FaL (obj != Fa)
    # Ti_mv_Fa_RL -> Ti_FaR ^ T(i+1)_FaL (the farm can move by himself) (similarly with LR)
    for i in xrange(len(objects)):
        for t in xrange(len(timestamp)-1): #0 to 6
            lit1_1 = "T"+str(t)+"_mv_"+objects[i]+"_LR"
            lit1_2 = "T"+str(t)+"_mv_"+objects[i]+"_RL"
            clause1 = lit1_1 +" -T"+str(t)+"_FaL -T"+str(t+1)+"_FaR"
            clause2 = lit1_2 +" -T"+str(t)+"_FaR -T"+str(t+1)+"_FaL"
            data.write("-"+lit1_1+" T"+str(t)+"_FaL\n")
            data.write("-"+lit1_1+" T"+str(t+1)+"_FaR\n")
            data.write("-"+lit1_2+" T"+str(t)+"_FaR\n")
            data.write("-"+lit1_2+" T"+str(t+1)+"_FaL\n")
            
            if objects[i] != "Fa":
                clause1 += " -T"+str(t)+"_"+objects[i]+"L -T"+str(t+1)+"_"+objects[i]+"R"
                clause2 += " -T"+str(t)+"_"+objects[i]+"R -T"+str(t+1)+"_"+objects[i]+"L"
                data.write(clause1+"\n")
                data.write(clause2+"\n")

                data.write("-"+lit1_1+" T"+str(t)+"_"+objects[i]+"L\n")
                data.write("-"+lit1_1+" T"+str(t+1)+"_"+objects[i]+"R\n")
                data.write("-"+lit1_2+" T"+str(t)+"_"+objects[i]+"R\n")
                data.write("-"+lit1_2+" T"+str(t+1)+"_"+objects[i]+"L\n")

    data.write("\n#Early actions\n")
    #ex: Tj_GrR -> Ti_mv_Gr_LR v T(i-1)_mv_Gr_LR v ... v T0_mv_Gr_LR, where j > i
    for i in xrange(1,len(objects)):
        for t in xrange(1,len(timestamp)):
            data.write("-T"+str(t)+"_"+objects[i]+"R")
            for j in xrange(t):
                data.write(" T"+str(j)+"_mv_"+objects[i]+"_LR")
            data.write("\n")

    data.close()


generateFile()