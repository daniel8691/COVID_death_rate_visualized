d3.csv("edited_countries.csv").then(function(data1) {

   
  
    console.log(data1)


    console.log(data1[0]['death_rate'])

    var death_rate = []
    var test1m = []
    var countries = []

    for( i = 0; i < data1.length; i++) {
        death_rate.push(data1[i]['death_rate'])
        test1m.push(data1[i]['test1m_pop'])
        countries.push(data1[i]['Country'])
    }
    console.log(death_rate)

    var death_plus = []
    for( i = 0; i < data1.length; i++) {
        death_plus.push(data1[i]['death_rate'] *3)
    }

    
  



    var sorted_data = data1.sort(function(a,b){
        return b.death_rate - a.death_rate
    })
    console.log(sorted_data)
    var death_sorted_countries = []
    death_sorted_rate = []
    for( i = 0; i < data1.length; i++) {
        death_sorted_countries.push(sorted_data[i]['Country'])
        death_sorted_rate.push(sorted_data[i]['death_rate'])
    }


    // Create Bar graph
    // Create traces
    var trace1 = {
        x:death_sorted_countries
            .slice(0,15),
            // .sort(function(a,b){
            //     return a.death_rate-b.death_rate
            // }),
        y:death_sorted_rate,
        text: death_sorted_rate,
        type:"bar"

    };
    var dataBar = [trace1];

    var layout = {
        title:{
            text: "Country Death Rates",
            size:24
        },
        xaxis: {
            title: {
                text:"Countries",
                size:18
            },
            type: "bottom"
        },
        yaxis: {
            title: {
                text: "Death Rates",
                size : 18
            }
        }
    }

    Plotly.newPlot('bar',dataBar, layout);

    
    data1[0]['death_rate']
    // Bubble Chart:
    var traceBubbles = {
        x: death_rate,
        y: test1m,
        text: countries,
        mode: "markers",
        marker: {
            size: death_plus ,
            color: countries
        }
     };

    var dataBubble = [traceBubbles];

    var layoutBubble = {
        title:{
            text: "Death Rates vs Test Numbers",
            size:24
        },
        xaxis: {
            title: {
                text:"Death Rates",
                size:18
            }
        },
        yaxis: {
            title: {
                text: "Tests / 1 million people",
                size : 18
            }
        }
    }
    Plotly.newPlot('bubble', dataBubble, layoutBubble)


});
