window.onload = function () { // this will be run when the whole page is loaded
    var barChart = document.getElementById("aUniqueId");
    var mapChart = document.getElementById("other3");

    var dbData = document.getElementById("dataP").textContent;
    var b = dbData.replace(/'/g, '"');
    var output = JSON.parse(b);
    console.log(output);
    var getMedicine;
    var getStatus;

    var barSelector = document.getElementById("aUniqueId").selectedIndex;
    var mapSelector = document.getElementById("other3").selectedIndex;
    var selectedText = document.getElementById("aUniqueId").options;

    var raceList = [["Caucasoid", 'green'], ["Negroid", 'blue'], ["Capoid", 'gray'], ["Mongoloid", 'red'], ["Australoid", 'orange']];
    var covidList = [["L-Type", 'blue'], ["S-Type", 'green']];
    google.charts.load('current', {
        'packages': ['geochart'],
        // Note: you will need to get a mapsApiKey for your project.
        // See: https://developers.google.com/chart/interactive/docs/basic_load_libs#load-settings
        'mapsApiKey': 'AIzaSyDuzdgUcmvMNNgvoaCV7-wxVeUhYGzVfQI'
    });
    google.charts.setOnLoadCallback(drawRegionsMap);

    google.charts.load("current", { packages: ['corechart'] });
    google.charts.setOnLoadCallback(drawChart);

    function drawRegionsMap() {

        var data;
        var dataArray;
        var colorArray = [];
        var valuesArray = [];
        var currentRace;
        var currentStrain;

        mapChart.addEventListener("change", function () {

            mapSelector = document.getElementById("other3").selectedIndex;
            selectedText = document.getElementById("aUniqueId").options;

            if (mapSelector == 0) {
                data = google.visualization.arrayToDataTable([
                    ['Country', 'Most Popular Treatment'],
                    ['Germany', 'Germany: Ritonavir'],
                    ['United States', 'United States: Flavonavir'],
                    ['Colombia', 'Colombia: Flu Medicine'],
                    ['Brazil', 'Brazil: Cold Medicine'],
                    ['Canada', 'Canada: Heart Medicine'],
                    ['France', 'France: Bronchitis Medicine'],
                    ['Russia', 'Russia: Eye Medicine']
                ]);
            } else if (mapSelector == 1) {
                dataArray = [
                    ['Country', 'COVID-19 Strain Color Code'],
                    ['Germany', 'Germany: L-Type'],
                    ['United States', 'United States: S-Type'],
                    ['Colombia', 'Colombia: L-Type'],
                    ['Brazil', 'Brazil: L-Type'],
                    ['Canada', 'Canada: L-Type'],
                    ['France', 'France: L-Type'],
                    ['Russia', 'Russia: L-Type']
                ]
                for (var i = 1; i < dataArray.length; i++) {
                    currentStrain = dataArray[i][1];
                    if (currentStrain.includes(covidList[0][0])) {
                        dataArray[i][1] = 0;
                    } else if (currentStrain.includes(covidList[1][0])) {
                        dataArray[i][1] = 1;
                    }
                }
                data = google.visualization.arrayToDataTable(dataArray);
                var options = {
                    colorAxis: {
                        colors: ["blue", "green"],
                        values: [0, 1]
                    }
                };
            } else if (mapSelector == 2) {
                dataArray = [
                    ['Country', 'Race Color Code'],
                    ['Germany', 'Caucasoid'],
                    ['United States', 'Mongoloid'],
                    ['Colombia', 'Caucasoid'],
                    ['Brazil', 'Australoid'],
                    ['Canada', 'Caucasoid'],
                    ['France', 'Mongoloid'],
                    ['Russia', 'Caucasoid']
                ]

                for (var i = 1; i < dataArray.length; i++) {
                    currentRace = dataArray[i][1];
                    if (currentRace.includes(raceList[0][0])) {
                        dataArray[i][1] = 0;
                    } else if (currentRace.includes(raceList[1][0])) {
                        dataArray[i][1] = 1;
                    } else if (currentRace.includes(raceList[2][0])) {
                        dataArray[i][1] = 2;
                    } else if (currentRace.includes(raceList[3][0])) {
                        dataArray[i][1] = 3;
                    } else if (currentRace.includes(raceList[4][0])) {
                        dataArray[i][1] = 4;
                    }
                }
                data = google.visualization.arrayToDataTable(dataArray);
                var options = {
                    colorAxis: {
                        colors: ["green", "blue", "gray", "red", "orange"],
                        values: [0, 1, 2, 3, 4]
                    }
                };
            } else if (mapSelector == 3) {
                dataArray = [
                    ['Country', 'Race with Least Recoveries'],
                    ['Germany', 'Germany: Caucasoid'],
                    ['United States', 'United States: Mongoloid'],
                    ['Colombia', 'Colombia: Caucasoid'],
                    ['Brazil', 'Brazil: Australoid'],
                    ['Canada', 'Canada: Caucasoid'],
                    ['France', 'France: Mongoloid'],
                    ['Russia', 'Russia: Caucasoid']
                ]
                for (var i = 1; i < dataArray.length; i++) {
                    currentRace = dataArray[i][1];
                    if (currentRace.includes(raceList[0][0])) {
                        dataArray[i][1] = 0;
                    } else if (currentRace.includes(raceList[1][0])) {
                        dataArray[i][1] = 1;
                    } else if (currentRace.includes(raceList[2][0])) {
                        dataArray[i][1] = 2;
                    } else if (currentRace.includes(raceList[3][0])) {
                        dataArray[i][1] = 3;
                    } else if (currentRace.includes(raceList[4][0])) {
                        dataArray[i][1] = 4;
                    }
                }
                data = google.visualization.arrayToDataTable(dataArray);
                var options = {
                    colorAxis: {
                        colors: ["green", "blue", "gray", "red", "orange"],
                        values: [0, 1, 2, 3, 4]
                    }
                };
            }


            var chart = new google.visualization.GeoChart(document.getElementById('regions_div'));
            chart.draw(data, options);
        });
    }

    function drawChart() {

        barChart.addEventListener("change", function () {

            barSelector = document.getElementById("aUniqueId").selectedIndex;
            selectedText = document.getElementById("aUniqueId").options;

            options = {
                title: selectedText[barSelector].text,
                width: 600,
                height: 400,
                bar: { groupWidth: "95%" },
                legend: { position: "none" },
            };

            var options;
            var data;
            var aList = [];
            var currentMedDat;
            var intList = [];
            var googleStandard = ["Medicine", "Deceased", { role: "style" }];
            var found = false;
            var currM;
            var randColor;

            if (barSelector == 0) {
                for (var i = 0; i < output.length; i++) {
                    found = false;
                    getMedicine = output[i][9];
                    getStatus = output[i][10];

                    getMedicine = getMedicine.replace(/\s/g, '');
                    intList = getMedicine.split(",")

                    if (getStatus != "D") {
                        continue;
                    }

                    for (var a = 0; a<intList.length; a++) {
                        currM = intList[a];
                        found = false;
                        for (var j = 0; j<aList.length; j++) {
                            found = false;
                            currentMedDat = aList[j][0];
        
                            if (currentMedDat == currM) {
                                found = true;
                                aList[j][1]++;
                                continue;
                            } 
                        } 
                        if (!found) {
                            found = false;
                            randColor = '#'+(0x1000000+(Math.random())*0xffffff).toString(16).substr(1,6);
                            aList.push([currM, 1, randColor]);
                        }
                    }   
                }

                aList.pop();

                aList.sort(sortFunction);
                function sortFunction(a, b) {
                    if (a[0] === b[0]) {
                        return 0;
                    }
                    return (a[1] > b[1]) ? 1 : -1;
                }

                aList.unshift(googleStandard);
                console.log(aList);

                data = google.visualization.arrayToDataTable(aList);
            } else if (barSelector == 1) {
                data = google.visualization.arrayToDataTable([
                    ["Medicine", "Recovered", { role: "style" }],
                    ["Favilavir", 8, "blue"],
                    ["Ritonavir", 54, "#b87333"],
                    ["Chloroquine", 200, "silver"],
                    ["Lopinavir", 400, "gold"]
                ]);
            } else if (barSelector == 2) {
                data = google.visualization.arrayToDataTable([
                    ["Medicine", "Popularity", { role: "style" }],
                    ["Favilavir", 1987, "blue"],
                    ["Ritonavir", 2500, "#b87333"],
                    ["Chloroquine", 4000, "silver"],
                    ["Lopinavir", 4500, "gold"]
                ]);
            } else if (barSelector == 3) {
                data = google.visualization.arrayToDataTable([
                    ["PreHealth", "Deceased", { role: "style" }],
                    ["Diabetes", 500, "blue"],
                    ["Heart Disease", 800, "#b87333"],
                    ["Pulmonary Oedema", 1000, "silver"],
                    ["Bronchitis", 5000, "gold"]
                ]);
            } else if (barSelector == 4) {
                data = google.visualization.arrayToDataTable([
                    ["PreHealth", "Recovered", { role: "style" }],
                    ["Overweight", 2, "blue"],
                    ["Asthma", 50, "#b87333"],
                    ["High Tension", 500, "silver"],
                    ["Cataracts", 5000, "gold"]
                ]);
            }

            var view = new google.visualization.DataView(data);
            view.setColumns([0, 1,
                {
                    calc: "stringify",
                    sourceColumn: 1,
                    type: "string",
                    role: "annotation"
                },
                2]);

            var chart = new google.visualization.ColumnChart(document.getElementById("columnchart_values"));
            chart.draw(view, options);
        });
    }
};