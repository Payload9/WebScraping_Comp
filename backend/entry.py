class CompanyEntry():
    """Creates a class containing company details."""
    def __init__(self, CompanyName:str, Industry:str, Revenue:int, RevenueGrowth:float, Employees:int):
        self.COMPANY_NAME = CompanyName
        self.INDUSTRY = Industry
        self.REVENUE = Revenue
        self.REVENUE_GROWTH = RevenueGrowth
        self.EMPLOYEE_COUNT = Employees
    
    def returnCompanyName(self):
        return self.COMPANY_NAME
    
    def returnRevenue(self):
        return self.REVENUE
    
    def returnRevenueGrowth(self):
        return self.REVENUE_GROWTH
    
    def returnEmployeeCount(self):
        return self.EMPLOYEE_COUNT
    
    def __str__(self):
        return self.COMPANY_NAME