const allGrades = {
    "Charlie" : {
        "Unit-3" : ["4/5", "2/5", "8/15"],
        "Unit-4" : ["4/5", "0/10"],
        "Unit-5" : ["2/5", "7/15"],
        "Unit-6" : ["7/15"],
        "Unit-7" : ["N/A", "2/5", "9/15"],
        "Unit-8" : ["2.5/5"],
    },
    "David" : {
        "Unit-3" : ["0/5", "2/5", "12/15"],
        "Unit-4" : ["2/5", "5.5/10"],
        "Unit-5" : ["3/5", "8/15"],
        "Unit-6" : ["11/15"],
        "Unit-7" : ["3/5", "1/5", "8/15"],
        "Unit-8" : ["3.5/5"],
    },
    "Hong" : {
        "Unit-3" : ["2/5", "5/5", "8/15"],
        "Unit-4" : ["N/A", "2/10"],
        "Unit-5" : ["1/5", "7/15"],
        "Unit-6" : ["5/15"],
        "Unit-7" : ["2/5", "2/5", "9/15"],
        "Unit-8" : ["1.5/5"],
    },
    "Jonathan" : {
        "Unit-3" : ["1/5", "3/5", "10/15"],
        "Unit-4" : ["3/5", "8.5/10"],
        "Unit-5" : ["5/5", "12/15"],
        "Unit-6" : ["13/15"],
        "Unit-7" : ["4/5", "4/5", "9/15"],
        "Unit-8" : ["2.5/5"],
    },
    "Paul" : {
        "Unit-3" : ["4/5", "3/5", "N/A"],
        "Unit-4" : ["2/5", "4/10"],
        "Unit-5" : ["1/5", "8/15"],
        "Unit-6" : ["8/15"],
        "Unit-7" : ["1/5", "2/5", "3/15"],
        "Unit-8" : ["4.5/5"],
    },
    "Victoria" : {
        "Unit-3" : ["N/A", "3/5", "7/15"],
        "Unit-4" : ["3/5", "N/A"],
        "Unit-5" : ["4/5", "10/15"],
        "Unit-6" : ["11/15"],
        "Unit-7" : ["4/5", "1/5", "11/15"],
        "Unit-8" : ["0.5/5"],
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

function setButtons()
{
    const accordion = document.getElementById("accordion");
    const allClasses = [
        "Scratch Friday Class",
        "Pygame Friday Class",
        "Pygame Thursday Class"];
    // console.log(accordion.children);
    for (let x = 0; x < accordion.children.length; x++)
    {
        accordion.children[x].lastChild.textContent = allClasses[x];
    }
}

function setAll()
{
    setButtons();
    setJava3();
    setClass1();
    setClass2();
    setClass3();
    //setClass5();
    //setClass6();
}

function setJava3()
{
    const notesUrl = "resources/APJava1/2022_05_07/_end_code_/Class14.zip";
    const notesName = "Class14.zip";
    const hwName = "Inheritance Part2";
    let hw = `CLASS 14 SEP 03 2022:
// Required:
// Implement magicSpeak() in Animal class
// Override magicSpeak() for Bird, Dog, Dolphin, Cat, Mosquito
// Animal.magicSpeak()
// -> My name is Sparky and I am 5 years old and I am 5m(s) tall and I weigh 1lb(s)
// Dolphin.magicSpeak()
// -> My name is Echo the Dolphin and I am 5 years old and I am 5cm(s) tall and I weigh 2lb(s)
//    Echo! Echo!
// Make an ArrayList called zoo that contains all the animals
// You should have 25 animals in total, 5 of ea.
// You can add new objects inline like so: zoo.add(new Mosquito("Evil", 5, 5, 10));
// Use a loop to have them all magicSpeak()
// zoo.get(0).magicSpeak();`;

    const java3end = document.getElementById("end-java3");
    const java3hw = document.getElementById("hw-java3");
    const java3grades = document.getElementById("grades-java3");
    java3end.setAttribute("href", notesUrl);
    java3end.innerHTML = notesName;

    java3hw.children[1].innerHTML = hwName;
    java3hw.children[2].innerHTML = hw;
    // java3grades.children[1].innerHTML = outputFraction(allGrades);
    // java3grades.innerHTML = calcAverage(allGrades);
    // console.log(outputDecimal(allGrades));
}

function setClass1()
{
    const title = "Scratch Friday Class";
    const endUrl = "";
    const endName = ""
    const hwTitle = "Scratch time";
    let hwStr = `
MAY 12 2023
Add three dancers to the stage
Make sure they're animated
    `;
    hwStr = hwStr.trim();

    const endAnchor = document.getElementById("end-class1").children[1].children[0];
    const hw = document.getElementById("hw-class1");

    endAnchor.setAttribute("href", endUrl);
    endAnchor.innerHTML = endName;

    hw.children[1].innerHTML = hwTitle;
    hw.children[2].innerHTML = hwStr;
}

function setClass2()
{
    // Pygame Friday Class
    const endCode = document.getElementById("code-class2");
    const endUrl = "";
    const endName = "Pygame";
    const hwTitle = "Pygame";
    let hwStr = `def q1(a, b, c):
    # 2023 MAY 12
    # Sum triple kinda
    # Given three numbers a, b and c
    # Return their sum
    # Unless a b and c are all the same then return triple (3x) their sum
    # If the sum of a and b is > than c then return quadruple (4x) their sum
    # Code goes here
    return 0 # random lel

# Test cases
print(q1(1, 2, 3)) # 6
print(q1(2, 2, 3)) # 28
print(q1(2, 2, 2)) # 18
print(q1(10, 1, 11)) # 66`;
    const hw = document.getElementById("hw-class2");
    // const end = document.getElementById("end-class5").children[1];
    hw.children[1].innerHTML = hwTitle;
    hw.children[2].innerHTML = hwStr;
}

function setClass3()
{
    // Pygame Thursday Class
    const endUrl = "";
    const endName = "Tkinter";
    const hwTitle = "Tkinter";
    let hwStr = `
# 2023 MAY 18
# CCC: CCC2022J1, CCC2023J1, CCC2004J1, CCC2005J1
`;
    hwStr = hwStr.trim();
    
    const endAnchor = document.getElementById("end-class3").children[1];
    const hw = document.getElementById("hw-class3");

    // endAnchor.setAttribute("href", endUrl);
    endAnchor.innerHTML = endName;

    hw.children[1].innerHTML = hwTitle;
    hw.children[2].innerHTML = hwStr;
}

function setClass5()
{
    // Pygame Friday Class
    const endCode = document.getElementById("code-class5");
    const endUrl = "";
    const endName = "Pygame";
    const hwTitle = "Pygame";
    const hwStr = `
# 2023 APR 14
# We have two inputs monkey_a, True/False and monkey_b, True/False
# If monkey_a is smiling and monkey_b is smiling we are in trouble
# If monkey_a is NOT smiling and monkey_b is NOT smiling we are in trouble
# Print "trouble" if we are in trouble
# Print "no trouble" if we are not in trouble
`;
    const hw = document.getElementById("hw-class5");
    // const end = document.getElementById("end-class5").children[1];
    hw.children[1].innerHTML = hwTitle;
    hw.children[2].innerHTML = hwStr;
}

function setClass6()
{
    // Python Algo Wednesday Class
    const endUrl = "";
    const endName = "Class2";
    const hwTitle = "TKinter";
    const hwStr = `# Hw-2022-NOV-23
# Codingbat: String-2 and List-2 all questions`;

    const endAnchor = document.getElementById("end-class6").children[1].children[0];
    const hw = document.getElementById("hw-class6");

    endAnchor.setAttribute("href", endUrl);
    endAnchor.innerHTML = endName;

    hw.children[1].innerHTML = hwTitle;
    hw.children[2].innerHTML = hwStr;
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

        out += "Overall: " + (calcAverage(tempGrades) * 100).toPrecision(2) + "%\n\n";
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
    return (sum / size);
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

window.onload = setAll;