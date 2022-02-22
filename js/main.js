const allGrades = {
    "Charlie" : {
        "Unit-3" : ["4/5", "2/5", "8/15"],
        "Unit-4" : ["4/5", "0/10"],
        "Unit-5" : ["2/5", "7/15"],
        "Unit-6" : ["7/15"],
        "Unit-7" : ["N/A"],
    },
    "David" : {
        "Unit-3" : ["0/5", "2/5", "12/15"],
        "Unit-4" : ["2/5", "5.5/10"],
        "Unit-5" : ["3/5", "8/15"],
        "Unit-6" : ["11/15"],
        "Unit-7" : ["3/5"],
    },
    "Hong" : {
        "Unit-3" : ["2/5", "5/5", "8/15"],
        "Unit-4" : ["N/A", "2/10"],
        "Unit-5" : ["1/5", "7/15"],
        "Unit-6" : ["5/15"],
        "Unit-7" : ["2/5"],
    },
    "Jonathan" : {
        "Unit-3" : ["1/5", "3/5", "10/15"],
        "Unit-4" : ["3/5", "8.5/10"],
        "Unit-5" : ["5/5", "12/15"],
        "Unit-6" : ["13/15"],
        "Unit-7" : ["4/5"],
    },
    "Paul" : {
        "Unit-3" : ["4/5", "3/5", "N/A"],
        "Unit-4" : ["2/5", "4/10"],
        "Unit-5" : ["1/5", "8/15"],
        "Unit-6" : ["8/15"],
        "Unit-7" : ["1/5"],
    },
    "Victoria" : {
        "Unit-3" : ["N/A", "3/5", "7/15"],
        "Unit-4" : ["3/5", "N/A"],
        "Unit-5" : ["4/5", "10/15"],
        "Unit-6" : ["11/15"],
        "Unit-7" : ["4/5"],
    },
};

// var finalOverall = [];

// class Grade
// {
//     #name = "";
//     #finalGrade = 0;
//     constructor(name, finalGrade)
//     {
//         this.#name = name;
//         this.#finalGrade = finalGrade;
//     }

//     getName()
//     {
//         return this.#name;
//     }

//     getGrade()
//     {
//         return this.#finalGrade;
//     }
// }

function setJava3()
{
    const notesUrl = "resources/APJava3/_notes/Unit-7-Notes.zip";
    const notesName = "Unit 7 Notes";
    const hwName = "Unit 7 Review";
    const hw = "// Required: \n// Quiz Part2 on Unit-7 \n// 5 Questions";

    const java3end = document.getElementById("end-java3");
    const java3hw = document.getElementById("hw-java3");
    const java3grades = document.getElementById("grades-java3");
    java3end.setAttribute("href", notesUrl);
    java3end.innerHTML = notesName;

    java3hw.children[1].innerHTML = hwName;
    java3hw.children[2].innerHTML = hw;
    java3grades.children[1].innerHTML = outputFraction(allGrades);
    // java3grades.innerHTML = calcAverage(allGrades);
    // console.log(outputDecimal(allGrades));
}

function outputDecimal(allUnits)
{
    let out = "";
    for (let name in allUnits)
    {
        let tempGrades = [];

        // Add extra line after name
        out += name + ": \n";
        grades = allUnits[name];

        for (let unit in grades)
        {
            out += unit + ": ";
            grades[unit].forEach((nums) => {

                let converted = convertFrac(nums);

                // tempGrades for each unit to calculate overall average
                tempGrades.push(converted);

                // convert to decimal
                out += converted + " ";
            });
            out += "\n";
        }
        out += "\n";

        out += "Overall: " + (calcAverage(tempGrades) * 100) + "%\n\n";

        // finalOverall.push(new Grade(name, calcAverage(tempGrades)));
    }
    return out;
}

function outputFraction(allUnits)
{
    let out = "";
    for (let name in allUnits)
    {
        let tempGrades = [];

        // Add extra line after name
        out += name + ": \n";
        grades = allUnits[name];

        for (let unit in grades)
        {
            out += unit + ": ";
            grades[unit].forEach((nums) => {

                // tempGrades for each unit to calculate overall average
                tempGrades.push(convertFrac(nums));

                // convert to decimal
                out += nums + " ";
            });
            out += "\n";
        }
        out += "\n";

        // Add overall at the end

        out += "Overall: " + (calcAverage(tempGrades) * 100) + "%\n\n";
    }
    return out;
}

function calcAverage(tmpGrades)
{
    let size = tmpGrades.length;
    let sum = 0;
    for (let num in tmpGrades)
    {
        if (isNaN(tmpGrades[num]))
            size--;
        else
            sum += parseFloat(tmpGrades[num]);
    }
    return (sum / size).toPrecision(2);
}

function convertFrac(grade)
{
    let out = grade.split('/');
    let done = out[0] / out[1];
    if (isNaN(done))
    return "N/A";
    else
    return done.toPrecision(2);
}

window.onload = setJava3;