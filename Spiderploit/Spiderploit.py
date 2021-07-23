if __name__ == "__main__":
    try:
        import requests
        import json
        import colorama
        import cfonts
        import time
    except:
        from json import loads
        from colorama.ansi import Fore
        from colorama.initialise import init
        from cfonts import (cli , render)

    REQ = [
        f"{colorama.ansi.Fore.WHITE}",
        f"{colorama.ansi.Fore.MAGENTA}",
        f"{colorama.ansi.Fore.GREEN}",
        f"{colorama.ansi.Fore.CYAN}",
        f"{colorama.ansi.Fore.RED}"
    ]

    def Headers():
        LOGO = """
                :=+=.          :=+=.               
            :*@%=                =@@+:            
      .=  -%@@+                    +@@#-  =.      
     +%..#@@@:                      :@@@#..%+     
   .%@::@@@@.                        :@@@@::@%.   
  .@@+ %@@@*                          *@@@@ =@@:  
 .@@@. .#@@@#:                      :#@@@#.  @@@. 
 *@@@+:  :#@@@%=.   +.       =   .=%@@@#:  :+@@@# 
 -#@@@@@*=.:#@@@@%+-%++#+=#+=%=+%@@@@#:.-*@@@@@%- 
   .-*%@@@@@##@@@@@@@@@@@@@@@@@@@@@@##@@@@@%*=.   
       .-+#@@@@@@@@@@@@@@@@@@@@@@@@@@@@%+-.       
 -**########@@@@@@@@@@@@@@@@@@@@@@@@@@######****- 
 :@@@@%##***@@@@@@@@@@@@@@@@@@@@@@@@@@***#%%@@@@- 
  @@@:  :+#@@@@#=#@@@@@@@@@@@@@@#=#@@@@#=:  :@@@  
  =@@=+@@@@@*-   %@@@@@@@@@@@@@@#   -*@@@@@+-@@=  
   *@%-@@@#      %@@@@@@@@@@@@@@#     .#@@@-#@#   
    *@-+@@@.     *@@@@@@@@@@@@@@*     .%@@+-@#    
     =@.+@@%.    :@@@@@@@@@@@@@@:    .%@@+.@+     
      .*::%@@-    *@@@@@@@@@@@@*    -@@%::*:      
        :  =%@#.   #@@@@@@@@@@*   .#@@=  :        
             -#@*.  -%@@@@@@%-  .*@#-             
                -++-. -*%%*: .-++-        
        """
        print(f"{REQ[3]}{LOGO}")
        time.sleep(1.5)
        spiderSploit = cfonts.render("Spiderploit" , colors = ["blue" , "cyan" , "bright_blue"] , font = "chrome" , align = "left")
        print(spiderSploit)

    Headers()

    def MainScript():
        Y = time.strftime("%Y/%m/%d")
        C = time.strftime("%H:%M:%S")
        API = requests.get("https://api.myip.com").content
        J = json.loads(API)
        PI = J["ip"]
        CT = J["country"]
        INPUT = str(input(f"{REQ[2]}[{REQ[1]}+{REQ[2]}] {REQ[3]}({REQ[4]}$piderpl0it{REQ[3]})-{REQ[3]}[{REQ[4]}~{REQ[3]}]{REQ[4]}--${REQ[0]} "))
        with open("list.txt" , "r") as LIST:
            for ELEMENT in LIST:
                Protocol = requests.get(f"https://{INPUT}{ELEMENT}")
                if Protocol.status_code == 200:
                    print(f"{REQ[3]}[{Y}][{C}] : [{PI}][{CT}]{REQ[0]} :: {REQ[2]}{ELEMENT} \t")
                    with open(r"{}".format("log/log.txt") , "a") as LOG:
                        LOG.write(f"{ELEMENT} is available in {INPUT}")
                        LOG.close()
                elif Protocol.status_code != 200:
                    print(f"{REQ[3]}[{Y}][{C}] : [{PI}][{CT}]{REQ[0]} :: {REQ[4]}{ELEMENT} \t")
                    with open(r"{}".format("log/log.txt") , "a") as LOG:
                        LOG.write(f"{ELEMENT} is not available in {INPUT}")
                        LOG.close()
    MainScript()