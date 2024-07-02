student_data={
    "ram":{"roll_no":10,"age":20,"cource":"python"},
    "mohan":{"roll_no":20,"age":22,"course":"java"}
}
print(student_data)


student_data={
    "ram":{"roll_no":10,"age":20,"cource":"python"},
    "mohan":{"roll_no":20,"age":22,"course":"java"}
}
print(student_data["mohan"])
print(student_data["mohan"]["roll_no"])
student_data["mohan"]["phon_no"]=938480332
print(student_data["mohan"])
