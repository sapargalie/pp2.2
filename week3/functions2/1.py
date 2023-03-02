movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]

def higher_score(movie_name): #<-- 1
    return ['True' for movie in movies if movie["name"] == movie_name and movie["imdb"] > 5.5] 

def MoviesGreaterList(movies): #<-- 2
    movies_greater = [movie["name"] for movie in movies if movie["imdb"] > 5.5] 
    return movies_greater 

def CategoryList(category): #<-- 3 
  
    category_list = [movie["name"] for movie in movies if movie["category"] == category]
    return category_list 
    
CategoryList("") #<-- category 

def AvgScore(movies): #<-- 4
    scores = [movie["imdb"] for movie in movies] 
    return (sum(scores)/len(scores)) 

AvgScore(movies)

def avg_imdb_acc_to_cat(movies, cat_name): #<-- 5
    cat_movies = return_movie_category(movies, cat_name)
    avg_score = avg_imdb_score(cat_movies)
    return avg_score

print('Average IMDB of movies in the Thriller category is: ')
s2=avg_imdb_acc_to_cat(movies,'Thriller')
print(s2)