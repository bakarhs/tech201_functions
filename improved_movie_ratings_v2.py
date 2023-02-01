# Movie Ratings V2
#
# def movie_rating(age):
#     user_prompt = True
#     while user_prompt:
#         age = input("What is your age?")
#         if age.isdigit() and int(age) < 117 and int(age) > 0:
#             print(movie_rating(age))
#             break
#         elif int(age) < 12:
#             return ('U and PG films are available')
#         elif int(age) < 15:
#             return ('U, PG and 12 films are available')
#         elif int(age) < 18:
#             return ("U, PG, 12 and 15 films are available")
#         elif int(age) >=18 and int(age) < 117:
#             return ('all films are available')
#         else:
#             return ("Please enter your answer in digits and bellow 117. If your child is under 1 yrs old we advise we do not advise bringing them into the movie.")
#
# movie_rating(age)


# def movie_rating(age):
#     if int(age) < 12:
#         return ('U and PG films are available')
#     elif int(age) < 15:
#         return ('U, PG and 12 films are available')
#     elif int(age) < 18:
#         return("U, PG, 12 and 15 films are available")
#     else:
#         return ('All films are available')
# user_prompt = True
#
# while user_prompt:
#     age = (input("What is your age?"))
#     if age.isdigit() and int(age) < 117 and int(age) > 0:
#         print(movie_rating(age))
#         break
#     else:
#         print("Please enter your answer in digits and bellow 117. If your child is under 1 yrs old we advise we do not advise bringing them into the movie.")
#
# movie_rating(age)

def movie_rating(age):
    if age < 12:
        return ('U and PG films are available')
    elif age < 15:
        return ('U, PG and 12 films are available')
    elif age < 18:
        return("U, PG, 12 and 15 films are available")
    elif age >= 18 and age < 117:
        return ('All films are available')
    else:
        return("Please enter your answer in digits and bellow 117. If your child is under 1 yrs old we advise we do not advise bringing them into the movie.")
age = int(input("What is your age:"))
movie_rating(age)
