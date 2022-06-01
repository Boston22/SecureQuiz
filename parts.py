import os
from flask import Flask, url_for, render_template, request, Markup
from flask import redirect
from flask import session

app = Flask(__name__)

# In order to use "sessions",you need a "secret key".
# This is something random you generate.
# For more info see: https://flask.palletsprojects.com/en/1.1.x/config/#SECRET_KEY

app.secret_key=os.environ["SECRET_KEY"]; #This is an environment variable.
                                     #The value should be set in Heroku (Settings->Config Vars).
                                     #To run locally, set in env.sh and include that file in gitignore so the secret key is not made public.
#l
@app.route('/')
def renderMain():
  return render_template('home.html')

@app.route('/startOver')
def startOver():
    session.clear()
    return redirect(url_for('renderMain')) # url_for('renderMain') could be replaced with '/'

@app.route('/P1')
def renderPage1():
    return render_template('Page1.html')

@app.route('/P2', methods=["POST"])
def renderPage2():
    if "cassette" not in session:

        #8-8
        session["cassette"]=request.form["cassette"] # 1. done
        session["chainRings"]=request.form["chainRings"] # 2.done
        session["chain"]=request.form["chain"] # 3. done
        session["rearShifter"]=request.form["rearShifter"] # 4 done
        session["frontShifter"]=request.form["frontShifter"] #5 done
        session["pedals"]=request.form["pedals"] #6 done
        session["crankArms"]=request.form["crankArms"] #7 done
        session["crankset"]=request.form["crankset"] #8 done

        #7-7
        session["rim"]=request.form["rim"] #9 done
        session["spokes"]=request.form["spokes"] #10 done
        session["spokeNipples"]=request.form["spokeNipples"] #11
        session["hub"]=request.form["hub"] #12
        session["tube"]=request.form["tube"] #13
        session["tire"]=request.form["tire"] #14
        session["valveSystem"]=request.form["valveSystem"] #15

        #2-2
        session["tubed"]=request.form["tubed"] #16
        session["tubeless"]=request.form["tubeless"] #17

        #6-6
        session["20"]=request.form["20"] #18
        session["24"]=request.form["24"] #19
        session["26"]=request.form["26"] #20
        session["27"]=request.form["27"] #21
        session["27.5"]=request.form["27.5"] #22
        session["29"]=request.form["29"] #23

        #2-2
        session["fullSuspension"]=request.form["fullSuspension"] #24
        session["frontSuspention"]=request.form["frontSuspention"] #25

        #16-16
        session["bottomTube"]=request.form["bottomTube"] #26
        session["topTube"]=request.form["topTube"] #27
        session["seatTube"]=request.form["seatTube"] #28
        session["seatPost"]=request.form["seatPost"] #29
        session["stem"]=request.form["stem"] #30
        session["headTube"]=request.form["headTube"] #31
        session["frontDropout"]=request.form["frontDropout"] #32
        session["forkLegs"]=request.form["forkLegs"] #33
        session["seatStays"]=request.form["seatStays"] #34
        session["headset"]=request.form["headset"] #35
        session["housingStop"]=request.form["housingStop"] #36
        session["rearDropout"]=request.form["rearDropout"] #37
        session["forkCrown"]=request.form["forkCrown"] #38
        session["adjustingBarrel"]=request.form["adjustingBarrel"] #39
        session["frontBrakes"]=request.form["frontBrakes"] #40
        session["rearBrakes"]=request.form["rearBrakes"] #41

        #3-3
        session["uBrakes"]=request.form["uBrakes"] #42
        session["rimBrakes"]=request.form["rimBrakes"] #43
        session["discBrakes"]=request.form["discBrakes"] #44
    return render_template('Page2.html')

@app.route('/Q')
def renderequestions():
  return render_template('Questions.html')

@app.route('/Test')
def renderTesting():
  return render_template('Test.html')

@app.route('/Answer', methods=["POST"])
def renderAnswers():
    if "shrader" not in session:
        session["shrader"]=request.form["shrader"] #45
        session["presta"]=request.form["presta"] #46
        session["rotor"]=request.form["rotor"] #47
        session["breakPads"]=request.form["breakPads"] #48
        session["hydrolicDisc"]=request.form["hydrolicDisc"] #49
        session["mechanicalDisc"]=request.form["mechanicalDisc"] #50
        session["c5"]=request.form["c5"] #51
        session["c6"]=request.form["c6"] #52
        session["c7"]=request.form["c7"] #53
        session["c8"]=request.form["c8"] #54
        session["c9"]=request.form["c9"] #55
        session["c10"]=request.form["c10"] #56
        session["c11"]=request.form["c11"] #57
        session["c12"]=request.form["c12"] #58
        session["c13"]=request.form["c13"] #59
    total=0
    incorrect=""
    if session["cassette"]=="rear gears":
        total=total+1
    else:
        incorrect=incorrect+Markup("1. Cassette "+ "<br><b>your answer</b> "+session["cassette"]+"<br> <b>correct answer</b>"+" rear gears<br><br>")

    if session["chainRings"]=="front gear" or session["chainRings"]=="front gears":
        total=total+1
    else:
        incorrect=incorrect+Markup("2. chain-rings "+ "<br><b>your answer</b> "+session["chainRings"]+"<br> <b>correct answer</b>"+" front gear(s)<br><br>")

    if session["chain"]=="connects cassette to chain-rings":
        total=total+1
    else:
        incorrect=incorrect+Markup("3. Chain "+ "<br><b>your answer</b> "+session["chain"]+"<br> <b>correct answer</b>"+" connects the cassette to the chain-rings <br><br>")

    if session["rearShifter"]=="shifts rear gears":
        total=total+1
    else:
        incorrect=incorrect+Markup("4. Rear shifter "+ "<br><b>your answer</b> "+session["rearShifter"]+"<br> <b>correct answer</b>"+" shifts rear gears<br><br>")

    if session["frontShifter"]=="shifts front gears":
        total=total+1
    else:
        incorrect=incorrect+Markup("5. Front shifter "+ "<br><b>your answer</b> "+session["frontShifter"]+"<br> <b>correct answer</b>"+" shifts front gears<br><br>")

    if session["pedals"]=="connected to crank arms":
        total=total+1
    else:
        incorrect=incorrect+Markup("6. Pedals "+ "<br><b>your answer</b> "+session["pedals"]+"<br> <b>correct answer</b>"+" connected to crank arms<br><br>")

    if session["crankArms"]=="connects pedals to bike frame" or session["crankArms"]=="connects the pedals to the crankset":
        total=total+1
    else:
        incorrect=incorrect+Markup("7. Crank arms "+ "<br><b>your answer</b> "+session["crankArms"]+"<br> <b>correct answer</b>"+" connects pedals to bike frame <b>or</b> connects the pedals to the crankset<br><br>")

    if session["crankset"]=="connects to crank arms to the bike frame" or session["crankset"]=="connects to crank arms to the bike frame":
        total=total+1
    else:
        incorrect=incorrect+Markup("8. Crankset "+ "<br><b>your answer</b> "+session["crankset"]+"<br> <b>correct answer</b>"+" connects to crank arms to the bike frame <b>or</b> <br><br>")

    if session["rim"]=="gives the wheel it's shape" or session["rim"]=="keeps the wheels in circular shape" or session["rim"]=="gives the wheels it's shape" or session["rim"]=="keeps the wheels in circular shape":
        total=total+1
    else:
        incorrect=incorrect+Markup("9. Rim "+ "<br><b>your answer</b> "+session["rim"]+"<br> <b>correct answer</b>"+" gives the wheel(s) it's shape <b>or</b> keeps the wheel(s) in circular shape<br><br>")

    if session["spokes"]=="connects hub to rim with spoke nipples" or session["spokes"]=="connects hub to rim" or session["spokes"]=="connects hub to spoke nipples":
        total=total+1
    else:
        incorrect=incorrect+Markup("10. Spokes "+ "<br><b>your answer</b> "+session["spokes"]+"<br> <b>correct answer</b>"+" connects hub to rim with spoke nipples <b>or</b> connects hub to rim <b>or</b> connects hub to spoke nipples<br><br>")

    if session["spokeNipples"]=="":
        total=total+1
    else:
        incorrect=incorrect+Markup("11. {value for value in variable}poke nipples "+ "<br><b>your answer</b> "+session["spokeNipples"]+"<br> <b>correct answer</b>"+" <br><br>")

    if session[""]=="":
        total=total+1
    else:
        incorrect=incorrect+Markup("12. "+ "<br><b>your answer</b> "+session[""]+"<br> <b>correct answer</b>"+" <br><br>")

    if session[""]=="":
        total=total+1
    else:
        incorrect=incorrect+Markup("13. "+ "<br><b>your answer</b> "+session[""]+"<br> <b>correct answer</b>"+" <br><br>")

    if session[""]=="":
        total=total+1
    else:
        incorrect=incorrect+Markup("14. "+ "<br><b>your answer</b> "+session[""]+"<br> <b>correct answer</b>"+" <br><br>")

    if session[""]=="":
        total=total+1
    else:
        incorrect=incorrect+Markup("15. "+ "<br><b>your answer</b> "+session[""]+"<br> <b>correct answer</b>"+" <br><br>")

    if session[""]=="":
        total=total+1
    else:
        incorrect=incorrect+Markup("16. "+ "<br><b>your answer</b> "+session[""]+"<br> <b>correct answer</b>"+" <br><br>")

    if session[""]=="":
        total=total+1
    else:
        incorrect=incorrect+Markup("17. "+ "<br><b>your answer</b> "+session[""]+"<br> <b>correct answer</b>"+" <br><br>")

    if session[""]=="":
        total=total+1
    else:
        incorrect=incorrect+Markup("18. "+ "<br><b>your answer</b> "+session[""]+"<br> <b>correct answer</b>"+" <br><br>")

    if session[""]=="":
        total=total+1
    else:
        incorrect=incorrect+Markup("19. "+ "<br><b>your answer</b> "+session[""]+"<br> <b>correct answer</b>"+" <br><br>")

    if session[""]=="":
        total=total+1
    else:
        incorrect=incorrect+Markup("20. "+ "<br><b>your answer</b> "+session[""]+"<br> <b>correct answer</b>"+" <br><br>")

    if session[""]=="":
        total=total+1
    else:
        incorrect=incorrect+Markup("21. "+ "<br><b>your answer</b> "+session[""]+"<br> <b>correct answer</b>"+" <br><br>")

    if session[""]=="":
        total=total+1
    else:
        incorrect=incorrect+Markup("22. "+ "<br><b>your answer</b> "+session[""]+"<br> <b>correct answer</b>"+" <br><br>")

    if session[""]=="":
        total=total+1
    else:
        incorrect=incorrect+Markup("23. "+ "<br><b>your answer</b> "+session[""]+"<br> <b>correct answer</b>"+" <br><br>")

    if session[""]=="":
        total=total+1
    else:
        incorrect=incorrect+Markup("24. "+ "<br><b>your answer</b> "+session[""]+"<br> <b>correct answer</b>"+" <br><br>")

    if session[""]=="":
        total=total+1
    else:
        incorrect=incorrect+Markup("25. "+ "<br><b>your answer</b> "+session[""]+"<br> <b>correct answer</b>"+" <br><br>")

    if session[""]=="":
        total=total+1
    else:
        incorrect=incorrect+Markup("26. "+ "<br><b>your answer</b> "+session[""]+"<br> <b>correct answer</b>"+" <br><br>")

    if session[""]=="":
        total=total+1
    else:
        incorrect=incorrect+Markup("27. "+ "<br><b>your answer</b> "+session[""]+"<br> <b>correct answer</b>"+" <br><br>")

    if session[""]=="":
        total=total+1
    else:
        incorrect=incorrect+Markup("28. "+ "<br><b>your answer</b> "+session[""]+"<br> <b>correct answer</b>"+" <br><br>")

    if session[""]=="":
        total=total+1
    else:
        incorrect=incorrect+Markup("29. "+ "<br><b>your answer</b> "+session[""]+"<br> <b>correct answer</b>"+" <br><br>")

    if session[""]=="":
        total=total+1
    else:
        incorrect=incorrect+Markup("30. "+ "<br><b>your answer</b> "+session[""]+"<br> <b>correct answer</b>"+" <br><br>")

    if session[""]=="":
        total=total+1
    else:
        incorrect=incorrect+Markup("31. "+ "<br><b>your answer</b> "+session[""]+"<br> <b>correct answer</b>"+" <br><br>")

    if session[""]=="":
        total=total+1
    else:
        incorrect=incorrect+Markup("32. "+ "<br><b>your answer</b> "+session[""]+"<br> <b>correct answer</b>"+" <br><br>")

    if session[""]=="":
        total=total+1
    else:
        incorrect=incorrect+Markup("33. "+ "<br><b>your answer</b> "+session[""]+"<br> <b>correct answer</b>"+" <br><br>")

    if session[""]=="":
        total=total+1
    else:
        incorrect=incorrect+Markup("34. "+ "<br><b>your answer</b> "+session[""]+"<br> <b>correct answer</b>"+" <br><br>")

    if session[""]=="":
        total=total+1
    else:
        incorrect=incorrect+Markup("35. "+ "<br><b>your answer</b> "+session[""]+"<br> <b>correct answer</b>"+" <br><br>")

    if session[""]=="":
        total=total+1
    else:
        incorrect=incorrect+Markup("36. "+ "<br><b>your answer</b> "+session[""]+"<br> <b>correct answer</b>"+" <br><br>")

    if session[""]=="":
        total=total+1
    else:
        incorrect=incorrect+Markup("37. "+ "<br><b>your answer</b> "+session[""]+"<br> <b>correct answer</b>"+" <br><br>")

    if session[""]=="":
        total=total+1
    else:
        incorrect=incorrect+Markup("38. "+ "<br><b>your answer</b> "+session[""]+"<br> <b>correct answer</b>"+" <br><br>")

    if session[""]=="":
        total=total+1
    else:
        incorrect=incorrect+Markup("39. "+ "<br><b>your answer</b> "+session[""]+"<br> <b>correct answer</b>"+" <br><br>")

    if session[""]=="":
        total=total+1
    else:
        incorrect=incorrect+Markup("40. "+ "<br><b>your answer</b> "+session[""]+"<br> <b>correct answer</b>"+" <br><br>")

    if session[""]=="":
        total=total+1
    else:
        incorrect=incorrect+Markup("41. "+ "<br><b>your answer</b> "+session[""]+"<br> <b>correct answer</b>"+" <br><br>")

    if session[""]=="":
        total=total+1
    else:
        incorrect=incorrect+Markup("42. "+ "<br><b>your answer</b> "+session[""]+"<br> <b>correct answer</b>"+" <br><br>")

    if session[""]=="":
        total=total+1
    else:
        incorrect=incorrect+Markup("43. "+ "<br><b>your answer</b> "+session[""]+"<br> <b>correct answer</b>"+" <br><br>")

    if session[""]=="":
        total=total+1
    else:
        incorrect=incorrect+Markup("44. "+ "<br><b>your answer</b> "+session[""]+"<br> <b>correct answer</b>"+" <br><br>")

    if session[""]=="":
        total=total+1
    else:
        incorrect=incorrect+Markup("45. "+ "<br><b>your answer</b> "+session[""]+"<br> <b>correct answer</b>"+" <br><br>")

    if session[""]=="":
        total=total+1
    else:
        incorrect=incorrect+Markup("46. "+ "<br><b>your answer</b> "+session[""]+"<br> <b>correct answer</b>"+" <br><br>")

    if session[""]=="":
        total=total+1
    else:
        incorrect=incorrect+Markup("47. "+ "<br><b>your answer</b> "+session[""]+"<br> <b>correct answer</b>"+" <br><br>")

    if session[""]=="":
        total=total+1
    else:
        incorrect=incorrect+Markup("48. "+ "<br><b>your answer</b> "+session[""]+"<br> <b>correct answer</b>"+" <br><br>")

    if session[""]=="":
        total=total+1
    else:
        incorrect=incorrect+Markup("49. "+ "<br><b>your answer</b> "+session[""]+"<br> <b>correct answer</b>"+" <br><br>")

    if session[""]=="":
        total=total+1
    else:
        incorrect=incorrect+Markup("50. "+ "<br><b>your answer</b> "+session[""]+"<br> <b>correct answer</b>"+" <br><br>")

    if session[""]=="":
        total=total+1
    else:
        incorrect=incorrect+Markup("51. "+ "<br><b>your answer</b> "+session[""]+"<br> <b>correct answer</b>"+" <br><br>")

    if session[""]=="":
        total=total+1
    else:
        incorrect=incorrect+Markup("52. "+ "<br><b>your answer</b> "+session[""]+"<br> <b>correct answer</b>"+" <br><br>")

    if session[""]=="":
        total=total+1
    else:
        incorrect=incorrect+Markup("53. "+ "<br><b>your answer</b> "+session[""]+"<br> <b>correct answer</b>"+" <br><br>")

    if session[""]=="":
        total=total+1
    else:
        incorrect=incorrect+Markup("54. "+ "<br><b>your answer</b> "+session[""]+"<br> <b>correct answer</b>"+" <br><br>")

    if session[""]=="":
        total=total+1
    else:
        incorrect=incorrect+Markup("55. "+ "<br><b>your answer</b> "+session[""]+"<br> <b>correct answer</b>"+" <br><br>")

    if session[""]=="":
        total=total+1
    else:
        incorrect=incorrect+Markup("56. "+ "<br><b>your answer</b> "+session[""]+"<br> <b>correct answer</b>"+" <br><br>")

    if session[""]=="":
        total=total+1
    else:
        incorrect=incorrect+Markup("57. "+ "<br><b>your answer</b> "+session[""]+"<br> <b>correct answer</b>"+" <br><br>")

    if session[""]=="":
        total=total+1
    else:
        incorrect=incorrect+Markup("58. "+ "<br><b>your answer</b> "+session[""]+"<br> <b>correct answer</b>"+" <br><br>")

    if session[""]=="":
        total=total+1
    else:
        incorrect=incorrect+Markup("59. "+ "<br><b>your answer</b> "+session[""]+"<br> <b>correct answer</b>"+" <br><br>")

    return render_template('Answers.html', incorrect=incorrect, score=total)








if __name__ == '__main__':
    app.run(debug=True)
