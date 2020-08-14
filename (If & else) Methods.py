is_magician= False
is_expert= True

#check if magician AND expert:"You are a master Magician"

if is_expert and is_magician:
  print('You are a master magician") 

#Check if magician but not expert: "atleast you are getting there"

elif is_magician and not is_expert:

print("at least you are getting there")

#if you are not a magician: "You need magic powers"

elif not is_magician:

print("You need magic powers")
