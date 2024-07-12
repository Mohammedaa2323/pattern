def gre(fn):
    def wrapper(user):
        data= "hello ! " + fn(user)
        return data
    return wrapper

@gre
def mor_gre(user):
    return f"good morning {user}"
@gre
def afn_gre(user):
    return f"good afternoon {user}"
@gre
def eve_gre(user):
    return f"good evening {user}"


print(mor_gre("mohammed"))
print(afn_gre("prashanth"))
print(eve_gre("jishnu"))

 

def hello_hai(fn):
    def wrapper():
        return "<b> " +fn()+ " <b>"
    return wrapper

@hello_hai
def get_hello():
    return "hello"

@hello_hai
def get_hai():
    return "hai"

print(get_hello())
print(get_hai())