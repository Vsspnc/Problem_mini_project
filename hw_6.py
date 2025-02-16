regions = {"ภาคเหนือ":[],
          "ภาคกลาง" : [],
          "ภาคอีสาน" :[],
          "ภาคใต้": []}

def display_menu():
    print("\n---------Main menu---------")
    print("1.Insert Data")
    print("2.Update Data")
    print("3.Search Data")
    print("4.Delete Data")
    print("5.View All Data")
    print("---------------------------")


def insert_data():
    region = input("กรุณาเลือกภาค (ภาคเหนือ, ภาคกลาง, ภาคอีสาน, ภาคใต้): ")
    if region in regions:
        province = input("กรุณาใส่ชื่อจังหวัดที่ต้องการเพิ่ม: ")
        if province not in regions[region]:
            regions[region].append(province)
            print(f"เพิ่มจังหวัด {province} ใน {region} เรียบร้อยแล้ว")
        else:
            print(f"จังหวัด {province} มีอยู่ใน {region} แล้ว")
    else:
        print("ไม่มีภาคนี้ในระบบ")

def update_data():
    pass

def serch_data():
    pass

def delete_data():
    pass

def View_alldat():
    print(regions())

def mainmenu():
    display_menu()
    choice_input = int(input("Enter your choice : "))
    if choice_input == 1:
        display_menu()
    elif choice_input == 2:
        update_data()
        