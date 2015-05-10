"""
Keishla D. Ortiz Lopez
CSCE 625 - Artificial Intelligence

P9: Goal regression for planning in the Blocksworld

Script to generate the blocksworld.opers file
"""

def main():
    blocks = ["a","b","c","d"]
    data = open("blocksworld.opers","w")
    data.write("# Operators for planning in the Blocksworld problem\n")
    data.write("# Pickup operator\n")
    for i in xrange(len(blocks)):
        for j in xrange(len(blocks)):
            if i==j:
                continue
            data.write("OPER pickup("+blocks[i]+","+blocks[j]+")\n")
            data.write("precond: clear("+blocks[i]+") on("+blocks[i]+","+blocks[j]+") gripper_empty()\n")
            data.write("addlist: holding("+blocks[i]+") clear("+blocks[j]+")\n")
            data.write("dellist: clear("+blocks[i]+") on("+blocks[i]+","+blocks[j]+") gripper_empty()\n")
            data.write("conflict: on("+blocks[i]+","+blocks[j]+") on("+blocks[j]+","+blocks[i]+") holding("+blocks[j]+") ")

            for k in xrange(len(blocks)):
                if k == i or k == j:
                    continue

                data.write("holding("+blocks[k]+") on("+blocks[k]+","+blocks[i]+") on("+blocks[i]+","+blocks[k]+") ")
            
            data.write("\nEND\n")

    #pickup(blocks[i],table), assume table is always clear!
    for i in xrange(len(blocks)):
        data.write("OPER pickup("+blocks[i]+",table)\n")
        data.write("precond: clear("+blocks[i]+") on("+blocks[i]+",table) gripper_empty()\n")
        data.write("addlist: holding("+blocks[i]+")\n")
        data.write("dellist: clear("+blocks[i]+") on("+blocks[i]+",table) gripper_empty()\n")
        data.write("conflict: on("+blocks[i]+",table) ")

        for k in xrange(len(blocks)):
            if k == i:
                continue

            data.write("holding("+blocks[k]+") on("+blocks[k]+","+blocks[i]+") on("+blocks[i]+","+blocks[k]+") ")
            
        data.write("\nEND\n")

    data.write("\n")
    data.write("# Puton operator\n")
    for i in xrange(len(blocks)):
        for j in xrange(len(blocks)):
            if i==j:
                continue
            data.write("OPER puton("+blocks[i]+","+blocks[j]+")\n")
            data.write("precond: holding("+blocks[i]+") clear("+blocks[j]+")\n")
            data.write("addlist: clear("+blocks[i]+") on("+blocks[i]+","+blocks[j]+") gripper_empty()\n")
            data.write("dellist: holding("+blocks[i]+") clear("+blocks[j]+")\n")
            data.write("conflict: holding("+blocks[i]+") on("+blocks[j]+","+blocks[i]+") holding("+blocks[j]+") ")

            for k in xrange(len(blocks)):
                if k == i or k == j:
                    continue

                data.write("holding("+blocks[k]+") on("+blocks[k]+","+blocks[i]+") on("+blocks[i]+","+blocks[k]+") on("+blocks[k]+","+blocks[j]+") ")
            
            data.write("\nEND\n")

    #puton(blocks[i],table), assume table is always clear!
    for i in xrange(len(blocks)):
        data.write("OPER puton("+blocks[i]+",table)\n")
        data.write("precond: holding("+blocks[i]+")\n")
        data.write("addlist: clear("+blocks[i]+") on("+blocks[i]+",table) gripper_empty()\n")
        data.write("dellist: holding("+blocks[i]+")\n")
        data.write("conflict: holding("+blocks[i]+") ")

        for k in xrange(len(blocks)):
            if k == i:
                continue

            data.write("holding("+blocks[k]+") on("+blocks[k]+","+blocks[i]+") on("+blocks[i]+","+blocks[k]+") ")
            
        data.write("\nEND\n")

    data.close()

if __name__ == '__main__':
    main()