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
        session["spokeNipples"]=request.form["spokeNipples"] #11 done
        session["hub"]=request.form["hub"] #12 staged
        session["tube"]=request.form["tube"] #13 staged
        session["tire"]=request.form["tire"] #14 staged
        session["valveSystem"]=request.form["valveSystem"] #15 staged

        #2-2
        session["tubed"]=request.form["tubed"] #16 staged
        session["tubeless"]=request.form["tubeless"] #17 staged

        #6-6
        session["s20"]=request.form["s20"] #18 staged
        session["s24"]=request.form["s24"] #19 staged
        session["s26"]=request.form["s26"] #20 staged
        session["s27"]=request.form["s27"] #21 staged
        session["s27.5"]=request.form["s27.5"] #22 staged
        session["s29"]=request.form["s29"] #23 staged

        #2-2
        session["fullSuspension"]=request.form["fullSuspension"] #24 staged
        session["frontSuspension"]=request.form["frontSuspension"] #25 staged

        #16-16
        session["bottomTube"]=request.form["bottomTube"] #26 staged
        session["topTube"]=request.form["topTube"] #27 staged
        session["seatTube"]=request.form["seatTube"] #28 staged
        session["seatPost"]=request.form["seatPost"] #29 staged
        session["stem"]=request.form["stem"] #30 staged
        session["headTube"]=request.form["headTube"] #31 staged
        session["frontDropout"]=request.form["frontDropout"] #32 staged
        session["forkLegs"]=request.form["forkLegs"] #33
        session["seatStays"]=request.form["seatStays"] #34 staged
        session["headset"]=request.form["headset"] #35
        session["housingStop"]=request.form["housingStop"] #36 staged
        session["rearDropout"]=request.form["rearDropout"] #37
        session["forkCrown"]=request.form["forkCrown"] #38 staged
        session["adjustingBarrel"]=request.form["adjustingBarrel"] #39
        session["frontBrakes"]=request.form["frontBrakes"] #40 staged
        session["rearBrakes"]=request.form["rearBrakes"] #41

        #3-3

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
        session["uBrakes"]=request.form["uBrakes"] #42 staged
        session["rimBrakes"]=request.form["rimBrakes"] #43
        session["discBrakes"]=request.form["discBrakes"] #44 staged
        session["shrader"]=request.form["shrader"] #45
        session["presta"]=request.form["presta"] #46 staged
        session["rotor"]=request.form["rotor"] #47
        session["breakPads"]=request.form["breakPads"] #48
        session["hydraulicDisc"]=request.form["hydraulicDisc"] #49
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
        incorrect=incorrect+Markup("1. Cassette "+ "<br><b>your answer:</b> "+session["cassette"]+"<br> <b>correct answer:</b>"+" rear gears<br><br>")

    if session["chainRings"]=="front gear" or session["chainRings"]=="front gears":
        total=total+1
    else:
        incorrect=incorrect+Markup("2. chain-rings "+ "<br><b>your answer:</b> "+session["chainRings"]+"<br> <b>correct answer:</b>"+" front gear(s)<br><br>")

    if session["chain"]=="connects cassette to chain-rings":
        total=total+1
    else:
        incorrect=incorrect+Markup("3. Chain "+ "<br><b>your answer:</b> "+session["chain"]+"<br> <b>correct answer:</b>"+" connects the cassette to the chain-rings <br><br>")

    if session["rearShifter"]=="shifts rear gears":
        total=total+1
    else:
        incorrect=incorrect+Markup("4. Rear shifter "+ "<br><b>your answer:</b> "+session["rearShifter"]+"<br> <b>correct answer:</b>"+" shifts rear gears<br><br>")

    if session["frontShifter"]=="shifts front gears":
        total=total+1
    else:
        incorrect=incorrect+Markup("5. Front shifter "+ "<br><b>your answer:</b> "+session["frontShifter"]+"<br> <b>correct answer:</b>"+" shifts front gears<br><br>")

    if session["pedals"]=="connected to crank arms":
        total=total+1
    else:
        incorrect=incorrect+Markup("6. Pedals "+ "<br><b>your answer:</b> "+session["pedals"]+"<br> <b>correct answer:</b>"+" connected to crank arms<br><br>")

    if session["crankArms"]=="connects pedals to bike frame" or session["crankArms"]=="connects the pedals to the crankset":
        total=total+1
    else:
        incorrect=incorrect+Markup("7. Crank arms "+ "<br><b>your answer:</b> "+session["crankArms"]+"<br> <b>correct answer:</b>"+" connects pedals to bike frame <b>or</b> connects the pedals to the crankset<br><br>")

    if session["crankset"]=="connects to crank arms to the bike frame" or session["crankset"]=="connects to crank arms to the bike frame":
        total=total+1
    else:
        incorrect=incorrect+Markup("8. Crankset "+ "<br><b>your answer:</b> "+session["crankset"]+"<br> <b>correct answer:</b>"+" connects to crank arms to the bike frame <b>or</b> <br><br>")

    if session["rim"]=="gives the wheel it's shape" or session["rim"]=="keeps the wheels in circular shape" or session["rim"]=="gives the wheels it's shape" or session["rim"]=="keeps the wheels in circular shape":
        total=total+1
    else:
        incorrect=incorrect+Markup("9. Rim "+ "<br><b>your answer:</b> "+session["rim"]+"<br> <b>correct answer:</b>"+" gives the wheel(s) it's shape <b>or</b> keeps the wheel(s) in circular shape<br><br>")

    if session["spokes"]=="connects hub to rim with spoke nipples" or session["spokes"]=="connects the hub to the rim" or session["spokes"]=="connects hub to spoke nipples":
        total=total+1
    else:
        incorrect=incorrect+Markup("10. Spokes "+ "<br><b>your answer:</b> "+session["spokes"]+"<br> <b>correct answer:</b>"+" connects hub to rim with spoke nipples <b>or</b> connects hub to rim <b>or</b> connects hub to spoke nipples<br><br>")

    if session["spokeNipples"]=="holds the spokes in the rim" or session["spokeNipples"]=="connects the rim to the spokes" or session["spokeNipples"]=="controls tightness of spokes":
        total=total+1
    else:
        incorrect=incorrect+Markup("11. Spoke nipples "+ "<br><b>your answer:</b> "+session["spokeNipples"]+"<br> <b>correct answer:</b>"+" holds the spokes in the rim <b>or</b> connects the rim to the spokes <b>or</b> controls tightness of spokes<br><br>")

    if "center of the wheel" in session["hub"]:
        total=total+1
    else:
        incorrect=incorrect+Markup("12. Hub "+ "<br><b>your answer:</b> "+session["hub"]+"<br> <b>correct answer:</b>"+" center of the wheel <b>or</b> the center of the wheels<br><br>")

    if "is inside tube" in session["tube"]:
        total=total+1
    else:
        incorrect=incorrect+Markup("13. Tube "+ "<br><b>your answer:</b> "+session["tube"]+"<br> <b>correct answer:</b>"+" it inflates inside of tube<br><br>")

    if "covers" in session["tire"] or "surrounds" in session["tire"] or "protects" in session["tire"] or "around" in session["tire"] or "connects" in session["tire"] or "connected" in session["tire"] or "connect" in session["tire"] or "damage" in session["tire"] or "protecting" in session["tire"] or "protect" in session["tire"]:
        total=total+1
    else:
        incorrect=incorrect+Markup("14. Tire "+ "<br><b>your answer:</b> "+session["tire"]+"<br> <b>correct answer:</b>"+" connects to the rim on both side and surrounds the tube/holds in air while protecting the rim from damage<br><br>")

    if "inflate" in session["valveSystem"] or "nozzle" in session["valveSystem"]:
        total=total+1
    else:
        incorrect=incorrect+Markup("15. Valve System "+ "<br><b>your answer:</b> "+session["valveSystem"]+"<br> <b>correct answer:</b>"+" the nozzle that is used to inflate tire<br><br>")

    if "has tube" in session["tubed"] or "tire" in session["tubed"]:
        total=total+1
    else:
        incorrect=incorrect+Markup("16. Tubed "+ "<br><b>your answer:</b> "+session["tubed"]+"<br> <b>correct answer:</b>"+" has a tube inside tire<br><br>")

    if "doesn't have tube" in session["tubeless"] or "tire" in session["tubeless"] or "no tube" in session["tubeless"]:
        total=total+1
    else:
        incorrect=incorrect+Markup("17. Tubeless "+ "<br><b>your answer:</b> "+session["tubeless"]+"<br> <b>correct answer:</b>"+" has a tube inside tire<br><br>")

    if "s20" in session["s20"]:
        total=total+1
    else:
        incorrect=incorrect+Markup("18. Size "+ "<br><b>your answer:</b> "+session["s20"]+"<br> <b>correct answer:</b>"+" 20<br><br>")

    if "s24" in session["s24"]:
        total=total+1
    else:
        incorrect=incorrect+Markup("19. Size "+ "<br><b>your answer:</b> "+session["s24"]+"<br> <b>correct answer:</b>"+" 24<br><br>")

    if "s26" in session["s26"]:
        total=total+1
    else:
        incorrect=incorrect+Markup("20. Size "+ "<br><b>your answer:</b> "+session["s26"]+"<br> <b>correct answer:</b>"+" 26<br><br>")

    if "s27" in session["s27"]:
        total=total+1
    else:
        incorrect=incorrect+Markup("21. Size "+ "<br><b>your answer:</b> "+session["s27"]+"<br> <b>correct answer:</b>"+" 27<br><br>")

    if "s27.5" in session["s27.5"]:
        total=total+1
    else:
        incorrect=incorrect+Markup("22. Size "+ "<br><b>your answer:</b> "+session["s27.5"]+"<br> <b>correct answer:</b>"+" 27.5<br><br>")

    if "s29" in session["s29"]:
        total=total+1
    else:
        incorrect=incorrect+Markup("23. Size "+ "<br><b>your answer:</b> "+session["s29"]+"<br> <b>correct answer:</b>"+" 29<br><br>")

    if "both" in session["fullSuspension"] or "front" in session["fullSuspension"] or "back" in session["fullSuspension"] or "rear" in session["fullSuspension"] or "suspension" in session["tire"] or "shocks" in session["tire"] or "bike" in session["fullSuspension"]:
        total=total+1
    else:
        incorrect=incorrect+Markup("24. Full Suspension "+ "<br><b>your answer:</b> "+session["fullSuspension"]+"<br> <b>correct answer:</b>"+" a bike that has suspension in the fork legs and somewhere between the top tube and bottom tube<br><br>")

    if "front" in session["frontSuspension"]:
        total=total+1
    else:
        incorrect=incorrect+Markup("25. Front Suspension "+ "<br><b>your answer:</b> "+session["frontSuspension"]+"<br> <b>correct answer:</b>"+" bike that only has suspension in front of bike frame<br><br>")

    if "down" in session["bottomTube"] or "bottom" in session["bottomTube"] or "tube" in session["bottomTube"] or "below" in session["bottomTube"] or "top" in session["bottomTube"]:
        total=total+1
    else:
        incorrect=incorrect+Markup("26. Bottom Tube "+ "<br><b>your answer:</b> "+session["bottomTube"]+"<br> <b>correct answer:</b>"+" runs along the bottom of the bike<br><br>")

    if "top" in session["topTube"] or "tube" in session["topTube"] or "above" in session["topTube"] or "top" in session["topTube"]:
        total=total+1
    else:
        incorrect=incorrect+Markup("27. Top Tube "+ "<br><b>your answer:</b> "+session["topTube"]+"<br> <b>correct answer:</b>"+" runs along the top of the bike<br><br>")

    if session["seatTube"]=="connects to the bottom of the seat":
        total=total+1
    else:
        incorrect=incorrect+Markup("28. Seat Tube "+ "<br><b>your answer:</b> "+session["seatTube"]+"<br> <b>correct answer:</b>"+" connects to the bottom of the seat<br><br>")

    if session["seatPost"]=="connects to the seat tube":
        total=total+1
    else:
        incorrect=incorrect+Markup("29. Seat Post "+ "<br><b>your answer:</b> "+session["seatPost"]+"<br> <b>correct answer:</b>"+" connects to the seat tube<br><br>")

    if session["stem"]=="connects the handlebars to the steerer tube of the bicycle fork":
        total=total+1
    else:
        incorrect=incorrect+Markup("30. Stem "+ "<br><b>your answer:</b> "+session["stem"]+"<br> <b>correct answer:</b>"+" connects the handlebars to the steerer tube of the bicycle fork<br><br>")

    if session["headTube"]==" short tube at the front of the frame, which connects the handlebars to the wheel fork":
        total=total+1
    else:
        incorrect=incorrect+Markup("31. Head Tube "+ "<br><b>your answer:</b> "+session["headTube"]+"<br> <b>correct answer:</b>"+"  short tube at the front of the frame, which connects the handlebars to the wheel fork<br><br>")

    if session["frontDropout"]=="slot in a frame or fork where the axle of the front wheel is attached":
        total=total+1
    else:
        incorrect=incorrect+Markup("32. Front Dropout "+ "<br><b>your answer:</b> "+session["frontDropout"]+"<br> <b>correct answer:</b>"+" slot in a frame or fork where the axle of the front wheel is attached<br><br>")

    if session["forkLegs"]=="connects the front wheel to the frame":
        total=total+1
    else:
        incorrect=incorrect+Markup("33. Fork Legs "+ "<br><b>your answer:</b> "+session["forkLegs"]+"<br> <b>correct answer:</b>"+" connects the front wheel to the frame<br><br>")

    if session["seatStays"]=="run diagonally down the rear of a bicycle frame and connect the seat tube to the chainstays/rear dropouts":
        total=total+1
    else:
        incorrect=incorrect+Markup("34. Seat Stays "+ "<br><b>your answer:</b> "+session["seatStays"]+"<br> <b>correct answer:</b>"+" run diagonally down the rear of a bicycle frame and connect the seat tube to the chainstays/rear dropouts<br><br>")

    if session["headset"]=="set of components on a bicycle that provides a rotatable interface between the bicycle fork and the head tube of a bicycle frame":
        total=total+1
    else:
        incorrect=incorrect+Markup("35. Headset "+ "<br><b>your answer:</b> "+session["headset"]+"<br> <b>correct answer:</b>"+" set of components on a bicycle that provides a rotatable interface between the bicycle fork and the head tube of a bicycle frame<br><br>")

    if session["housingStop"]=="stops the housing from moving around":
        total=total+1
    else:
        incorrect=incorrect+Markup("36. Housing Stop "+ "<br><b>your answer:</b> "+session["housingStop"]+"<br> <b>correct answer:</b>"+" stops the housing from moving around<br><br>")

    if session["rearDropout"]=="slot in a frame or fork where the axle of the rear wheel is attached":
        total=total+1
    else:
        incorrect=incorrect+Markup("37. Rear Dropout "+ "<br><b>your answer:</b> "+session["rearDropout"]+"<br> <b>correct answer:</b>"+" slot in a frame or fork where the axle of the rear wheel is attached<br><br>")

    if session["forkCrown"]=="connects between fork legs":
        total=total+1
    else:
        incorrect=incorrect+Markup("38. Fork Crown "+ "<br><b>your answer:</b> "+session["frokCrown"]+"<br> <b>correct answer:</b>"+" bridges gap between the fork legs and helps keep them sturdy<br><br>")

    if session["adjustingBarrel"]=="built-in solutions to cable tension":
        total=total+1
    else:
        incorrect=incorrect+Markup("39. Adjusting Barrel "+ "<br><b>your answer:</b> "+session[""]+"<br> <b>correct answer:</b>"+" built-in solutions to cable tension<br><br>")

    if session["frontBrakes"]=="break for front wheel":
        total=total+1
    else:
        incorrect=incorrect+Markup("40. Front brakes "+ "<br><b>your answer:</b> "+session["frontBrakes"]+"<br> <b>correct answer:</b>"+" brakes for front wheel<br><br>")

    if session["rearBrakes"]=="brakes for front wheel":
        total=total+1
    else:
        incorrect=incorrect+Markup("41. Rear brakes "+ "<br><b>your answer:</b> "+session["rearBrakes"]+"<br> <b>correct answer:</b>"+" brakes for front wheel<br><br>")

    if session["uBrakes"]=="":
        total=total+1
    else:
        incorrect=incorrect+Markup("42. U-brakes "+ "<br><b>your answer:</b> "+session[""]+"<br> <b>correct answer:</b>"+" <br><br>")

    if session["rimBrakes"]=="":
        total=total+1
    else:
        incorrect=incorrect+Markup("43. "+ "<br><b>your answer:</b> "+session[""]+"<br> <b>correct answer:</b>"+" <br><br>")

    if session["discBrakes"]=="":
        total=total+1
    else:
        incorrect=incorrect+Markup("44. Disc brakes "+ "<br><b>your answer:</b> "+session[""]+"<br> <b>correct answer:</b>"+" <br><br>")

    if session["shrader"]=="":
        total=total+1
    else:
        incorrect=incorrect+Markup("45. shrader "+ "<br><b>your answer:</b> "+session[""]+"<br> <b>correct answer:</b>"+" <br><br>")

    if session["presta"]=="the skinny and long valve system with a piece on end that can be loosened by twisting":
        total=total+1
    else:
        incorrect=incorrect+Markup("46. Presta "+ "<br><b>your answer:</b> "+session[""]+"<br> <b>correct answer:</b>"+" the skinny and long valve system with a piece on end that can be loosened by twisting<br><br>")

    if session["rotor"]==" metal disc affixed to each wheel hub that runs in between the brake pads in the brake calipers on the bike frame":
        total=total+1
    else:
        incorrect=incorrect+Markup(+ "<br><b>your answer:</b> "+session[""]+"<br> <b>correct answer:</b>"+"  metal disc affixed to each wheel hub that runs in between the brake pads in the brake calipers on the bike frame<br><br>")

    if "break" in session["tire"] or "hydrolic" in session["tire"] or "mechanical" in session["tire"] or "rim" in session["tire"] or "rotor" in session["breakPads"]:
        total=total+1
    else:
        incorrect=incorrect+Markup("48. Break Pads "+ "<br><b>your answer:</b> "+session["breakPads"]+"<br> <b>correct answer:</b>"+" used by brakes to stop the bike<br><br>")

    if "liquid" in session["hydraulicDisc"] or "fluid" in session["hydraulicDisc"] or "housing" in session["hydraulicDisc"] or "rotor" in session["hydraulicDisc"] or "hub" in session["hydraulicDisc"] or "center" in session["hydraulicDisc"] or "wheel" in session["hydraulicDisc"] or "middle" in session["hydraulicDisc"] or "break pads" in session["hydraulicDisc"] or "cable" in session["hydraulicDisc"]:
        total=total+1
    else:
        incorrect=incorrect+Markup("49. Hydraulic Disc "+ "<br><b>your answer:</b> "+session["hydraulicDisc"]+"<br> <b>correct answer:</b>"+" uses a cable to have the break levers  close the brake pads on the rotor<br><br>")

    if "rotor" in session["mechanicalDisc"] or "hub" in session["mechanicalDisc"] or "center" in session["mechanicalDisc"] or "wheel" in session["mechanicalDisc"] or "middle" in session["mechanicalDisc"] or "break pads" in session["mechanicalDisc"] or "cable" in session["mechanicalDisc"] or "liquid" in session["mechanicalDisc"] or "fluid" in session["mechanicalDisc"] or "housing" in session["mechanicalDisc"]:
        total=total+1
    else:
        incorrect=incorrect+Markup("50. Mechanical Disc "+ "<br><b>your answer:</b> "+session["mechanicalDisc"]+"<br> <b>correct answer:</b>"+" uses a cable to have the break levers close the brake pads on the rotor<br><br>")

    if "5" in session["c5"]:
        total=total+1
    else:
        incorrect=incorrect+Markup("51. Size "+ "<br><b>your answer:</b> "+session["c5"]+"<br> <b>correct answer:</b>"+" 5<br><br>")

    if "6" in session["c6"]:
        total=total+1
    else:
        incorrect=incorrect+Markup("52. Size "+ "<br><b>your answer:</b> "+session["c6"]+"<br> <b>correct answer:</b>"+" 6<br><br>")

    if "7" in session["c7"]:
        total=total+1
    else:
        incorrect=incorrect+Markup("53. Size "+ "<br><b>your answer:</b> "+session["c7"]+"<br> <b>correct answer:</b>"+" 7<br><br>")

    if "8" in session["c8"]:
        total=total+1
    else:
        incorrect=incorrect+Markup("54. Size "+ "<br><b>your answer:</b> "+session["c8"]+"<br> <b>correct answer:</b>"+" 8<br><br>")

    if "9" in session["c9"]:
        total=total+1
    else:
        incorrect=incorrect+Markup("55. Size "+ "<br><b>your answer:</b> "+session["c9"]+"<br> <b>correct answer:</b>"+" 9<br><br>")

    if "10" in session["c10"]:
        total=total+1
    else:
        incorrect=incorrect+Markup("56. Size "+ "<br><b>your answer:</b> "+session["c10"]+"<br> <b>correct answer:</b>"+" 10<br><br>")

    if "11" in session["c11"]:
        total=total+1
    else:
        incorrect=incorrect+Markup("57. Size "+ "<br><b>your answer:</b> "+session["c11"]+"<br> <b>correct answer:</b>"+" 11<br><br>")

    if "12" in session["c12"]:
        total=total+1
    else:
        incorrect=incorrect+Markup("58. Size "+ "<br><b>your answer:</b> "+session["c12"]+"<br> <b>correct answer:</b>"+" 12<br><br>")

    if "13" in session["c13"]:
        total=total+1
    else:
        incorrect=incorrect+Markup("59. Size "+ "<br><b>your answer:</b> "+session["c13"]+"<br> <b>correct answer:</b>"+" 13<br><br>")

    return render_template('Answers.html', wrong=incorrect, score=total)








if __name__ == '__main__':
    app.run(debug=True)
