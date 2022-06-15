import os
import glob

EXE_FILE = glob.glob(os.path.dirname(os.path.abspath(__file__))+'\\'+'*.exe')[0]
IN_FILE = glob.glob(os.path.dirname(os.path.abspath(__file__))+'\\'+'*.in')

test_out_arr = IN_FILE = glob.glob(os.path.dirname(os.path.abspath(__file__))+'\\'+'*.out')
my_out_arr = []

for file in IN_FILE:
    input_file = file
    output_file = os.path.splitext(file)[0]+"_my.out"
    
    os.system(f"{EXE_FILE} < {input_file} > {output_file}")
    my_out_arr.append(output_file)


# file open
result = open(result.txt, 'w')

for out in my_out_arr:
    if out.replace("_my", "") in test_out_arr:        
        myfile = open(out, 'r',encoding='utf-8')
        output = open(out.replace("_my", ""), 'r',encoding='utf-8')

        result.write(out.replace("_my", "") + "\t\t" + out)
        result.write("==================================\n")

        line_num = 0
        wrong_cnt = 0

        while True:
            line_num += 1
            my_line = myfile.readline().replace('\n','')
            out_line = output.readline().replace('\n','')

            if (not my_line) or (not out_line):
                if not my_line and not out_line:
                    print(f"[!] {out.replace('_my', '')}:Success")
                    break

                if not my_line:
                    print(f"[!] {out.replace('_my', '')}:End My Output")
                else :
                    print(f"[!] {out.replace('_my', '')}:End Sample Output")

                break

            if my_line != out_line:
                result.write(f"[!{wrong_cnt:^6}] line{line_num}:{my_line}\t\t{out_line}\n")
                wrong_cnt += 1
            else:
                continue

            
        myfile.close()
        output.close()

        result.write('\n')
    
    else:
        print(f"[!] No Have {out.replace('_my', '')}")

result.close()
