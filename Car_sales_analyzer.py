import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
try:
    try:
        FILE = "cars-sales_excel_file_2.xlsx"
        sales = pd.read_excel(FILE)
        car = pd.read_excel(FILE,sheet_name="cars")
        dealer = pd.read_excel(FILE,sheet_name="dealers")
        sales["Revenue"] = sales['Unit_sold']*sales["Sale_Price"]
    except:
        print("Somthing Wrong while loading file.")
    def all_cars():
        print("===== All Listed Cars ======")
        for i,j in enumerate(car["Model"].unique().tolist()):
            print(f"{i+1}.{car.loc[car['Model']==str(j),"Brand"].iloc[0]} {j}")
    def safe_input(out,types):
        while True:
            try:
                take =  types(input(out))
                break
            except:
                print("")
        return take
        
        
    def amount_writer(amount):

        if amount >= 10000000:
            return f"{round(amount / 10000000, 2)} Cr."

        elif amount >= 100000:
            return f"{round(amount / 100000, 2)} Lakh"

        elif amount >= 1000:
            return f"{round(amount / 1000, 2)} K"

        else:
            return amount
    def most_sales_car():
        print("====== MOST SALES =======")
        most =sales.groupby(sales["Model"])["Unit_sold"].sum().sort_values(ascending=False)
        brand = car.loc[car["Model"]==most.idxmax(),"Brand"].iloc[0]
        print(f"Top sales : {brand} {most.idxmax()}"
            f"\n Units sales : {most.max()}")
        print("====== TOP 10 CARS ======")
        print(f"{most.head(10)}")
    

    def most_revenue():
        most_money = sales.groupby(["Model"])["Revenue"].sum().sort_values(ascending=False)
        brand = car.loc[car["Model"]==most_money.idxmax() , "Brand"].iloc[0]
        print( f"MOSt Revenue Car : {brand } { most_money.idxmax()}")
        print(f"Revenue : {amount_writer(most_money.max())}")

    # def pie_chart():
    #    chart = sales.groupby(["Model"])["Unit_sold"].sum().sort_values(ascending=False)
    #    print(chart)
    #    plt.pie(chart.values.astype(int).tolist(), labels=chart.index.astype(str).tolist(), autopct="%.1f%%")
    #    plt.show()


    # 🚘 Car Features
    # Brand
    # Model
    # Segment
    # Fuel_Type
    # Transmission
    # Engine_CC
    # Color

    def profit_margin():
    
        sell = sales["Unit_sold"]*sales["Sale_Price"]
        profit = sell - sales["Unit_sold"]* sales["Base_Price"]
        profit = profit.sum()
        print(f"Total Revenue : {amount_writer(sales['Revenue'].sum())}")
        print(f"Total Profit : {amount_writer(profit)}")


    def price_category():
        while True :
            print("==== Price Car Finder =====")
            try:
                price = int(input("Enter price : "))
                print("0.Back")
                if price == 0:
                    break
                cars = sales[sales["Base_Price"]>=price]
                print(f"Total cars : {len(cars)}")
                top_10=cars["Model"].unique().tolist()
                print("cars name : - ")
                print(*top_10,end=",")
            except:
                print("invalid input")
            
            


    def time_wise_category():
        while True:
            print(f"===== Time Caluator ===== ")
            while True:
                try:
                    choose = int(input((f"1.check year\n2.check month\n3.custom\n4.Back\nEnter : ")))
                    break
                except:
                    print("invalid input")
            if choose ==1 :

                try:
                    year = int(input("enter year : "))
                except:
                    print("INVAILD INPUT!!  ")
                gotten = sales[sales["Date"].dt.year==year]
                print(f'Total cars sales : {len(gotten)}')
                most = gotten.groupby(["Model"])["Unit_sold"].sum().sort_values(ascending=False)
                brand = sales.loc[sales["Model"]==most.idxmax(),"Brand"].iloc[0]

                print(f"Top sales : {brand} {most.idxmax()}")
            elif choose ==2:
                month = int(input("enter month in number : "))
                check = sales[sales["Date"].dt.month==month]
                Total_cars = len(check)
                most= check.groupby(check["Model"])["Unit_sold"].value_counts()
                brand = sales.loc[sales["Model"]==most.idxmax(),"Brand"].iloc[0]
                print(f"Total cars sales : {Total_cars}")
                print(f"Most sale car : {brand} {most.idxmax()}")
                print(f"{most.idxmax()}'s sales : {most.max()}")
            elif choose ==3:
                date1 = str(input("Enter first date : "))
                date2 = str(input("Enter last date : "))
                check = sales[(sales["Date"].dt.date >= pd.to_datetime(date1,dayfirst=True).date()) 
                            & 
                            (sales["Date"].dt.date <= pd.to_datetime(date2,dayfirst=True).date())]
                if check.empty :
                    print("No cars sale in this time")
                else :
                    print(f"Total sales : {len(check)}")
                    most = check.groupby(["Model"])["Unit_sold"].sum().sort_values(ascending=False)
                    brand = check.loc[check["Model"]==most.idxmax(),"Brand"].iloc[0]
                    print(f"Maximum sale : {brand} {most.idxmax()}")
                    print(f"        Unit : {most.max()}")
            elif choose ==4:
                break
            else:
                print("Invalid choice!!")

    def customer_slection():
        while True:
            print(f"1.Age-wise\n2.Gender\n3.Rating\n4.Back")
            choice = int(input("Enter your choice : "))
            if choice==1:
                age1 = int(input("Enter minimum age : "))
                age2 = int(input("Enter maximum age : "))
                customer = sales[(sales["Custmor_age"] >= age1) & (sales["Custmor_age"]<=age2)]
                print(f"=================")
                print(f"Total custmor : {len(customer)}")
                print(f"Most sale car : {customer.groupby(customer["Model"])["Model"].value_counts().idxmax()}")
                print(f"Total Unit_sold : {customer["Unit_sold"].sum()}")
            elif choice == 2:
                print(" Choose Gender : \n1.Male\n2.Female")
                gender = input("Enter : ").strip()
                if gender in ("1","Male" ,"male"):
                    custmor = sales[sales["Custmor_Gender"] == "Male"]
                    print("============================")
                    print(f" Total custmor : {len(custmor)}")
                    print(f" Total Units_sold : {custmor["Unit_sold"].sum()}")
                    print("=================================")
                elif gender in ("2" , "Female" , "female"):
                    custmor = sales[sales["Custmor_Gender"] == "Female"]
                    print("==========================")
                    print(f" Total custmor : {len(custmor)}")
                    print(f" Top sale model : {custmor.groupby(custmor["Model"])["Model"].value_counts().idxmax()}")
                    print(f" Total Units_sold : {custmor["Unit_sold"].sum()}")
                    print("==========================")
            elif choice==3:
                    while True:
                        try:
                            rt1 = float(input("Minimum rating : "))
                            rt2 = float(input("Maximum rating : "))
                            if rt1 >= 0 and rt2 <=5:
                                break
                            else:
                                print("Enter rating between 0 to 5 ")
                        except:
                            print("Invalid Input!!")
                        
                    ratings = sales[(sales["Rating"]>=rt1) & (sales["Rating"] <=rt2)]
                    print(f" Total sales : {len(ratings)}")
                    print(f"Top rated cars :\n {list(ratings.loc[ratings.groupby(ratings["Model"])["Rating"].idxmax(),"Model"])}")
            elif choice == 4:
                break
            else:
                print("Invalid choice!!")
                
    def find_top_region_dealer(region):
        region = str(region).strip().title()
        dealer_north = dealer.loc[dealer['Region']==region,'Dealer_ID'].tolist()
        top_north = sales[sales["Dealer_ID"].isin(dealer_north)].groupby("Dealer_ID")["Revenue"].sum().sort_values(ascending=False)
        print(f"Top Dealer : {dealer.loc[dealer['Dealer_ID']==top_north.idxmax(),'Dealer_Name'].iloc[0]}")
        print(f"Revenue : {amount_writer(top_north.max())}")
    def find_city_info(city):
        city = str(city).title().strip()
        cities = dealer["cities"].unique().tolist()
        if city not in cities :
            print(f"No Dealer In {city} exist!")
        else :
            city_dealer = dealer.loc[dealer["cities"]== city,"Dealer_ID"].tolist()
            city_revenue = sales[sales["Dealer_ID"].isin(city_dealer)].groupby(["Dealer_ID"])["Revenue"].sum().sort_values(ascending=False)
            print(f"Top Dealer : {dealer.loc[dealer["Dealer_ID"]==city_revenue.idxmax(),"Dealer_Name"].iloc[0]}")
            print(f"Revenue : {amount_writer(city_revenue.max())}")
    def find_dealer_model_info(model):
        all_model = car["Model"].unique().tolist()
        if model not in all_model:
            print(f"Unable to find {model}!!")
        else:
            model = str(model)
            dealer_model_sales = sales[sales["Model"]==model].groupby(sales["Dealer_ID"])["Unit_sold"].sum()
            print(f"-- Brand : {car.loc[car['Model']==model,"Brand"].iloc[0]}, Model : {model}")
            print(f"Total Sales : {sales[sales["Model"]==model]["Unit_sold"].sum()}")
            print(f"Top Sales : {dealer.loc[dealer["Dealer_ID"]==dealer_model_sales.idxmax(),"Dealer_Name"].iloc[0]}")
            print(f"Units sold : {dealer_model_sales.max()}")

    def all_dealer_info(store):
        store = str(store)
        all_store = dealer["Dealer_Name"].unique().tolist()
        if store not in all_store:
            print("Dealer not found !")
        else:
            dealer_id = dealer.loc[dealer["Dealer_Name"]==store,"Dealer_ID"].iloc[0]
            storing = sales[sales["Dealer_ID"]==dealer_id]
            dealer_revenue = storing["Revenue"].sum()
            dealer_unit_sold = storing["Unit_sold"].sum()
            city,state,region = dealer.loc[dealer["Dealer_ID"]==dealer_id,["cities","States","Region"]].iloc[0]
            top_sales_model = sales[sales["Dealer_ID"]==dealer_id].groupby(sales["Model"])["Unit_sold"].sum()
            dealer_profit = (storing["Revenue"] - storing["Base_Price"] * storing["Unit_sold"]).sum()
            print(f"================== {dealer_id} ===================")
            print(f"Dealer location : | City : {city} | State : {state} | Region : {region} |")
            print(f"Dealer ID : {dealer_id},\nDealer Name : {store}")
            print(f"Total Revenue : {amount_writer(dealer_revenue)}")
            print(f"Total Profit : {amount_writer(dealer_profit)}")
            print(f"Total Units Sold : {dealer_unit_sold}")
            print(f"Top Sales Model_Name  : {car.loc[car["Model"]==str(top_sales_model.idxmax()),"Brand"].iloc[0]} {top_sales_model.idxmax()}")
        
    def dealer_information():
        while True:
            print("========= Dealer's Window ========")
            print("1.Most Sales\n2.Region\n3.City/State\n4.Car\n5.Dealer Info\n6.Back")
            choice = int(input("Enter : "))
            if choice == 1:
                dealer_unit_sold = sales.groupby(sales["Dealer_ID"])["Unit_sold"].sum().sort_values(ascending=False)
                Unit_sold = dealer_unit_sold.values[0]
                big_name = dealer.loc[dealer["Dealer_ID"] == dealer_unit_sold.idxmax(),"Dealer_Name"].iloc[0]
                ################################
                that_name = dealer_unit_sold.index[1]
                big_name2 = dealer.loc[dealer["Dealer_ID"] ==that_name,"Dealer_Name"]
                Unit_sold2 = dealer_unit_sold.values[1]
                print(f"1st . Dealer Name : {big_name}")
                print(f"Total Unit Sold : {Unit_sold}")
                print(f"2nd . Dealer Name : {big_name2}")
                print(f"Total Unit Sold : {Unit_sold2}")
            elif choice == 2:
                print(f"1.East\n2.West\n3.North\n4.South\nEnter : ")
                region = input().strip().lower()
                deal_id = sales.groupby(sales["Dealer_ID"])["Revenue"].sum().sort_values(ascending=False)
                if region in ("1","east"):
                    find_top_region_dealer("East")
                    
                elif region in ('2','west'):
                    find_top_region_dealer("West")
                    
                elif region in ("3","north"):
                    find_top_region_dealer("North")
                    
                elif region in ('4','south'):
                    find_top_region_dealer("South")
                else :
                    print(f"Invalid Region!")
            elif choice == 3 :
                cities = dealer['cities'].unique().tolist()
                for i,j in zip(cities,list(range(1,len(cities)+1))):
                    print(f"{j}.{i}")
                print(f"====== Cities ====== ")
                city = input("Enter city name or sr.no : ")
                if city.isdigit() and 1 <= int(city) <= len(cities):
                    city = int(city)
                    city = cities[city-1]
                    find_city_info(city)
                elif city.isalpha():
                    find_city_info(city)
                else:
                    print("Invalid sr.no!!!")
            elif choice == 4 :
                all_model = car["Model"].unique().tolist()
                for i,j in zip(all_model,list(range(1,len(all_model)+1))):
                    print(f"{j}.{car.loc[car['Model']==str(i),"Brand"].iloc[0]} {i}")
                model = input("Enter (Car's name or Sr.no) : ")
                if model.isdigit():
                    model = int(model)
                    model = all_model[model-1]
                    find_dealer_model_info(model)
                elif model.isalpha():
                    model = model.upper()    
                    find_dealer_model_info(model)
            elif choice ==5 :
                all_dealer = dealer["Dealer_Name"].unique().tolist()
                all_dealer_id = dealer["Dealer_ID"].unique().tolist()
                for i,j,k in zip(all_dealer,list(range(1,len(all_dealer)+1)),all_dealer_id):
                    print(f"{j}.{k} - {i}")
                distibutor = input("Enter (Sr.no or Dealer_ID or Dealer_Name) : ")
                if distibutor.isdigit():
                    distibutor =  int(distibutor)
                    distibutor = all_dealer[distibutor-1]
                    all_dealer_info(distibutor)
                elif distibutor.isalpha:
                    all_dealer_info(distibutor)
                else:
                    print("Invalid choice!!")
            elif choice == 6:
                break
            else:
                print("Invalid choice")

    def multi_analyise():
        while True :
            print("================= Multi - Analyise ==================")
            print("1.Seller_Rank\n2.Brand_Sales_Rank\n3.Dealer_Rank\n4.Model_Rank\n5.Back")
            choice = int(input("Enter : "))
            if choice == 1:
                tops = int(input("Top : "))
                seller_rank = sales.groupby([sales["Sales_Person"]])["Unit_sold"].sum().sort_values(ascending=False).head(tops)
                for i,(j,k) in enumerate(zip(seller_rank.index.tolist(),seller_rank.values.tolist())):
                    print(f"=======\n RANK : {i+1} ========\nSeller_Name : {j}\nCars_Sell : {k}\n") 
            elif choice == 2:
                tops = int(input("Top : "))
                brand_rank = sales.groupby(sales["Brand"])['Unit_sold'].sum().sort_values(ascending=False).head(tops)
                for i,(j,k) in enumerate(zip(brand_rank.index.tolist(),brand_rank.values.tolist())):
                    print(f"====== RANK : {i+1} ======\nBrand : {j}\nCar Saled : {k}\n")
            elif choice == 3:
                tops = int(input("Top : "))
                dealer_rank = sales.groupby(sales["Dealer_ID"])['Unit_sold'].sum().sort_values(ascending=False).head(tops)
                for i,(j,k) in enumerate(zip(dealer_rank.index.tolist(),dealer_rank.values.tolist())):
                    print(f"====== RANK : {i+1} ======\nDealer_Name : {dealer.loc[dealer["Dealer_ID"]==str(j),"Dealer_Name"].iloc[0]}\nCar Saled : {k}\n")
            elif choice == 4:
                tops = int(input("Top : "))
                model_rank = sales.groupby(sales["Model"])['Unit_sold'].sum().sort_values(ascending=False).head(tops)
                for i,(j,k) in enumerate(zip(model_rank.index.tolist(),model_rank.values.tolist())):
                    print(f"====== RANK : {i+1} ======\nModel_Name : {car.loc[car["Model"]==str(j),"Brand"].iloc[0]} {j}\nCar Sales : {k}\n")
            elif choice == 5:
                break
            else:
                print("Invalid Choice!!")
                
    def pie_chart_for_payment_method():
        payment_method = sales.groupby(sales["Payment_method"])["Payment_method"].count().sort_values(ascending=False)
        plt.pie(payment_method.values.astype(int).tolist(),labels=payment_method.index.astype(str).tolist(),autopct="%.2f%%")   
        plt.show()
            
    while True:

        print("""
    ========================================================
                    🚗 CAR SALES ANALYZER
    ========================================================

    1.  Show All Cars
    2.  Most Sales Car
    3.  Most Revenue Car
    4.  Price Category
    5.  Time-wise Analysis
    6.  Customer Selection

    7.  Dealer Information
    8.  Find Top Region Dealer
    9.  Find City Information
    10. Find Dealer Model Information
    11. All Dealer Information

    12. Multiple Analysis / Rankings
    13. Payment Method Chart

    14. Profit

    0.  Exit
    ========================================================
    """)

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            all_cars()

        elif choice == "2":
            most_sales_car()

        elif choice == "3":
            most_revenue()

        elif choice == "4":
            price_category()

        elif choice == "5":
            time_wise_category()

        elif choice == "6":
            customer_slection()

        elif choice == "7":
            dealer_information()

        elif choice == "8":
            region = input("Enter Region: ")
            find_top_region_dealer(region)

        elif choice == "9":
            city = input("Enter City: ")
            find_city_info(city)

        elif choice == "10":
            model = input("Enter Car Model: ")
            find_dealer_model_info(model)

        elif choice == "11":
            store = input("Enter Dealer Name: ")
            all_dealer_info(store)

        elif choice == "12":
            multi_analyise()

        elif choice == "13":
            pie_chart_for_payment_method()

        elif choice == "14":
            profit_margin()

        elif choice == "0":
            print("Thank you for using Car Sales Analyzer!")
            break

        else:
            print("Invalid choice! Please enter a number from 0-14.")
except:
    print("Something Went Wrong!!")