# def insert_patient_data(name,age):

#     print(name)
#     print(age)
#     print('inserted into database')

# insert_patient_data('vikas','thirty')    # data as insert in schema but thirty is a str but age in a schema a int so that i schema value is wrong insert.

# # above problem solution is python type hinting use for this problem solution.

# def insert_patient_data(name:str,age:int):

#     print(name)
#     print(age)
#     print('inserted into database')

# insert_patient_data('vikas','30')

# # This is good. But if any programmer age value by mistake
# # 30 is write in quation like '30'. then value print 
# # int like 30 but in schema store as a str value that is 
# # wrong way in the schema.
# # but this problem for solution use pydantic part like 
# # data validation. it is perfect solution that reason
# # if any body define wrong way value that is no problem 
# # that reason data validation automatic solve this problem
# # in database means schema.

# def insert_patient_data(name:str,age:int):

#     if type(name)== str and type(age)==int:
#         print(name)
#         print(age)
#         print('inserted into database')
#     else:
#         raise TypeError('Incorrect data type')

# insert_patient_data('vikas',30)        

from pydantic import BaseModel # type: ignore

class Patient(BaseModel):

    name: str
    age: int

def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print('inserted')
   

patient_info = {'name':'vikas', 'age':22}   

patient1 = Patient(**patient_info)

insert_patient_data(patient1)