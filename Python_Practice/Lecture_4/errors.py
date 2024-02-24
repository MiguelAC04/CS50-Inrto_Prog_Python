def main():
    import sys
    try:
        try:
            f = open('myfile.txt')
            s = f.readline()
            # i = int(s.strip())
            raise Exception('Nono Paila')
        except OSError as err:
            print("OS error:", err)
        except ValueError:
            print("Could not convert data to an integer.")
        except Exception as err:
            print(f"Unexpected {err=}, {type(err)=}")
            raise err
    except Exception as err:
        print("Final Error:", err)
    
    
    try:
        nums = input('n>> ').split(',')
        print(*(nums := list(map(int, nums))))
        nums[2] = int(nums[2])**2
    except ValueError as err:
        error = err
    except IndexError as err:
        error = err
    else:
        print("Terminated")
        exit(0)
    print(error)
    
    try:
        n=int(input("n>> "))
    except ValueError:
        print("Enter some number")
    else:
        print("B")
    
    class A_Error(Exception):pass
    
    def custom_Error():    
        try:
            n=int(input('n3>> '))
            if not n: raise A_Error
            else:     return n
        except ValueError as err:
            return err
        finally:
            print("'finally' clause executed", end=': ')
            return "A_Error bypassed"
    print(custom_Error())
    
    try:        
        try:
            raise ExceptionGroup(
                "Group 1",
            [
                    OSError(1),
                    ValueError(2),
                    ExceptionGroup("Group 2",
                [
                        RecursionError(3),
                        A_Error()
                ])])
        except* OSError as os_Err:
            print("\n\tOSError")
        except* RecursionError as rs_Err:
            print("\n\tRecusion Error")
    except Exception as group_Excs:
        excs = ()
        group_Excs.derive(excs)
        group_Excs.add_note("\n\t**Note for the highest Exception**\n")
        raise
        
main()