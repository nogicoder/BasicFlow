import sys


def primer():
   num = int(input())
   prims = [2]
   check_num = 3
   if num < 2:
       print(0)
   while check_num <= num:
       found_primer = True
       for i in prims:
           if check_num % i == 0:
               check_num += 2
               found_primer = False
               break
           if found_primer is True:
           prims.append(check_num)
           check_num += 2
       print("Let's print the prime numbers up to? ", num)
   for a in prims:
       print(a)


def primer_alternative():
   num = int(input())
   prims = [2,3]
   check = prims[-1]
   while prims[-1] < num:
       found_primer = True
       check += 2
       itera = 0
       item = prims[itera]
       while item < check/2:
           if check % item == 0:
               found_primer = False
               break
           itera += 1
           item = prims[itera]
           if found_primer is False:
           continue
       prims.append(check)
   print("Let's print the prime numbers up to? ", num)
   for a in prims:
       print(a)


def main(args):
   if "1" in args:
       primer()
   else:
       print("args: ", args)
       primer_alternative()
   if __name__ == "__main__":
       main(sys.argv[1:])
