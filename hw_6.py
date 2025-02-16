regions = {"ภาคเหนือ":[],
          "ภาคกลาง" : [],
          "ภาคอีสาน" :[],
          "ภาคตะวันตก": [],
          "ภาคตะวันออก": [],
          "ภาคใต้": []}

def display_menu():
    print("\n---------Main menu---------")
    print("1.Insert Data")
    print("2.Update Data")
    print("3.Search Data")
    print("4.Delete Data")
    print("5.View All Data")
    print("6.Exit ")
    print("---------------------------")


def insert_data():
    region = input("กรุณาเลือกภาค (ภาคเหนือ, ภาคกลาง, ภาคอีสาน, ภาคใต้,ภาคตะวันตก,ภาคตะวันออก): ")
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
    province_edit = input("กรุณาใส่จังหวัดที่ต้องการแก้ไข: ")
    for region in regions:
        if province_edit in regions[region]:
            province_new = input("กรุณาใส่ชื่อจังหวัดใหม่: ")
            regions[region].remove(province_edit)
            regions[region].append(province_new)
            print(f"{province_edit} ถูกแก้ไขเป็น {province_new} ใน {region} เรียบร้อยแล้ว")
            return
    print("ไม่พบข้อมูลที่ต้องการแก้ไข")

def serch_data():
    region = input("กรุณาใส่ภาคของท่าน: ")
    if region in regions and len(regions[region]) > 0:
        print(regions[region])
    else:
        print("ไม่พบข้อมูล")

def delete_data():
    province = input("กรุณาใส่จังหวัดที่ต้องการลบ: ")
    for region in regions:
        if province in regions[region]:
            regions[region].remove(province)
            print(f"{province} ถูกลบออกจาก {region} เรียบร้อยแล้ว")
            return
    print("ไม่พบข้อมูลที่ต้องการลบ")

def View_alldata():
    print("\n--- ข้อมูลจังหวัดทั้งหมด ---")
    for region, provinces in regions.items():
        print(f"{region}: {', '.join(provinces) if provinces else 'ไม่มีข้อมูล'}")

def mainmenu():
    while True:
        display_menu()
        choice_input = str(input("Enter your choice : "))
        if choice_input == "1":
            insert_data()
        elif choice_input == "2":
            update_data()
        elif choice_input == "3":
            serch_data()
        elif choice_input == "4":
            delete_data()
        elif choice_input == "5":
            View_alldata()
        elif choice_input == "6":
            print("Exit Program!")
            break
        else:
            print("กรุณาเลือก Choice ใหม่")


if __name__ == "__main__":
    mainmenu()