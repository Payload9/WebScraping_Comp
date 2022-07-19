# intended usage example: sort.by_name(Comp1, Comp2, Comp3, Comp4, Comp5, Comp6, Comp7, Comp8, Comp9, Comp10)

from backend.entry import CompanyEntry
from prettytable import PrettyTable
from colorama import Fore
import colorama
from random import shuffle

colorama.init(autoreset=True)


def by_name(Comp1:CompanyEntry, Comp2:CompanyEntry, Comp3:CompanyEntry, Comp4:CompanyEntry, Comp5:CompanyEntry, Comp6:CompanyEntry, Comp7:CompanyEntry, Comp8:CompanyEntry, Comp9:CompanyEntry, Comp10:CompanyEntry):
    
    """Sorts companies in alphabetical order."""
    
    # print("Creating table...")
    table = PrettyTable([f'{Fore.BLUE}▼ Company Name{Fore.RESET}', 'Company Industry', 'Revenue (in millions)', 'Revenue Growth', 'Employee Count'])
    
    # print("Creating lists (step 1/2)...")
    COMPANY_LIST = []
    
    # print("Creating lists (step 2/2)...")
    COMPANY_LIST.extend([Comp1, Comp2, Comp3, Comp4, Comp5, Comp6, Comp7, Comp8, Comp9, Comp10])
    
    # print(COMPANY_LIST)
    
    # print("Sorting lists (step 1/1)...")
    COMPANY_LIST_SORTED = sorted(COMPANY_LIST, key=CompanyEntry.returnCompanyName)
    
    # print(COMPANY_LIST)
    
    # print("Adding results to sorted table...")
    for item in COMPANY_LIST_SORTED:
        table.add_row([item.COMPANY_NAME, item.INDUSTRY, f"${item.REVENUE:,}", str(item.REVENUE_GROWTH) + "%", f"{item.EMPLOYEE_COUNT:,}"])
    
    # print("Printing table...")
    print(table)
    
    return
    
def by_revenue(Comp1:CompanyEntry, Comp2:CompanyEntry, Comp3:CompanyEntry, Comp4:CompanyEntry, Comp5:CompanyEntry, Comp6:CompanyEntry, Comp7:CompanyEntry, Comp8:CompanyEntry, Comp9:CompanyEntry, Comp10:CompanyEntry):
    
    """Sorts companies based on their revenue."""
    
    # print("Creating table...")
    table = PrettyTable(['Company Name', 'Company Industry', f'{Fore.BLUE}▼ Revenue (in millions){Fore.RESET}', 'Revenue Growth', 'Employee Count'])
    
    # print("Creating lists (step 1/2)...")
    COMPANY_LIST = []
    
    # print("Creating lists (step 2/2)...")
    COMPANY_LIST.extend([Comp1, Comp2, Comp3, Comp4, Comp5, Comp6, Comp7, Comp8, Comp9, Comp10])
    
    # print(COMPANY_LIST)
    
    # print("Sorting lists (step 1/1)...")
    COMPANY_LIST_SORTED = sorted(COMPANY_LIST, key=CompanyEntry.returnRevenue, reverse=True)
    
    # print(COMPANY_LIST)
    
    # print("Adding results to sorted table...")
    for item in COMPANY_LIST_SORTED:
        table.add_row([item.COMPANY_NAME, item.INDUSTRY, f"${item.REVENUE:,}", str(item.REVENUE_GROWTH) + "%", f"{item.EMPLOYEE_COUNT:,}"])
    
    # print("Printing table...")
    print(table)
    
    return

def by_revenue_growth(Comp1:CompanyEntry, Comp2:CompanyEntry, Comp3:CompanyEntry, Comp4:CompanyEntry, Comp5:CompanyEntry, Comp6:CompanyEntry, Comp7:CompanyEntry, Comp8:CompanyEntry, Comp9:CompanyEntry, Comp10:CompanyEntry):
    
    """Sorts companies based on their revenue growth percentage."""
    
    # print("Creating table...")
    table = PrettyTable(['Company Name', 'Company Industry', 'Revenue (in millions)', f'{Fore.BLUE}▼ Revenue Growth{Fore.RESET}', 'Employee Count'])
    
    # print("Creating lists (step 1/2)...")
    COMPANY_LIST = []
    
    # print("Creating lists (step 2/2)...")
    COMPANY_LIST.extend([Comp1, Comp2, Comp3, Comp4, Comp5, Comp6, Comp7, Comp8, Comp9, Comp10])
    
    # print(COMPANY_LIST)
    
    # print("Sorting lists (step 1/1)...")
    COMPANY_LIST_SORTED = sorted(COMPANY_LIST, key=CompanyEntry.returnRevenueGrowth, reverse=True)
    
    # print(COMPANY_LIST)
    
    # print("Adding results to sorted table...")
    for item in COMPANY_LIST_SORTED:
        table.add_row([item.COMPANY_NAME, item.INDUSTRY, f"${item.REVENUE:,}", str(item.REVENUE_GROWTH) + "%", f"{item.EMPLOYEE_COUNT:,}"])
    
    # print("Printing table...")
    print(table)
    
    return

def by_employee_count(Comp1:CompanyEntry, Comp2:CompanyEntry, Comp3:CompanyEntry, Comp4:CompanyEntry, Comp5:CompanyEntry, Comp6:CompanyEntry, Comp7:CompanyEntry, Comp8:CompanyEntry, Comp9:CompanyEntry, Comp10:CompanyEntry):
    
    """Sorts companies based on the number of employees they have."""
    
    # print("Creating table...")
    table = PrettyTable(['Company Name', 'Company Industry', 'Revenue (in millions)', 'Revenue Growth', f'{Fore.BLUE}▼ Employee Count{Fore.RESET}'])
    
    # print("Creating lists (step 1/2)...")
    COMPANY_LIST = []
    
    # print("Creating lists (step 2/2)...")
    COMPANY_LIST.extend([Comp1, Comp2, Comp3, Comp4, Comp5, Comp6, Comp7, Comp8, Comp9, Comp10])
    
    # print(COMPANY_LIST)
    
    # print("Sorting lists (step 1/1)...")
    COMPANY_LIST_SORTED = sorted(COMPANY_LIST, key=CompanyEntry.returnEmployeeCount, reverse=True)
    
    # print(COMPANY_LIST)
    
    # print("Adding results to sorted table...")
    for item in COMPANY_LIST_SORTED:
        table.add_row([item.COMPANY_NAME, item.INDUSTRY, f"${item.REVENUE:,}", str(item.REVENUE_GROWTH) + "%", f"{item.EMPLOYEE_COUNT:,}"])
    
    # print("Printing table...")
    print(table)
    
    return

def randomly(Comp1:CompanyEntry, Comp2:CompanyEntry, Comp3:CompanyEntry, Comp4:CompanyEntry, Comp5:CompanyEntry, Comp6:CompanyEntry, Comp7:CompanyEntry, Comp8:CompanyEntry, Comp9:CompanyEntry, Comp10:CompanyEntry):
    
    """Sorts companies randomly."""
    
    # print("Creating table...")
    table = PrettyTable(['Company Name', 'Company Industry', 'Revenue (in millions)', 'Revenue Growth', f'Employee Count'])
    
    # print("Creating lists (step 1/2)...")
    COMPANY_LIST = []
    
    # print("Creating lists (step 2/2)...")
    COMPANY_LIST.extend([Comp1, Comp2, Comp3, Comp4, Comp5, Comp6, Comp7, Comp8, Comp9, Comp10])
    
    # print(COMPANY_LIST)
    
    # print("Sorting lists (step 1/1)...")
    shuffle(COMPANY_LIST)
    
    # print(COMPANY_LIST)
    
    # print("Adding results to sorted table...")
    for item in COMPANY_LIST:
        table.add_row([item.COMPANY_NAME, item.INDUSTRY, f"${item.REVENUE:,}", str(item.REVENUE_GROWTH) + "%", f"{item.EMPLOYEE_COUNT:,}"])
    
    # print("Printing table...")
    print(table)
    
    return