# This is for the intermediate challenge for the Intermediate Python Web Scraping challenge. Seperated into some different files because this code isn't supposed to be Super Mario's favorite food.

# (c) Payload9 2022 | plz don't steal thanks
try:
    from bs4 import BeautifulSoup
    import requests
    from backend import entry
    from backend import sort
    import colorama
    from colorama import Fore
    from PyInquirer import prompt, Separator
    import os
except ImportError:
    print("Missing modules detected! Did you run `ModuleInstaller.py` before running this?")
    exit()

colorama.init(autoreset=True)
os.system('cls')


def main():
    # print("Setting URL...")
    url = "https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue"

    # print("Retreiving content...")
    req = requests.get(url)
    chickenNoodle = BeautifulSoup(req.text, "html.parser")

    # print("Finding all elements with the tag 'tr'...")
    results = chickenNoodle.find_all('tr')

    # print("Creating unset varibles...")
    Company1 = None
    Company2 = None
    Company3 = None
    Company4 = None
    Company5 = None
    Company6 = None
    Company7 = None
    Company8 = None
    Company9 = None
    Company10 = None

    for result in results:
        try:
            
            tds = result.find_all("td")
            # tds[1] -> Company Name
            # tds[2] -> Company Industry
            # tds[3] -> Compnay Revenue
            # tds[4] -> Comapny Revenue Growth
            # tds[5] -> Number of Employees
            
            CompanyName = str(tds[1].text).strip()
            CompanyIndustry = str(tds[2].text).strip()
            CompanyRevenueTemp = str(tds[3].text).strip()
            CompanyRevenue = int(CompanyRevenueTemp.replace(",", ''))
            CompanyRevenueGrowthTemp = str(tds[4].text).strip()
            CompanyRevenueGrowth = float(CompanyRevenueGrowthTemp.replace("%", ''))
            CompanyEmployeeCountTemp = str(tds[5].text).strip()
            CompanyEmployeeCount = int(CompanyEmployeeCountTemp.replace(",", ''))
            
            if Company1 == None:
                Company1 = entry.CompanyEntry(CompanyName, CompanyIndustry, CompanyRevenue, CompanyRevenueGrowth, CompanyEmployeeCount)
            
            elif Company2 == None:
                Company2 = entry.CompanyEntry(CompanyName, CompanyIndustry, CompanyRevenue, CompanyRevenueGrowth, CompanyEmployeeCount)
            
            elif Company3 == None:
                Company3 = entry.CompanyEntry(CompanyName, CompanyIndustry, CompanyRevenue, CompanyRevenueGrowth, CompanyEmployeeCount)
            
            elif Company4 == None:
                Company4 = entry.CompanyEntry(CompanyName, CompanyIndustry, CompanyRevenue, CompanyRevenueGrowth, CompanyEmployeeCount)
            
            elif Company5 == None:
                Company5 = entry.CompanyEntry(CompanyName, CompanyIndustry, CompanyRevenue, CompanyRevenueGrowth, CompanyEmployeeCount)
            
            elif Company6 == None:
                Company6 = entry.CompanyEntry(CompanyName, CompanyIndustry, CompanyRevenue, CompanyRevenueGrowth, CompanyEmployeeCount)
            
            elif Company7 == None:
                Company7 = entry.CompanyEntry(CompanyName, CompanyIndustry, CompanyRevenue, CompanyRevenueGrowth, CompanyEmployeeCount)
            
            elif Company8 == None:
                Company8 = entry.CompanyEntry(CompanyName, CompanyIndustry, CompanyRevenue, CompanyRevenueGrowth, CompanyEmployeeCount)
            
            elif Company9 == None:
                Company9 = entry.CompanyEntry(CompanyName, CompanyIndustry, CompanyRevenue, CompanyRevenueGrowth, CompanyEmployeeCount)
            
            elif Company10 == None:
                Company10 = entry.CompanyEntry(CompanyName, CompanyIndustry, CompanyRevenue, CompanyRevenueGrowth, CompanyEmployeeCount)
            
            else:
                # print("All slots filled, stopping.")
                break
        
        except IndexError:
            # print("Ignoring index error.")
            continue
        except Exception as e:
            # print(f"Something else went wrong: {e}")
            input()
            
    print(f"{Fore.GREEN}Successfully retreived information from Wikipedia!")

    mainMenu = [
        {
            'type': 'list',
            'name': 'menuOption',
            'message': 'Select a way to view the data.',
            'choices': [
                'By Name',
                'By Revenue',
                'By Revenue Growth',
                'By Number of Employees',
                'Randomly',
                Separator(),
                {
                    'name': 'Exit',
                }
            ]
        }
    ]

    userResponse = prompt(mainMenu)
    selection = userResponse.get("menuOption")

    if selection == 'By Name':
        sort.by_name(Company1, Company2, Company3, Company4, Company5, Company6, Company7, Company8, Company9, Company10)
        input("\n Press any key to return to the main menu. . .")
        os.system('cls')
        main()
    if selection == 'By Revenue':
        sort.by_revenue(Company1, Company2, Company3, Company4, Company5, Company6, Company7, Company8, Company9, Company10)
        input("\n Press any key to return to the main menu. . .")
        os.system('cls')
        main()
    if selection == 'By Revenue Growth':
        sort.by_revenue_growth(Company1, Company2, Company3, Company4, Company5, Company6, Company7, Company8, Company9, Company10)
        input("\n Press any key to return to the main menu. . .")
        os.system('cls')
        main()
    if selection == 'By Number of Employees':
        sort.by_employee_count(Company1, Company2, Company3, Company4, Company5, Company6, Company7, Company8, Company9, Company10)
        input("\n Press any key to return to the main menu. . .")
        os.system('cls')
        main()
    if selection == 'Randomly':
        sort.randomly(Company1, Company2, Company3, Company4, Company5, Company6, Company7, Company8, Company9, Company10)
        input("\n Press any key to return to the main menu. . .")
        os.system('cls')
        main()
main()