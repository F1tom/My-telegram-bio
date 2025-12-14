from colorama import init, Fore

init(autoreset=True)

output = f"""{Fore.CYAN}+-----------------------------------+
{Fore.CYAN}|  {Fore.GREEN}$ ./identity --scan --user=Nee4_To      
{Fore.CYAN}|  {Fore.YELLOW}[+]{Fore.WHITE} Querying database...                   
{Fore.CYAN}|  {Fore.GREEN}[+]{Fore.WHITE} USERNAME:     {Fore.CYAN}Nee4_To                   
{Fore.CYAN}|  {Fore.YELLOW}[-]{Fore.WHITE} REAL_NAME:    {Fore.RED}[RESTRICTED]   
{Fore.CYAN}|  {Fore.GREEN}[+]{Fore.WHITE} AGE:          {Fore.CYAN}17            
{Fore.CYAN}|  {Fore.GREEN}[+]{Fore.WHITE} PERSONALITY:  {Fore.CYAN}ENTJ-A        
{Fore.CYAN}|  {Fore.GREEN}[+]{Fore.WHITE} FOCUS:        {Fore.CYAN}SYSTEMS_DEV   
{Fore.CYAN}|  {Fore.RED}[-]{Fore.WHITE} STATUS:       {Fore.RED}NO_SIGNAL    
{Fore.CYAN}|                                  
{Fore.CYAN}|  {Fore.GREEN}$ access_repo --primary          
{Fore.CYAN}|  {Fore.BLUE}[>]{Fore.WHITE} Target: {Fore.CYAN}github.com/F1tom     
{Fore.CYAN}|  {Fore.GREEN}[+]{Fore.WHITE} Connection established       
{Fore.CYAN}+-----------------------------------+"""

print(output)

input("Press Enter to exit...")