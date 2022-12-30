import ast  
regularexpression = ast.parse("print('a+b+c(d+e)')")  
print(regularexpression)  
print(ast.dump(regularexpression))
exec(compile(regularexpression, filename="", mode="exec"))

