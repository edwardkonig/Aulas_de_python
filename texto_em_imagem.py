# from PIL import Image, ImageDraw, ImageFont, ImageOps
# from random import randint
# import requests, io 
# endpoint_image = "https://picsum.photos/"
# (a,b) = ("800", "600")
# endpoint_image_size = endpoint_image + a  + "/" + b
# response = requests.get(endpoint_image_size)
# image = io.BytesIO(response.content)
# image_open = Image.open(image)
# img_with_border = ImageOps.expand(Image.open(image),border=20,fill='black')
# # image_bytes = Image.frombytes("RGBA",(int (a),int(b)),image_open)
# draw = ImageDraw.Draw(img_with_border)
# endpoint_joke = "https://icanhazdadjoke.com/"
# resposta = requests.get(endpoint_joke, headers = {"Accept": "application/json"})
# if resposta.status_code == 200 and len(resposta.json()) > 0:
#     piada = resposta.json()
#     joke = piada["joke"].upper()
#     pontuacao = [". ",", ","? ", "! ", "- ", "... "]
#     for ponto in pontuacao:
#         if ponto in joke:
#             (frase1, frase2) = joke.split(ponto)
#             font = ImageFont.truetype('Impact', size=20)
#             (x, y) = (200, 100)
#             (s,t) = (200,400)
#             color = 'rgb(265, 265, 265)' 
#             draw.text((x, y), frase1, fill=color, font=font, align = "center")
#             draw.text((s, t), frase2, fill=color, font=font, align = "center")
   



# img_with_border.save('random_image_test.jpeg')

endpoint_twitter = "https://api.twitter.com/2/tweets/"
twitter_id = 1067094924124872705
twitter_parameters = "?expansions=attachments.poll_ids"
twitter_request = endpoint_twitter + str(twitter_id)
response_twitter = requests.get(twitter_request, headers = {"Authorization": "Bearer AAAAAAAAAAAAAAAAAAAAAN55GwEAAAAAs3gW2v0UzkS7XhDf8LGSPlw75%2Bs%3DwjKcyg51J6twC9rtt9dP7StMKfv2NtYZ5T47TBfvUdMCznaAEp"})
if response_twitter.status_code == 200:
    print (response_twitter.json())


'''
https://icanhazdadjoke.com/api
https://picsum.photos
https://haptik.ai/tech/putting-text-on-image-using-python/
'''

'''
'''