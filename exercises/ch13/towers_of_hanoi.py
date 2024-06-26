#!/usr/bin/env python3
'''
Exercise Summary
:d is the decimal format type
:s is the [UNIDENTIFIED] format type
values must be set to a specified format type when using the .format method | ex.. n={:d}
the values must be passed in to the right of the .format method | ex.. .format(n, etc)
'''
def move_disk(n, src, dest, temp):
    print("move_disk(n={:d}, src={:s}, dest={:s}, temp={:s})".format(n, src, dest, temp)
    ) 

    if n == 0:
        return
    else:
        move_disk(n-1, src, temp, dest)
        print("Move disk", n, "from", src, "to", dest)
        move_disk(n-1, temp, dest, src)
        
def main():
    print("**** TOWERS OF HANOI ****")
    print()
    num_disks = int(input("Enter number of disks: "))
    print()
    
    move_disk(num_disks, "A", "C", "B")

    print()
    print("All disks have been moved.")

if __name__ == "__main__":
    main()
