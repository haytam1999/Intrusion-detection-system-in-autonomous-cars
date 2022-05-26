import pickle
import random
    
loaded_model = pickle.load(open('knn_model.pkl', 'rb'))


import pyrebase

#Initialize Firebase


firebaseConfig = {
  "apiKey": "AIzaSyCNdV6Jb8M5f50PqtEznvDxCvhkc0fi0fo",
  "authDomain": "pyrebaseproj-7a021.firebaseapp.com",
  "databaseURL": "https://pyrebaseproj-7a021-default-rtdb.europe-west1.firebasedatabase.app",
  "projectId": "pyrebaseproj-7a021",
  "storageBucket": "pyrebaseproj-7a021.appspot.com",
  "messagingSenderId": "307035606917",
  "appId": "1:307035606917:web:e787d2d44c6c85ffc33eec",
  "measurementId": "G-5KDNYSM31E"
}

firebase=pyrebase.initialize_app(firebaseConfig)

db=firebase.database()

# data -9.982113e+06	-1.220211e+06	2.105482e+05	-1.088019e+05	-184533.219920	-4.604241e+04	-2.775633e+04
#expected : 0
# data  = {
#     "feature1": "-9.982113e+06",
#     "feature2": "-1.220211e+06",
#     "feature3":"2.105482e+05",
#     "feature4": "-1.088019e+05",
#     "feature5": "-184533.219920",
#     "feature6": "-4.604241e+04",
#     "feature7": "-2.775633e+04",
# }

# generate random bengin attaks
# data = list()
# for j in range(0,1000):
#     for i in range (0,7):
#         data.append(random.randint(-1e+07, 1e+06))
        
#     db.push(data)
#     print(data)
#     data = list()


str = "-1.002183e+07	-1.021075e+06	202351.587118	-114002.606752	-215573.235295	-58280.359846	-37580.412270".split('\t')
print(str)

#db.push(str)

dictionnary = db.child().get().val()
print(dictionnary)

lst = []
for key in dictionnary:
    for j in dictionnary[key]:
        lst.append(int(float(j)))
    lst = [lst]
    print(lst)
    new_output = loaded_model.predict(lst)
    print(new_output)
    lst = list()


# define input
# new_input = [[-1.002119e+07, -1.078089e+0666e+05, -1.140099e+05, -21,	2.02385559.973975, -5.826997e+04,	-3.756456e+04]]


