from flask import Flask, render_template, request
import pickle


app = Flask(__name__,template_folder='template')
model = pickle.load(open('finalized_model.pickle', 'rb'))

@app.route("/",methods=["GET"])
def Home_page():
    return render_template("index.html")


@app.route("/predict",methods=["POST"])
def prediction_page():
    if request.method == "POST":
        Age = float(request.form["Age"])
        Gender = float(request.form["Gender"])
        self_employed = float(request.form["self_employed"])
        family_history = float(request.form["family_history"])
        work_interfere= float(request.form["work_interfere"])
        no_employees = float(request.form["no_employees"])
        remote_work = float(request.form["remote_work"])
        tech_company = float(request.form["tech_company"])
        benefits = float(request.form["benefits"])
        care_options = float(request.form["care_options"])
        wellness_program = float(request.form["wellness_program"])
        seek_help = float(request.form["seek_help"])
        anonymity = float(request.form["anonymity"])
        leave = float(request.form["leave"])
        mental_health_consequence = float(request.form["mental_health_consequence"])
        phys_health_consequence = float(request.form["phys_health_consequence"])
        coworkers = float(request.form["coworkers"])
        supervisor = float(request.form["supervisor"])
        mental_health_interview = float(request.form["mental_health_interview"])
        phys_health_interview = float(request.form["phys_health_interview"])
        mental_vs_physical = float(request.form["mental_vs_physical"])
        obs_consequence = float(request.form["obs_consequence"])


        prediction = model.predict([[Age, Gender, self_employed, family_history, work_interfere, no_employees, remote_work, tech_company, benefits, care_options, wellness_program, seek_help, anonymity, leave, mental_health_consequence, phys_health_consequence, coworkers, supervisor, mental_health_interview, phys_health_interview, mental_vs_physical, obs_consequence]])

        return render_template('result.html',result=prediction)
        print("Employee need a treatment")

    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)