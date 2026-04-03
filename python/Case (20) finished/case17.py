n = int(input())

if 10 <= n <= 40:
    tens = n // 10
    units = n % 10
    
    if 10 <= n <= 19:
        match n:
            case 10: res = "tenth"
            case 11: res = "eleventh"
            case 12: res = "twelfth"
            case 13: res = "thirteenth"
            case 14: res = "fourteenth"
            case 15: res = "fifteenth"
            case 16: res = "sixteenth"
            case 17: res = "seventeenth"
            case 18: res = "eighteenth"
            case 19: res = "nineteenth"
    else:
        match tens:
            case 2: t_txt = "twenty"
            case 3: t_txt = "thirty"
            case 4: t_txt = "forty"
            
        match units:
            case 0: res = t_txt[:-1] + "ieth"
            case 1: res = t_txt + "-first"
            case 2: res = t_txt + "-second"
            case 3: res = t_txt + "-third"
            case 4: res = t_txt + "-fourth"
            case 5: res = t_txt + "-fifth"
            case 6: res = t_txt + "-sixth"
            case 7: res = t_txt + "-seventh"
            case 8: res = t_txt + "-eighth"
            case 9: res = t_txt + "-ninth"
            
    print(f"the {res} task")