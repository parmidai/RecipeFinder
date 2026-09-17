# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 18:27:25 2026

@author: parmi

"""
favorites_food=[]
import requests

while True:
    print("*****************")
    menu=int(input("1.search meal by name\n2.show a random meals\n3.show my favorite\n4.exit\n"))
    print("*****************")

    if menu==1:
        food_name=input("enter your food name: ")
        
        params={
                "s":food_name
                }

        response=requests.get("https://www.themealdb.com/api/json/v1/1/search.php?", params=params)
        data=response.json()
        
        if data["meals"] is None:
            print("food not found")
            
        else:
            for i in range(len(data["meals"])):
                print(i+1, "-", data["meals"][i]["strMeal"])
            choice=int(input("wich food do you like to learn?"))
            meal=data["meals"][choice -1]
                        
                           
            #mavad_avalie_va_meghdar:
            print("Ingredient: ")
            for i in range(1,21):
                Ingredient=meal[f"strIngredient{i}"]
                Measure=meal[f"strMeasure{i}"]
                if Ingredient:
                    print(Ingredient + " " + Measure )
        
            #dastor_pokht:
            print("Instructions:")
            print(meal["strInstructions"])
            favorite=input("do you want to add thid meal to favorite foods?(y/n)")
            if favorite=="y":
                favorites_food.append(meal["strMeal"])
                print("successfully added")

    elif menu==2:
        response=requests.get("https://www.themealdb.com/api/json/v1/1/random.php")
        data=response.json()
        print(data["meals"][0]["strMeal"]+ ":")
        print("Ingredient: ")
        for i in range(1,21):
            Ingredient=data["meals"][0][f"strIngredient{i}"]
            Measure=data["meals"][0][f"strMeasure{i}"]
            if Ingredient:
                print(Ingredient + " " + Measure )
        print("Instructions:")
        print(data["meals"][0]["strInstructions"])
        favorite=input("do you want to add thid meal to favorite foods?(y/n)")
        if favorite=="y":
            favorites_food.append(data["meals"][0]["strMeal"])
    elif menu==3:
        print("favorite foods menu:")
        print(" ")
        for food in favorites_food:
            print(food)
    elif menu==4:
        break
        
        