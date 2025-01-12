#Enter Building Dimensions
width=float(input("Enter room width (meters):"))
length=float(input("Enter room length (meters):"))
ceiling_height=float(input("Enter ceiling height (meters):"))

#Calculate Areas
Perimeter = 2*(width+length)
floor_area = width*length 
print("01. floor area:",floor_area)
Wall_Area=Perimeter*ceiling_height
print("wall area:",Wall_Area)

#Select desired floor assembly and associated unit cost
floor_assembly_type=input("02. Enter material assembly (e.g., tile, stone, lvt):")
if "tile":
      floor_material_unit_cost=float(10)
elif "stone":
      floor_material_unit_cost=float(15)
elif "lvt":
       floor_material_unit_cost=float(14)
else: input ("Material type not available in data set.")

#Select desired wall assembly and associated unit cost
wall_assembly_type=input("Enter material assembly (e.g., brick, stone, lumber, steel):")
if "brick":
      wall_material_unit_cost=float(10)
elif "stone":
      wall_material_unit_cost=float(15)
elif "lumber":
      wall_material_unit_cost=float(14)
elif "steel":
      wall_material_unit_cost=float(16.5)
else: input ("Material type not available in data set.")


estimated_floor_cost=floor_area*float(floor_material_unit_cost)
estimated_wall_cost=Wall_Area*float(wall_material_unit_cost)
estimated_material_cost=Wall_Area*float(wall_material_unit_cost)+floor_area*float(floor_material_unit_cost)

print("03.Material Cost",(estimated_material_cost))

#EXTRA: Estimate Labor, Overhead & Profit and Tax
labor=estimated_material_cost*.7
print("labor",(labor))
tax=.3*estimated_material_cost
print("tax",(tax))
OnP=.2*(estimated_material_cost+labor)
print("Overhead and Profit",(OnP))
Total_Cost = estimated_material_cost + labor+tax+ OnP
print ("TOTAL COST",Total_Cost)

#Save
save_to_csv=input ("Do you want to save this project?:")
if "yes":
      def save_to_csv(projects, file_name="building material cost estimator.csv"):
            with open(file_name, 'w') as file:
                  write = csv.write(file)
                  write.writerow(["width","length","ceiling height","wall type","floor type"])
                  for project in projects:
                        w.writerow(project)
                        print(f"projects saved to {file_name}")
else: input ("Invalid response. Please enter yes or quit")




