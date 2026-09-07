
import sys

print("==============================")
print("      حاسبة الميزانية  ")
print("      Budget Calculator  ")
print("==============================")


print("------------------------------")
print("==>    Choose your language    <==")
print("==>    اختر لغتك    <==")

language = input (":English - 2 اختار اللغة: 1 - عربي \n")

print("------------------------------")

if language == "1" :
    print("    اهلاً بيك ")
elif language == "2" :
    print("    welcome ")
else :
    print("اختيار غير صحيح")


print("==============================")
print("      القائمة الرئيسية")
print("      Main Menu")
print("==============================")

sum_expenses = 0
while True :
    if language == "1" :
        print("حساب الميزانية - 1 ")
        print("عرض النتيجة - 2 ")
        print("خروج - 3 ")

    else :
        print("1 - Budget Calculate")
        print("2 -  Show Result")
        print("3 - Exit")


    choice = input("اختار رقماً من القائمة /     Choose a number from the menu:\n")
    if choice == "1" :
        if language == "1" :
            print("تم اختيار حساب الميزانية")
        else:
            print(" Budget calulation selected")
        try :
            if language == "1" :
                amount = int(input(":اكتب المبلغ اللي معاك"))
                print(amount)
            else :
                amount = int(input("Enter the amount you have: "))
                print(amount)
        except :
            if language == "1" :
                print("الإدخال غير صحيح")
            else :
                print("Invalid input ")
        try :
            if language == "1" :
                food = int(input("اكتب مصاريف الاكل:"))
                print(food)
            else :
                food = int(input("Enter food expenses"))
                print(food)
        except :
            if language == "1" :
                print("الإدخال غير صحيح")
            else :
                print("Invalid input ")
        try :
            if language == "1" :
                transport = int(input("اكتب مصاريف المواصلات:"))
                print(transport)
            else :
                transport = int(input("Enter transportation expenses :"))
                print(transport)
        except :
            if language == "1" :
                print("الإدخال غير صحيح")
            else :
                print("Invalid input")
        try :
            if language == "1" :
                other = int(input("اكتب مصاريف اخرى:"))
                print(other)
            else :
                other = int(input("Enter other expenses"))
                print(other)
        except :
            if language == "1" :
                print("الإدخال غير صحيح")
            else :
                print("Invalid input")
        total = food + transport + other 
        sum_expenses = total
        remaining = amount - total
        print(remaining)
        if language == "1" :
            print("إجمالي المصاريف:" , sum_expenses )
            print("المبلغ المتبقي:" , remaining)
        else :
            print("Total expenses : " , sum_expenses )
            print("Remaining amount : " , remaining)                                                                      

        while True :
            if language == "1" :
                expense = int(input("اكتب قيمة المصروف:"))
            else :
                expense = int(input("Enter the expense : "))
            if expense > remaining :
                if language == "1" :
                    print("المصروف اكبر من المبلغ المتبقي")
                else :
                    print("The expense is greater than the remaining amount ")
                continue
            sum_expenses = sum_expenses + expense
            remaining = amount - sum_expenses
            if language == "1" :
                print("المبلغ المتبقي:" , remaining)
            else :
                print("Remaining amount :" , remaining)


            if remaining <= 0 :
                if language == "1" :
                    print("تم صرف المبلغ بالكامل")
                else :
                    print("The amount has been fully spent")
                break

                if language == "1" :
                    print("إجمالي المصاريف:" , sum_expenses) 
                else :
                    print("Total expenses: " , sum_expenses)


    elif choice == "2" :
        if language == "1" :
            print("تم اختيار عرض النتيجة")
        else :
            print("Show result selected ")
        if sum_expenses > 0 :
            if language == "1" :
                print("المبلغ الاصلي:" , amount)
                print("مصاريف الاكل :" , food)
                print("مصاريف المواصلات :" , transport)
                print("مصاريف اخرى :" , other)
                print("إجمالي المصاريف:" , sum_expenses )
                print("المبلغ المتبقي:" , remaining)
            else :
                print("Original amount:" , amount)
                print("Food expenses :" , food)
                print("Transportation :" , transport)
                print("Other expenses :" , other)
                print("Total expenses:" , sum_expenses )
                print("Remaining amount:" , remaining)
        else :
            if language == "1" :
                print("يرجى حساب المصاريف اولاً")
            else :
                print("Please calculate the expenses first")

    elif choice == "3" :
        if language == "1" :
            print("شكراً لاستخدامك البرنامج . وداعاً")
        else :
            print(" Thank you for using the program Goodbye!")
        sys.exit()
        
    else :
        if language == "1" :
            print("اختيار غير صحيح، يرجى إعادة المحاولة مرة اخرى.")
        else :
            print(" Invalid choice. Please try again.")






if remaining < 0 :
    if language == "1" :
        print("إن المصاريف اكبر من المبلغ المتاح") 
    else :
        print("Expenses are greater than the available amount ")

else :
    if language == "1" :
        print("المبلغ كافي ")
    else :
        print("The amount is enough")


